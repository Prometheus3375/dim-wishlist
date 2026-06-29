from wishlist import *


class CataphractGL3(RollDefinition):
    """
    Strand Drum Grenade Launcher, Adaptive Frame, Anti-Barrier
    Source: Saint-14
    https://www.light.gg/db/items/3805679279
    https://destiny.report/w/3805679279
    """
    item = Item('Cataphract GL3', hash=3805679279)
    rolls = [
        Roll(
            'Damage dealing',
            [launcher_barrel.HardLaunch, AnyPerk],
            [magazine.SpikeGrenades, AnyPerk],
            [trait.EnviousAssassin, trait.EnviousArsenal, trait.AutoLoadingHolster],
            [trait.BaitAndSwitch],
            ),
        Roll(
            'High DPS',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.SpikeGrenades, AnyPerk],
            [trait.EnviousArsenal, trait.AutoLoadingHolster, trait.EnviousAssassin],
            [trait.ExplosiveLight],
            ),
        ]


class TheEverPresent(RollDefinition):
    """
    Strand Drum Grenade Launcher, Rapid-Fire Frame, Anti-Overload
    Source: The Desert Perpetual (Epic)
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
