from wishlist import *


class HighAlbedo(RollDefinition):
    """
    Kinetic Sidearm, Micro-Missile Frame, Anti-Unstoppable
    Source: Europa
    https://www.light.gg/db/items/2662459958
    https://destiny.report/w/2662459958
    """
    item = Item('High Albedo', hash=2662459958)


class IndebtedKindness(RollDefinition):
    """
    Arc Sidearm, Micro-Missile Frame, Anti-Unstoppable
    Source: Warlord's Ruin
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


class AberrantAction(RollDefinition):
    """
    Solar Sidearm, Micro-Missile Frame, Anti-Unstoppable, Craftable
    Source: Exotic mission "Encore"
    https://www.light.gg/db/items/2198166292
    https://destiny.report/w/2198166292
    """
    item = Item('Aberrant Action', hash=2198166292)


class ReturnedMemory(RollDefinition):
    """
    Solar Sidearm, Micro-Missile Frame, Anti-Unstoppable
    Source: Lord Shaxx
    https://www.light.gg/db/items/4049127142
    https://destiny.report/w/4049127142
    """
    item = Item('Returned Memory', hash=4049127142)
    rolls = [
        Roll(
            """
            PvE.
            Note for Redirection: stacks are granted and consumed for every hit,
            i.e., 2 * (1 [impact] + #[targets hit by an explosion]).
            If a target dies to impact, explosion doesn't hit it.
            Multiplier 2 is replaced with 3 for consumption if perk is not enhanced.
            """,
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.HealClip, trait.ImpulseAmplifier],
            [trait.Incandescent, trait.OneForAll, trait.Redirection],
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
    Source: Lord Saladin
    https://www.light.gg/db/items/247984828
    https://destiny.report/w/247984828
    """
    item = Item("Tinasha's Mastery", hash=247984828)


class TheCall(RollDefinition):
    """
    Strand Sidearm, Micro-Missile Frame, Anti-Unstoppable, Craftable
    Source: The Pale Heart
    https://www.light.gg/db/items/3947966653
    https://destiny.report/w/3947966653
    """
    item = Item('The Call', hash=3947966653)
