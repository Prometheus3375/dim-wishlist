import json
import os
from collections import defaultdict
from collections.abc import Iterable, Iterator, Mapping, Sequence, Set
from enum import IntEnum
from functools import cached_property
from http.client import HTTPResponse
from os.path import dirname, join
from typing import Any, ClassVar, NamedTuple, Self
from urllib.request import Request, urlopen

from json_helpers import *

__all__ = (
    'AmmunitionType',
    'PerkTuple',
    'Manifest',
    'PlugSet',
    'Weapon'
    )


class AmmunitionType(IntEnum):
    """
    Available ammunition types in Destiny 2.
    `Source <https://bungie-net.github.io/multi/schema_Destiny-DestinyAmmunitionType.html#schema_Destiny-DestinyAmmunitionType>`_
    """
    None_ = 0
    Primary = 1
    Special = 2
    Heavy = 3
    Unknown = 4


class PerkTuple(NamedTuple):
    """
    Contains a name of a weapon perk, its hash and hash of its enhanced version if any.
    """
    name: str
    regular: int
    enhanced: int = 0

    @property
    def proper_name(self, /) -> str:
        """
        Basically the name, but can be changed a bit in some exceptional cases.
        """
        return self.name

    @classmethod
    def choose_best(cls, first: Self, second: Self, /) -> Self | None:
        """
        If both tuples are identical, returns the first of them.
        If both tuples have the same name and regular
        and one of the does not define enhanced,
        then returns the one with defined enhanced.
        Otherwise, returns ``None``.
        """
        if first.name == second.name and first.regular == second.regular:
            if first.enhanced == second.enhanced:
                return first

            if second.enhanced == 0 and first.enhanced >= 0:
                return first

            if first.enhanced == 0 and second.enhanced >= 0:
                return second

        return None


class Manifest(JSONObjectWrapper):
    """
    A convenience wrapper around Destiny 2 game data.
    """
    __slots__ = '__dict__',

    # region Class attributes and methods

    CACHE_DIR: ClassVar[str] = join(dirname(dirname(__file__)), '.manifest-cache')
    """
    Directory where cached manifests are stored.
    """
    os.makedirs(CACHE_DIR, exist_ok=True)

    @classmethod
    def list_cached_versions(cls, /) -> set[str]:
        """
        Returns a set of versions of cached manifests.
        """
        return {
            filename[:-5]
            for filename in os.listdir(cls.CACHE_DIR)
            if filename.endswith('.json')
            }

    @classmethod
    def clear_cache_directory(cls, /) -> None:
        """
        Removes all cached manifests but the most recent one.
        """
        files = [
            filename
            for filename in os.listdir(cls.CACHE_DIR)
            if filename.endswith('.json')
            ]

        files.sort()
        files.pop()

        for filename in files:
            os.remove(join(cls.CACHE_DIR, filename))

    @classmethod
    def from_file(cls, filepath: str, /) -> Self:
        """
        Creates an instance of :class:`Manifest` from a file.
        """
        with open(filepath) as f:
            manifest = json.load(f)

        return cls(manifest)

    TABLES_TO_COPY: ClassVar[list[str]] = [
        'DestinyInventoryItemDefinition',
        'DestinyPlugSetDefinition',
        'DestinyCollectibleDefinition',
        'DestinyItemCategoryDefinition',
        'DestinySocketCategoryDefinition',
        'DestinyDamageTypeDefinition',
        ]

    @classmethod
    def from_api(cls, /) -> Self:
        """
        Creates an instance of :class:`Manifest` from calling Bungie.net API.
        API docs: https://bungie-net.github.io/multi

        Once game data is downloaded, necessary tables are cached in ``CACHE_DIR`` in a JSON file.
        If manifest version is unchanged, this method loads respective cached game data.
        """
        req = Request('https://www.bungie.net/Platform/Destiny2/Manifest', method='GET')
        response: HTTPResponse
        with urlopen(req) as response:
            manifest = json.loads(response.read())['Response']

        version = manifest['version']
        cached_versions = cls.list_cached_versions()
        if version in cached_versions:
            return cls.from_file(join(cls.CACHE_DIR, f'{version}.json'))

        datapath = manifest['jsonWorldContentPaths']['en']
        req = Request(f'https://www.bungie.net{datapath}', method='GET')
        with urlopen(req) as response:
            data = json.load(response)

        manifest = {
            table_name: data[table_name]
            for table_name in cls.TABLES_TO_COPY
            }
        manifest['version'] = version

        with open(join(cls.CACHE_DIR, f'{version}.json'), 'w') as f:
            json.dump(manifest, f, ensure_ascii=False, indent=2, sort_keys=True)
            f.write('\n')

        return cls(manifest)

    # endregion

    @property
    def version(self, /) -> str:
        """
        Version of this manifest.
        """
        return self['version']

    def get_item(self, hash_: int, /) -> JSONObjectWrapper:
        """
        Returns definition of the inventory item with the given hash.
        """
        return self['DestinyInventoryItemDefinition', hash_]

    def get_plug_set(self, hash_: int, /) -> JSONObjectWrapper:
        """
        Returns definition of the plug set item with the given hash.
        """
        return self['DestinyPlugSetDefinition', hash_]

    def get_collectible(self, hash_: int, /) -> JSONObjectWrapper:
        """
        Returns definition of the collectible with the given hash.
        """
        return self['DestinyCollectibleDefinition', hash_]

    def _get_mapping_between_hashes_and_names(self, table_name: str, /) -> Mapping[int, str]:
        return {
            definition['hash']: definition['displayProperties.name']
            for definition in self[table_name].values()
            }

    @cached_property
    def item_category_names(self, /) -> Mapping[int, str]:
        """
        Mapping between item category hashes and their names.
        """
        return self._get_mapping_between_hashes_and_names('DestinyItemCategoryDefinition')

    @cached_property
    def socket_category_names(self, /) -> Mapping[int, str]:
        """
        Mapping between socket category hashes and their names.
        """
        return self._get_mapping_between_hashes_and_names('DestinySocketCategoryDefinition')

    @cached_property
    def damage_type_names(self, /) -> Mapping[int, str]:
        """
        Mapping between damage type hashes and their names.
        """
        return self._get_mapping_between_hashes_and_names('DestinyDamageTypeDefinition')

    @cached_property
    def legendary_weapons(self, /) -> Sequence['Weapon']:
        """
        List of ALL legendary weapons.
        """
        li = []
        definition: JSONObjectWrapper
        for definition in self['DestinyInventoryItemDefinition'].values():
            category_hashes = definition.get('itemCategoryHashes', ())
            is_weapon = any(self.item_category_names[h] == 'Weapon' for h in category_hashes)
            if not is_weapon: continue

            if definition['inventory.tierTypeName'] == 'Legendary':
                li.append(Weapon(definition, self))

        return li

    def iterate_legendary_weapons_since_release(self, release_string: str, /) -> Iterator['Weapon']:
        """
        Returns an iterator over instances of :class:`Weapon`
        which were released at the given release or later.
        """
        return (w for w in self.legendary_weapons if w.release_string >= release_string)

    def legendary_weapons_perks(self, release_string: str = '', /) -> set[PerkTuple]:
        """
        Returns a set of instances of :class:`PerkTuple`
        which are found in legendary weapons.

        Parameter *release_string* can be used to use weapons
        that were released at the given release or later.
        """
        if release_string:
            weapons = self.iterate_legendary_weapons_since_release(release_string)
        else:
            weapons = iter(self.legendary_weapons)

        name2perk = {}
        plug_sets = {
            plug_set
            for weapon in weapons
            for plug_set in weapon.iterate_perk_plug_sets()
            }
        for plug_set in plug_sets:
            for perk_tuple in plug_set.iterate_perks(self):
                name = perk_tuple.proper_name
                present = name2perk.get(name)
                if present:
                    best = PerkTuple.choose_best(present, perk_tuple)
                    if best is None:
                        raise ValueError(
                            f'there are two perk tuples named {name!r}: '
                            f'{present} and {perk_tuple}'
                            )

                    name2perk[name] = best
                else:
                    name2perk[name] = perk_tuple

        return set(name2perk.values())


class PlugSet:
    """
    Holder of plug set hash and plug item hashes.
    """
    __slots__ = '_plug_hashes', '_hash'

    def __init__(
            self,
            /,
            *,
            definition: JSONObjectWrapper | None = None,
            plug_hashes: Iterable[int] | None = None,
            ) -> None:
        if definition is None and plug_hashes is None:
            raise ValueError('plug set must be defined with either a definition or plug hashes')

        if definition is None:
            plug_hashes = tuple(plug_hashes)
            if not all(isinstance(h, int) for h in plug_hashes):
                raise TypeError('all plug hashes must be integers')

            self._hash = 0

        elif plug_hashes is None:
            if not isinstance(definition, JSONObjectWrapper):
                raise TypeError(
                    f'plug set definition must be of type {JSONObjectWrapper}, '
                    f'got {type(definition)}'
                    )

            self._hash = definition['hash']
            plug_entry: JSONObjectWrapper
            plug_hashes = [
                plug_entry['plugItemHash']
                for plug_entry in definition['reusablePlugItems']
                ]

        else:
            raise ValueError('both definition and plug hashes are specified, only one is allowed')

        self._plug_hashes = frozenset(plug_hashes)

    def hash(self, /) -> int:
        """
        Predefined hash of this plug set.
        It is zero if this plug set is defined from plug hashes.
        """
        return self._hash

    def plug_hashes(self, /) -> Set[int]:
        """
        Plug hashes defined in this plug set.
        """
        return self._plug_hashes

    def __eq__(self, other: Any, /) -> bool:
        if isinstance(other, PlugSet):
            return self._plug_hashes == other._plug_hashes

        return NotImplemented

    def __hash__(self, /) -> int:
        return hash(self._plug_hashes)

    def iterate_perks(self, manifest: Manifest, /) -> Iterator[PerkTuple]:
        """
        Returns an iterator over instances of :class:`Perk` obtained from this plug set.
        """
        name2defs = defaultdict(list)
        for h in self._plug_hashes:
            definition = manifest.get_item(h)
            name = definition['displayProperties.name']
            name2defs[name].append(definition)

        for name, definitions in name2defs.items():
            match len(definitions):
                case 1:
                    yield PerkTuple(name, definitions[0]['hash'])
                case 2:
                    first, second = definitions
                    first_hash = first['hash']
                    second_hash = second['hash']
                    is_first_enhanced = first['itemTypeDisplayName'].startswith('Enhanced')
                    is_second_enhanced = second['itemTypeDisplayName'].startswith('Enhanced')
                    if is_first_enhanced and not is_second_enhanced:
                        yield PerkTuple(name, regular=second_hash, enhanced=first_hash)
                    elif not is_first_enhanced and is_second_enhanced:
                        yield PerkTuple(name, regular=first_hash, enhanced=second_hash)
                    else:
                        raise ValueError(
                            f'plug set {self._hash} has 2 perks of name {name!r} '
                            f'with hashes {first_hash} and {second_hash}, '
                            f'both are {'enhanced' if is_first_enhanced else 'not enhanced'}'
                            )
                case n:
                    raise ValueError(
                        f'plug set {self._hash} has {n} perks of name {name!r} '
                        f'with hashes {', '.join(str(d['hash']) for d in definitions)}'
                        )


class Weapon:
    """
    A convenience wrapper around a weapon definition.
    """
    __slots__ = '_definition', '_manifest', '__dict__'

    def __init__(self, definition: JSONObjectWrapper, manifest: Manifest, /) -> None:
        if not isinstance(definition, JSONObjectWrapper):
            raise TypeError(
                f'weapon definition must be of type {JSONObjectWrapper}, '
                f'got {type(definition)}'
                )

        self._definition = definition
        self._manifest = manifest

    @property
    def hash(self, /) -> int:
        """
        Hash of this weapon.
        """
        return self._definition['hash']

    @property
    def name(self, /) -> str:
        """
        Name of this weapon.
        """
        return self._definition['displayProperties.name']

    @cached_property
    def damage_types(self, /) -> Sequence[str]:
        """
        Names of damage types of this weapon.
        """
        return [
            self._manifest.damage_type_names[dt_hash]
            for dt_hash in self._definition['damageTypeHashes']
            ]

    @property
    def ammo_type(self, /) -> AmmunitionType:
        """
        Ammo type of this weapon.
        """
        return AmmunitionType(self._definition['equippingBlock.ammoType'])

    @property
    def weapon_type(self, /) -> str:
        """
        Type of this weapon.
        """
        return self._definition['itemTypeDisplayName']

    @property
    def source(self, /) -> str:
        """
        From where this weapon can be obtained.
        """
        collectible_hash = self._definition['collectibleHash']
        return self._manifest.get_collectible(collectible_hash)['sourceString']

    @cached_property
    def release_string(self, /) -> str:
        """
        Returns release string when this weapon was added.
        Can be the empty string, if no proper release string is present.
        """
        return max(
            (
                v
                for v in self._definition['traitIds']
                if v.startswith('releases')
                ),
            default='',
            )

    def _get_socket_indexes_by_category_name(self, category_name: str, /) -> list[int]:
        indexes = []
        sc: JSONObjectWrapper
        for sc in self._definition['sockets.socketCategories']:
            sc_hash = sc['socketCategoryHash']
            if self._manifest.socket_category_names[sc_hash] == category_name:
                indexes.extend(sc['socketIndexes'])

        return indexes

    @cached_property
    def intrinsics(self, /) -> Sequence[str]:
        """
        Names of intrinsics of this weapon.
        """
        socket_indexes = self._get_socket_indexes_by_category_name('INTRINSIC TRAITS')
        socket_entries = self._definition['sockets.socketEntries']
        return [
            self._manifest.get_item(hash_)['displayProperties.name']
            for index in socket_indexes
            if (hash_ := socket_entries[index, 'singleInitialItemHash'] > 0)
            ]

    def iterate_perk_plug_sets(self, /) -> Iterator[PlugSet]:
        """
        Returns an iterator over plug sets of weapon perks defined in this weapon.
        """
        socket_indexes = self._get_socket_indexes_by_category_name('WEAPON PERKS')
        socket_entries = self._definition['sockets.socketEntries']
        plug_sets = set()
        for index in socket_indexes:
            entry = socket_entries[index]
            reusable_hash = entry.get('reusablePlugSetHash')
            if reusable_hash:
                yield PlugSet(definition=self._manifest.get_plug_set(reusable_hash))

            randomized_hash = entry.get('randomizedPlugSetHash')
            if randomized_hash:
                yield PlugSet(definition=self._manifest.get_plug_set(randomized_hash))

            reusable_plugs: JSONArrayWrapper = entry.get('reusablePlugItems')
            if reusable_plugs:
                yield PlugSet(plug_hashes=(d['plugItemHash'] for d in reusable_plugs))

        return plug_sets
