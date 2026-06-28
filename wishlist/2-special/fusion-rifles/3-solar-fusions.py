from wishlist import *


class CartesianCoordinate(RollDefinition):
    """
    Solar Fusion Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Unspecified
    https://www.light.gg/db/items/3719824177
    https://destiny.report/w/3719824177
    """
    item = Item('Cartesian Coordinate', hash=3719824177)


class DreamBreaker(RollDefinition):
    """
    Solar Fusion Rifle, Adaptive Frame, Anti-Barrier
    Source: Unspecified
    https://www.light.gg/db/items/219610523
    https://destiny.report/w/219610523
    """
    item = Item('Dream Breaker', hash=219610523)


class ExilesCurse(RollDefinition):
    """
    Solar Fusion Rifle, High-Impact Frame, Anti-Unstoppable
    Source: Trials of Osiris
    https://www.light.gg/db/items/1117787139
    https://destiny.report/w/1117787139
    """
    item = Item("Exile's Curse", hash=1117787139)


class FiniteMaybe(RollDefinition):
    """
    Solar Fusion Rifle, Aggressive Frame, Anti-Unstoppable
    Source: "The Desert Perpetual" Raid
    https://www.light.gg/db/items/3241217409
    https://destiny.report/w/3241217409
    """
    item = Item('Finite Maybe', hash=3241217409)
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.AcceleratedCoils, AnyPerk],
            [trait.Incandescent],
            [trait.Discord],
            ),
        Roll(
            'Damage dealing',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.AcceleratedCoils, AnyPerk],
            [trait.Reconstruction],
            [trait.BaitAndSwitch, trait.ControlledBurst],
            ),
        ]
