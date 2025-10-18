from wishlist import *


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
            'Heal Clip',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.TacticalMag, AnyPerk],
            [traits.HealClip],
            [traits.OneForAll, traits.Redirection, traits.Incandescent],
            ),
        Roll(
            'Ad clear',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.TacticalMag, AnyPerk],
            [traits.ImpulseAmplifier],
            [traits.OneForAll, traits.Redirection],
            ),
        ]


class MIDAMacroTool(RollDefinition):
    """
    Arc Shotgun, Precision Frame
    https://www.light.gg/db/items/2699423382
    """
    item = Item(name='MIDA Macro-Tool', hash=2699423382)
    roll = Roll(
        'PvP',
        [barrels.Smallbore, barrels.CorkscrewRifling, barrels.BarrelShroud],
        [magazines.AccurizedRounds, magazines.LightMag],
        [traits.ThreatDetector],
        [traits.ClosingTime, traits.OpeningShot],
        )
