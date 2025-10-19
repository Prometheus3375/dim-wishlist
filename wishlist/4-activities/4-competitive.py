from wishlist import *


class SolemnRemembrance(RollDefinition):
    """
    Stasis Hand Cannon, Precision Frame
    https://www.light.gg/db/items/4116518582
    """
    item = Item(name='Solemn Remembrance', hash=4116518582)
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.Headstone],
            [trait.Firefly],
            [grip.PolymerGrip, AnyPerk],
            ),
        Roll(
            'Stasis combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.Headstone],
            [trait.Rimestealer],
            [grip.PolymerGrip, AnyPerk],
            ),
        ]
