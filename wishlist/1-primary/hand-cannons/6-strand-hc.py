from wishlist import *
from . import *


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
    rolls = [
        Roll(
            'Super roll',
            [barrel.ChamberedCompensator, AnyPerk],
            default_mags,
            [trait.Reconstruction],
            [trait.Slice],
            [trait.ExplosivePayload],
            [trait.Hatchling],
            ),
        Roll(
            'Strand combo',
            [barrel.ChamberedCompensator, AnyPerk],
            default_mags,
            [trait.Slice],
            [trait.Hatchling],
            ),
        ]


class CorundumHammer(RollDefinition):
    """
    Strand Hand Cannon, Adaptive Frame, Anti-Barrier
    Source: Saint-14
    https://www.light.gg/db/items/2263462407
    https://destiny.report/w/2263462407
    """
    item = Item('Corundum Hammer', hash=2263462407)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            [barrel.ArrowheadBrake, AnyPerk],
            default_mags,
            [trait.Firefly],
            [trait.ShootToLoot],
            [trait.Tear],
            [trait.ExplosivePayload],
            ),
        Roll(
            'Shoot to Loot',
            [barrel.ArrowheadBrake, AnyPerk],
            default_mags,
            [trait.ShootToLoot],
            [trait.ExplosivePayload],
            ),
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            default_mags,
            [trait.Firefly],
            [trait.Tear],
            ),
        ]


class KeptConfidence(RollDefinition):
    """
    Strand Hand Cannon, Adaptive Frame, Anti-Barrier, Craftable
    Source: Xûr
    https://www.light.gg/db/items/1875512595
    https://destiny.report/w/1875512595
    """
    item = Item('Kept Confidence', hash=1875512595)


class RoundRobin(RollDefinition):
    """
    Strand Hand Cannon, Aggressive Frame, Anti-Unstoppable, Craftable
    Source: Neomuna
    https://www.light.gg/db/items/2034215657
    https://destiny.report/w/2034215657
    """
    item = Item('Round Robin', hash=2034215657)


class SixthSense(RollDefinition):
    """
    Strand Hand Cannon, Aggressive Frame, Anti-Unstoppable
    Source: Events during season "Lawless"
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
    Source: Dungeon "Sundered Doctrine"
    https://www.light.gg/db/items/388390591
    https://destiny.report/w/388390591
    """
    item = Item('Unloved', hash=388390591)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            [barrel.ChamberedCompensator, AnyPerk],
            [magazine.AlloyMagazine, AnyPerk],
            [trait.Dragonfly],
            [trait.Hatchling],
            [trait.Tear],
            [trait.ParacausalAffinity],
            ),
        Roll(
            'Strand combo',
            [barrel.ChamberedCompensator, AnyPerk],
            [magazine.AlloyMagazine, AnyPerk],
            [trait.Hatchling],
            [trait.Tear],
            ),
        ]
