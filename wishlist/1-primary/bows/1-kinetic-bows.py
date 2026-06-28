from wishlist import *


class BitingWinds(RollDefinition):
    """
    Kinetic Combat Bow, Precision Frame, Anti-Barrier
    Source: Europa
    https://www.light.gg/db/items/2485400469
    https://destiny.report/w/2485400469
    """
    item = Item('Biting Winds', hash=2485400469)


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
