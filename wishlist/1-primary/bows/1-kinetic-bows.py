from wishlist import *


class AccruedRedemption(RollDefinition):
    """
    Kinetic Combat Bow, Precision Frame, Anti-Barrier, Craftable
    Source: Garden of Salvation
    https://www.light.gg/db/items/3621336854
    https://destiny.report/w/3621336854
    """
    item = Item('Accrued Redemption', hash=3621336854)


class BitingWinds(RollDefinition):
    """
    Kinetic Combat Bow, Precision Frame, Anti-Barrier
    Source: Europa
    https://www.light.gg/db/items/2485400469
    https://destiny.report/w/2485400469
    """
    item = Item('Biting Winds', hash=2485400469)


class FelTaradiddle(RollDefinition):
    """
    Kinetic Combat Bow, Lightweight Frame, Anti-Overload, Craftable
    Source: Wellspring Boss Bor'gong, Warden of the Spring
    https://www.light.gg/db/items/1399109800
    https://destiny.report/w/1399109800
    """
    item = Item('Fel Taradiddle', hash=1399109800)


class MercuryA(RollDefinition):
    """
    Kinetic Combat Bow, High-Impact Longbow, Anti-Unstoppable
    Source: Commander Zavala
    https://www.light.gg/db/items/2838279629
    https://destiny.report/w/2838279629
    """
    item = Item('Mercury-A', hash=2838279629)
    roll = Roll(
        "Hit combo; hits with Kinetic Tremors grant progress for Attrition Orbs",
        [bowstring.ElasticString, AnyPerk],
        [arrow.CompactArrowShaft, AnyPerk],
        [trait.AttritionOrbs],
        [trait.KineticTremors],
        )
