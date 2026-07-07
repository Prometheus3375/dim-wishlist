from wishlist import *

_precision_strings = [bowstring.ElasticString, AnyPerk]
_precision_arrows = [arrow.CompactArrowShaft, AnyPerk]
_lightweight_strings = [bowstring.PolymerString, AnyPerk]
_lightweight_arrows = [arrow.FiberglassArrowShaft, AnyPerk]


class AccruedRedemption(RollDefinition):
    """
    Kinetic Combat Bow, Precision Frame, Anti-Barrier, Craftable
    Source: Garden of Salvation
    https://www.light.gg/db/items/3621336854
    https://destiny.report/w/3621336854
    """
    item = Item('Accrued Redemption', hash=3621336854)
    roll = Roll(
        'Ad clear',
        _precision_strings,
        _precision_arrows,
        [trait.ArchersTempo, trait.AttritionOrbs],
        [trait.KineticTremors],
        )


class BitingWinds(RollDefinition):
    """
    Kinetic Combat Bow, Precision Frame, Anti-Barrier
    Source: Europa
    https://www.light.gg/db/items/2485400469
    https://destiny.report/w/2485400469
    """
    item = Item('Biting Winds', hash=2485400469)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            _precision_strings,
            _precision_arrows,
            [trait.ArchersTempo],
            [trait.BewilderingBurst],
            [trait.ImpromptuAmmunition],
            [trait.ExplosiveHead],
            [trait.KineticTremors],
            ),
        ]


class FelTaradiddle(RollDefinition):
    """
    Kinetic Combat Bow, Lightweight Frame, Anti-Overload, Craftable
    Source: Wellspring Boss Bor'gong, Warden of the Spring
    https://www.light.gg/db/items/1399109800
    https://destiny.report/w/1399109800
    """
    item = Item('Fel Taradiddle', hash=1399109800)
    roll = Roll(
        'Ad clear',
        _lightweight_strings,
        _lightweight_arrows,
        [trait.ArchersTempo],
        [trait.OneForAll],
        )


class MercuryA(RollDefinition):
    """
    Kinetic High-Impact Longbow, Anti-Unstoppable
    Source: Commander Zavala
    https://www.light.gg/db/items/2838279629
    https://destiny.report/w/2838279629
    """
    item = Item('Mercury-A', hash=2838279629)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            _precision_strings,
            _precision_arrows,
            [trait.Demolitionist],
            [trait.AttritionOrbs],
            [trait.KineticTremors],
            [trait.AdrenalineJunkie],
            ),
        Roll(
            "Hit combo; hits with Kinetic Tremors grant progress for Attrition Orbs",
            _precision_strings,
            _precision_arrows,
            [trait.AttritionOrbs],
            [trait.KineticTremors],
            ),
        Roll(
            'Grenade combo',
            _precision_strings,
            _precision_arrows,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        ]
