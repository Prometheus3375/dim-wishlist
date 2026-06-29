from wishlist import *


class ColdComfort(RollDefinition):
    """
    Stasis Rocket Launcher, Aggressive Frame, Anti-Unstoppable
    Source: Ghosts of the Deep
    https://www.light.gg/db/items/2287287549
    https://destiny.report/w/2287287549
    """
    item = Item('Cold Comfort', hash=2287287549)


class TheWhenAndWhere(RollDefinition):
    """
    Stasis Rocket Launcher, Adaptive Frame, Anti-Barrier
    Source: The Desert Perpetual (Both)
    https://www.light.gg/db/items/1090936013
    https://destiny.report/w/1090936013
    """
    item = Item('The When And Where', hash=1090936013)
    rolls = [
        Roll(
            'Damage dealing',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.ImpactCasing, AnyPerk],
            [trait.Reconstruction, trait.Overflow, trait.ClownCartridge],
            [trait.BaitAndSwitch, trait.ElementalHoning, trait.ReapersTithe],
            ),
        ]
