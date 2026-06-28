from wishlist import *


class AllOrNothing(RollDefinition):
    """
    Strand Pulse Rifle, Dynamic Heat Weapon, Anti-Overload
    Source: Renegades
    https://www.light.gg/db/items/3984776322
    https://destiny.report/w/3984776322
    """
    items = [
        Item('All or Nothing', hash=3984776322),
        Item('All or Nothing', hash=2023002233),
        ]
    rolls = [
        Roll(
            'Precision combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.Firefly],
            [trait.Hatchling],
            ),
        ]


class LastThursday(RollDefinition):
    """
    Strand Pulse Rifle, Adaptive Frame, Anti-Barrier
    Source: Exploring Kepler
    https://www.light.gg/db/items/3813721211
    https://destiny.report/w/3813721211
    """
    item = Item('Last Thursday', hash=3813721211)
    rolls = [
        Roll(
            'Slice',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Strategist],
            [trait.Slice],
            ),
        Roll(
            'Hatchling',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Demolitionist, trait.Strategist],
            [trait.Hatchling],
            ),
        ]
