from wishlist import *
from . import *


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
            'Super roll',
            default_barrels,
            default_mags,
            [trait.EnviousAssassin],
            [trait.EnviousArsenal],
            [trait.BlastDistributor],
            [trait.BaitAndSwitch],
            [trait.ExplosiveLight],
            [trait.Demolitionist],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.EnviousArsenal, trait.EnviousAssassin],
            [trait.ExplosiveLight, trait.BaitAndSwitch],
            ),
        Roll(
            'Grenade combo',
            default_barrels,
            default_mags,
            [trait.BlastDistributor],
            [trait.Demolitionist],
            ),
        ]


class KoraxissDistress(RollDefinition):
    """
    Strand Drum Grenade Launcher, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Raid "Root of Nightmares"
    https://www.light.gg/db/items/2972949637
    https://destiny.report/w/2972949637
    """
    items = [
        Item("Koraxis's Distress", hash=2972949637),
        Item("Koraxis's Distress (Adept)", hash=495442100),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.EnviousAssassin],
            [trait.ChainReaction],
            [trait.EnviousArsenal],
            [trait.Surrounded],
            [trait.Hatchling],
            [trait.BaitAndSwitch],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.EnviousArsenal, trait.EnviousAssassin],
            [trait.BaitAndSwitch, trait.Surrounded],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.ChainReaction],
            [trait.Surrounded, trait.Hatchling],
            ),
        ]


class TheEverPresent(RollDefinition):
    """
    Strand Drum Grenade Launcher, Rapid-Fire Frame, Anti-Overload
    Source: Epic raid "The Desert Perpetual"
    https://www.light.gg/db/items/3177074192
    https://destiny.report/w/3177074192
    """
    item = Item('The Ever-Present', hash=3177074192)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Hatchling],
            [trait.EnviousArsenal],
            [trait.AutoLoadingHolster],
            [trait.ExplosiveLight],
            [trait.AggregateCharge],
            [trait.ChainReaction],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.EnviousArsenal, trait.AutoLoadingHolster],
            [trait.ExplosiveLight, trait.AggregateCharge],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.Hatchling],
            [trait.ChainReaction],
            ),
        ]
