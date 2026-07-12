from wishlist import *
from . import *


class AbyssDefiant(RollDefinition):
    """
    Solar Auto Rifle, High-Impact Frame, Anti-Unstoppable, Craftable
    Source: Raid "Crota's End"
    https://www.light.gg/db/items/833898322
    https://destiny.report/w/833898322
    """
    items = [
        Item('Abyss Defiant', hash=833898322),
        Item('Abyss Defiant (Adept)', hash=3782662983),
        ]


class AhabChar(RollDefinition):
    """
    Solar Auto Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Banshee-44; Tenet of Bravery
    https://www.light.gg/db/items/1411560894
    https://destiny.report/w/1411560894
    """
    item = Item('Ahab Char', hash=1411560894)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.HealClip],
            [trait.KillClip],
            [trait.BurningAmbition],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.HealClip],
            [trait.BurningAmbition, trait.KillClip],
            ),
        ]


class AmmitAR2(RollDefinition):
    """
    Solar Auto Rifle, Precision Frame, Anti-Barrier, Craftable
    Source: Quest "Foundry Resonance"
    https://www.light.gg/db/items/2119346509
    https://destiny.report/w/2119346509
    """
    item = Item('Ammit AR2', hash=2119346509)


class ArcticHaze(RollDefinition):
    """
    Solar Auto Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Europa
    https://www.light.gg/db/items/2187337757
    https://destiny.report/w/2187337757
    """
    item = Item('Arctic Haze', hash=2187337757)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Incandescent],
            [trait.HealClip],
            [trait.Demolitionist],
            [trait.BurningAmbition],
            [trait.KillClip],
            ),
        Roll(
            'Solar combo',
            default_barrels,
            default_mags,
            [trait.Incandescent],
            [trait.BurningAmbition],
            ),
        Roll(
            'Clip combo',
            default_barrels,
            default_mags,
            [trait.HealClip],
            [trait.KillClip],
            ),
        ]


class TheRingingNail(RollDefinition):
    """
    Solar Auto Rifle, Precision Frame, Anti-Barrier
    Source: Arena Ops
    https://www.light.gg/db/items/3326135421
    https://destiny.report/w/3326135421
    """
    items = [
        Item('The Ringing Nail', hash=3326135421),
        Item('The Ringing Nail', hash=4206550094),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Incandescent],
            [trait.ImpromptuAmmunition],
            [trait.HealClip],
            [trait.BurningAmbition],
            [trait.Firefly],
            ),
        Roll(
            'Solar combo',
            default_barrels,
            default_mags,
            [trait.Incandescent],
            [trait.BurningAmbition, trait.Firefly],
            ),
        Roll(
            'Solar combo',
            default_barrels,
            default_mags,
            [trait.HealClip],
            [trait.Firefly],
            ),
        ]


class TheSummoner(RollDefinition):
    """
    Solar Auto Rifle, Adaptive Frame, Anti-Barrier
    Source: Trials of Osiris
    https://www.light.gg/db/items/2884908760
    https://destiny.report/w/2884908760
    """
    item = Item('The Summoner', hash=2884908760)


class ZealousIdeal(RollDefinition):
    """
    Solar Auto Rifle, Balanced Heat Weapon, Anti-Overload
    Source: Dungeon "Equilibrium"
    https://www.light.gg/db/items/1863583117
    https://destiny.report/w/1863583117
    """
    item = Item('Zealous Ideal', hash=1863583117)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            [barrel.PolygonalRifling, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.HealClip],
            [trait.CoolingBaubles],
            [trait.AttritionOrbs],
            [trait.OneForAll],
            [trait.Incandescent],
            ),
        Roll(
            'Ad clear',
            [barrel.PolygonalRifling, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.HealClip],
            [trait.Incandescent, trait.OneForAll],
            ),
        ]
