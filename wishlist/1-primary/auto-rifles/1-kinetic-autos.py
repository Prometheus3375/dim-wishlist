from wishlist import *
from . import *


class Breakneck(RollDefinition):
    """
    Kinetic Auto Rifle, Precision Frame, Anti-Barrier
    Source: The Drifter
    https://www.light.gg/db/items/2065366343
    https://destiny.report/w/2065366343
    """
    item = Item('Breakneck', hash=2065366343)


class ChromaRush(RollDefinition):
    """
    Kinetic Auto Rifle, Rapid-Fire Frame, Anti-Overload
    Source: World
    https://www.light.gg/db/items/771811871
    https://destiny.report/w/771811871
    """
    item = Item('Chroma Rush', hash=771811871)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            [magazine.AlloyMagazine, AnyPerk],
            [trait.Subsistence],
            [trait.StoppingPower],
            [trait.BewilderingBurst],
            [trait.Rampage],
            [trait.KineticTremors],
            [trait.AncillaryOrdinance],
            ),
        Roll(
            'Bewildering Burst',
            default_barrels,
            [magazine.AlloyMagazine, AnyPerk],
            [trait.BewilderingBurst],
            [trait.KineticTremors, trait.Rampage],
            ),
        Roll(
            'Classic combo',
            default_barrels,
            [magazine.AlloyMagazine, AnyPerk],
            [trait.Subsistence],
            [trait.Rampage],
            ),
        ]


class DutyBound(RollDefinition):
    """
    Kinetic Auto Rifle, Adaptive Frame, Anti-Barrier
    Source: Commander Zavala
    https://www.light.gg/db/items/260532765
    https://destiny.report/w/260532765
    """
    items = [
        Item('Duty Bound', hash=260532765),
        Item('Duty Bound', hash=89693562),
        ]


class EverburningGlitz(RollDefinition):
    """
    Kinetic Auto Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Saint-14
    https://www.light.gg/db/items/2857870254
    https://destiny.report/w/2857870254
    """
    item = Item('Everburning Glitz', hash=2857870254)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.AttritionOrbs],
            [trait.BewilderingBurst],
            [trait.KineticTremors],
            [trait.OneForAll],
            ),
        Roll(
            'Attrition Orbs',
            default_barrels,
            default_mags,
            [trait.AttritionOrbs],
            [trait.KineticTremors, trait.OneForAll],
            ),
        Roll(
            'Bewildering Burst',
            default_barrels,
            default_mags,
            [trait.BewilderingBurst],
            [trait.KineticTremors, trait.OneForAll],
            ),
        ]


class Firefright(RollDefinition):
    """
    Kinetic Auto Rifle, Precision Frame, Anti-Barrier, Craftable
    Source: Exotic mission "Presage"
    https://www.light.gg/db/items/2778013407
    https://destiny.report/w/2778013407
    """
    item = Item('Firefright', hash=2778013407)


class GiversBlessing(RollDefinition):
    """
    Kinetic Auto Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Kepler
    https://www.light.gg/db/items/970034755
    https://destiny.report/w/970034755
    """
    item = Item("Giver's Blessing", hash=970034755)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.ImpromptuAmmunition],
            [trait.Demolitionist],
            [trait.KineticTremors],
            [trait.OneForAll],
            [trait.AdrenalineJunkie],
            ),
        Roll(
            'Ammo generation',
            default_barrels,
            default_mags,
            [trait.ImpromptuAmmunition],
            [trait.KineticTremors, trait.OneForAll],
            ),
        Roll(
            'Grenade combo',
            default_barrels,
            default_mags,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        ]


class OriginStory(RollDefinition):
    """
    Kinetic Auto Rifle, Precision Frame, Anti-Barrier
    Source: Commander Zavala
    https://www.light.gg/db/items/2188356726
    https://destiny.report/w/2188356726
    """
    item = Item('Origin Story', hash=2188356726)


class Pluperfect(RollDefinition):
    """
    Kinetic Auto Rifle, High-Impact Frame, Anti-Unstoppable
    Source: Nessus, Unstable Centaur
    https://www.light.gg/db/items/2203881482
    https://destiny.report/w/2203881482
    """
    item = Item('Pluperfect', hash=2203881482)


class Scathelocke(RollDefinition):
    """
    Kinetic Auto Rifle, Adaptive Frame, Anti-Barrier
    Source: European Dead Zone
    https://www.light.gg/db/items/3332538050
    https://destiny.report/w/3332538050
    """
    item = Item('Scathelocke', hash=3332538050)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Subsistence],
            [trait.Overflow],
            [trait.AttritionOrbs],
            [trait.OneForAll],
            [trait.AncillaryOrdinance],
            [trait.KineticTremors],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.Overflow, trait.AttritionOrbs],
            [trait.KineticTremors, trait.OneForAll],
            ),
        ]


class SeventhSeraphCarbine(RollDefinition):
    """
    Kinetic Auto Rifle, Precision Frame, Anti-Barrier
    Source: Cosmodrome
    https://www.light.gg/db/items/2560370239
    https://destiny.report/w/2560370239
    """
    item = Item('Seventh Seraph Carbine', hash=2560370239)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            [magazine.SeraphRounds, AnyPerk],
            [trait.Reconstruction],
            [trait.StoppingPower],
            [trait.AttritionOrbs],
            [trait.AllStar],
            [trait.KineticTremors],
            [trait.AncillaryOrdinance],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            [magazine.SeraphRounds, AnyPerk],
            [trait.Reconstruction, trait.AttritionOrbs, trait.StoppingPower],
            [trait.KineticTremors],
            ),
        ]


class SteelfeatherRepeater(RollDefinition):
    """
    Kinetic Auto Rifle, Rapid-Fire Frame, Anti-Overload
    Source: World
    https://www.light.gg/db/items/771811870
    https://destiny.report/w/771811870
    """
    item = Item('Steelfeather Repeater', hash=771811870)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.BewilderingBurst],
            [trait.ProximityPower],
            [trait.Surrounded],
            [trait.Swashbuckler],
            ),
        Roll(
            'Melee combo',
            default_barrels,
            default_mags,
            [trait.ProximityPower],
            [trait.Swashbuckler, trait.Surrounded],
            ),
        ]


class Tigerspite(RollDefinition):
    """
    Kinetic Auto Rifle, Precision Frame, Anti-Barrier
    Source: The Dreaming City
    https://www.light.gg/db/items/1709137958
    https://destiny.report/w/1709137958
    """
    item = Item('Tigerspite', hash=1709137958)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Overflow],
            [trait.BewilderingBurst],
            [trait.StoppingPower],
            [trait.KineticTremors],
            [trait.OneForAll],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.Overflow, trait.BewilderingBurst],
            [trait.KineticTremors, trait.OneForAll],
            ),
        ]
