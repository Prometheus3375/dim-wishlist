from wishlist import *
from . import *


class Jurisprudent(RollDefinition):
    """
    Stasis Scout Rifle, High-Impact Frame, Anti-Unstoppable
    Source: Banshee-44; Tenet of Bravery
    https://www.light.gg/db/items/4090134063
    https://destiny.report/w/4090134063
    """
    item = Item('Jurisprudent', hash=4090134063)
    roll = Roll(
        'Stasis combo',
        default_barrels,
        default_mags,
        [trait.Rimestealer],
        [trait.Headstone],
        )


class LiveFire(RollDefinition):
    """
    Stasis Scout Rifle, Precision Frame, Anti-Barrier
    Source: Banshee-44
    https://www.light.gg/db/items/3156551031
    https://destiny.report/w/3156551031
    """
    item = Item('Live Fire', hash=3156551031)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Rimestealer],
            [trait.AirTrigger],
            [trait.Headstone],
            [trait.ShootToLoot],
            ),
        Roll(
            'Stasis combo',
            default_barrels,
            default_mags,
            [trait.Rimestealer],
            [trait.Headstone],
            ),
        ]


class RedTape(RollDefinition):
    """
    Stasis Scout Rifle, Lightweight Frame, Anti-Overload
    Source: World
    https://www.light.gg/db/items/736362511
    https://destiny.report/w/736362511
    """
    item = Item('Red Tape', hash=736362511)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Rimestealer],
            [trait.AttritionOrbs],
            [trait.Demolitionist],
            [trait.Headstone],
            [trait.AdrenalineJunkie],
            [trait.ExplosivePayload],
            ),
        Roll(
            'Stasis combo',
            default_barrels,
            default_mags,
            [trait.Rimestealer],
            [trait.Headstone],
            ),
        Roll(
            'Hit combo',
            default_barrels,
            default_mags,
            [trait.AttritionOrbs],
            [trait.ExplosivePayload],
            ),
        Roll(
            'Grenade combo',
            default_barrels,
            default_mags,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        ]
