from wishlist import *

# Quick Launch is used because -5 points of Blast Radius from Hard Launch
# are removed by any Masterwork on T5 weapon.
default_barrels = [launcher_barrel.QuickLaunch, AnyPerk]
default_magazine = [magazine.SpikeGrenades, AnyPerk]


class WildStyle(RollDefinition):
    """
    Solar Breechloaded Grenade Launcher, Double Fire, Anti-Unstoppable
    Source: Commander Zavala
    https://www.light.gg/db/items/4021098352
    https://destiny.report/w/4021098352
    """
    item = Item('Wild Style', hash=4021098352)


class Wilderflight(RollDefinition):
    """
    Void Breechloaded Grenade Launcher, Double Fire, Anti-Unstoppable
    Source: Dungeon "Spire of the Watcher"
    https://www.light.gg/db/items/408862798
    https://destiny.report/w/408862798
    """
    item = Item('Wilderflight', hash=408862798)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_magazine,
            [trait.AutoLoadingHolster],
            [trait.EnviousArsenal],
            [trait.ReapersTithe],
            [trait.AggregateCharge],
            ),
        Roll(
            'Damage rotations',
            default_barrels,
            default_magazine,
            [trait.EnviousArsenal, trait.AutoLoadingHolster],
            [trait.AggregateCharge, trait.ReapersTithe],
            ),
        ]


class Liturgy(RollDefinition):
    """
    Stasis Breechloaded Grenade Launcher, Double Fire, Anti-Unstoppable
    Source: World
    https://www.light.gg/db/items/3377522331
    https://destiny.report/w/3377522331
    """
    item = Item('Liturgy', hash=3377522331)
    roll = Roll(
        'Damage rotations',
        default_barrels,
        default_magazine,
        [trait.EnviousArsenal],
        [trait.ChillClip],
        )
