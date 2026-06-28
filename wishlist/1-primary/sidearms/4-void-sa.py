from wishlist import *


class CompactDefender(RollDefinition):
    """
    Void Sidearm, Dynamic Heat Weapon, Anti-Overload
    Source: Renegades
    https://www.light.gg/db/items/2819552809
    https://destiny.report/w/2819552809
    """
    items = [
        Item('Compact Defender', hash=2819552809),
        Item('Compact Defender', hash=2659286158),
        ]
    roll = Roll(
        'Void combo',
        [barrel.ExtendedBarrel, AnyPerk],
        [battery.IonizedHeatsink, AnyPerk],
        [trait.DestabilizingRounds],
        [trait.RepulsorBrace],
        )
