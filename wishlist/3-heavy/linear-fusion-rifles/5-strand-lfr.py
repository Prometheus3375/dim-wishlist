from wishlist import *
from . import *


class LaserPainter(RollDefinition):
    """
    Strand Linear Fusion Rifle, Precision Frame, Anti-Barrier
    Source: The Drifter
    https://www.light.gg/db/items/1439354195
    https://destiny.report/w/1439354195
    """
    items = [
        Item('Laser Painter', hash=1439354195),
        Item('Laser Painter', hash=3221722018),
        ]


class Scintillation(RollDefinition):
    """
    Strand Linear Fusion Rifle, Adaptive Burst, Anti-Barrier
    Source: Commander Zavala
    https://www.light.gg/db/items/1207321710
    https://destiny.report/w/1207321710
    """
    items = [
        Item('Scintillation', hash=1207321710),
        Item('Scintillation (Adept)', hash=1492522228),
        Item('Scintillation', hash=2591257541),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_batteries,
            [trait.EnviousAssassin],
            [trait.Cornered],
            [trait.Surrounded],
            [trait.BaitAndSwitch],
            [origin.VeistStinger],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_batteries,
            [trait.EnviousAssassin],
            [trait.BaitAndSwitch],
            [origin.VeistStinger],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_batteries,
            [trait.EnviousAssassin, trait.Cornered],
            [trait.Surrounded],
            [origin.VeistStinger],
            ),
        ]
