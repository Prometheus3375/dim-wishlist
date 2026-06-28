from wishlist import *


class AuroraDawn(RollDefinition):
    """
    Stasis Sword, Wave Sword Frame, Anti-Unstoppable
    Source: Fireteam Ops
    https://www.light.gg/db/items/2111625436
    https://destiny.report/w/2111625436
    """
    item = Item('Aurora Dawn', hash=2111625436)
    rolls = [
        Roll(
            'Ad clear',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.TirelessBlade, trait.Unrelenting],
            [trait.OneForAll, trait.ColdSteel],
            ),
        Roll(
            'Damage dealing with Ergo Sum',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.SharpHarvest],
            [trait.WhirlwindBlade],
            ),
        Roll(
            'Damage blocking. Flash Counter applies Cold Steel',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.FlashCounter],
            [trait.ColdSteel],
            ),
        ]


class TheSlammer(RollDefinition):
    """
    Stasis Sword, Vortex Frame, Anti-Overload
    Source: Pinnacle Ops
    https://www.light.gg/db/items/2466028274
    https://destiny.report/w/2466028274
    """
    items = [
        Item('The Slammer', hash=2466028274),
        Item('The Slammer', hash=189854537),
        ]


class Zephyr(RollDefinition):
    """
    Stasis Sword, Adaptive Frame, Anti-Barrier
    Source: The Dawning
    https://www.light.gg/db/items/3003492238
    https://destiny.report/w/3003492238
    """
    item = Item('Zephyr', hash=3003492238)
