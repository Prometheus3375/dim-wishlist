from wishlist import *


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
            [barrel.FlutedBarrel, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.ThreatDetector],
            [trait.OneTwoPunch],
            ),
        Roll(
            'Damage dealing',
            [barrel.FlutedBarrel, AnyPerk],
            [magazine.AppendedMag, AnyPerk],
            [trait.ThreatDetector],
            [trait.Surrounded],
            ),
        Roll(
            'Ad clear',
            [barrel.FlutedBarrel, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.ThreatDetector],
            [trait.Incandescent],
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
        [barrel.Smallbore, AnyPerk],
        [battery.LightBattery, AnyPerk],
        [trait.Subsistence],
        [trait.Redirection, trait.DetonatorBeam],
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
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.AssaultMag, AnyPerk],
            [trait.Rimestealer],
            [trait.Headstone],
            ),
        Roll(
            'Chill Clip',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.AssaultMag, AnyPerk],
            [trait.LeadFromGold],
            [trait.ChillClip],
            ),
        Roll(
            'Damage dealing',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.AssaultMag, AnyPerk],
            [trait.RapidHit, trait.LeadFromGold],
            [trait.PrecisionInstrument],
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
            [blade.HonedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.AssassinsBlade],
            [trait.EagerEdge],
            ),
        Roll(
            'Ad clear',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.RelentlessStrikes],
            [trait.ChainReaction],
            ),
        Roll(
            'Damage dealing',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.RelentlessStrikes],
            [trait.Surrounded, trait.ElementalHoning],
            ),
        ]
