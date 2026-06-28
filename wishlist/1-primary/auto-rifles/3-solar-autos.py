from wishlist import *


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
