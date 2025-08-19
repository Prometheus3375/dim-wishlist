from database import *


class SolemnRemembrance(RollDefinition):
    """
    Stasis Hand Cannon, Precision Frame
    https://www.light.gg/db/items/4116518582
    """
    item = Item(name='Solemn Remembrance', hash=4116518582)
    rolls = [
        Roll(
            'Ad clear',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.TacticalMag, AnyPerk],
            [traits.Headstone],
            [traits.Firefly],
            [grips.PolymerGrip, AnyPerk],
            ),
        Roll(
            'Stasis combo',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.TacticalMag, AnyPerk],
            [traits.Headstone],
            [traits.Rimestealer],
            [grips.PolymerGrip, AnyPerk],
            ),
        ]
