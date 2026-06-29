from wishlist import *


class LongArm(RollDefinition):
    """
    Arc Scout Rifle, Aggressive Frame, Anti-Unstoppable
    Source: Spire of the Watcher
    https://www.light.gg/db/items/3418719964
    https://destiny.report/w/3418719964
    """
    item = Item('Long Arm', hash=3418719964)


class NoFeelings(RollDefinition):
    """
    Arc Scout Rifle, Precision Frame, Anti-Barrier
    Source: Arena Ops
    https://www.light.gg/db/items/1271275406
    https://destiny.report/w/1271275406
    """
    items = [
        Item('No Feelings', hash=1271275406),
        Item('No Feelings', hash=2979764077),
        ]


class Sublimation(RollDefinition):
    """
    Arc Scout Rifle, High-Impact Frame, Anti-Unstoppable
    Source: Kepler
    https://www.light.gg/db/items/1674692344
    https://destiny.report/w/1674692344
    """
    item = Item('Sublimation', hash=1674692344)


class Unworthy(RollDefinition):
    """
    Arc Scout Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Sundered Doctrine
    https://www.light.gg/db/items/1700366811
    https://destiny.report/w/1700366811
    """
    item = Item('Unworthy', hash=1700366811)


class VoltaicShade(RollDefinition):
    """
    Arc Scout Rifle, Balanced Heat Weapon, Anti-Overload
    Source: Equilibrium
    https://www.light.gg/db/items/71057630
    https://destiny.report/w/71057630
    """
    item = Item('Voltaic Shade', hash=71057630)
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.JoltingFeedback],
            [trait.Voltshot, trait.Meganeura],
            ),
        ]
