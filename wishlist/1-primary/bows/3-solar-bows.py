from wishlist import *


class Hush(RollDefinition):
    """
    Solar Combat Bow, Precision Frame, Anti-Barrier
    Source: Gambit
    https://www.light.gg/db/items/3638723317
    https://destiny.report/w/3638723317
    """
    item = Item('Hush', hash=3638723317)


class PreAstyanaxIV(RollDefinition):
    """
    Solar Combat Bow, Precision Frame, Anti-Barrier
    Source: Commander Zavala
    https://www.light.gg/db/items/471764396
    https://destiny.report/w/471764396
    """
    item = Item('Pre Astyanax IV', hash=471764396)
    roll = Roll(
        'Solar combo',
        [bowstring.ElasticString, AnyPerk],
        [arrow.CompactArrowShaft, AnyPerk],
        [trait.Incandescent],
        [trait.BurningAmbition],
        )
