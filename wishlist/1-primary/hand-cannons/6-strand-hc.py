from wishlist import *


class BetterDevils(RollDefinition):
    """
    Strand Hand Cannon, Adaptive Frame, Anti-Barrier
    Source: Crucible
    https://www.light.gg/db/items/4059111041
    https://destiny.report/w/4059111041
    """
    items = [
        Item('Better Devils', hash=4059111041),
        Item('Better Devils', hash=2106353446),
        ]


class CorundumHammer(RollDefinition):
    """
    Strand Hand Cannon, Adaptive Frame, Anti-Barrier
    Source: Saint-14
    https://www.light.gg/db/items/2263462407
    https://destiny.report/w/2263462407
    """
    item = Item('Corundum Hammer', hash=2263462407)
    rolls = [
        Roll(
            'Shoot to Loot',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.ShootToLoot],
            [trait.ExplosivePayload],
            ),
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.Firefly],
            [trait.Tear],
            ),
        ]


class SixthSense(RollDefinition):
    """
    Strand Hand Cannon, Aggressive Frame, Anti-Unstoppable
    Source: Lawless Events
    https://www.light.gg/db/items/3163473092
    https://destiny.report/w/3163473092
    """
    items = [
        Item('Sixth Sense', hash=3163473092),
        Item('Sixth Sense', hash=4032097588),
        Item('Sixth Sense', hash=4032097589),
        Item('Sixth Sense', hash=4032097590),
        Item('Sixth Sense', hash=4032097591),
        ]


class Unloved(RollDefinition):
    """
    Strand Hand Cannon, Heavy Burst, Anti-Unstoppable
    Source: Sundered Doctrine
    https://www.light.gg/db/items/388390591
    https://destiny.report/w/388390591
    """
    item = Item('Unloved', hash=388390591)
