from wishlist import *


class AdmetusD(RollDefinition):
    """
    Solar Scout Rifle, High-Impact Frame, Anti-Unstoppable
    Source: Banshee-44
    https://www.light.gg/db/items/3156551029
    https://destiny.report/w/3156551029
    """
    item = Item('Admetus-D', hash=3156551029)


class OxygenSR3(RollDefinition):
    """
    Solar Scout Rifle, Precision Frame, Anti-Barrier
    Source: Commander Zavala
    https://www.light.gg/db/items/4104613038
    https://destiny.report/w/4104613038
    """
    items = [
        Item('Oxygen SR3', hash=4104613038),
        Item('Oxygen SR3', hash=444627789),
        ]
    rolls = [
        Roll(
            'PvE',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.HealClip],
            [trait.Meganeura],
            ),
        ]
