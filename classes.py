from collections import Counter
from collections.abc import Iterable, Sequence
from dataclasses import InitVar, dataclass, field
from itertools import product
from typing import Any, ClassVar, Self, TextIO, TypeGuard

__all__ = 'Item', 'AnyItem', 'AnyPerk', 'Wishlist', 'Roll', 'RollDefinition'


@dataclass(frozen=True, kw_only=True, slots=True)
class Item:
    """
    A common class for armor, weapons, traits, categories, etc.
    """
    __hash2item: ClassVar[dict[int, Self]] = {}

    name: str
    hash: int

    # noinspection PyDataclass
    def __post_init__(self, /) -> None:
        existing = self.__hash2item.get(self.hash)
        if existing:
            raise ValueError(f'item with hash {self.hash} already exists')

        self.__hash2item[self.hash] = self

    @classmethod
    def from_hash(cls, hash_: int, /) -> Self | None:
        """
        Returns an existing item with the given hash value
        or ``None`` if no item with such hash exists.
        """
        return cls.__hash2item.get(hash_)

    def __eq__(self, other: Any, /) -> bool:
        return self.hash == other.hash if isinstance(other, Item) else False

    def __ne__(self, other: Any, /) -> bool:
        return self.hash != other.hash if isinstance(other, Item) else True

    def __hash__(self, /) -> int:
        return self.hash

    def __lt__(self, other: Self, /) -> bool:
        return self.hash < other.hash if isinstance(other, Item) else NotImplemented

    def __le__(self, other: Self, /) -> bool:
        return self.hash <= other.hash if isinstance(other, Item) else NotImplemented

    def __gt__(self, other: Self, /) -> bool:
        return self.hash > other.hash if isinstance(other, Item) else NotImplemented

    def __ge__(self, other: Self, /) -> bool:
        return self.hash >= other.hash if isinstance(other, Item) else NotImplemented

    @property
    def light_gg(self, /) -> str:
        """
        Link to the page of this item on light.gg.
        """
        return f'https://www.light.gg/db/items/{self.hash}'


AnyItem = Item(name='DIM Wildcard', hash=-69420)
"""
Special item for DIM to denote any item.
"""
AnyPerk = Item(name='Any Perk', hash=-1)
"""
Special item to denote an empty selection for a perk column.
"""

type OrderedSet[T] = dict[T, None]
type PerkList = Sequence[Item]
type AnnotatedRoll = tuple[str, bool, tuple[PerkList, ...]]


@dataclass(frozen=True, kw_only=True, slots=True)
class WishlistEntry:
    """
    A separate entry of a wishlist.
    """
    item: Item
    notes: str
    perk_lists: InitVar[Sequence[PerkList]]
    combos: OrderedSet[PerkList] = field(init=False)

    # noinspection PyDataclass
    def __post_init__(self, perk_lists: Sequence[PerkList], /):
        # Remove empty lists and convert remaining to ordered sets
        perk_sets: Iterable[OrderedSet[Item]] = map(dict.fromkeys, filter(None, perk_lists))

        # Use product to produce every possible combo.
        # From every combo remove AnyPerk and remain only non-empty ones.
        # Use dict to remove duplicated combos and preserve order.
        combos: OrderedSet[PerkList] = {
            reduced_combo: None
            for combo in product(*perk_sets)
            if (reduced_combo := tuple(i for i in combo if i is not AnyPerk))
            }

        object.__setattr__(self, 'combos', combos)

    def to_dim_wishlist(self, trash: bool, /) -> str:
        item_hash = -self.item.hash if trash else self.item.hash

        if len(self.combos) < 2:
            if len(self.combos) == 1:
                combo = next(iter(self.combos))
                combo_str = ','.join(str(i.hash) for i in combo)
                combo_str = f'&perks={combo_str}'
            elif trash:
                combo_str = ''
            else:
                raise ValueError(f'impossible to wishlist {self.item.name!r} with zero combos')

            return (
                f'//notes:{self.notes}\n'
                f'dimwishlist:'
                f'item={item_hash}'
                f'{combo_str}'
            )

        lines = [f'//notes:{self.notes}']
        for combo in self.combos:
            combo_str = ','.join(str(i.hash) for i in combo)
            lines.append(f'dimwishlist:item={item_hash}&perks={combo_str}')

        return '\n'.join(lines)


def Roll(notes: str, /, *perk_lists: PerkList, is_trash: bool = False) -> AnnotatedRoll:
    """
    Creates an annotated roll definition from the given notes and perk lists.
    """
    return notes, is_trash, perk_lists


def is_annotated_roll(obj: Any, /) -> TypeGuard[AnnotatedRoll]:
    """
    Returns ``True`` if passed object is an annotated roll.
    """
    return (
            isinstance(obj, tuple)
            and len(obj) == 3
            and isinstance(obj[0], str)
            and isinstance(obj[1], bool)
            and isinstance(obj[2], tuple)
            and
            all(
                isinstance(ps, Sequence) and all(isinstance(i, Item) for i in ps)
                for ps in obj[2]
                )
    )


@dataclass(kw_only=True, slots=True)
class Wishlist:
    """
    A collection of roll definitions.
    """
    title: str
    description: str

    _wishes: list[WishlistEntry] = field(default_factory=list)
    _trashes: list[WishlistEntry] = field(default_factory=list)

    def add(
            self,
            item: Item,
            notes: str,
            /,
            *perk_lists: PerkList,
            is_trash: bool = False,
            ) -> None:
        """
        Adds a new roll definition for an item to this wishlist.
        Roll definition takes an arbitrary number of perk sets,
        then makes any possible combination of them.
        If ``is_trash`` is ``True``, then this roll is marked as trash.
        """
        # Wildcard cannot be used in trash rolls
        if item is AnyItem and is_trash:
            raise ValueError(f'AnyItem cannot be used inside trash rolls')

        # Clear strings
        notes = ' '.join(notes.split())
        if not notes:
            raise ValueError('notes cannot be empty')

        # Determine a list and add entry
        li = self._trashes if is_trash else self._wishes
        li.append(
            WishlistEntry(
                item=item,
                notes=notes,
                perk_lists=perk_lists,
                )
            )

    def add_many(self, item: Item, /, *rolls: AnnotatedRoll) -> None:
        """
        A convenient function to add several roll definitions
        with different notes to the same item.
        """
        for notes, is_trash, perk_sets in rolls:
            self.add(item, notes, *perk_sets, is_trash=is_trash)

    def to_dim_wishlist_file(self, filepath: str, /) -> None:
        """
        Writes this wishlist to a file.
        """

        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(f'title:{self.title}\n')
            if self.description:
                file.write(f'description:{self.description}\n')

            file.write(f'\n')

            added_rolls: Counter[tuple[Item, frozenset[Item]]] = Counter()
            self._write_wishlist_entry_list(file, added_rolls, trash_list=False)
            self._write_wishlist_entry_list(file, added_rolls, trash_list=True)

            errors = [
                ValueError(
                    f'{item.name} [{item.hash}] with '
                    f'{', '.join(perk.name for perk in combo)} '
                    f'is duplicated {count - 1} {'time' if count == 2 else 'times'}'
                    )
                for (item, combo), count in added_rolls.items()
                if count > 1
                ]
            if errors:
                raise ExceptionGroup('some perk combinations are duplicated', errors)

    def _write_wishlist_entry_list(
            self,
            file: TextIO,
            added_rolls: Counter[tuple[Item, frozenset[Item]]],
            /,
            trash_list: bool,
            ) -> None:
        """
        Writes the trash list or the wish list to the given file.
        Every roll encountered is added to the given set.
        """
        if trash_list:
            title = '// Trash rolls\n\n'
            entry_list = self._trashes
        else:
            title = '// Wish rolls\n\n'
            entry_list = self._wishes

        if entry_list:
            file.write(title)
            last_name = ''
            for entry in entry_list:
                for combo in entry.combos:
                    added_rolls[entry.item, frozenset(combo)] += 1

                curr_name = entry.item.name
                if curr_name != last_name:
                    file.write(f'// {curr_name}\n')
                    last_name = curr_name

                file.write(entry.to_dim_wishlist(trash_list))
                file.write('\n\n')


class RollDefinition:
    """
    A special class to verbosely define a set of rolls for specific items.
    """

    item: Item
    """
    An instance of :class:`Item` for which rolls are specified.
    Cannot be specified with ``items``.
    """
    items: Sequence[Item]
    """
    A set of instances of :class:`Item` for which rolls are specified.
    Cannot be specified with ``item``.
    """

    roll: AnnotatedRoll
    """
    One roll definition for the item. Cannot be specified with ``rolls``.
    """
    rolls: Sequence[AnnotatedRoll]
    """
    A set of roll definitions for the item. Cannot be specified with ``roll``.
    """

    def __init_subclass__(cls, /) -> None:
        item = getattr(cls, 'item', None)
        items = getattr(cls, 'items', None)

        if item and items:
            raise TypeError(f'items and item cannot be both specified in {cls.__name__}')
        elif item:
            if isinstance(item, Item):
                cls.items = (item,)
                del cls.item
            else:
                raise TypeError(f'item must be of type {Item.__name__}, got {item!r}')
        elif items:
            if not isinstance(items, tuple):
                # noinspection PyTypeChecker
                items = cls.items = tuple(items)

            if not all(isinstance(i, Item) for i in items):
                raise TypeError(f'items must be a sequence of {Item.__name__}, got {items!r}')
        else:
            raise TypeError(f'either items or item must be specified in {cls.__name__}')

        roll = getattr(cls, 'roll', None)
        rolls = getattr(cls, 'rolls', None)

        if roll and rolls:
            raise TypeError(f'rolls and roll cannot be both specified in {cls.__name__}')
        elif roll:
            if is_annotated_roll(roll):
                cls.rolls = (roll,)
                del cls.roll
            else:
                raise TypeError(f'roll must be of type {AnnotatedRoll.__name__}, got {roll!r}')
        elif rolls:
            if not isinstance(rolls, tuple):
                # noinspection PyTypeChecker
                rolls = cls.rolls = tuple(rolls)

            if not all(map(is_annotated_roll, rolls)):
                raise TypeError(
                    f'rolls must be a sequence of {AnnotatedRoll.__name__}, got {rolls!r}'
                    )
        else:
            cls.rolls = ()
