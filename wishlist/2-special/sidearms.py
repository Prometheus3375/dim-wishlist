from wishlist import *

default_barrels = [launcher_barrel.VolatileLaunch, AnyPerk]
default_mags = [magazine.TacticalMag, AnyPerk]


class HighAlbedo(RollDefinition):
    """
    Kinetic Sidearm, Micro-Missile Frame, Anti-Unstoppable
    Source: Europa
    https://www.light.gg/db/items/2662459958
    https://destiny.report/w/2662459958
    """
    item = Item('High Albedo', hash=2662459958)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.AutoLoadingHolster],
            [trait.ImpulseAmplifier],
            [trait.BlastDistributor],
            [trait.KineticTremors],
            [trait.OneForAll],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.ImpulseAmplifier, trait.AutoLoadingHolster],
            [trait.OneForAll, trait.KineticTremors],
            ),
        Roll(
            'Blast Distributor',
            default_barrels,
            default_mags,
            [trait.BlastDistributor],
            [trait.OneForAll, trait.KineticTremors],
            ),
        ]


class IndebtedKindness(RollDefinition):
    """
    Arc Sidearm, Micro-Missile Frame, Anti-Unstoppable
    Source: Dungeon "Warlord's Ruin"
    https://www.light.gg/db/items/2554513694
    https://destiny.report/w/2554513694
    """
    item = Item('Indebted Kindness', hash=2554513694)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.ImpulseAmplifier],
            [trait.Deconstruct],
            [trait.AirTrigger],
            [trait.GearShift],
            [trait.ChainReaction],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.AirTrigger, trait.ImpulseAmplifier],
            [trait.GearShift, trait.ChainReaction],
            ),
        ]


class Unfall(RollDefinition):
    """
    Arc Sidearm, Together Forever, Anti-Overload
    Source: Commander Zavala; Tenet of Bravery
    https://www.light.gg/db/items/738446555
    https://destiny.report/w/738446555
    """
    item = Item('Unfall', hash=738446555)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.ImpulseAmplifier],
            [trait.JoltingFeedback],
            [trait.Deconstruct],
            [trait.OneForAll],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.ImpulseAmplifier],
            [trait.OneForAll, trait.JoltingFeedback],
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
    roll = Roll(
        'Solar combo',
        default_barrels,
        default_mags,
        [trait.HealClip],
        [trait.Incandescent],
        )


class ReturnedMemory(RollDefinition):
    """
    Solar Sidearm, Micro-Missile Frame, Anti-Unstoppable
    Source: Lord Shaxx; Tenet of Bravery
    https://www.light.gg/db/items/4049127142
    https://destiny.report/w/4049127142
    """
    item = Item('Returned Memory', hash=4049127142)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.ImpromptuAmmunition],
            [trait.HealClip],
            [trait.BlastDistributor],
            [trait.Incandescent],
            [trait.OneForAll],
            [trait.Redirection],
            ),
        Roll(
            """
            Ad clear.
            Note for Redirection: stacks are granted and consumed for every hit,
            i.e., 2 * (1 [impact] + #[targets hit by an explosion]).
            If a target dies to impact, explosion doesn't hit it.
            Multiplier 2 is replaced with 3 for consumption if perk is not enhanced.
            """,
            default_barrels,
            default_mags,
            [trait.HealClip, trait.ImpromptuAmmunition],
            [trait.Incandescent, trait.OneForAll, trait.Redirection],
            ),
        Roll(
            'Blast Distributor',
            default_barrels,
            default_mags,
            [trait.BlastDistributor],
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
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Reconstruction],
            [trait.RepulsorBrace],
            [trait.AirTrigger],
            [trait.DestabilizingRounds],
            [trait.CollectiveAction],
            [trait.WitheringGaze],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.AirTrigger, trait.Reconstruction],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Void combo',
            default_barrels,
            default_mags,
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        ]


class TinashasMastery(RollDefinition):
    """
    Stasis Sidearm, Micro-Missile Frame, Anti-Unstoppable
    Source: Lord Saladin
    https://www.light.gg/db/items/247984828
    https://destiny.report/w/247984828
    """
    item = Item("Tinasha's Mastery", hash=247984828)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.AirTrigger],
            [trait.Deconstruct],
            [trait.ChillClip],
            [trait.OneForAll],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.AirTrigger],
            [trait.ChillClip, trait.OneForAll],
            ),
        ]


class TheCall(RollDefinition):
    """
    Strand Sidearm, Micro-Missile Frame, Anti-Unstoppable, Craftable
    Source: The Pale Heart
    https://www.light.gg/db/items/3947966653
    https://destiny.report/w/3947966653
    """
    item = Item('The Call', hash=3947966653)
    is_chosen = True
    roll = Roll(
        'Ad clear',
        default_barrels,
        default_mags,
        [trait.Reconstruction],
        [trait.Hatchling],
        )
