from wishlist import *


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
            [bowstring.ElasticString, AnyPerk],
            [arrow.CompactArrowShaft, AnyPerk],
            [trait.Tear, trait.Slice],
            [trait.Hatchling],
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
            [barrel.ChamberedCompensator, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.ThreatDetector, trait.LeadFromLight],
            [trait.KineticTremors],
            ),
        Roll(
            'Orb combo',
            [barrel.ChamberedCompensator, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.LeadFromLight],
            [trait.AttritionOrbs],
            ),
        Roll(
            'Missile combo',
            [barrel.ChamberedCompensator, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.BewilderingBurst],
            [trait.AncillaryOrdinance],
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
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.TacticalMag, AnyPerk],
        [trait.FourthTimesTheCharm],
        [trait.PrecisionInstrument, trait.AggregateCharge, trait.Surrounded],
        )
