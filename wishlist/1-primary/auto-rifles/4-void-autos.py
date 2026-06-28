from wishlist import *


class CuspSempiternal(RollDefinition):
    """
    Void Auto Rifle, Support Frame, Anti-Overload
    Source: "The Desert Perpetual" Epic Raid
    https://www.light.gg/db/items/2579693381
    https://destiny.report/w/2579693381
    """
    item = Item('Cusp Sempiternal', hash=2579693381)
    rolls = [
        Roll(
            'Self-healing',
            [barrel.FullBore, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Reciprocity],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Ad clear',
            [barrel.FullBore, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Reconstruction, trait.AttritionOrbs],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Void combo',
            [barrel.FullBore, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        ]
