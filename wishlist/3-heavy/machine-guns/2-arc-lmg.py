from wishlist import *


class A21Delirium(RollDefinition):
    """
    Arc Machine Gun, Rapid-Fire Frame, Anti-Overload
    Source: Gambit
    https://www.light.gg/db/items/3001598094
    https://destiny.report/w/3001598094
    """
    item = Item('21% Delirium', hash=3001598094)


class AFineMemorial(RollDefinition):
    """
    Arc Machine Gun, Adaptive Frame, Anti-Barrier
    Source: Unspecified
    https://www.light.gg/db/items/3211332727
    https://destiny.report/w/3211332727
    """
    item = Item('A Fine Memorial', hash=3211332727)


class BitterEnd(RollDefinition):
    """
    Arc Machine Gun, Balanced Heat Weapon, Anti-Overload
    Source: Equilibrium
    https://www.light.gg/db/items/954563454
    https://destiny.report/w/954563454
    """
    item = Item('Bitter End', hash=954563454)
    rolls = [
        Roll(
            """
            Ad clear.
            Using Overclocked over Ionized Heatsink
            because Cooling Baubles keep the weapon cool.
            """,
            [barrel.ChamberedCompensator, AnyPerk],
            [battery.OverclockedHeatsink, AnyPerk],
            [trait.CoolingBaubles],
            [trait.KillingTally, trait.JoltingFeedback, trait.OneForAll],
            ),
        Roll(
            'Damage dealing',
            [barrel.ChamberedCompensator, AnyPerk],
            [battery.OverclockedHeatsink, AnyPerk],
            [trait.TrickleCharge],
            [trait.KillingTally],
            ),
        ]


class SeventhSeraphSAW(RollDefinition):
    """
    Arc Machine Gun, High-Impact Frame, Anti-Unstoppable
    Source: Unspecified
    https://www.light.gg/db/items/2584201248
    https://destiny.report/w/2584201248
    """
    item = Item('Seventh Seraph SAW', hash=2584201248)


class TerminusHorizon(RollDefinition):
    """
    Arc Machine Gun, High-Impact Frame, Anti-Unstoppable
    Source: "Spire of the Watcher" Dungeon
    https://www.light.gg/db/items/3814261872
    https://destiny.report/w/3814261872
    """
    item = Item('Terminus Horizon', hash=3814261872)


class WatchfulEye(RollDefinition):
    """
    Arc Machine Gun, Aggressive Frame, Anti-Unstoppable
    Source: Unspecified
    https://www.light.gg/db/items/3058845782
    https://destiny.report/w/3058845782
    """
    item = Item('Watchful Eye', hash=3058845782)
