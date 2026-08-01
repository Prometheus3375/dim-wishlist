from wishlist import *
from . import *


class FireAndForget(RollDefinition):
    """
    Stasis Linear Fusion Rifle, Adaptive Burst, Anti-Barrier, Craftable
    Source: Exotic mission "Seraph's Shield"
    https://www.light.gg/db/items/2272041093
    https://destiny.report/w/2272041093
    """
    item = Item('Fire and Forget', hash=2272041093)


class ReedsRegret(RollDefinition):
    """
    Stasis Linear Fusion Rifle, Precision Frame, Anti-Barrier
    Source: Saint-14
    https://www.light.gg/db/items/3267997292
    https://destiny.report/w/3267997292
    """
    item = Item("Reed's Regret", hash=3267997292)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            [battery.IonizedBattery, AnyPerk],
            [trait.ClownCartridge],
            [trait.TripleTap],
            [trait.FiringLine],
            [trait.FocusedFury],
            [origin.VeistStinger],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            [battery.IonizedBattery, AnyPerk],
            [trait.TripleTap, trait.ClownCartridge],
            [trait.FiringLine, trait.FocusedFury],
            [origin.VeistStinger],
            ),
        ]
