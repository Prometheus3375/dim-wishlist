from wishlist import *
from . import *


class AxialLacuna(RollDefinition):
    """
    Solar Fusion Rifle, Precision Frame, Anti-Barrier, Craftable
    Source: The Pale Heart
    https://www.light.gg/db/items/3867373351
    https://destiny.report/w/3867373351
    """
    item = Item('Axial Lacuna', hash=3867373351)


class CartesianCoordinate(RollDefinition):
    """
    Solar Fusion Rifle, Rapid-Fire Frame, Anti-Overload
    Source: European Dead Zone
    https://www.light.gg/db/items/3719824177
    https://destiny.report/w/3719824177
    """
    item = Item('Cartesian Coordinate', hash=3719824177)


class DreamBreaker(RollDefinition):
    """
    Solar Fusion Rifle, Adaptive Frame, Anti-Barrier
    Source: The Moon
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
    roll = Roll(
        'PvP',
        [barrel.HammerForgedRifling, AnyPerk],
        [battery.ProjectionFuse, AnyPerk],
        [trait.UnderPressure],
        [trait.ClosingTime],
        ),


class FiniteMaybe(RollDefinition):
    """
    Solar Fusion Rifle, Aggressive Frame, Anti-Unstoppable
    Source: Raid "The Desert Perpetual"
    https://www.light.gg/db/items/3241217409
    https://destiny.report/w/3241217409
    """
    item = Item('Finite Maybe', hash=3241217409)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_battery,
            [trait.Incandescent],
            [trait.AmbitiousAssassin],
            [trait.Demolitionist],
            [trait.Discord],
            [trait.BurningAmbition],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_battery,
            [trait.Incandescent],
            [trait.Discord, trait.BurningAmbition],
            ),
        ]


class RoyalExecutioner(RollDefinition):
    """
    Solar Fusion Rifle, Adaptive Frame, Anti-Barrier, Craftable
    Source: Exotic mission "//NODE.OVRD.AVALON//"
    https://www.light.gg/db/items/1720503118
    https://destiny.report/w/1720503118
    """
    item = Item('Royal Executioner', hash=1720503118)


class TheBeacon(RollDefinition):
    """
    Solar Fusion Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Guardian Games
    https://www.light.gg/db/items/2161618499
    https://destiny.report/w/2161618499
    """
    items = [
        Item('The Beacon', hash=2161618499),
        Item('The Beacon', hash=76739872),
        ]


class TheEremite(RollDefinition):
    """
    Solar Fusion Rifle, High-Impact Frame, Anti-Unstoppable, Craftable
    Source: Xûr
    https://www.light.gg/db/items/3347946548
    https://destiny.report/w/3347946548
    """
    item = Item('The Eremite', hash=3347946548)
    is_chosen = True
    roll = Roll(
        'Damage dealing',
        default_barrels,
        default_battery,
        [trait.EnviousAssassin],
        [trait.ControlledBurst],
        ),
