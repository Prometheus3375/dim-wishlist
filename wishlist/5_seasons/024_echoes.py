from database import *


class Breachlight(RD):
    item = Item(name='Breachlight', hash=2328923181)
    _mags = [magazines.FlaredMagwell, magazines.TacticalMag, magazines.AppendedMag]
    rolls = [
        Roll(
            'Hatchling roll',
            _mags,
            [traits.Demolitionist, traits.Pugilist, traits.ThreatDetector],
            [traits.Hatchling],
            ),
        Roll(
            'Good PvE roll; '
            'for this weapon Desperate Measures is better than Swashbuckler and Adrenaline Junkie '
            'because DM can be activated while stowed and lasts longer',
            _mags,
            [traits.Demolitionist, traits.Pugilist, traits.ThreatDetector],
            [traits.DesperateMeasures],
            ),
        ]


class PatronOfLostCauses(RD):
    item = Item(name='Patron of Lost Causes', hash=2249996761)
    rolls = [
        Roll(
            'Roll to get class ability energy from afar',
            [traits.Strategist],
            [traits.KineticTremors, traits.ExplosivePayload],
            ),
        Roll(
            'Classic PvE roll for a scout rifle',
            [traits.RapidHit],
            [traits.KineticTremors, traits.ExplosivePayload],
            ),
        ]


class PerfectParadox(RD):
    item = Item(name='Perfect Paradox', hash=1298672084)
    _barrels = [barrels.BarrelShroud, barrels.CorkscrewRifling, barrels.Smallbore]
    _mags = [magazines.TacticalMag, magazines.LightMag]
    rolls = [
        Roll(
            """
            Melee damage increase;
            Ready/Stow speed-wise Pugilist is better than Threat Detector x1,
            but is worse than Threat Detector x2
            """,
            _barrels,
            _mags,
            [traits.Pugilist, traits.ThreatDetector],
            [traits.OneTwoPunch],
            ),
        Roll(
            'Roll for damage dealing',
            _barrels,
            _mags,
            [traits.DualLoader, traits.Pugilist],
            [traits.TrenchBarrel],
            )
        ]


class MartyrsRetribution(RD):
    item = Item(name="Martyr's Retribution", hash=2584830733)
    rolls = [
        Roll(
            'Incandescent roll; the preferred roll as there is already a Solar Wave Frame GL '
            'with damage increase perks, Explosive Personality with One for All',
            [barrels.VolatileLaunch],
            [magazines.HighVelocityRounds],
            [traits.Demolitionist, traits.HealClip],
            [traits.Incandescent],
            ),
        Roll(
            'Clip combo',
            [barrels.VolatileLaunch],
            [magazines.HighVelocityRounds],
            [traits.HealClip],
            [traits.KillClip],
            ),
        Roll(
            'Good PvE roll; '
            'for this weapon Adrenaline Junkie is better than Desperate Measures '
            'because AJ can achieve max stacks easily with 1-2 shots, '
            'while DM requires two ability kills',
            [barrels.VolatileLaunch],
            [magazines.HighVelocityRounds],
            [traits.Demolitionist, traits.HealClip],
            [traits.AdrenalineJunkie],
            ),
        ]


class LineInTheSand(RD):
    item = Item(name='Line in the Sand', hash=2450049485)
    roll = Roll(
        'Roll for damage dealing',
        [barrels.ArrowheadBrake, AnyPerk],
        [batteries.AcceleratedCoils, AnyPerk],
        [traits.Demolitionist, traits.ClownCartridge],
        [traits.BaitAndSwitch],
        )
