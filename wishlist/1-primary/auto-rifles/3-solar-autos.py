from wishlist import *


class AbyssDefiant(RollDefinition):
    """
    Solar Auto Rifle, High-Impact Frame, Anti-Unstoppable, Craftable
    Source: "Crota's End" Raid
    https://www.light.gg/db/items/833898322
    https://destiny.report/w/833898322
    """
    item = Item('Abyss Defiant', hash=833898322)


class AhabChar(RollDefinition):
    """
    Solar Auto Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Banshee-44
    https://www.light.gg/db/items/1411560894
    https://destiny.report/w/1411560894
    """
    item = Item('Ahab Char', hash=1411560894)
    roll = Roll(
        'PvE',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.FlaredMagwell, AnyPerk],
        [trait.HealClip],
        [trait.BurningAmbition, trait.KillClip],
        )


class AmmitAR2(RollDefinition):
    """
    Solar Auto Rifle, Precision Frame, Anti-Barrier, Craftable
    Source: Open Legendary engrams and earn faction rank-up packages.
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


class NoHesitation(RollDefinition):
    """
    Solar Auto Rifle, Support Frame, Anti-Overload, Craftable
    Source: Exploring the Pale Heart
    https://www.light.gg/db/items/1801007332
    https://destiny.report/w/1801007332
    """
    item = Item('No Hesitation', hash=1801007332)


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
    Source: Equilibrium
    https://www.light.gg/db/items/1863583117
    https://destiny.report/w/1863583117
    """
    item = Item('Zealous Ideal', hash=1863583117)
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ChamberedCompensator, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.HealClip],
            [trait.Incandescent, trait.OneForAll],
            ),
        ]
