from wishlist import *


class KingOrfeo(RollDefinition):
    """
    Arc Combat Bow, Precision Frame, Anti-Barrier
    Source: Lawless Events
    https://www.light.gg/db/items/3481382332
    https://destiny.report/w/3481382332
    """
    items = [
        Item('King Orfeo', hash=3481382332),
        Item('King Orfeo', hash=784540300),
        Item('King Orfeo', hash=784540301),
        Item('King Orfeo', hash=784540302),
        Item('King Orfeo', hash=784540303),
        ]
    rolls = [
        Roll(
            'Ad clear',
            [bowstring.ElasticString, AnyPerk],
            [arrow.CompactArrowShaft, AnyPerk],
            [trait.ArchersTempo],
            [trait.Meganeura, trait.JoltingFeedback],
            ),
        Roll(
            'Ad clear',
            [bowstring.ElasticString, AnyPerk],
            [arrow.CompactArrowShaft, AnyPerk],
            [trait.ExplosiveHead],
            [trait.JoltingFeedback],
            ),
        ]


class PointOfTheStag(RollDefinition):
    """
    Arc Combat Bow, Precision Frame, Anti-Barrier
    Source: Iron Banner
    https://www.light.gg/db/items/911019136
    https://destiny.report/w/911019136
    """
    item = Item('Point of the Stag', hash=911019136)
