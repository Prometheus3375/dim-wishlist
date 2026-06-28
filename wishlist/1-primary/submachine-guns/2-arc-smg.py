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


class OutOfBounds(RollDefinition):
    """
    Arc Submachine Gun, Lightweight Frame, Anti-Overload
    Source: Unspecified
    https://www.light.gg/db/items/2579239008
    https://destiny.report/w/2579239008
    """
    items = [
        Item('Out of Bounds', hash=2579239008),
        Item('Out of Bounds', hash=3021407779),
        ]


class SeventhSeraphVY7(RollDefinition):
    """
    Arc Submachine Gun, Precision Frame, Anti-Barrier
    Source: Unspecified
    https://www.light.gg/db/items/1719169808
    https://destiny.report/w/1719169808
    """
    item = Item('Seventh Seraph VY-7', hash=1719169808)


class Whatchamacallit(RollDefinition):
    """
    Arc Submachine Gun, Aggressive Burst, Anti-Unstoppable
    Source: Pinnacle Ops
    https://www.light.gg/db/items/357669417
    https://destiny.report/w/357669417
    """
    items = [
        Item('Whatchamacallit', hash=357669417),
        Item('Whatchamacallit', hash=149110926),
        ]
