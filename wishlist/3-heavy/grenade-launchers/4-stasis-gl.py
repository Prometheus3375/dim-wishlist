from wishlist import *
from . import *


class VSChillInhibitor(RollDefinition):
    """
    Stasis Drum Grenade Launcher, Rapid-Fire Frame, Anti-Overload
    Source: Dungeon "Vesper's Host"
    https://www.light.gg/db/items/2452936817
    https://destiny.report/w/2452936817
    """
    item = Item('VS Chill Inhibitor', hash=2452936817)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.CascadePoint],
            [trait.ChillClip],
            [trait.EnviousArsenal],
            [trait.AggregateCharge],
            [trait.ChainReaction],
            [trait.ExplosiveLight],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.EnviousArsenal, trait.CascadePoint],
            [trait.ExplosiveLight, trait.AggregateCharge],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.ChillClip],
            [trait.ChainReaction],
            ),
        ]
