from wishlist import *
from . import *


class Adjudicator(RollDefinition):
    """
    Kinetic Submachine Gun, Precision Frame, Anti-Barrier
    Source: Dungeon "Prophecy"
    https://www.light.gg/db/items/140914741
    https://destiny.report/w/140914741
    """
    item = Item('Adjudicator', hash=140914741)
    rolls = [
        Roll(
            'Super roll',
            [barrel.ArrowheadBrake, AnyPerk],
            default_mags,
            [trait.ThreatDetector],
            [trait.AmbitiousAssassin],
            [trait.AttritionOrbs],
            [trait.KineticTremors],
            [trait.AllStar],
            ),
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            default_mags,
            [trait.ThreatDetector, trait.AttritionOrbs],
            [trait.KineticTremors],
            ),
        ]


class Gunburn(RollDefinition):
    """
    Kinetic Submachine Gun, Lightweight Frame, Anti-Overload
    Source: Festival of the Lost
    https://www.light.gg/db/items/3431536253
    https://destiny.report/w/3431536253
    """
    items = [
        Item('Gunburn', hash=3431536253),
        Item('Gunburn', hash=72775246),
        ]
    rolls = [
        Roll(
            'Super roll',
            [barrel.ExtendedBarrel, AnyPerk],
            default_mags,
            [trait.BewilderingBurst],
            [trait.ThreatDetector],
            [trait.LeadFromLight],
            [trait.AttritionOrbs],
            [trait.KineticTremors],
            [trait.AncillaryOrdinance],
            [origin.VeistStinger],
            ),
        Roll(
            'Ad clear',
            [barrel.ExtendedBarrel, AnyPerk],
            default_mags,
            [trait.ThreatDetector, trait.BewilderingBurst],
            [trait.KineticTremors],
            [origin.VeistStinger],
            ),
        Roll(
            'Orb combo',
            [barrel.ExtendedBarrel, AnyPerk],
            default_mags,
            [trait.LeadFromLight],
            [trait.AttritionOrbs],
            [origin.VeistStinger],
            ),
        ]


class MultimachCCX(RollDefinition):
    """
    Kinetic Submachine Gun, Lightweight Frame, Anti-Overload
    Source: Iron Banner
    https://www.light.gg/db/items/3026836571
    https://destiny.report/w/3026836571
    """
    item = Item('Multimach CCX', hash=3026836571)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.StoppingPower],
            [trait.BewilderingBurst],
            [trait.AttritionOrbs],
            [trait.KineticTremors],
            [trait.AllStar],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.StoppingPower, trait.BewilderingBurst],
            [trait.KineticTremors],
            ),
        Roll(
            'Hit combo',
            default_barrels,
            default_mags,
            [trait.AttritionOrbs],
            [trait.KineticTremors],
            ),
        ]


class PeculiarCharm(RollDefinition):
    """
    Kinetic Submachine Gun, Aggressive Burst, Anti-Unstoppable
    Source: Competitive Crucible
    https://www.light.gg/db/items/3620277039
    https://destiny.report/w/3620277039
    """
    item = Item('Peculiar Charm', hash=3620277039)
    rolls = [
        Roll(
            'Super roll',
            [barrel.Smallbore, AnyPerk],
            default_mags,
            [trait.AttritionOrbs],
            [trait.ImpromptuAmmunition],
            [trait.StoppingPower],
            [trait.AllStar],
            [trait.KineticTremors],
            [stock.FittedStock, AnyPerk],
            ),
        Roll(
            'Ad clear',
            [barrel.Smallbore, AnyPerk],
            default_mags,
            [trait.StoppingPower, trait.AttritionOrbs],
            [trait.KineticTremors],
            [stock.FittedStock, AnyPerk],
            ),
        Roll(
            'Ammo combo',
            [barrel.Smallbore, AnyPerk],
            default_mags,
            [trait.ImpromptuAmmunition],
            [trait.AllStar],
            [stock.FittedStock, AnyPerk],
            ),
        ]


class Submission(RollDefinition):
    """
    Kinetic Submachine Gun, Lightweight Frame, Anti-Overload, Craftable
    Source: Raid "Vow of the Disciple"
    https://www.light.gg/db/items/3886416794
    https://destiny.report/w/3886416794
    """
    items = [
        Item('Submission', hash=3886416794),
        Item('Submission (Adept)', hash=1941816543),
        ]
    is_chosen = True
    roll = Roll(
        'Ad clear',
        default_barrels,
        default_mags,
        [trait.KineticTremors],
        [trait.ChaosReshaped],
        )
