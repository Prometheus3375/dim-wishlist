from wishlist import *


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
