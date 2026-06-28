from wishlist import *


class HighTyrant(RollDefinition):
    """
    Void Pulse Rifle, Balanced Heat Weapon, Anti-Overload
    Source: Equilibrium
    https://www.light.gg/db/items/2873508409
    https://destiny.report/w/2873508409
    """
    item = Item('High Tyrant', hash=2873508409)
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.DestabilizingRounds, trait.Demolitionist],
            [trait.MasterOfArms, trait.Meganeura, trait.Demoralize],
            ),
        Roll(
            'Void combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.RepulsorBrace],
            [trait.Demoralize],
            ),
        Roll(
            'Withering Gaze',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.DestabilizingRounds],
            [trait.WitheringGaze],
            ),
        ]
