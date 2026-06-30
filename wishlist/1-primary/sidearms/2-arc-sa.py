from wishlist import *


class AnonymousAutumn(RollDefinition):
    """
    Arc Sidearm, Lightweight Frame, Anti-Overload
    Source: Lord Shaxx
    https://www.light.gg/db/items/1644501332
    https://destiny.report/w/1644501332
    """
    item = Item('Anonymous Autumn', hash=1644501332)


class BrigandsLaw(RollDefinition):
    """
    Arc Sidearm, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Xûr
    https://www.light.gg/db/items/1298815317
    https://destiny.report/w/1298815317
    """
    item = Item("Brigand's Law", hash=1298815317)


class FimbulwinterStitch(RollDefinition):
    """
    Arc Sidearm, Precision Frame, Anti-Barrier
    Source: The Dawning
    https://www.light.gg/db/items/3685829362
    https://destiny.report/w/3685829362
    """
    items = [
        Item('Fimbulwinter Stitch', hash=3685829362),
        Item('Fimbulwinter Stitch', hash=2645567209),
        ]
    rolls = [
        Roll(
            'Ad clear',
            [barrel.FlutedBarrel, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.SuperchargedMagazine],
            [trait.JoltingFeedback, trait.Redirection],
            ),
        Roll(
            'Ad clear',
            [barrel.FlutedBarrel, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.LooseChange],
            [trait.Voltshot],
            ),
        ]


class Forgiveness(RollDefinition):
    """
    Arc Sidearm, Heavy Burst, Anti-Unstoppable
    Source: Saint-14
    https://www.light.gg/db/items/1552443158
    https://destiny.report/w/1552443158
    """
    item = Item('Forgiveness', hash=1552443158)


class TheKeening(RollDefinition):
    """
    Arc Sidearm, Adaptive Frame, Anti-Barrier
    Source: Crucible
    https://www.light.gg/db/items/3902351469
    https://destiny.report/w/3902351469
    """
    items = [
        Item('The Keening', hash=3902351469),
        Item('The Keening', hash=2839128618),
        ]


class TheLastDance(RollDefinition):
    """
    Arc Sidearm, Adaptive Burst, Anti-Barrier
    Source: Commander Zavala
    https://www.light.gg/db/items/4045298483
    https://destiny.report/w/4045298483
    """
    item = Item('The Last Dance', hash=4045298483)
