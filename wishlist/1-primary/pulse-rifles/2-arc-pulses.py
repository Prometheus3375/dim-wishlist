from wishlist import *


class CruelMercy(RollDefinition):
    """
    Arc Pulse Rifle, Heavy Burst, Anti-Unstoppable
    Source: Commander Zavala
    https://www.light.gg/db/items/4011513985
    https://destiny.report/w/4011513985
    """
    item = Item('Cruel Mercy', hash=4011513985)


class HorrorsLeast(RollDefinition):
    """
    Arc Pulse Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Commander Zavala
    https://www.light.gg/db/items/827835657
    https://destiny.report/w/827835657
    """
    items = [
        Item("Horror's Least", hash=827835657),
        Item("Horror's Least", hash=1018012078),
        ]
    rolls = [
        Roll(
            'Arc combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.SuperchargedMagazine],
            [trait.JoltingFeedback],
            ),
        ]


class InfinitePaths8(RollDefinition):
    """
    Arc Pulse Rifle, Lightweight Frame, Anti-Overload
    Source: World
    https://www.light.gg/db/items/3176697588
    https://destiny.report/w/3176697588
    """
    item = Item('Infinite Paths 8', hash=3176697588)


class TheThirdAxiom(RollDefinition):
    """
    Arc Pulse Rifle, Adaptive Frame, Anti-Barrier
    Source: Commander Zavala
    https://www.light.gg/db/items/3744058588
    https://destiny.report/w/3744058588
    """
    item = Item('The Third Axiom', hash=3744058588)
