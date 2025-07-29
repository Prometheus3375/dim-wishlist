from database import *


class Taraxippos(RollDefinition):
    """
    Strand Scout Rifle, Lightweight Frame
    https://www.light.gg/db/items/2595813005
    """
    item = Item(name='Taraxippos', hash=2595813005)


class Title(RollDefinition):
    """
    Void Submachine Gun, Aggressive Frame
    https://www.light.gg/db/items/55393445
    """
    item = Item(name='The Title', hash=55393445)
    rolls = [
        Roll(
            'Void combo',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.RepulsorBrace],
            [traits.DestabilizingRounds],
            ),
        Roll(
            'Classic combo',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.ThreatDetector],
            [traits.Surrounded],
            ),
        ]


class Keraunios(RollDefinition):
    """
    Arc Trace Rifle, Adaptive Frame
    https://www.light.gg/db/items/2029899814
    """
    item = Item(name='Keraunios', hash=2029899814)
    rolls = [
        Roll(
            'PvE',
            [barrels.Smallbore, AnyPerk],
            [batteries.EnhancedBattery, batteries.TacticalBattery, AnyPerk],
            [traits.Overflow, traits.TripleTap],
            [traits.JoltingFeedback, traits.DetonatorBeam, traits.KillingTally],
            ),
        Roll(
            'Arc combo',
            [barrels.Smallbore, AnyPerk],
            [batteries.EnhancedBattery, batteries.TacticalBattery, AnyPerk],
            [traits.EddyCurrent],
            [traits.JoltingFeedback],
            ),
        ]


class Hullabaloo(RollDefinition):
    """
    Arc Heavy Grenade Launcher, Compressed Wave Frame
    https://www.light.gg/db/items/2666273249
    """
    item = Item(name='Hullabaloo', hash=2666273249)
    rolls = [
        Roll(
            'Ad clear',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.HighVelocityRounds],
            [traits.Voltshot, traits.Demolitionist],
            [traits.ChainReaction, traits.OneForAll],
            ),
        Roll(
            'Damage dealing',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.HighVelocityRounds],
            [traits.EnviousAssassin],
            [traits.OneForAll],
            ),
        ]
