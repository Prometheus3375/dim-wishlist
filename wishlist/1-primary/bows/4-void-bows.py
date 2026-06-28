from wishlist import *


class ConvenedRecurve(RollDefinition):
    """
    Void Combat Bow, High-Impact Longbow, Anti-Unstoppable
    Source: Fireteam Ops
    https://www.light.gg/db/items/3667861447
    https://destiny.report/w/3667861447
    """
    items = [
        Item('Convened Recurve', hash=3667861447),
        Item('Convened Recurve', hash=2271714488),
        ]


class FortunateStar(RollDefinition):
    """
    Void Combat Bow, Lightweight Frame, Anti-Overload
    Source: Solstice
    https://www.light.gg/db/items/2631466936
    https://destiny.report/w/2631466936
    """
    items = [
        Item('Fortunate Star', hash=2631466936),
        Item('Fortunate Star', hash=591672323),
        ]
    rolls = [
        Roll(
            'Ad clear',
            [bowstring.PolymerString, AnyPerk],
            [arrow.FiberglassArrowShaft, AnyPerk],
            [trait.Dragonfly, trait.ArchersTempo],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Void combo',
            [bowstring.PolymerString, AnyPerk],
            [arrow.FiberglassArrowShaft, AnyPerk],
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds, trait.Demoralize],
            ),
        ]
