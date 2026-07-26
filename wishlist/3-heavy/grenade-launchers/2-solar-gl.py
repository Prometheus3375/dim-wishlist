from wishlist import *
from . import *


class CanisMajor(RollDefinition):
    """
    Solar Drum Grenade Launcher, Rapid-Fire Frame, Anti-Overload
    Source: Dungeon "The Shattered Throne"
    https://www.light.gg/db/items/2966714447
    https://destiny.report/w/2966714447
    """
    item = Item('Canis Major', hash=2966714447)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.ClownCartridge],
            [trait.Incandescent],
            [trait.Reconstruction],
            [trait.ChainReaction],
            [trait.AggregateCharge],
            [trait.ExplosiveLight],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.ClownCartridge, trait.Reconstruction],
            [trait.ExplosiveLight, trait.AggregateCharge],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.Incandescent],
            [trait.ChainReaction],
            ),
        ]


class CryMutiny(RollDefinition):
    """
    Solar Drum Grenade Launcher, Adaptive Frame, Anti-Barrier
    Source: Solo Ops
    https://www.light.gg/db/items/768696858
    https://destiny.report/w/768696858
    """
    item = Item('Cry Mutiny', hash=768696858)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Incandescent],
            [trait.DangerZone],
            [trait.Surrounded],
            [trait.MegaKillClip],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.Incandescent],
            [trait.MegaKillClip, trait.Surrounded],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.DangerZone],
            [trait.Surrounded],
            ),
        ]


class OutrageousFortune(RollDefinition):
    """
    Solar Drum Grenade Launcher, Rapid-Fire Frame, Anti-Overload
    Source: Commander Zavala; Tenet of Bravery
    https://www.light.gg/db/items/4146673634
    https://destiny.report/w/4146673634
    """
    item = Item('Outrageous Fortune', hash=4146673634)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.EnviousArsenal],
            [trait.Incandescent],
            [trait.ChainReaction],
            [trait.BaitAndSwitch],
            [trait.ExplosiveLight],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.EnviousArsenal],
            [trait.ExplosiveLight, trait.BaitAndSwitch],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.Incandescent],
            [trait.ChainReaction],
            ),
        ]
