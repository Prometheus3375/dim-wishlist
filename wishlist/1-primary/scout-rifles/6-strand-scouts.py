from wishlist import *
from . import *


class FangOfIrYut(RollDefinition):
    """
    Strand Scout Rifle, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Raid "Crota's End"
    https://www.light.gg/db/items/1432682459
    https://destiny.report/w/1432682459
    """
    items = [
        Item('Fang of Ir Yût', hash=1432682459),
        Item('Fang of Ir Yût (Adept)', hash=128782990),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.ShootToLoot],
            [trait.Slice],
            [trait.Tear],
            [trait.Hatchling],
            [trait.Meganeura],
            ),
        Roll(
            'Precision combo',
            default_barrels,
            default_mags,
            [trait.Tear],
            [trait.Hatchling, trait.Meganeura],
            ),
        ]


class Glissando47(RollDefinition):
    """
    Strand Scout Rifle, Precision Frame, Anti-Barrier
    Source: Banshee-44
    https://www.light.gg/db/items/3156551028
    https://destiny.report/w/3156551028
    """
    items = [
        Item('Glissando-47', hash=3156551028),
        Item('Glissando-47', hash=222606050),
        ]
    roll = Roll(
        'Ad clear',
        default_barrels,
        default_mags,
        [trait.Reconstruction],
        [trait.Hatchling],
        )


class Taraxippos(RollDefinition):
    """
    Strand Scout Rifle, Lightweight Frame, Anti-Overload
    Source: Guardian Games
    https://www.light.gg/db/items/4148460558
    https://destiny.report/w/4148460558
    """
    items = [
        Item('Taraxippos', hash=4148460558),
        Item('Taraxippos', hash=2595813005),
        ]


class TheScholar(RollDefinition):
    """
    Strand Scout Rifle, High-Impact Frame, Anti-Unstoppable
    Source: Trials of Osiris
    https://www.light.gg/db/items/3790632261
    https://destiny.report/w/3790632261
    """
    item = Item('The Scholar', hash=3790632261)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Slice],
            [trait.ShootToLoot],
            [trait.Firefly],
            [trait.ExplosivePayload],
            [trait.Tear],
            [trait.Hatchling],
            ),
        Roll(
            'Precision combo',
            default_barrels,
            default_mags,
            [trait.Firefly],
            [trait.Hatchling, trait.Tear],
            ),
        Roll(
            'Shoot to Loot',
            default_barrels,
            default_mags,
            [trait.ShootToLoot],
            [trait.ExplosivePayload],
            ),
        ]
