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


class StarsInShadow(RollDefinition):
    """
    Solar Pulse Rifle, High-Impact Frame
    https://www.light.gg/db/items/3602242905
    """
    item = Item(name='Stars In Shadow', hash=3602242905)


# Special


class PureRecollection(RollDefinition):
    """
    Void Shotgun, Heavy Burst
    https://www.light.gg/db/items/1956186483
    """
    item = Item(name='Void Shotgun', hash=1956186483)


class ReturnedMemory(RollDefinition):
    """
    Solar Sidearm, Rocket-Assisted Frame
    https://www.light.gg/db/items/4049127142
    """
    item = Item(name='Returned Memory', hash=4049127142)
    rolls = [
        Roll(
            'Ad clear',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.TacticalMag, AnyPerk],
            [traits.ImpulseAmplifier],
            [traits.OneForAll, traits.Redirection],
            ),
        Roll(
            'Solar combo',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.TacticalMag, AnyPerk],
            [traits.HealClip],
            [traits.Incandescent],
            ),
        ]
