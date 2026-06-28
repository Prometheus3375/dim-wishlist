from wishlist import *


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
