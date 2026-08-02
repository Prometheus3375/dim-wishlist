from wishlist import *
from . import *


class Accelerando42(RollDefinition):
    """
    Strand Fusion Rifle, Precision Frame, Anti-Barrier
    Source: Sparrow Racing League
    https://www.light.gg/db/items/3610531207
    https://destiny.report/w/3610531207
    """
    items = [
        Item('Accelerando-42', hash=3610531207),
        Item('Accelerando-42', hash=1540621132),
        ]


class NoxPerennialV(RollDefinition):
    """
    Strand Fusion Rifle, High-Impact Frame, Anti-Unstoppable
    Source: World
    https://www.light.gg/db/items/2366022261
    https://destiny.report/w/2366022261
    """
    items = [
        Item('Nox Perennial V', hash=2366022261),
        Item('Nox Perennial V', hash=2767393525),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_battery,
            [trait.EnviousAssassin],
            [trait.ThreatDetector],
            [trait.ControlledBurst],
            [trait.Hatchling],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_battery,
            [trait.EnviousAssassin],
            [trait.ControlledBurst],
            ),
        ]


class PressurizedPrecision(RollDefinition):
    """
    Strand Fusion Rifle, Adaptive Frame, Anti-Barrier
    Source: Iron Banner
    https://www.light.gg/db/items/293709640
    https://destiny.report/w/293709640
    """
    item = Item('Pressurized Precision', hash=293709640)


class Resounding(RollDefinition):
    """
    Strand Fusion Rifle, Aggressive Frame, Anti-Unstoppable
    Source: Solo Ops
    https://www.light.gg/db/items/3273807888
    https://destiny.report/w/3273807888
    """
    item = Item('Resounding', hash=3273807888)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_battery,
            [trait.Cornered],
            [trait.AmbitiousAssassin],
            [trait.Slice],
            [trait.Hatchling],
            [trait.ReservoirBurst],
            [trait.Surrounded],
            ),
        Roll(
            'Strand combo',
            default_barrels,
            default_battery,
            [trait.Slice],
            [trait.Hatchling],
            ),
        Roll(
            'Mag combo',
            default_barrels,
            default_battery,
            [trait.AmbitiousAssassin],
            [trait.ReservoirBurst],
            ),
        Roll(
            'Surrounded combo',
            default_barrels,
            default_battery,
            [trait.Cornered],
            [trait.Surrounded],
            ),
        ]


class ScatterSignal(RollDefinition):
    """
    Strand Fusion Rifle, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Exotic mission "Starcrossed"
    https://www.light.gg/db/items/2558925366
    https://destiny.report/w/2558925366
    """
    item = Item('Scatter Signal', hash=2558925366)


class TAHOMA01(RollDefinition):
    """
    Strand Fusion Rifle, Aggressive Frame, Anti-Unstoppable
    Source: Distortions
    https://www.light.gg/db/items/1225851434
    https://destiny.report/w/1225851434
    """
    item = Item('TAHOMA 01', hash=1225851434)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_battery,
            [trait.Hatchling],
            [trait.CollectiveDemolition],
            [trait.ReservoirBurst],
            [trait.CollectiveAction],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_battery,
            [trait.Hatchling],
            [trait.ReservoirBurst],
            ),
        Roll(
            'Collective combo',
            default_barrels,
            default_battery,
            [trait.CollectiveDemolition],
            [trait.CollectiveAction],
            ),
        ]
