from wishlist import *


class AishasEmbrace(RollDefinition):
    """
    Void Scout Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Saint-14
    https://www.light.gg/db/items/3709368142
    https://destiny.report/w/3709368142
    """
    item = Item("Aisha's Embrace", hash=3709368142)
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.RapidHit, trait.Demoralize],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Withering Gaze',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.RapidHit, trait.Demoralize],
            [trait.WitheringGaze],
            ),
        ]


class Vouchsafe(RollDefinition):
    """
    Void Scout Rifle, Lightweight Frame, Anti-Overload
    Source: Unspecified
    https://www.light.gg/db/items/3218302023
    https://destiny.report/w/3218302023
    """
    item = Item('Vouchsafe', hash=3218302023)
