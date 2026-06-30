from wishlist import *


class Antedate(RollDefinition):
    """
    Arc Submachine Gun, Adaptive Frame, Anti-Barrier
    Source: The Desert Perpetual (Both)
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


class IKELOS_SMG_v103(RollDefinition):
    """
    Arc Submachine Gun, Aggressive Frame, Anti-Unstoppable, Craftable
    Source: Season of the Seraph
    https://www.light.gg/db/items/2149683300
    https://destiny.report/w/2149683300
    """
    item = Item('IKELOS_SMG_v1.0.3', hash=2149683300)


class OutOfBounds(RollDefinition):
    """
    Arc Submachine Gun, Lightweight Frame, Anti-Overload
    Source: Crucible
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
    Source: Cosmodrome
    https://www.light.gg/db/items/1719169808
    https://destiny.report/w/1719169808
    """
    item = Item('Seventh Seraph VY-7', hash=1719169808)


class Subjunctive(RollDefinition):
    """
    Arc Submachine Gun, Lightweight Frame, Anti-Overload, Craftable
    Source: Season of the Wish Activities
    https://www.light.gg/db/items/1447836603
    https://destiny.report/w/1447836603
    """
    item = Item('Subjunctive', hash=1447836603)


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
