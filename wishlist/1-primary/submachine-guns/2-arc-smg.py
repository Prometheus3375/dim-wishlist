from wishlist import *


class Antedate(RollDefinition):
    """
    Arc Submachine Gun, Adaptive Frame, Anti-Barrier
    Source: "The Desert Perpetual" Raid
    https://www.light.gg/db/items/1435808083
    https://destiny.report/w/1435808083
    """
    item = Item('Antedate', hash=1435808083)
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Dragonfly, trait.Strategist],
            [trait.JoltingFeedback],
            ),
        Roll(
            'Super regen',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.RewindRounds],
            [trait.TargetLock],
            ),
        ]
