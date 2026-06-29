from wishlist import *


class Heretic(RollDefinition):
    """
    Arc Rocket Launcher, Aggressive Frame, Anti-Unstoppable
    Source: Altars of Sorrow
    https://www.light.gg/db/items/2136808079
    https://destiny.report/w/2136808079
    """
    item = Item('Heretic', hash=2136808079)


class Micromort(RollDefinition):
    """
    Arc Rocket Launcher, Precision Frame, Anti-Barrier
    Source: Lawless Events
    https://www.light.gg/db/items/474671201
    https://destiny.report/w/474671201
    """
    items = [
        Item('Micromort', hash=474671201),
        Item('Micromort', hash=602331464),
        Item('Micromort', hash=602331465),
        Item('Micromort', hash=602331466),
        Item('Micromort', hash=602331467),
        ]
    rolls = [
        Roll(
            'Super roll',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.ImpactCasing, AnyPerk],
            [trait.ClusterBomb],
            [trait.EnviousArsenal],
            [trait.ClownCartridge],
            [trait.BaitAndSwitch],
            ),
        Roll(
            'Damage dealing',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.ImpactCasing, AnyPerk],
            [trait.ClusterBomb, trait.EnviousArsenal, trait.ClownCartridge],
            [trait.BaitAndSwitch],
            ),
        ]


class Sleepless(RollDefinition):
    """
    Arc Rocket Launcher, High-Impact Frame, Anti-Unstoppable
    Source: The Dreaming City
    https://www.light.gg/db/items/1738552769
    https://destiny.report/w/1738552769
    """
    item = Item('Sleepless', hash=1738552769)


class SubzeroSalvo(RollDefinition):
    """
    Arc Rocket Launcher, Precision Frame, Anti-Barrier
    Source: Europe
    https://www.light.gg/db/items/978122008
    https://destiny.report/w/978122008
    """
    item = Item('Subzero Salvo', hash=978122008)


class TheHothead(RollDefinition):
    """
    Arc Rocket Launcher, Adaptive Frame, Anti-Barrier
    Source: Pinnacle Ops
    https://www.light.gg/db/items/1692372662
    https://destiny.report/w/1692372662
    """
    items = [
        Item('The Hothead', hash=1692372662),
        Item('The Hothead', hash=3960301269),
        ]
