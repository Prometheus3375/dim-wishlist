from wishlist import *


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
