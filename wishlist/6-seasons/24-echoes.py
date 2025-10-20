from wishlist import *


class Breachlight(RollDefinition):
    """
    Strand Sidearm, Heavy Burst
    https://www.light.gg/db/items/2328923181
    """
    item = Item('Breachlight', hash=2328923181)
    _mags = [magazine.FlaredMagwell, magazine.TacticalMag, AnyPerk]
    rolls = [
        Roll(
            'Hatchling',
            [barrel.ArrowheadBrake, AnyPerk],
            _mags,
            [trait.Demolitionist, trait.Pugilist, trait.ThreatDetector],
            [trait.Hatchling],
            ),
        Roll(
            """
            Desperate Measures.
            For this weapon Desperate Measures is better than Swashbuckler and Adrenaline Junkie
            because DM can be activated while stowed and lasts longer
            """,
            [barrel.ArrowheadBrake, AnyPerk],
            _mags,
            [trait.Demolitionist, trait.Pugilist, trait.ThreatDetector],
            [trait.DesperateMeasures],
            ),
        ]


class PatronOfLostCauses(RollDefinition):
    """
    Kinetic Scout Rifle, Lightweight Frame
    https://www.light.gg/db/items/2249996761
    """
    item = Item('Patron of Lost Causes', hash=2249996761)
    rolls = [
        Roll(
            'Classic PvE combo for a scout rifle',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, magazine.TacticalMag, AnyPerk],
            [trait.RapidHit],
            [trait.KineticTremors, trait.ExplosivePayload],
            ),
        Roll(
            'Strategist',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, magazine.TacticalMag, AnyPerk],
            [trait.Strategist],
            [trait.KineticTremors, trait.ExplosivePayload],
            ),
        ]


class PerfectParadox(RollDefinition):
    """
    Kinetic Shotgun, Rapid-Fire Frame
    https://www.light.gg/db/items/1298672084
    """
    item = Item('Perfect Paradox', hash=1298672084)
    _barrels = [barrel.BarrelShroud, barrel.CorkscrewRifling, barrel.Smallbore]
    _mags = [magazine.TacticalMag, magazine.LightMag]
    rolls = [
        Roll(
            """
            Melee damage increase.
            Ready/Stow speed-wise Pugilist is better than Threat Detector x1,
            but is worse than Threat Detector x2
            """,
            _barrels,
            _mags,
            [trait.Pugilist, trait.ThreatDetector],
            [trait.OneTwoPunch],
            ),
        Roll(
            'Damage dealing',
            _barrels,
            _mags,
            [trait.DualLoader, trait.Pugilist],
            [trait.TrenchBarrel],
            )
        ]


class MartyrsRetribution(RollDefinition):
    """
    Solar Breechloaded Grenade Launcher, Wave Frame
    https://www.light.gg/db/items/2584830733
    """
    item = Item("Martyr's Retribution", hash=2584830733)
    rolls = [
        Roll(
            """
            Incandescent.
            The preferred roll as there is already a Solar Wave Frame GL
            with damage increase perks: Explosive Personality with One for All
            """,
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.Demolitionist, trait.HealClip],
            [trait.Incandescent],
            ),
        Roll(
            'Clip combo',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.HealClip],
            [trait.KillClip],
            ),
        Roll(
            """
            Adrenaline Junkie.
            For this weapon Adrenaline Junkie is better than Desperate Measures
            because AJ can achieve max stacks easily with 1-2 shots,
            while DM requires two ability kills
            """,
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.Demolitionist, trait.HealClip],
            [trait.AdrenalineJunkie],
            ),
        ]


class LineInTheSand(RollDefinition):
    """
    Arc Linear Fusion Rifle, Precision Frame
    https://www.light.gg/db/items/2450049485
    """
    item = Item('Line in the Sand', hash=2450049485)
    roll = Roll(
        'Damage dealing',
        [barrel.ArrowheadBrake, AnyPerk],
        [battery.AcceleratedCoils, AnyPerk],
        [trait.Demolitionist, trait.ClownCartridge],
        [trait.BaitAndSwitch],
        )
