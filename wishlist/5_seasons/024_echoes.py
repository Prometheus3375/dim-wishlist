from database import *


class Breachlight(RollDefinition):
    """
    Strand Sidearm, Heavy Burst
    https://www.light.gg/db/items/2328923181
    """
    item = Item(name='Breachlight', hash=2328923181)
    _mags = [magazines.FlaredMagwell, magazines.TacticalMag, AnyPerk]
    rolls = [
        Roll(
            'Hatchling',
            [barrels.ArrowheadBrake, AnyPerk],
            _mags,
            [traits.Demolitionist, traits.Pugilist, traits.ThreatDetector],
            [traits.Hatchling],
            ),
        Roll(
            """
            Desperate Measures.
            For this weapon Desperate Measures is better than Swashbuckler and Adrenaline Junkie
            because DM can be activated while stowed and lasts longer
            """,
            [barrels.ArrowheadBrake, AnyPerk],
            [traits.Demolitionist, traits.Pugilist, traits.ThreatDetector],
            [traits.DesperateMeasures],
            ),
        ]


class PatronOfLostCauses(RollDefinition):
    """
    Kinetic Scout Rifle, Lightweight Frame
    https://www.light.gg/db/items/2249996761
    """
    item = Item(name='Patron of Lost Causes', hash=2249996761)
    rolls = [
        Roll(
            'Classic PvE combo for a scout rifle',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, magazines.TacticalMag, AnyPerk],
            [traits.RapidHit],
            [traits.KineticTremors, traits.ExplosivePayload],
            ),
        Roll(
            'Strategist',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, magazines.TacticalMag, AnyPerk],
            [traits.Strategist],
            [traits.KineticTremors, traits.ExplosivePayload],
            ),
        ]


class PerfectParadox(RollDefinition):
    """
    Kinetic Shotgun, Rapid-Fire Frame
    https://www.light.gg/db/items/1298672084
    """
    item = Item(name='Perfect Paradox', hash=1298672084)
    _barrels = [barrels.BarrelShroud, barrels.CorkscrewRifling, barrels.Smallbore]
    _mags = [magazines.TacticalMag, magazines.LightMag]
    rolls = [
        Roll(
            """
            Melee damage increase.
            Ready/Stow speed-wise Pugilist is better than Threat Detector x1,
            but is worse than Threat Detector x2
            """,
            _barrels,
            _mags,
            [traits.Pugilist, traits.ThreatDetector],
            [traits.OneTwoPunch],
            ),
        Roll(
            'Damage dealing',
            _barrels,
            _mags,
            [traits.DualLoader, traits.Pugilist],
            [traits.TrenchBarrel],
            )
        ]


class MartyrsRetribution(RollDefinition):
    """
    Solar Breechloaded Grenade Launcher, Wave Frame
    https://www.light.gg/db/items/2584830733
    """
    item = Item(name="Martyr's Retribution", hash=2584830733)
    rolls = [
        Roll(
            """
            Incandescent.
            The preferred roll as there is already a Solar Wave Frame GL
            with damage increase perks: Explosive Personality with One for All
            """,
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.HighVelocityRounds],
            [traits.Demolitionist, traits.HealClip],
            [traits.Incandescent],
            ),
        Roll(
            'Clip combo',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.HighVelocityRounds],
            [traits.HealClip],
            [traits.KillClip],
            ),
        Roll(
            """
            Adrenaline Junkie.
            For this weapon Adrenaline Junkie is better than Desperate Measures
            because AJ can achieve max stacks easily with 1-2 shots,
            while DM requires two ability kills
            """,
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.HighVelocityRounds],
            [traits.Demolitionist, traits.HealClip],
            [traits.AdrenalineJunkie],
            ),
        ]


class LineInTheSand(RollDefinition):
    """
    Arc Linear Fusion Rifle, Precision Frame
    https://www.light.gg/db/items/2450049485
    """
    item = Item(name='Line in the Sand', hash=2450049485)
    roll = Roll(
        'Damage dealing',
        [barrels.ArrowheadBrake, AnyPerk],
        [batteries.AcceleratedCoils, AnyPerk],
        [traits.Demolitionist, traits.ClownCartridge],
        [traits.BaitAndSwitch],
        )
