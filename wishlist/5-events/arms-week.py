from database import *


class PhoneutriaFera(RollDefinition):
    """
    Solar hand cannon, Spread Shot
    https://www.light.gg/db/items/3496887154
    """
    items = [
        Item(name='Phoneutria Fera', hash=3496887154),
        Item(name='Phoneutria Fera', hash=3804242792),
        Item(name='Phoneutria Fera', hash=3804242793),
        ]
    rolls = [
        Roll(
            'Melee damage increase',
            [barrels.FlutedBarrel, AnyPerk],
            [magazines.TacticalMag, AnyPerk],
            [traits.ThreatDetector],
            [traits.OneTwoPunch],
            ),
        Roll(
            'Damage dealing',
            [barrels.FlutedBarrel, AnyPerk],
            [magazines.AppendedMag, AnyPerk],
            [traits.ThreatDetector],
            [traits.Surrounded],
            ),
        Roll(
            'Ad clear',
            [barrels.FlutedBarrel, AnyPerk],
            [magazines.TacticalMag, AnyPerk],
            [traits.ThreatDetector],
            [traits.Incandescent],
            ),
        ]


# Special


class Ribbontail(RollDefinition):
    """
    Strand Trace Rifle, Adaptive Frame
    https://www.light.gg/db/items/3576134513
    """
    items = [
        Item(name='Ribbontail', hash=3576134513),
        Item(name='Ribbontail', hash=407150810),
        Item(name='Ribbontail', hash=407150811),
        ]
    roll = Roll(
        'Ad clear',
        [barrels.Smallbore, AnyPerk],
        [batteries.LightBattery, AnyPerk],
        [traits.Subsistence],
        [traits.Redirection, traits.DetonatorBeam],
        )


class Trachinus(RollDefinition):
    """
    Stasis Shotgun, Rapid Fire Slug
    https://www.light.gg/db/items/3635232671
    """
    items = [
        Item(name='Trachinus', hash=3635232671),
        Item(name='Trachinus', hash=2888021252),
        Item(name='Trachinus', hash=2888021253),
        ]


# Heavy


class Synanceia(RollDefinition):
    """
    Solar Sword, Wave Sword Frame
    https://www.light.gg/db/items/1823308496
    """
    items = [
        Item(name='Synanceia', hash=1823308496),
        Item(name='Synanceia', hash=2765451290),
        Item(name='Synanceia', hash=2765451291),
        ]
    rolls = [
        Roll(
            'Ad clear',
            [blades.JaggedEdge, AnyPerk],
            [guards.SwordmastersGuard, AnyPerk],
            [traits.AssassinsBlade, traits.RelentlessStrikes],
            [traits.ChainReaction],
            ),
        Roll(
            'Damage dealing',
            [blades.JaggedEdge, AnyPerk],
            [guards.SwordmastersGuard, AnyPerk],
            [traits.RelentlessStrikes],
            [traits.Surrounded],
            ),
        ]
