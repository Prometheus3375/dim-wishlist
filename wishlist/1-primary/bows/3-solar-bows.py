from wishlist import *

_precision_strings = [bowstring.ElasticString, AnyPerk]
_precision_arrows = [arrow.CompactArrowShaft, AnyPerk]
_lightweight_strings = [bowstring.PolymerString, AnyPerk]
_lightweight_arrows = [arrow.FiberglassArrowShaft, AnyPerk]


class Hush(RollDefinition):
    """
    Solar Combat Bow, Precision Frame, Anti-Barrier
    Source: Gambit
    https://www.light.gg/db/items/3638723317
    https://destiny.report/w/3638723317
    """
    item = Item('Hush', hash=3638723317)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            _precision_strings,
            _precision_arrows,
            [trait.ArchersTempo],
            [trait.HipFireGrip],
            [trait.Firefly],
            [trait.Incandescent],
            [trait.ArchersGambit],
            [trait.Meganeura],
            ),
        Roll(
            'Ad clear',
            _precision_strings,
            _precision_arrows,
            [trait.ArchersTempo, trait.Firefly],
            [trait.Incandescent, trait.Meganeura],
            ),
        Roll(
            'Hip-fire combo',
            _precision_strings,
            [arrow.FiberglassArrowShaft, AnyPerk],
            [trait.HipFireGrip],
            [trait.ArchersGambit],
            ),
        ]


class PreAstyanaxIV(RollDefinition):
    """
    Solar Combat Bow, Precision Frame, Anti-Barrier
    Source: Commander Zavala
    https://www.light.gg/db/items/471764396
    https://destiny.report/w/471764396
    """
    item = Item('Pre Astyanax IV', hash=471764396)
    roll = [
        Roll(
            'Super roll',
            _precision_strings,
            _precision_arrows,
            [trait.Firefly],
            [trait.Incandescent],
            [trait.BurningAmbition],
            [trait.ExplosiveHead],
            ),
        Roll(
            'Solar combo',
            _precision_strings,
            _precision_arrows,
            [trait.Incandescent],
            [trait.BurningAmbition],
            ),
        ]


class TyrannyOfHeaven(RollDefinition):
    """
    Solar Combat Bow, Lightweight Frame, Anti-Overload, Craftable
    Source: Last Wish
    https://www.light.gg/db/items/3388655311
    https://destiny.report/w/3388655311
    """
    item = Item('Tyranny of Heaven', hash=3388655311)
    roll = Roll(
        'Solar combo',
        _lightweight_strings,
        _lightweight_arrows,
        [trait.BurningAmbition],
        [trait.Incandescent],
        ),
