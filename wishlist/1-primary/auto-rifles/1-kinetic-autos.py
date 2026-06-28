from wishlist import *


class GiversBlessing(RollDefinition):
    """
    Kinetic Auto Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Exploring Kepler
    https://www.light.gg/db/items/970034755
    https://destiny.report/w/970034755
    """
    item = Item("Giver's Blessing", hash=970034755)
    rolls = [
        Roll(
            'Ammo generation',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.ImpromptuAmmunition],
            [trait.KineticTremors, trait.OneForAll],
            ),
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Demolitionist, trait.FeedingFrenzy],
            [trait.KineticTremors, trait.OneForAll],
            ),
        ]
