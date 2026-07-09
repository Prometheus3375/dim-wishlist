from wishlist import *
from . import *


class AccruedRedemption(RollDefinition):
    """
    Kinetic Combat Bow, Precision Frame, Anti-Barrier, Craftable
    Source: Raid "Garden of Salvation"
    https://www.light.gg/db/items/3621336854
    https://destiny.report/w/3621336854
    """
    item = Item('Accrued Redemption', hash=3621336854)
    roll = Roll(
        'Ad clear',
        precision_strings,
        precision_arrows,
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
            precision_strings,
            precision_arrows,
            [trait.ArchersTempo],
            [trait.BewilderingBurst],
            [trait.ImpromptuAmmunition],
            [trait.ExplosiveHead],
            [trait.KineticTremors],
            [trait.AllStar],
            ),
        Roll(
            'Ad clear',
            precision_strings,
            precision_arrows,
            [trait.BewilderingBurst],
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
        lightweight_strings,
        lightweight_arrows,
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
            precision_strings,
            precision_arrows,
            [trait.Demolitionist],
            [trait.AttritionOrbs],
            [trait.KineticTremors],
            [trait.AdrenalineJunkie],
            ),
        Roll(
            "Hit combo; hits with Kinetic Tremors grant progress for Attrition Orbs",
            precision_strings,
            precision_arrows,
            [trait.AttritionOrbs],
            [trait.KineticTremors],
            ),
        Roll(
            'Grenade combo',
            precision_strings,
            precision_arrows,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        ]
