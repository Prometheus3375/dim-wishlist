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
        Item(name='Phoneutria Fera', hash=3804242794),
        Item(name='Phoneutria Fera', hash=3804242795),
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
        Item(name='Ribbontail', hash=407150808),
        Item(name='Ribbontail', hash=407150809),
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
        Item(name='Trachinus', hash=2888021254),
        Item(name='Trachinus', hash=2888021255),
        ]
    rolls = [
        Roll(
            'Stasis combo',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.AssaultMag, AnyPerk],
            [traits.Rimestealer],
            [traits.Headstone],
            ),
        Roll(
            'Chill Clip',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.AssaultMag, AnyPerk],
            [traits.LeadFromGold],
            [traits.ChillClip],
            ),
        Roll(
            'Damage dealing',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.AssaultMag, AnyPerk],
            [traits.RapidHit, traits.LeadFromGold],
            [traits.PrecisionInstrument],
            ),
        ]


# Heavy


class Synanceia(RollDefinition):
    """
    Solar Sword, Wave Sword Frame
    https://www.light.gg/db/items/1823308496
    """
    items = [
        Item(name='Synanceia', hash=1823308496),
        Item(name='Synanceia', hash=2765451288),
        Item(name='Synanceia', hash=2765451289),
        Item(name='Synanceia', hash=2765451290),
        Item(name='Synanceia', hash=2765451291),
        ]
    rolls = [
        Roll(
            'Movement',
            [blades.HonedEdge, AnyPerk],
            [guards.SwordmastersGuard, AnyPerk],
            [traits.AssassinsBlade],
            [traits.EagerEdge],
            ),
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
