from wishlist import *
from . import *


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
            'Super roll',
            precision_strings,
            precision_arrows,
            [trait.ArchersTempo],
            [trait.ExplosiveHead],
            [trait.Meganeura],
            [trait.JoltingFeedback],
            ),
        Roll(
            'Ad clear',
            precision_strings,
            precision_arrows,
            [trait.ArchersTempo],
            [trait.Meganeura, trait.JoltingFeedback],
            ),
        Roll(
            'Ad clear',
            precision_strings,
            precision_arrows,
            [trait.ExplosiveHead],
            [trait.JoltingFeedback],
            ),
        ]


class NonDenouement(RollDefinition):
    """
    Arc Combat Bow, Precision Frame, Anti-Barrier, Craftable
    Source: Salvation's Edge
    https://www.light.gg/db/items/1770490683
    https://destiny.report/w/1770490683
    """
    items = [
        Item('Non-Denouement', hash=1770490683),
        Item('Non-Denouement (Adept)', hash=1039915310),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            precision_strings,
            precision_arrows,
            [trait.Dragonfly],
            [trait.ArchersTempo],
            [trait.ChaosReshaped],
            [trait.Voltshot],
            [trait.Meganeura],
            ),
        Roll(
            'Ad clear',
            precision_strings,
            precision_arrows,
            [trait.ArchersTempo],
            [trait.Voltshot, trait.Meganeura],
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
    rolls = [
        Roll(
            'Super roll',
            precision_strings,
            precision_arrows,
            [trait.ArchersTempo],
            [trait.Dragonfly],
            [trait.HipFireGrip],
            [trait.Voltshot],
            [trait.VorpalWeapon],
            [trait.ArchersGambit],
            ),
        Roll(
            'Ad clear',
            precision_strings,
            precision_arrows,
            [trait.ArchersTempo],
            [trait.Voltshot],
            ),
        Roll(
            'Hip-fire combo',
            precision_strings,
            hipfire_arrows,
            [trait.HipFireGrip],
            [trait.ArchersGambit],
            ),
        ]


class TripwireCanary(RollDefinition):
    """
    Arc Combat Bow, Lightweight Frame, Anti-Overload, Craftable
    Source: Seraph's Shield
    https://www.light.gg/db/items/3849444474
    https://destiny.report/w/3849444474
    """
    item = Item('Tripwire Canary', hash=3849444474)
    roll = Roll(
        'Ad clear',
        lightweight_strings,
        lightweight_arrows,
        [trait.ArchersTempo],
        [trait.ExplosiveHead],
        )
