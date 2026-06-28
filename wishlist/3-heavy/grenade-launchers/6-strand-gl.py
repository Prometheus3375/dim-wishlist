from wishlist import *


class TheEverPresent(RollDefinition):
    """
    Strand Drum Grenade Launcher, Rapid-Fire Frame, Anti-Overload
    Source: "The Desert Perpetual" Epic Raid
    https://www.light.gg/db/items/3177074192
    https://destiny.report/w/3177074192
    """
    item = Item('The Ever-Present', hash=3177074192)
    rolls = [
        Roll(
            'Damage dealing',
            [launcher_barrel.HardLaunch, AnyPerk],
            [magazine.SpikeGrenades, AnyPerk],
            [trait.EnviousArsenal],
            [trait.AggregateCharge, trait.BaitAndSwitch, trait.ElementalHoning],
            ),
        Roll(
            'High DPS',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.SpikeGrenades, AnyPerk],
            [trait.AutoLoadingHolster],
            [trait.ExplosiveLight],
            ),
        Roll(
            'Ad clear',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.AlloyCasing, AnyPerk],
            [trait.Hatchling],
            [trait.ChainReaction],
            ),
        ]
