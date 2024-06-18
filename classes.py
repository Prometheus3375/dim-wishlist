from collections.abc import Set
from dataclasses import dataclass, field
from itertools import product
from typing import ClassVar, Self


@dataclass(frozen=True, kw_only=True, slots=True)
class Item:
    """
    A common class for armor, weapons, traits, categories, etc.
    """
    __hash2item: ClassVar[dict[int, Self]] = {}

    name: str
    hash: int
    icon: str | None = None

    # noinspection PyDataclass
    def __post_init__(self, /) -> None:
        existing = self.__hash2item.get(self.hash)
        if existing:
            raise ValueError(f'Item with hash {self.hash} already exists')

        self.__hash2item[self.hash] = self

    @classmethod
    def from_hash(cls, hash_: int, /) -> Self | None:
        """
        Returns an existing item by passed hash value
        or ``None`` if no item with such hash exists.
        """
        return cls.__hash2item.get(hash_)

    def __eq__(self, other: Self, /) -> bool:
        return self.hash == other.hash if isinstance(other, Item) else False

    def __ne__(self, other: Self, /) -> bool:
        return self.hash != other.hash if isinstance(other, Item) else True

    def __hash__(self, /) -> int:
        return self.hash


@dataclass(frozen=True, kw_only=True, slots=True)
class WishlistEntry:
    """
    A separate entry of a wishlist.
    """
    item: Item
    perk_sets: tuple[Set[Item], ...]
    notes: str

    def to_dim_wishlist(self, trash: bool, /) -> str:
        combos: list[tuple[Item, ...]] = list(product(*self.perk_sets))
        item_hash = -self.item.hash if trash else self.item.hash

        if len(combos) < 2:
            if len(combos) == 1:
                combo_str = ','.join(str(i.hash) for i in combos[0])
                combo_str = f'&perks={combo_str}'
            else:
                combo_str = ''

            return (
                f'//notes:{self.notes}\n'
                f'dimwishlist:'
                f'item={item_hash}'
                f'{combo_str}'
            )

        lines = [f'//notes:{self.notes}']
        for combo in combos:
            combo_str = ','.join(str(i.hash) for i in combo)
            lines.append(f'dimwishlist:item={item_hash}&perks={combo_str}')

        return '\n'.join(lines)


type AnnotatedRoll = tuple[str, tuple[Set[Item], ...]]


def roll(notes: str, /, *perk_sets: Set[Item]) -> AnnotatedRoll:
    """
    Creates an annotated roll definition from the given notes and perk sets.
    """
    return notes, perk_sets


@dataclass(kw_only=True, slots=True)
class Wishlist:
    """
    A collection of roll definitions.
    """
    title: str
    description: str

    _wishes: list[WishlistEntry] = field(default_factory=list)
    _trashes: list[WishlistEntry] = field(default_factory=list)

    def add(self, item: Item, notes: str, /, *perk_sets: Set[Item], trash: bool = False) -> None:
        """
        Adds a new roll definition for an item to this wishlist.
        Roll definition takes an arbitrary number of perk sets,
        then makes any possible combination of them.
        If ``trash`` is ``True``, then this roll is marked as trash.
        """
        from database.items import AnyItem

        # Wildcard cannot be used in trash rolls
        if item is AnyItem and trash:
            raise ValueError(f'AnyItem cannot be used inside trash rolls')

        # Clear strings
        notes = ' '.join(notes.split())
        if not notes:
            raise ValueError('Notes cannot be empty')

        # Remove empty sets
        perk_sets = tuple(filter(None, perk_sets))
        # Determine a list and add entry
        li = self._trashes if trash else self._wishes
        li.append(
            WishlistEntry(
                item=item,
                perk_sets=perk_sets,
                notes=notes,
                )
            )

    def add_many(self, item: Item, /, *rolls: AnnotatedRoll, trash: bool = False) -> None:
        """
        A convenient function to add several roll definitions
        with different notes to the same item.
        Every roll definition takes an arbitrary number of perk sets,
        then makes any possible combination of them.
        If ``trash`` is ``True``, then **all** rolls are marked as trash.
        """
        for notes, perk_sets in rolls:
            self.add(item, notes, *perk_sets, trash=trash)

    def to_dim_wishlist_file(self, filepath: str, /) -> None:
        """
        Writes this wishlist to a file.
        """
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(f'title:{self.title}\n')
            if self.description:
                file.write(f'description:{self.description}\n')

            file.write(f'\n')

            if self._wishes:
                file.write('// Wish rolls\n\n')
                for entry in self._wishes:
                    file.write(entry.to_dim_wishlist(False))
                    file.write('\n\n')

            if self._trashes:
                file.write('// Trash rolls\n\n')
                for entry in self._trashes:
                    file.write(entry.to_dim_wishlist(True))
                    file.write('\n\n')


__all__ = 'Item', 'Wishlist', 'roll'
