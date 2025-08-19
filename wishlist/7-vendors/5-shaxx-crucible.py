from database import *


class AnonymousAutumn(RollDefinition):
    """
    Arc Sidearm, Lightweight Frame
    https://www.light.gg/db/items/1051949956
    """
    item = Item(name='Anonymous Autumn', hash=1051949956)
    roll = Roll(
        'PvE',
        [traits.EddyCurrent, traits.AttritionOrbs, traits.Demolitionist],
        [traits.Voltshot],
        )


class JoxersLongsword(RollDefinition):
    """
    Void Pulse Rifle, Heavy Burst
    https://www.light.gg/db/items/157601190
    """
    item = Item(name="Joxer's Longsword", hash=157601190)
    rolls = [
        Roll(
            'Ad clear',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.Dragonfly],
            [traits.DestabilizingRounds, traits.Demoralize],
            ),
        Roll(
            'Void combo',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.RepulsorBrace],
            [traits.DestabilizingRounds],
            ),
        Roll(
            'Withering Gaze',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.Demolitionist],
            [traits.WitheringGaze],
            ),
        ]
