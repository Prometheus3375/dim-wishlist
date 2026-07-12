from wishlist import *
from . import *


class Imminence(RollDefinition):
    """
    Strand Submachine Gun, Lightweight Frame, Anti-Overload, Craftable
    Source: Raid "Salvation's Edge"
    https://www.light.gg/db/items/1258168956
    https://destiny.report/w/1258168956
    """
    items = [
        Item('Imminence', hash=1258168956),
        Item('Imminence (Adept)', hash=3951511045),
        ]
    rolls = [
        Roll(
            'Super roll',
            [barrel.ExtendedBarrel, AnyPerk],
            default_mags,
            [trait.Demolitionist],
            [trait.Tear],
            [trait.AmbitiousAssassin],
            [trait.Firefly],
            [trait.ChaosReshaped],
            [trait.Hatchling],
            ),
        Roll(
            'Precision combo',
            [barrel.ExtendedBarrel, AnyPerk],
            default_mags,
            [trait.Tear],
            [trait.Firefly, trait.Hatchling],
            ),
        ]


class QuaNilusII(RollDefinition):
    """
    Strand Submachine Gun, Adaptive Frame, Anti-Barrier
    Source: Commander Zavala
    https://www.light.gg/db/items/190747610
    https://destiny.report/w/190747610
    """
    item = Item('Qua Nilus II', hash=190747610)
    roll = Roll(
        'Strand combo',
        [barrel.ExtendedBarrel, AnyPerk],
        default_mags,
        [trait.Slice],
        [trait.Hatchling],
        )


class SynchronicRoulette(RollDefinition):
    """
    Strand Submachine Gun, Precision Frame, Anti-Barrier
    Source: Terminal Overload
    https://www.light.gg/db/items/3752860091
    https://destiny.report/w/3752860091
    """
    item = Item('Synchronic Roulette', hash=3752860091)
    rolls = [
        Roll(
            'Super roll',
            [barrel.ArrowheadBrake, AnyPerk],
            default_mags,
            [trait.AttritionOrbs],
            [trait.CollectiveDemolition],
            [trait.Hatchling],
            [trait.CollectiveAction],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Collective combo',
            [barrel.ArrowheadBrake, AnyPerk],
            default_mags,
            [trait.CollectiveDemolition],
            [trait.CollectiveAction],
            ),
        ]


class TheImmortal(RollDefinition):
    """
    Strand Submachine Gun, Aggressive Frame, Anti-Unstoppable
    Source: Saint-14
    https://www.light.gg/db/items/2872063099
    https://destiny.report/w/2872063099
    """
    item = Item('The Immortal', hash=2872063099)
    rolls = [
        Roll(
            'Super roll',
            [barrel.PolygonalRifling, AnyPerk],
            default_barrels,
            [trait.ThreatDetector],
            [trait.Hatchling],
            [trait.Demolitionist],
            [trait.MasterOfArms],
            ),
        Roll(
            'Ad clear',
            [barrel.PolygonalRifling, AnyPerk],
            default_barrels,
            [trait.Hatchling, trait.ThreatDetector],
            [trait.MasterOfArms],
            ),
        ]
