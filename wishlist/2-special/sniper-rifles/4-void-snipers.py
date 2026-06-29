from wishlist import *


class A1000YardStare(RollDefinition):
    """
    Void Sniper Rifle, Adaptive Frame, Anti-Barrier
    Source: Grasp of Avarice
    https://www.light.gg/db/items/1648948519
    https://destiny.report/w/1648948519
    """
    item = Item('1000 Yard Stare', hash=1648948519)


class FrozenOrbit(RollDefinition):
    """
    Void Sniper Rifle, Aggressive Frame, Anti-Unstoppable
    Source: Crucible
    https://www.light.gg/db/items/1516542120
    https://destiny.report/w/1516542120
    """
    items = [
        Item('Frozen Orbit', hash=1516542120),
        Item('Frozen Orbit', hash=232119851),
        ]


class ShorelineDissident(RollDefinition):
    """
    Void Sniper Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Banshee-44
    https://www.light.gg/db/items/1193318082
    https://destiny.report/w/1193318082
    """
    item = Item('Shoreline Dissident', hash=1193318082)
    roll = Roll(
        'Damage dealing',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.TacticalMag, AnyPerk],
        [trait.TripleTap],
        [trait.PrecisionInstrument],
        )


class TrophyHunter(RollDefinition):
    """
    Void Sniper Rifle, Aggressive Frame, Anti-Unstoppable
    Source: Nessus, Unstable Centaur
    https://www.light.gg/db/items/2566169398
    https://destiny.report/w/2566169398
    """
    item = Item('Trophy Hunter', hash=2566169398)
