from wishlist import *


class FiniteImpactor(RollDefinition):
    """
    Solar Hand Cannon, Adaptive Frame
    https://www.light.gg/db/items/1917334929
    """
    item = Item('Finite Impactor', hash=1917334929)


class ReghusksPledge(RollDefinition):
    """
    Void Auto Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/2370525224
    """
    item = Item("Reghusk's Pledge", hash=2370525224)
    rolls = [
        Roll(
            'Void combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.DestabilizingRounds],
            [trait.RepulsorBrace],
            ),
        Roll(
            'Ammo generation',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.ImpromptuAmmunition],
            [trait.KillClip, trait.AttritionOrbs],
            ),
        ]
