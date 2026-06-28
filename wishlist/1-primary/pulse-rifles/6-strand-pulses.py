from wishlist import *


class AishasCare(RollDefinition):
    """
    Strand Pulse Rifle, Heavy Burst, Anti-Unstoppable
    Source: Unspecified
    https://www.light.gg/db/items/3614211586
    https://destiny.report/w/3614211586
    """
    item = Item("Aisha's Care", hash=3614211586)


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


class BelisariusD(RollDefinition):
    """
    Strand Pulse Rifle, Aggressive Burst, Anti-Unstoppable
    Source: Unspecified
    https://www.light.gg/db/items/747743637
    https://destiny.report/w/747743637
    """
    item = Item('Belisarius-D', hash=747743637)


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


class Nightshade(RollDefinition):
    """
    Strand Pulse Rifle, Lightweight Frame, Anti-Overload
    Source: Unspecified
    https://www.light.gg/db/items/34731066
    https://destiny.report/w/34731066
    """
    items = [
        Item('Nightshade', hash=34731066),
        Item('Nightshade', hash=1559068369),
        ]


class Relentless(RollDefinition):
    """
    Strand Pulse Rifle, High-Impact Frame, Anti-Unstoppable
    Source: "Prophecy" Dungeon
    https://www.light.gg/db/items/2831259643
    https://destiny.report/w/2831259643
    """
    item = Item('Relentless', hash=2831259643)
