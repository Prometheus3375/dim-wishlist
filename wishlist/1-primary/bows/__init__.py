__all__ = (
    'precision_strings',
    'precision_arrows',
    'lightweight_strings',
    'lightweight_arrows',
    'hipfire_arrows',
    )

from wishlist import AnyPerk, arrow, bowstring

precision_strings = [bowstring.ElasticString, AnyPerk]
precision_arrows = [arrow.CompactArrowShaft, AnyPerk]
lightweight_strings = [bowstring.PolymerString, AnyPerk]
lightweight_arrows = [arrow.FiberglassArrowShaft, AnyPerk]
hipfire_arrows = [arrow.FiberglassArrowShaft, AnyPerk]
