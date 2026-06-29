from wishlist import *


class CanisMajor(RollDefinition):
    """
    Solar Drum Grenade Launcher, Rapid-Fire Frame, Anti-Overload
    Source: The Shattered Throne
    https://www.light.gg/db/items/2966714447
    https://destiny.report/w/2966714447
    """
    item = Item('Canis Major', hash=2966714447)


class CryMutiny(RollDefinition):
    """
    Solar Drum Grenade Launcher, Adaptive Frame, Anti-Barrier
    Source: Solo Ops
    https://www.light.gg/db/items/768696858
    https://destiny.report/w/768696858
    """
    item = Item('Cry Mutiny', hash=768696858)


class LoveAndDeath(RollDefinition):
    """
    Solar Drum Grenade Launcher, Compressed Wave Frame, Anti-Unstoppable
    Source: Unspecified
    https://www.light.gg/db/items/3482299617
    https://destiny.report/w/3482299617
    """
    item = Item('Love and Death', hash=3482299617)


class OutrageousFortune(RollDefinition):
    """
    Solar Drum Grenade Launcher, Rapid-Fire Frame, Anti-Overload
    Source: Commander Zavala
    https://www.light.gg/db/items/4146673634
    https://destiny.report/w/4146673634
    """
    item = Item('Outrageous Fortune', hash=4146673634)
    rolls = [
        Roll(
            'Damage dealing',
            [launcher_barrel.HardLaunch, AnyPerk],
            [magazine.SpikeGrenades, AnyPerk],
            [trait.EnviousArsenal],
            [trait.BaitAndSwitch],
            ),
        Roll(
            'High DPS',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.SpikeGrenades, AnyPerk],
            [trait.EnviousArsenal],
            [trait.ExplosiveLight],
            ),
        Roll(
            'Ad clear',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighExplosiveOrdnance, AnyPerk],
            [trait.Incandescent],
            [trait.ChainReaction],
            ),
        ]
