from wishlist import *
from . import *


class Raconteur(RollDefinition):
    """
    Stasis Combat Bow, Precision Frame, Anti-Barrier, Craftable
    Source: Exotic mission "NODE.OVRD.AVALON"
    https://www.light.gg/db/items/45643573
    https://destiny.report/w/45643573
    """
    item = Item('Raconteur', hash=45643573)
    roll = Roll(
        'Stasis combo',
        precision_strings,
        precision_arrows,
        [trait.ArchersTempo],
        [trait.Headstone],
        )


class TheSpitefulFang(RollDefinition):
    """
    Stasis Combat Bow, Lightweight Frame, Anti-Overload
    Source: Arena Ops
    https://www.light.gg/db/items/1094998581
    https://destiny.report/w/1094998581
    """
    items = [
        Item('The Spiteful Fang', hash=1094998581),
        Item('The Spiteful Fang', hash=1704597062),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            lightweight_strings,
            lightweight_arrows,
            [trait.Rimestealer],
            [trait.ImpromptuAmmunition],
            [trait.Headstone],
            [trait.Firefly],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Stasis combo',
            lightweight_strings,
            lightweight_arrows,
            [trait.Rimestealer, trait.Headstone],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Precision combo',
            lightweight_strings,
            lightweight_arrows,
            [trait.Headstone],
            [trait.Firefly],
            ),
        ]
