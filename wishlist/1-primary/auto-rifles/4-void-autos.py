from wishlist import *


class CuspSempiternal(RollDefinition):
    """
    Void Auto Rifle, Support Frame, Anti-Overload
    Source: The Desert Perpetual (Epic)
    https://www.light.gg/db/items/2579693381
    https://destiny.report/w/2579693381
    """
    item = Item('Cusp Sempiternal', hash=2579693381)
    rolls = [
        Roll(
            'Self-healing',
            [barrel.FullBore, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Reciprocity],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Ad clear',
            [barrel.FullBore, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Reconstruction, trait.AttritionOrbs],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Void combo',
            [barrel.FullBore, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        ]


class GnawingHunger(RollDefinition):
    """
    Void Auto Rifle, Adaptive Frame, Anti-Barrier
    Source: Gambit
    https://www.light.gg/db/items/214545213
    https://destiny.report/w/214545213
    """
    item = Item('Gnawing Hunger', hash=214545213)


class PositiveOutlook(RollDefinition):
    """
    Void Auto Rifle, Precision Frame, Anti-Barrier
    Source: Fireteam Ops
    https://www.light.gg/db/items/3625635456
    https://destiny.report/w/3625635456
    """
    items = [
        Item('Positive Outlook', hash=3625635456),
        Item('Positive Outlook', hash=1832481283),
        ]


class RecklessOracle(RollDefinition):
    """
    Void Auto Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Pantheon
    https://www.light.gg/db/items/4158265643
    https://destiny.report/w/4158265643
    """
    items = [
        Item('Reckless Oracle', hash=4158265643),
        Item('Reckless Oracle', hash=1802315656),
        ]


class ReghusksPledge(RollDefinition):
    """
    Void Auto Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Iron Banner
    https://www.light.gg/db/items/2370525224
    https://destiny.report/w/2370525224
    """
    item = Item("Reghusk's Pledge", hash=2370525224)
    rolls = [
        Roll(
            'Super roll',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.DestabilizingRounds],
            [trait.ImpromptuAmmunition],
            [trait.RepulsorBrace],
            [trait.AttritionOrbs],
            ),
        Roll(
            'Void combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.DestabilizingRounds],
            [trait.RepulsorBrace],
            ),
        Roll(
            'Ammo generation',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.ImpromptuAmmunition],
            [trait.KillClip, trait.AttritionOrbs],
            ),
        ]


class TheRiposte(RollDefinition):
    """
    Void Auto Rifle, Lightweight Frame, Anti-Overload
    Source: Competitive Crucible
    https://www.light.gg/db/items/866434750
    https://destiny.report/w/866434750
    """
    item = Item('The Riposte', hash=866434750)
