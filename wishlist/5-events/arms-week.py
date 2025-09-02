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
