from wishlist import *


class Adjudicator(RollDefinition):
    """
    Kinetic Submachine Gun, Precision Frame, Anti-Barrier
    Source: Dungeon "Prophecy"
    https://www.light.gg/db/items/140914741
    https://destiny.report/w/140914741
    """
    item = Item('Adjudicator', hash=140914741)


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
            'Kinetic Tremors',
            [barrel.ChamberedCompensator, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.ThreatDetector, trait.BewilderingBurst, trait.LeadFromLight],
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


class MultimachCCX(RollDefinition):
    """
    Kinetic Submachine Gun, Lightweight Frame, Anti-Overload
    Source: Iron Banner
    https://www.light.gg/db/items/3026836571
    https://destiny.report/w/3026836571
    """
    item = Item('Multimach CCX', hash=3026836571)


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
            'Kinetic Tremors',
            [barrel.Smallbore, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.ImpromptuAmmunition, trait.AttritionOrbs],
            [trait.KineticTremors],
            [stock.FittedStock, AnyPerk],
            )
        ]


class Submission(RollDefinition):
    """
    Kinetic Submachine Gun, Lightweight Frame, Anti-Overload, Craftable
    Source: Vow of the Disciple
    https://www.light.gg/db/items/3886416794
    https://destiny.report/w/3886416794
    """
    items = [
        Item('Submission', hash=3886416794),
        Item('Submission (Adept)', hash=1941816543),
        ]
