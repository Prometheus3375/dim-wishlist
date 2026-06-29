from wishlist import *


class RomanticDeath(RollDefinition):
    """
    Void Breechloaded Grenade Launcher, Wave Frame, Anti-Unstoppable
    Source: Reclamation Events
    https://www.light.gg/db/items/4169082039
    https://destiny.report/w/4169082039
    """
    items = [
        Item('Romantic Death', hash=4169082039),
        Item('Romantic Death', hash=2979965244),
        Item('Romantic Death', hash=2979965245),
        Item('Romantic Death', hash=2979965246),
        Item('Romantic Death', hash=2979965247),
        ]
    rolls = [
        Roll(
            'Ad clear',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.FeedingFrenzy],
            [trait.DestabilizingRounds, trait.OneForAll, trait.ChainReaction],
            ),
        Roll(
            'Void combo',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        ]


class VSVelocityBaton(RollDefinition):
    """
    Void Breechloaded Grenade Launcher, Area Denial Frame, Anti-Overload
    Source: Vesper's Host
    https://www.light.gg/db/items/2452936816
    https://destiny.report/w/2452936816
    """
    item = Item('VS Velocity Baton', hash=2452936816)


class Wilderflight(RollDefinition):
    """
    Void Breechloaded Grenade Launcher, Double Fire, Anti-Unstoppable
    Source: Spire of the Watcher
    https://www.light.gg/db/items/408862798
    https://destiny.report/w/408862798
    """
    item = Item('Wilderflight', hash=408862798)
