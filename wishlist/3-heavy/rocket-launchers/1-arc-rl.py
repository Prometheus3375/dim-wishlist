from wishlist import *
from . import *


class Heretic(RollDefinition):
    """
    Arc Rocket Launcher, Aggressive Frame, Anti-Unstoppable
    Source: Altars of Sorrow
    https://www.light.gg/db/items/2136808079
    https://destiny.report/w/2136808079
    """
    item = Item('Heretic', hash=2136808079)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.SuperchargedMagazine],
            [trait.ClusterBomb],
            [trait.EnviousArsenal],
            [trait.GearShift],
            [trait.Bipod],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.ClusterBomb, trait.EnviousArsenal, trait.SuperchargedMagazine],
            [trait.GearShift],
            ),
        ]


class Micromort(RollDefinition):
    """
    Arc Rocket Launcher, Precision Frame, Anti-Barrier
    Source: Events during season "Lawless"
    https://www.light.gg/db/items/474671201
    https://destiny.report/w/474671201
    """
    items = [
        Item('Micromort', hash=474671201),
        Item('Micromort', hash=602331464),
        Item('Micromort', hash=602331465),
        Item('Micromort', hash=602331466),
        Item('Micromort', hash=602331467),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.ClusterBomb],
            [trait.EnviousArsenal],
            [trait.ClownCartridge],
            [trait.BaitAndSwitch],
            [trait.Bipod],
            ),
        Roll(
            'Anti-construct',
            default_barrels,
            default_mags,
            [trait.ClusterBomb, trait.ClownCartridge],
            [trait.Bipod],
            [origin.HakkeBreachArmaments],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.ClusterBomb, trait.EnviousArsenal, trait.ClownCartridge],
            [trait.BaitAndSwitch],
            ),
        ]


class Sleepless(RollDefinition):
    """
    Arc Rocket Launcher, High-Impact Frame, Anti-Unstoppable
    Source: The Dreaming City
    https://www.light.gg/db/items/1738552769
    https://destiny.report/w/1738552769
    """
    item = Item('Sleepless', hash=1738552769)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.AutoLoadingHolster],
            [trait.BaitAndSwitch],
            [trait.GearShift],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.AutoLoadingHolster],
            [trait.BaitAndSwitch, trait.GearShift],
            ),
        ]


class SubzeroSalvo(RollDefinition):
    """
    Arc Rocket Launcher, Precision Frame, Anti-Barrier
    Source: Europa
    https://www.light.gg/db/items/978122008
    https://destiny.report/w/978122008
    """
    item = Item('Subzero Salvo', hash=978122008)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.SuperchargedMagazine],
            [trait.AutoLoadingHolster],
            [trait.GearShift],
            [trait.LastingImpression],
            [trait.AggregateCharge],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.AutoLoadingHolster, trait.SuperchargedMagazine],
            [trait.AggregateCharge, trait.GearShift, trait.LastingImpression],
            ),
        ]


class TheHothead(RollDefinition):
    """
    Arc Rocket Launcher, Adaptive Frame, Anti-Barrier
    Source: Pinnacle Ops
    https://www.light.gg/db/items/1692372662
    https://destiny.report/w/1692372662
    """
    items = [
        Item('The Hothead', hash=1692372662),
        Item('The Hothead', hash=3960301269),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.AutoLoadingHolster],
            [trait.EnviousArsenal],
            [trait.AggregateCharge],
            [trait.BaitAndSwitch],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.EnviousArsenal, trait.AutoLoadingHolster],
            [trait.AggregateCharge, trait.BaitAndSwitch],
            ),
        ]
