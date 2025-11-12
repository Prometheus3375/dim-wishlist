from wishlist import *


class PhoneutriaFera(RollDefinition):
    """
    Solar hand cannon, Spread Shot
    https://www.light.gg/db/items/3496887154
    """
    items = [
        Item('Phoneutria Fera', hash=3496887154),
        Item('Phoneutria Fera', hash=3804242792),
        Item('Phoneutria Fera', hash=3804242793),
        Item('Phoneutria Fera', hash=3804242794),
        Item('Phoneutria Fera', hash=3804242795),
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
        Item('Ribbontail', hash=3576134513),
        Item('Ribbontail', hash=407150808),
        Item('Ribbontail', hash=407150809),
        Item('Ribbontail', hash=407150810),
        Item('Ribbontail', hash=407150811),
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
        Item('Trachinus', hash=3635232671),
        Item('Trachinus', hash=2888021252),
        Item('Trachinus', hash=2888021253),
        Item('Trachinus', hash=2888021254),
        Item('Trachinus', hash=2888021255),
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
            [trait.RapidHit, trait.LeadFromGold],
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


class RomanticDeath(RollDefinition):
    """
    Void Breechloaded Grenade Launcher, Wave Frame
    https://www.light.gg/db/items/4169082039
    """
    items = [
        Item('Romantic Death', hash=4169082039),
        Item('Romantic Death', hash=2979965244),
        Item('Romantic Death', hash=2979965245),
        Item('Romantic Death', hash=2979965246),
        Item('Romantic Death', hash=2979965247),
        ]
    rolls = [
        Roll(
            'Ad clear',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.FeedingFrenzy],
            [trait.DestabilizingRounds, trait.OneForAll, trait.ChainReaction],
            ),
        Roll(
            'Void combo',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        ]


# Heavy


class Synanceia(RollDefinition):
    """
    Solar Sword, Wave Sword Frame
    https://www.light.gg/db/items/1823308496
    """
    items = [
        Item('Synanceia', hash=1823308496),
        Item('Synanceia', hash=2765451288),
        Item('Synanceia', hash=2765451289),
        Item('Synanceia', hash=2765451290),
        Item('Synanceia', hash=2765451291),
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


class FoldedRoot(RollDefinition):
    """
    Void Rocket Launcher, Aggressive Frame
    https://www.light.gg/db/items/2725894221
    """
    items = [
        Item('Folded Root', hash=2725894221),
        Item('Folded Root', hash=3184457500),
        Item('Folded Root', hash=3184457501),
        Item('Folded Root', hash=3184457502),
        Item('Folded Root', hash=3184457503),
        ]
    roll = Roll(
        'Damage dealing',
        [launcher_barrel.QuickLaunch, AnyPerk],
        [magazine.ImpactCasing, AnyPerk],
        [trait.ClusterBomb],
        [trait.LastingImpression, trait.Frenzy],
        )


class Submersion(RollDefinition):
    """
    Stasis Crossbow, High-Impact Frame
    https://www.light.gg/db/items/3524386983
    """
    items = [
        Item('Submersion', hash=3524386983),
        Item('Submersion', hash=1724104236),
        ]
    rolls = [
        Roll(
            'Damage dealing',
            [rail.LowProfileRail, AnyPerk],
            [bolt.HeavyBolts, AnyPerk],
            [trait.ImpulseAmplifier, trait.BoltScavenger, trait.AutoLoadingHolster],
            [trait.AggregateCharge, trait.HighGround, trait.FiringLine],
            ),
        Roll(
            """
            Chill Clip.
            Both Serrated Bolts and Explosive Bolts shatter targets frozen by Chill Clip.
            """,
            [rail.LowProfileRail, AnyPerk],
            [bolt.SerratedBolts, bolt.ExplosiveBolts, bolt.HeavyBolts, AnyPerk],
            [trait.ImpulseAmplifier, trait.BoltScavenger, trait.AutoLoadingHolster],
            [trait.ChillClip],
            ),
        Roll(
            """
            Headstone.
            Explosive Bolts do not explode Stasis crystals on Ultimatum.
            They also prevent killing Elite combatants with precision hits.
            Anyway, crystals can explode instantly because of the movement of a killing bolt.
            """,
            [rail.LowProfileRail, AnyPerk],
            [bolt.HeavyBolts, AnyPerk],
            [trait.ImpulseAmplifier, trait.BoltScavenger, trait.AutoLoadingHolster],
            [trait.Headstone],
            ),
        ]
