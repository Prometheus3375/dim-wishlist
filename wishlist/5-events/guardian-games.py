from wishlist import *


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
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Classic combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.ThreatDetector],
            [trait.Surrounded],
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
            [barrel.Smallbore, AnyPerk],
            [battery.TacticalBattery, AnyPerk],
            [trait.Overflow, trait.TripleTap],
            [trait.JoltingFeedback, trait.DetonatorBeam, trait.KillingTally],
            ),
        Roll(
            'Arc combo',
            [barrel.Smallbore, AnyPerk],
            [battery.TacticalBattery, AnyPerk],
            [trait.EddyCurrent],
            [trait.JoltingFeedback],
            ),
        ]


class Hullabaloo(RollDefinition):
    """
    Arc Drum Grenade Launcher, Compressed Wave Frame
    https://www.light.gg/db/items/2666273249
    """
    item = Item(name='Hullabaloo', hash=2666273249)
    rolls = [
        Roll(
            'Ad clear',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.Voltshot, trait.Demolitionist],
            [trait.ChainReaction, trait.OneForAll],
            ),
        Roll(
            'Damage dealing',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.EnviousAssassin],
            [trait.OneForAll],
            ),
        ]
