from database import *


class HushedWhisper(RollDefinition):
    """
    Strand Combat Bow, Precision Frame
    https://www.light.gg/db/items/1175295126
    """
    items = [
        Item(name='Hushed Whisper', hash=1175295126),
        Item(name='Hushed Whisper', hash=3574168117),
        ]
    rolls = [
        Roll(
            'Strand combo',
            [strings.ElasticString, AnyPerk],
            [arrows.CompactArrowShaft, AnyPerk],
            [traits.Tear, traits.Slice],
            [traits.Hatchling],
            ),
        ]


class Gunburn(RollDefinition):
    """
    Kinetic Submachine Gun, Lightweight Frame
    https://www.light.gg/db/items/3431536253
    """
    items = [
        Item(name='Gunburn', hash=3431536253),
        Item(name='Gunburn', hash=72775246),
        ]
    rolls = [
        Roll(
            'Kinetic Tremors',
            [barrels.ChamberedCompensator, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.ThreatDetector, traits.LeadFromLight],
            [traits.KineticTremors],
            ),
        Roll(
            'Orb combo',
            [barrels.ChamberedCompensator, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.LeadFromLight],
            [traits.AttritionOrbs],
            ),
        Roll(
            'Missile combo',
            [barrels.ChamberedCompensator, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.BewilderingBurst],
            [traits.AncillaryOrdinance],
            ),
        ]


# Special


class ArcaneEmbrace(RollDefinition):
    """
    Arc Shotgun, Heavy Burst
    https://www.light.gg/db/items/3328019216
    """
    items = [
        Item(name='Arcane Embrace', hash=3328019216),
        Item(name='Arcane Embrace', hash=1813474267),
        ]
    roll = Roll(
        'Damage dealing',
        [barrels.ArrowheadBrake, AnyPerk],
        [magazines.TacticalMag, AnyPerk],
        [traits.FourthTimesTheCharm],
        [traits.PrecisionInstrument, traits.AggregateCharge, traits.Surrounded],
        )
