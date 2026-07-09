from wishlist import *
from . import *


class HushedWhisper(RollDefinition):
    """
    Strand Combat Bow, Precision Frame, Anti-Barrier
    Source: Festival of the Lost
    https://www.light.gg/db/items/1175295126
    https://destiny.report/w/1175295126
    """
    items = [
        Item('Hushed Whisper', hash=1175295126),
        Item('Hushed Whisper', hash=3574168117),
        ]
    rolls = [
        Roll(
            'Strand combo',
            precision_strings,
            precision_arrows,
            [trait.Tear, trait.Slice],
            [trait.Hatchling],
            ),
        ]


class VengefulWhisper(RollDefinition):
    """
    Strand Combat Bow, Precision Frame, Anti-Barrier
    Source: Dungeon "Warlord's Ruin"
    https://www.light.gg/db/items/1054567917
    https://destiny.report/w/1054567917
    """
    item = Item('Vengeful Whisper', hash=1054567917)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            precision_strings,
            precision_arrows,
            [trait.Tear],
            [trait.HipFireGrip],
            [trait.ExplosiveHead],
            [trait.Hatchling],
            [trait.ArchersGambit],
            [trait.Meganeura],
            ),
        Roll(
            'Strand combo',
            precision_strings,
            precision_arrows,
            [trait.Tear],
            [trait.Hatchling],
            ),
        Roll(
            'Hip-fire combo',
            precision_strings,
            hipfire_arrows,
            [trait.HipFireGrip],
            [trait.ArchersGambit],
            ),
        ]
