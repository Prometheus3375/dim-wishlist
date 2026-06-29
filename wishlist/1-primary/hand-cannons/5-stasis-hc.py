from wishlist import *


class Eyasluna(RollDefinition):
    """
    Stasis Hand Cannon, Adaptive Frame, Anti-Barrier
    Source: Grasp of Avarice
    https://www.light.gg/db/items/386864872
    https://destiny.report/w/386864872
    """
    item = Item('Eyasluna', hash=386864872)


class Judgment(RollDefinition):
    """
    Stasis Hand Cannon, Adaptive Frame, Anti-Barrier
    Source: Dungeon "Prophecy"
    https://www.light.gg/db/items/1567585973
    https://destiny.report/w/1567585973
    """
    item = Item('Judgment', hash=1567585973)


class LoudLullaby(RollDefinition):
    """
    Stasis Hand Cannon, Aggressive Frame, Anti-Unstoppable
    Source: The Moon
    https://www.light.gg/db/items/868076517
    https://destiny.report/w/868076517
    """
    item = Item('Loud Lullaby', hash=868076517)


class ModifiedB7Pistol(RollDefinition):
    """
    Stasis Hand Cannon, Dynamic Heat Weapon, Anti-Overload
    Source: Lawless Frontier
    https://www.light.gg/db/items/3146657388
    https://destiny.report/w/3146657388
    """
    items = [
        Item('Modified B-7 Pistol', hash=3146657388),
        Item('Modified B-7 Pistol', hash=1872906663),
        ]
    rolls = [
        Roll(
            'Stasis combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.Rimestealer],
            [trait.CrystallineCorpsebloom, trait.Headstone],
            ),
        Roll(
            'Precision combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.Firefly],
            [trait.Headstone],
            ),
        Roll(
            'Demolitionist',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.Demolitionist],
            [trait.CrystallineCorpsebloom, trait.Headstone],
            ),
        ]


class SolemnRemembrance(RollDefinition):
    """
    Stasis Hand Cannon, Precision Frame, Anti-Barrier
    Source: Competitive Crucible
    https://www.light.gg/db/items/4116518582
    https://destiny.report/w/4116518582
    """
    item = Item('Solemn Remembrance', hash=4116518582)
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.Headstone],
            [trait.Firefly],
            [grip.PolymerGrip, AnyPerk],
            ),
        Roll(
            'Stasis combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.Headstone],
            [trait.Rimestealer],
            [grip.PolymerGrip, AnyPerk],
            ),
        ]


class SomethingNew(RollDefinition):
    """
    Stasis Hand Cannon, Aggressive Frame, Anti-Unstoppable
    Source: Solstice
    https://www.light.gg/db/items/1705150753
    https://destiny.report/w/1705150753
    """
    items = [
        Item('Something New', hash=1705150753),
        Item('Something New', hash=2877020298),
        ]


class SpareRations(RollDefinition):
    """
    Stasis Hand Cannon, Lightweight Frame, Anti-Overload
    Source: Gambit
    https://www.light.gg/db/items/810474119
    https://destiny.report/w/810474119
    """
    item = Item('Spare Rations', hash=810474119)


class TripleLaureate(RollDefinition):
    """
    Stasis Hand Cannon, Spread Shot, Anti-Overload
    Source: Guardian Games
    https://www.light.gg/db/items/1605599021
    https://destiny.report/w/1605599021
    """
    items = [
        Item('Triple Laureate', hash=1605599021),
        Item('Triple Laureate', hash=2908653246),
        ]
    rolls = [
        Roll(
            'Super roll',
            [barrel.BarrelShroud, AnyPerk],
            [magazine.AppendedMag, AnyPerk],
            [trait.GraveRobber],
            [trait.AmbitiousAssassin],
            [trait.CrystallineCorpsebloom],
            [trait.TrenchBarrel],
            [trait.OneTwoPunch],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Melee damage increase',
            [barrel.BarrelShroud, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.GraveRobber],
            [trait.OneTwoPunch],
            ),
        Roll(
            'Ad clear',
            [barrel.BarrelShroud, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.CrystallineCorpsebloom],
            [trait.TrenchBarrel, trait.ChaosReshaped],
            ),
        ]


class Vulpecula(RollDefinition):
    """
    Stasis Hand Cannon, Precision Frame, Anti-Barrier
    Source: The Shattered Throne
    https://www.light.gg/db/items/3245446311
    https://destiny.report/w/3245446311
    """
    item = Item('Vulpecula', hash=3245446311)
