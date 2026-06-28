from wishlist import *


class Intercalary(RollDefinition):
    """
    Stasis Auto Rifle, Adaptive Frame, Anti-Barrier
    Source: "The Desert Perpetual" Raid
    https://www.light.gg/db/items/2725426834
    https://destiny.report/w/2725426834
    """
    item = Item('Intercalary', hash=2725426834)
    rolls = [
        Roll(
            'Stasis Combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Headstone],
            [trait.Rimestealer],
            ),
        Roll(
            'One for All',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Headstone, trait.Demolitionist],
            [trait.OneForAll],
            ),
        ]
