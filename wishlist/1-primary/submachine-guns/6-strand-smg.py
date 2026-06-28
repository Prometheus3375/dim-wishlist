from wishlist import *


class SynchronicRoulette(RollDefinition):
    """
    Strand Submachine Gun, Precision Frame, Anti-Barrier
    Source: Unspecified
    https://www.light.gg/db/items/3752860091
    https://destiny.report/w/3752860091
    """
    item = Item('Synchronic Roulette', hash=3752860091)


class QuaNilusII(RollDefinition):
    """
    Strand Submachine Gun, Adaptive Frame, Anti-Barrier
    Source: Commander Zavala
    https://www.light.gg/db/items/190747610
    https://destiny.report/w/190747610
    """
    item = Item('Qua Nilus II', hash=190747610)
    roll = Roll(
        'PvE',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.FlaredMagwell, AnyPerk],
        [trait.Slice],
        [trait.Hatchling, trait.Surrounded],
        )
