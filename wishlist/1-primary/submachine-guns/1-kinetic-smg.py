from wishlist import *


class Adjudicator(RollDefinition):
    """
    Kinetic Submachine Gun, Precision Frame, Anti-Barrier
    Source: "Prophecy" Dungeon
    https://www.light.gg/db/items/140914741
    https://destiny.report/w/140914741
    """
    item = Item('Adjudicator', hash=140914741)


class MultimachCCX(RollDefinition):
    """
    Kinetic Submachine Gun, Lightweight Frame, Anti-Overload
    Source: Iron Banner
    https://www.light.gg/db/items/3026836571
    https://destiny.report/w/3026836571
    """
    item = Item('Multimach CCX', hash=3026836571)


class PeculiarCharm(RollDefinition):
    """
    Kinetic Submachine Gun, Aggressive Burst, Anti-Unstoppable
    Source: Competitive Crucible
    https://www.light.gg/db/items/3620277039
    https://destiny.report/w/3620277039
    """
    item = Item('Peculiar Charm', hash=3620277039)
    rolls = [
        Roll(
            'Kinetic Tremors',
            [barrel.Smallbore, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.ImpromptuAmmunition, trait.AttritionOrbs],
            [trait.KineticTremors],
            [stock.FittedStock, AnyPerk],
            )
        ]
