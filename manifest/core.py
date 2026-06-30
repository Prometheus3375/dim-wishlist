__all__ = (
    'AmmunitionType',
    'PerkTuple',
    'PERK_TUPLE_SORT_BY_COMPLETENESS',
    'PerkTupleDuplicationWarning',
    'get_perk_category',
    'is_perk_enhanced',
    'PlugSet',
    'PlugSetPerkDuplicationWarning',
    'Weapon',
    'Manifest',
    )

import json
import os
from collections import defaultdict
from collections.abc import Iterable, Iterator, Mapping, Sequence, Set
from enum import IntEnum
from functools import cached_property
from http.client import HTTPResponse
from operator import attrgetter
from os.path import dirname, join
from typing import Any, ClassVar, NamedTuple, Self
from urllib.request import Request, urlopen
from warnings import warn

from json_helpers import *


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
    Contains the name of a weapon perk, its hash and hash of its enhanced version.
    """
    name: str
    category: str
    regular: int = 0
    enhanced: int = 0

    @property
    def is_complete(self, /) -> bool:
        """
        Whether this tuple has both regular and enhanced hashes.
        """
        return self.regular > 0 and self.enhanced > 0

    @property
    def not_complete(self, /) -> bool:
        """
        Whether this tuple misses either regular hash or enhanced hash.
        """
        return self.regular <= 0 or self.enhanced <= 0

    def add_to_tuple_set(self, tuple_set: set['PerkTuple'], /) -> None:
        """
        Conditionally modifies the given set of tuples.

        If this tuple is complete, and the set contains incomplete versions
        with the same regular or enhanced hashes,
        then removes all incomplete versions from the set and adds this tuple.
        If this tuple is incomplete, and the set contains the complete version,
        then does nothing.

        In any other case adds this tuple to the set.
        """
        to_remove = []
        add_self = True
        for other in tuple_set:
            if self.regular == other.regular:
                if self.enhanced > 0 and other.enhanced == 0:
                    to_remove.append(other)
                elif other.enhanced > 0 and self.enhanced == 0:
                    add_self = False

            elif self.enhanced == other.enhanced:
                if self.regular > 0 and other.regular == 0:
                    to_remove.append(other)
                elif other.regular > 0 and self.regular == 0:
                    add_self = False

        for other in to_remove:
            tuple_set.remove(other)

        if add_self:
            tuple_set.add(self)


PERK_TUPLE_SORT_BY_COMPLETENESS = attrgetter('not_complete', 'regular', 'enhanced')
"""
Callable to use for sorting instances of :class:`PerkTuple` by completeness.
"""


class PerkTupleDuplicationWarning(Warning):
    """
    Warnings about duplicated instances of :class:`PerkTuple`.
    """


class PlugSetPerkDuplicationWarning(Warning):
    """
    Warnings about duplicated perks inside instances of :class:`PlugSet`.
    """


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
        'DestinyCollectibleDefinition',
        'DestinyDamageTypeDefinition',
        'DestinyInventoryItemDefinition',
        'DestinyItemCategoryDefinition',
        'DestinyPlugSetDefinition',
        'DestinySandboxPerkDefinition',
        'DestinySocketCategoryDefinition',
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

    @classmethod
    def from_recent(cls, /) -> Self:
        """
        Creates an instance of :class:`Manifest`
        from the most recent cached version stored inside ``CACHED_DIR``.

        Fallbacks to ``from_api`` if there is no cached version.
        """
        filename = max(
            (
                filename
                for filename in os.listdir(cls.CACHE_DIR)
                if filename.endswith('.json')
                ),
            default='',
            )

        if filename:
            return cls.from_file(join(cls.CACHE_DIR, filename))

        return cls.from_api()

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

    def get_sandbox_perk(self, hash_: int, /) -> JSONObjectWrapper:
        """
        Returns definition of the sandbox perk with the given hash.
        """
        return self['DestinySandboxPerkDefinition', hash_]

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
            is_dummy = any(self.item_category_names[h] == 'Dummies' for h in category_hashes)
            if is_dummy or not is_weapon: continue

            if definition['inventory.tierTypeName'] == 'Legendary':
                li.append(Weapon(definition, self))

        return tuple(li)

    @cached_property
    def release_strings(self, /) -> Set[str]:
        """
        All release strings met in legendary weapons.
        """
        return frozenset(
            weapon.release_string
            for weapon in self.legendary_weapons
            if weapon.release_string
            )

    def iterate_legendary_weapons_since_release(self, release_string: str, /) -> Iterator['Weapon']:
        """
        Returns an iterator over instances of :class:`Weapon`
        that were released at the given release or later.
        """
        return (w for w in self.legendary_weapons if w.release_string >= release_string)

    def get_legendary_weapon_perks(self, release_string: str = '', /) -> dict[str, set[PerkTuple]]:
        """
        Returns a mapping between perk names and sets of instances of :class:`PerkTuple`
        that are found in legendary weapons.

        Parameter *release_string* can be used to use only weapons
        that were released at the given release or later.
        """
        if release_string:
            weapons = self.iterate_legendary_weapons_since_release(release_string)
        else:
            weapons = iter(self.legendary_weapons)

        name_to_tuple_set: dict[str, set[PerkTuple]] = defaultdict(set)
        plug_sets = {
            plug_set
            for weapon in weapons
            for plug_set in weapon.iterate_perk_plug_sets()
            }
        for plug_set in plug_sets:
            for perk_tuple in plug_set.iterate_perks(self):
                perk_tuple.add_to_tuple_set(name_to_tuple_set[perk_tuple.name])

        for name, tuple_set in name_to_tuple_set.items():
            count_complete = sum(t.is_complete for t in tuple_set)
            if count_complete > 1:
                tuples_desc = ', '.join(
                    f'(regular={t.regular}, enhanced={t.enhanced})'
                    for t in sorted(tuple_set, key=PERK_TUPLE_SORT_BY_COMPLETENESS)
                    )
                warn(
                    f'there are {count_complete} complete perk tuples '
                    f'named {name!r}: {tuples_desc}',
                    category=PerkTupleDuplicationWarning,
                    stacklevel=2,
                    )

        return name_to_tuple_set


def get_perk_name(definition: JSONObjectWrapper, /) -> str:
    """
    Returns a proper perk name from the given item definition.
    """
    # Some enhanced perks has Enhanced in the name, for example:
    # https://data.destinysets.com/i/InventoryItem:4290541820
    name = definition['displayProperties.name']
    if name.endswith('Enhanced'):
        return name[:-9]

    return name


def get_perk_category(definition: JSONObjectWrapper, /) -> str:
    """
    Returns a proper perk category from the given item definition.
    """
    category = definition['itemTypeDisplayName']
    if category.startswith('Enhanced'):
        return category[9:]

    return category


def is_perk_enhanced(definition: JSONObjectWrapper, /) -> bool:
    """
    Whether the perk described by the given definition is enhanced.
    """
    # Some enhanced perks do not have Enhanced prefix, for example:
    # https://data.destinysets.com/i/InventoryItem:1164602481
    # Some enhanced perks do not have Uncommon rarity, for example:
    # https://data.destinysets.com/i/InventoryItem:745577913
    return (
            definition['itemTypeDisplayName'].startswith('Enhanced')
            or
            definition['itemTypeAndTierDisplayName'].startswith('Uncommon')
    )


def handle_exceptional_plug_sets(
        name: str,
        definitions: list[JSONObjectWrapper],
        /,
        ) -> Sequence[PerkTuple] | None:
    """
    Handles some exceptional cases in plug sets, providing correct instances of :class:`PerkTuple`.

    If the case is not exceptional, returns ``None``.
    """
    hash2def = {d['hash']: d for d in definitions}
    match name:
        case 'Pulse Monitor':
            if hash2def.keys() == {205890336, 972757866}:
                # They are both regular versions.
                # Example of a weapon that rolls both:
                # https://www.light.gg/db/items/1402766122/retrofuturist
                h1 = 972757866
                h2 = 205890336
                return [
                    PerkTuple(name, get_perk_category(hash2def[h1]), regular=h1),
                    PerkTuple(name, get_perk_category(hash2def[h2]), regular=h2),
                    ]

            elif hash2def.keys() == {972757866, 1685378950, 205890336, 320071920}:
                # Example of a weapon that rolls all these versions:
                # https://www.light.gg/db/items/963732594/xenoclast-iv
                h1 = 972757866
                h2 = 205890336
                return [
                    PerkTuple(
                        name,
                        get_perk_category(hash2def[h1]),
                        regular=h1,
                        enhanced=1685378950,
                        ),
                    PerkTuple(
                        name,
                        get_perk_category(hash2def[h2]),
                        regular=h2,
                        enhanced=320071920,
                        ),
                    ]

        case 'Concussion Grenades':
            # DestinyPlugSetDefinition.3299814502
            if hash2def.keys() == {1716000303, 2406549743}:
                h = 1716000303
                return [
                    PerkTuple(name, get_perk_category(hash2def[h]), regular=h, enhanced=2406549743)
                    ]

        case 'Drop Mag':
            # DestinyPlugSetDefinition.811071122
            # DestinyPlugSetDefinition.3985973594
            # DestinyPlugSetDefinition.1942462581
            if hash2def.keys() == {4134353779, 3678323611}:
                h = 4134353779
                return [
                    PerkTuple(name, get_perk_category(hash2def[h]), regular=h, enhanced=3678323611)
                    ]

    return None


class PlugSet:
    """
    Holder of plug set identifier and plug item hashes.
    """
    __slots__ = '_plug_hashes', '_identifier'

    def __init__(self, plug_hashes: Iterable[int], identifier: JSONPath, /) -> None:
        plug_hashes = tuple(plug_hashes)
        if not all(isinstance(h, int) for h in plug_hashes):
            raise TypeError('all plug hashes must be integers')

        if not is_json_path(identifier):
            raise TypeError('identifier must be a JSON path')

        self._plug_hashes = frozenset(plug_hashes)
        self._identifier = identifier

    @classmethod
    def from_definition(cls, definition: JSONObjectWrapper, /) -> Self:
        """
        Creates an instance of :class:`PlugSet` from a plug set definition.
        """
        if not isinstance(definition, JSONObjectWrapper):
            raise TypeError(
                f'plug set definition must be of type {JSONObjectWrapper}, '
                f'got {type(definition)}'
                )

        identifier = 'DestinyPlugSetDefinition', definition['hash']
        plug_entry: JSONObjectWrapper
        plug_hashes = (
            plug_entry['plugItemHash']
            for plug_entry in definition['reusablePlugItems']
            if plug_entry['currentlyCanRoll']
            )
        return cls(plug_hashes, identifier)

    @property
    def identifier(self, /) -> str:
        """
        Identifier of this plug set.
        """
        return json_path_to_str(self._identifier)

    @property
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
            # Ignore perks with no item type
            if definition['itemTypeDisplayName']:
                name = get_perk_name(definition)
                name2defs[name].append(definition)

        for name, definitions in name2defs.items():
            match len(definitions):
                case 1:
                    def1 = definitions[0]
                    if is_perk_enhanced(def1):
                        yield PerkTuple(name, get_perk_category(def1), enhanced=def1['hash'])
                    else:
                        yield PerkTuple(name, get_perk_category(def1), regular=def1['hash'])

                case 2:
                    result = handle_exceptional_plug_sets(name, definitions)
                    if result is None:
                        def1, def2 = definitions
                        def1_hash = def1['hash']
                        def2_hash = def2['hash']
                        is_def1_enhanced = is_perk_enhanced(def1)
                        is_def2_enhanced = is_perk_enhanced(def2)
                        if is_def1_enhanced and not is_def2_enhanced:
                            yield PerkTuple(
                                name,
                                get_perk_category(def2),
                                regular=def2_hash,
                                enhanced=def1_hash,
                                )

                        elif not is_def1_enhanced and is_def2_enhanced:
                            yield PerkTuple(
                                name,
                                get_perk_category(def1),
                                regular=def1_hash,
                                enhanced=def2_hash,
                                )

                        else:
                            warn(
                                f'plug set {self.identifier!r} has 2 perks named {name!r} '
                                f'with hashes {def1_hash} and {def2_hash}, '
                                f'both are {'enhanced' if is_def1_enhanced else 'not enhanced'}',
                                category=PlugSetPerkDuplicationWarning,
                                stacklevel=2,
                                )
                    else:
                        yield from result

                case n:
                    result = handle_exceptional_plug_sets(name, definitions)
                    if result is None:
                        warn(
                            f'plug set {self.identifier!r} has {n} perks named {name!r} '
                            f'with hashes {', '.join(str(d['hash']) for d in definitions)}',
                            category=PlugSetPerkDuplicationWarning,
                            stacklevel=2,
                            )
                    else:
                        yield from result


class WeaponMultipleIntrinsicsWarning(Warning):
    """
    Warnings about weapons that have multiple intrinsics.
    """


class WeaponMultipleBreakerTypesWarning(Warning):
    """
    Warnings about weapons that have multiple breaker types.
    """


WEAPON_NAME_POSTFIXES = ('(Adept)', '(Harrowed)', '(Timelost)')


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

    def __repr__(self, /) -> str:
        return f'<{self.__class__.__name__} {self.name!r} hash={self.hash}>'

    @property
    def hash(self, /) -> int:
        """
        Hash of this weapon.
        """
        return self._definition['hash']

    @property
    def fullname(self, /) -> str:
        """
        Full name of this weapon.
        """
        return self._definition['displayProperties.name']

    @cached_property
    def name(self, /) -> str:
        """
        Name of this weapon without postfix.
        """
        name = self.fullname
        if name.endswith(WEAPON_NAME_POSTFIXES):
            name = name[:name.rindex('(')].strip()

        return name

    @property
    def is_adept(self, /) -> str:
        """
        Whether this weapon is adept.
        """
        return self._definition['isAdept']

    @cached_property
    def damage_types(self, /) -> Sequence[str]:
        """
        Names of damage types of this weapon.
        """
        return tuple(
            self._manifest.damage_type_names[dt_hash]
            for dt_hash in self._definition['damageTypeHashes']
            )

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

    @cached_property
    def source(self, /) -> str:
        """
        From where this weapon can be obtained.
        Can be the empty string if no collectible is present.
        """
        collectible_hash = self._definition.get('collectibleHash')
        if collectible_hash is None:
            return ''

        return self._manifest.get_collectible(collectible_hash)['sourceString']

    @cached_property
    def is_craftable(self, /) -> bool:
        """
        Whether this weapon is craftable.
        """
        return any(
            # https://data.destinysets.com/i/InventoryItem:1961918267
            socket_entry['singleInitialItemHash'] == 1961918267
            for socket_entry in self._definition['sockets.socketEntries']
            )

    @cached_property
    def release_string(self, /) -> str:
        """
        Returns release string when this weapon was added.
        Can be the empty string if no proper release string is present.
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
    def intrinsic_object(self, /) -> JSONObjectWrapper:
        """
        Intrinsic definition of this weapon.
        """
        socket_indexes = self._get_socket_indexes_by_category_name('INTRINSIC TRAITS')
        socket_entries = self._definition['sockets.socketEntries']
        intrinsics = tuple(
            self._manifest.get_item(socket_entries[index, 'singleInitialItemHash'])
            for index in socket_indexes
            )
        if len(intrinsics) > 1:
            warn(
                f'weapon {self.name!r} ({self.hash}) has {len(intrinsics)} intrinsics '
                f'with hashes {', '.join(str(d['hash']) for d in intrinsics)}',
                category=WeaponMultipleIntrinsicsWarning,
                stacklevel=2,
                )

        return intrinsics[0]

    @property
    def intrinsic(self, /) -> str:
        """
        Names of the intrinsic trait of this weapon.
        """
        return self.intrinsic_object['displayProperties.name']

    @cached_property
    def breaker_type(self, /) -> str:
        """
        Breaker type of this weapon.
        """
        perks = [
            self._manifest.get_sandbox_perk(p['perkHash'])
            for p in self.intrinsic_object['perks']
            ]
        breaker_types = [d for d in perks if d['displayProperties.name'].startswith('[')]
        if len(breaker_types) > 1:
            warn(
                f'weapon {self.name!r} ({self.hash}) has {len(breaker_types)} breaker types '
                f'with hashes {', '.join(str(d['hash']) for d in breaker_types)}',
                category=WeaponMultipleBreakerTypesWarning,
                stacklevel=2,
                )

        return breaker_types[0]['displayProperties.name']

    def iterate_perk_plug_sets(self, /) -> Iterator[PlugSet]:
        """
        Returns an iterator over plug sets of weapon perks defined in this weapon.
        """
        socket_indexes = self._get_socket_indexes_by_category_name('WEAPON PERKS')
        socket_entries = self._definition['sockets.socketEntries']
        for index in socket_indexes:
            entry = socket_entries[index]
            reusable_hash = entry.get('reusablePlugSetHash')
            if reusable_hash:
                yield PlugSet.from_definition(self._manifest.get_plug_set(reusable_hash))

            randomized_hash = entry.get('randomizedPlugSetHash')
            if randomized_hash:
                yield PlugSet.from_definition(self._manifest.get_plug_set(randomized_hash))

            reusable_plugs: JSONArrayWrapper = entry.get('reusablePlugItems')
            if reusable_plugs:
                plug_hashes = (plug_entry['plugItemHash'] for plug_entry in reusable_plugs)
                identifier = (
                    'DestinyInventoryItemDefinition',
                    self.hash,
                    'sockets',
                    'socketEntries',
                    index,
                    'reusablePlugItems',
                    )
                yield PlugSet(plug_hashes, identifier)

    @cached_property
    def perks(self, /) -> frozenset[PerkTuple]:
        """
        Set of perks with which this weapon can roll.
        """
        return frozenset(
            perk
            for plug_set in self.iterate_perk_plug_sets()
            for perk in plug_set.iterate_perks(self._manifest)
            )
