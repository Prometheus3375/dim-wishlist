from wishlist import *


class Agape(RollDefinition):
    """
    Solar Hand Cannon, Heavy Burst, Anti-Unstoppable
    Source: Exploring Kepler
    https://www.light.gg/db/items/4124362340
    https://destiny.report/w/4124362340
    """
    item = Item('Agape', hash=4124362340)
    rolls = [
        Roll(
            'Lucky Pants combo',
            [barrel.ChamberedCompensator, AnyPerk],
            [magazine.AppendedMag, AnyPerk],
            [trait.RewindRounds],
            [trait.PrecisionInstrument],
            ),
        Roll(
            'Solar combo',
            [barrel.ChamberedCompensator, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.HealClip],
            [trait.Incandescent],
            ),
        ]
