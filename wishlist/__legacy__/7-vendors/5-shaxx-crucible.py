from wishlist import *


class AnonymousAutumn(RollDefinition):
    """
    Arc Sidearm, Lightweight Frame
    https://www.light.gg/db/items/1051949956
    """
    item = Item('Anonymous Autumn', hash=1051949956)
    roll = Roll(
        'PvE',
        [trait.EddyCurrent, trait.AttritionOrbs, trait.Demolitionist],
        [trait.Voltshot],
        )


class JoxersLongsword(RollDefinition):
    """
    Void Pulse Rifle, Heavy Burst
    https://www.light.gg/db/items/157601190
    """
    item = Item("Joxer's Longsword", hash=157601190)
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Dragonfly],
            [trait.DestabilizingRounds, trait.Demoralize],
            ),
        Roll(
            'Void combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Withering Gaze',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Demolitionist],
            [trait.WitheringGaze],
            ),
        ]
