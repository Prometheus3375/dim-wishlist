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
