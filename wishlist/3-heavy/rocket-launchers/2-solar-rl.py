from wishlist import *
from . import *


class ApexPredator(RollDefinition):
    """
    Solar Rocket Launcher, Adaptive Frame, Anti-Barrier, Craftable
    Source: Raid "Last Wish"
    https://www.light.gg/db/items/1851777734
    https://destiny.report/w/1851777734
    """
    item = Item('Apex Predator', hash=1851777734)
    roll = Roll(
        'Rocket spam',
        default_barrels,
        default_mags,
        [trait.Demolitionist],
        [trait.CollectiveDemolition],
        )


class Ascendancy(RollDefinition):
    """
    Solar Rocket Launcher, Precision Frame, Anti-Barrier
    Source: Solo Ops
    https://www.light.gg/db/items/1713388226
    https://destiny.report/w/1713388226
    """
    item = Item('Ascendancy', hash=1713388226)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.AttritionOrbs],
            [trait.ExplosiveLight],
            [trait.ChainReaction],
            [trait.ClusterBomb],
            ),
        Roll(
            'Attrition orbs',
            default_barrels,
            default_mags,
            [trait.AttritionOrbs],
            [trait.ExplosiveLight, trait.ClusterBomb, trait.ChainReaction],
            ),
        ]


class HezenVengeance(RollDefinition):
    """
    Solar Rocket Launcher, Aggressive Frame, Anti-Unstoppable, Craftable
    Source: Raid "Vault of Glass"
    https://www.light.gg/db/items/2265407516
    https://destiny.report/w/2265407516
    """
    items = [
        Item('Hezen Vengeance', hash=2265407516),
        Item('Hezen Vengeance (Timelost)', hash=3623686757),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Overflow],
            [trait.ClusterBomb],
            [trait.EnviousArsenal],
            [trait.Bipod],
            [trait.BaitAndSwitch],
            [trait.AggregateCharge],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.Overflow, trait.EnviousArsenal, trait.ClusterBomb],
            [trait.AggregateCharge, trait.BaitAndSwitch],
            ),
        ]


class PyroclasticFlow(RollDefinition):
    """
    Solar Rocket Launcher, Precision Frame, Anti-Barrier
    Source: Nessus, Unstable Centaur
    https://www.light.gg/db/items/3161496501
    https://destiny.report/w/3161496501
    """
    item = Item('Pyroclastic Flow', hash=3161496501)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.AutoLoadingHolster],
            [trait.ClusterBomb],
            [trait.Bipod],
            [trait.AggregateCharge],
            [trait.BaitAndSwitch],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.ClusterBomb, trait.AutoLoadingHolster],
            [trait.AggregateCharge, trait.BaitAndSwitch],
            ),
        ]


class RoarOfTheBear(RollDefinition):
    """
    Solar Rocket Launcher, High-Impact Frame, Anti-Unstoppable
    Source: Iron Banner
    https://www.light.gg/db/items/2881109029
    https://destiny.report/w/2881109029
    """
    item = Item('Roar of the Bear', hash=2881109029)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Demolitionist],
            [trait.AutoLoadingHolster],
            [trait.ExplosiveLight],
            [trait.Bipod],
            [trait.ReapersTithe],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.ExplosiveLight, trait.AutoLoadingHolster],
            [trait.ReapersTithe],
            ),
        Roll(
            'Grapple flying',
            [launcher_barrel.ConfinedLaunch, AnyPerk],
            [magazine.AlloyCasing, AnyPerk],
            [trait.Demolitionist],
            [trait.Bipod],
            ),
        ]
