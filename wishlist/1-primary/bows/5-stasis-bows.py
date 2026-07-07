from wishlist import *

_precision_strings = [bowstring.ElasticString, AnyPerk]
_precision_arrows = [arrow.CompactArrowShaft, AnyPerk]
_lightweight_strings = [bowstring.PolymerString, AnyPerk]
_lightweight_arrows = [arrow.FiberglassArrowShaft, AnyPerk]


class Raconteur(RollDefinition):
    """
    Stasis Combat Bow, Precision Frame, Anti-Barrier, Craftable
    Source: NODE.OVRD.AVALON
    https://www.light.gg/db/items/45643573
    https://destiny.report/w/45643573
    """
    item = Item('Raconteur', hash=45643573)
    roll = Roll(
        'Stasis combo',
        _precision_strings,
        _precision_arrows,
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
            _lightweight_strings,
            _lightweight_arrows,
            [trait.Rimestealer],
            [trait.ImpromptuAmmunition],
            [trait.Headstone],
            [trait.Firefly],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Stasis combo',
            _lightweight_strings,
            _lightweight_arrows,
            [trait.Rimestealer, trait.Headstone],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Precision combo',
            _lightweight_strings,
            _lightweight_arrows,
            [trait.Headstone],
            [trait.Firefly],
            ),
        ]
