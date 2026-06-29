from wishlist import *


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
            [bowstring.ElasticString, AnyPerk],
            [arrow.CompactArrowShaft, AnyPerk],
            [trait.Tear, trait.Slice],
            [trait.Hatchling],
            ),
        ]


class VengefulWhisper(RollDefinition):
    """
    Strand Combat Bow, Precision Frame, Anti-Barrier
    Source: Warlord's Ruin
    https://www.light.gg/db/items/1054567917
    https://destiny.report/w/1054567917
    """
    item = Item('Vengeful Whisper', hash=1054567917)
