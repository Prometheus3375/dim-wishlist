from wishlist import *


class HighAlbedo(RollDefinition):
    """
    Kinetic Sidearm, Micro-Missile Frame, Anti-Unstoppable
    Source: Unspecified
    https://www.light.gg/db/items/2662459958
    https://destiny.report/w/2662459958
    """
    item = Item('High Albedo', hash=2662459958)


class IndebtedKindness(RollDefinition):
    """
    Arc Sidearm, Micro-Missile Frame, Anti-Unstoppable
    Source: "Warlord's Ruin" Dungeon
    https://www.light.gg/db/items/2554513694
    https://destiny.report/w/2554513694
    """
    item = Item('Indebted Kindness', hash=2554513694)


class Unfall(RollDefinition):
    """
    Arc Sidearm, Together Forever, Anti-Overload
    Source: Commander Zavala
    https://www.light.gg/db/items/738446555
    https://destiny.report/w/738446555
    """
    item = Item('Unfall', hash=738446555)
    rolls = [
        Roll(
            'Ad clear',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.ImpulseAmplifier],
            [trait.OneForAll, trait.JoltingFeedback],
            ),
        Roll(
            'Deconstruct',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.ImpulseAmplifier],
            [trait.Deconstruct],
            ),
        ]


class LotusEater(RollDefinition):
    """
    Void Sidearm, Micro-Missile Frame, Anti-Unstoppable
    Source: Pinnacle Ops
    https://www.light.gg/db/items/924095500
    https://destiny.report/w/924095500
    """
    items = [
        Item('Lotus-Eater', hash=924095500),
        Item('Lotus-Eater', hash=837298567),
        ]


class TinashasMastery(RollDefinition):
    """
    Stasis Sidearm, Micro-Missile Frame, Anti-Unstoppable
    Source: Unspecified
    https://www.light.gg/db/items/247984828
    https://destiny.report/w/247984828
    """
    item = Item("Tinasha's Mastery", hash=247984828)
