from wishlist import *
from . import *


class Acosmic(RollDefinition):
    """
    Void Drum Grenade Launcher, Rapid-Fire Frame, Anti-Overload
    Source: Festival of the Lost
    https://www.light.gg/db/items/1106017703
    https://destiny.report/w/1106017703
    """
    items = [
        Item('Acosmic', hash=1106017703),
        Item('Acosmic', hash=425681240),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.ClownCartridge],
            [trait.AirTrigger],
            [trait.ExplosiveLight],
            [trait.DestabilizingRounds],
            [trait.BaitAndSwitch],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.ClownCartridge],
            [trait.ExplosiveLight, trait.BaitAndSwitch],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.AirTrigger],
            [trait.DestabilizingRounds],
            ),
        ]


class EdgeTransit(RollDefinition):
    """
    Void Drum Grenade Launcher, Adaptive Frame, Anti-Barrier
    Source: Onslaught
    https://www.light.gg/db/items/3736001863
    https://destiny.report/w/3736001863
    """
    item = Item('Edge Transit', hash=3736001863)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.EnviousArsenal],
            [trait.CascadePoint],
            [trait.ChainReaction],
            [trait.DestabilizingRounds],
            [trait.ExplosiveLight],
            [trait.BaitAndSwitch],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.EnviousArsenal, trait.CascadePoint],
            [trait.ExplosiveLight, trait.BaitAndSwitch],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.ChainReaction],
            [trait.DestabilizingRounds],
            ),
        ]


class Regnant(RollDefinition):
    """
    Void Drum Grenade Launcher, Adaptive Frame, Anti-Barrier, Craftable
    Source: Exotic mission "//NODE.OVRD.AVALON//"
    https://www.light.gg/db/items/268260372
    https://destiny.report/w/268260372
    """
    item = Item('Regnant', hash=268260372)
    roll = Roll(
        'Damage dealing',
        default_barrels,
        default_mags,
        [trait.AutoLoadingHolster],
        [trait.ExplosiveLight],
        )
