from wishlist import *


class ApexPredator(RollDefinition):
    """
    Solar Rocket Launcher, Adaptive Frame, Anti-Barrier, Craftable
    Source: Last Wish
    https://www.light.gg/db/items/1851777734
    https://destiny.report/w/1851777734
    """
    item = Item('Apex Predator', hash=1851777734)


class Ascendancy(RollDefinition):
    """
    Solar Rocket Launcher, Precision Frame, Anti-Barrier
    Source: Solo Ops
    https://www.light.gg/db/items/1713388226
    https://destiny.report/w/1713388226
    """
    item = Item('Ascendancy', hash=1713388226)


class HezenVengeance(RollDefinition):
    """
    Solar Rocket Launcher, Aggressive Frame, Anti-Unstoppable, Craftable
    Source: Vault of Glass
    https://www.light.gg/db/items/2265407516
    https://destiny.report/w/2265407516
    """
    items = [
        Item('Hezen Vengeance', hash=2265407516),
        Item('Hezen Vengeance (Timelost)', hash=3623686757),
        ]


class PyroclasticFlow(RollDefinition):
    """
    Solar Rocket Launcher, Precision Frame, Anti-Barrier
    Source: Nessus, Unstable Centaur
    https://www.light.gg/db/items/3161496501
    https://destiny.report/w/3161496501
    """
    item = Item('Pyroclastic Flow', hash=3161496501)


class RoarOfTheBear(RollDefinition):
    """
    Solar Rocket Launcher, High-Impact Frame, Anti-Unstoppable
    Source: Iron Banner
    https://www.light.gg/db/items/2881109029
    https://destiny.report/w/2881109029
    """
    item = Item('Roar of the Bear', hash=2881109029)
