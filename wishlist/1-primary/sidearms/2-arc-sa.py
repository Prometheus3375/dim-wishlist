from wishlist import *
from . import *


class AnonymousAutumn(RollDefinition):
    """
    Arc Sidearm, Lightweight Frame, Anti-Overload
    Source: Lord Shaxx
    https://www.light.gg/db/items/1644501332
    https://destiny.report/w/1644501332
    """
    item = Item('Anonymous Autumn', hash=1644501332)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Demolitionist],
            [trait.EddyCurrent],
            [trait.AdrenalineJunkie],
            [trait.Voltshot],
            ),
        Roll(
            'Arc combo',
            default_barrels,
            default_mags,
            [trait.EddyCurrent],
            [trait.Voltshot],
            ),
        Roll(
            'Grenade combo',
            default_barrels,
            default_mags,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        ]


class BrigandsLaw(RollDefinition):
    """
    Arc Sidearm, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Xûr
    https://www.light.gg/db/items/1298815317
    https://destiny.report/w/1298815317
    """
    item = Item("Brigand's Law", hash=1298815317)
    is_chosen = True
    roll = Roll(
        'Ad clear',
        default_barrels,
        default_mags,
        [trait.ThreatDetector],
        [trait.Voltshot],
        )


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
            'Super roll',
            [barrel.FlutedBarrel, AnyPerk],
            default_mags,
            [trait.LooseChange],
            [trait.SuperchargedMagazine],
            [trait.JoltingFeedback],
            [trait.Redirection],
            [trait.Voltshot],
            ),
        Roll(
            'Ad clear',
            [barrel.FlutedBarrel, AnyPerk],
            default_mags,
            [trait.SuperchargedMagazine],
            [trait.JoltingFeedback, trait.Redirection],
            ),
        Roll(
            'Reload combo',
            [barrel.FlutedBarrel, AnyPerk],
            default_mags,
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
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Voltshot],
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            [trait.LooseChange],
            ),
        Roll(
            'Reload combo',
            default_barrels,
            default_mags,
            [trait.Voltshot],
            [trait.LooseChange],
            ),
        Roll(
            'Grenade combo',
            default_barrels,
            default_mags,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        ]


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
    roll = Roll(
        'Arc combo',
        default_barrels,
        default_mags,
        [trait.Voltshot],
        [trait.JoltingFeedback],
        )


class TheLastDance(RollDefinition):
    """
    Arc Sidearm, Adaptive Burst, Anti-Barrier
    Source: Commander Zavala
    https://www.light.gg/db/items/4045298483
    https://destiny.report/w/4045298483
    """
    item = Item('The Last Dance', hash=4045298483)
