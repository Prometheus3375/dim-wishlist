from wishlist import *


class TheWhenAndWhere(RollDefinition):
    """
    Stasis Rocket Launcher, Adaptive Frame, Anti-Barrier
    Source: "The Desert Perpetual" Raid
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
