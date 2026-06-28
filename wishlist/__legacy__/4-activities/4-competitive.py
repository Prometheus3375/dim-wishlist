from wishlist import *


class SolemnRemembrance(RollDefinition):
    """
    Stasis Hand Cannon, Precision Frame
    https://www.light.gg/db/items/4116518582
    """
    item = Item('Solemn Remembrance', hash=4116518582)
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


class PeculiarCharm(RollDefinition):
    """
    Kinetic Submachine Gun, Aggressive Burst
    https://www.light.gg/db/items/3620277039
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
