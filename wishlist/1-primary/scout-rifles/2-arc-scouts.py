from wishlist import *


class Sublimation(RollDefinition):
    """
    Arc Scout Rifle, High-Impact Frame, Anti-Unstoppable
    Source: Exploring Kepler
    https://www.light.gg/db/items/1674692344
    https://destiny.report/w/1674692344
    """
    item = Item('Sublimation', hash=1674692344)


class VoltaicShade(RollDefinition):
    """
    Arc Scout Rifle, Balanced Heat Weapon, Anti-Overload
    Source: Equilibrium
    https://www.light.gg/db/items/71057630
    https://destiny.report/w/71057630
    """
    item = Item('Voltaic Shade', hash=71057630)
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.JoltingFeedback],
            [trait.Voltshot, trait.Meganeura],
            ),
        ]
