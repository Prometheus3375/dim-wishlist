from wishlist import *
from . import *


class BloodFeud(RollDefinition):
    """
    Stasis Submachine Gun, Aggressive Frame, Anti-Unstoppable, Craftable
    Source: Xûr
    https://www.light.gg/db/items/1509167284
    https://destiny.report/w/1509167284
    """
    item = Item('Blood Feud', hash=1509167284)
    roll = Roll(
        'Melee combo',
        [barrel.PolygonalRifling, AnyPerk],
        default_mags,
        [trait.Pugilist, trait.GraveRobber],
        [trait.Swashbuckler],
        )


class DEADHORSE04(RollDefinition):
    """
    Stasis Submachine Gun, Adaptive Frame, Anti-Barrier
    Source: Distortions
    https://www.light.gg/db/items/822872238
    https://destiny.report/w/822872238
    """
    item = Item('DEADHORSE 04', hash=822872238)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            [barrel.ArrowheadBrake, AnyPerk],
            default_mags,
            [trait.Rimestealer],
            [trait.ImpromptuAmmunition],
            [trait.CrystallineCorpsebloom],
            [trait.Redirection],
            ),
        Roll(
            'Stasis combo',
            [barrel.ArrowheadBrake, AnyPerk],
            default_mags,
            [trait.Rimestealer],
            [trait.CrystallineCorpsebloom],
            ),
        ]


class ForensicNightmare(RollDefinition):
    """
    Stasis Submachine Gun, Precision Frame, Anti-Barrier, Craftable
    Source: Savathûn's Throne World
    https://www.light.gg/db/items/1526296434
    https://destiny.report/w/1526296434
    """
    item = Item('Forensic Nightmare', hash=1526296434)
    roll = Roll(
        'Stasis combo',
        [barrel.FlutedBarrel, AnyPerk],
        default_mags,
        [trait.Rimestealer],
        [trait.CrystallineCorpsebloom],
        )


class M17FastTalker(RollDefinition):
    """
    Stasis Submachine Gun, Balanced Heat Weapon, Anti-Overload
    Source: Lawless Frontier
    https://www.light.gg/db/items/1419158093
    https://destiny.report/w/1419158093
    """
    items = [
        Item('M-17 "Fast Talker"', hash=1419158093),
        Item('M-17 "Fast Talker"', hash=2770035786),
        ]
    rolls = [
        Roll(
            'Super roll',
            [barrel.ExtendedBarrel, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.Demolitionist],
            [trait.CoolingBaubles],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Ad clear',
            [barrel.ExtendedBarrel, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.CoolingBaubles],
            [trait.CrystallineCorpsebloom],
            ),
        ]


class ProlongedEngagement(RollDefinition):
    """
    Stasis Submachine Gun, Lightweight Frame, Anti-Overload
    Source: Fireteam Ops
    https://www.light.gg/db/items/2624561525
    https://destiny.report/w/2624561525
    """
    items = [
        Item('Prolonged Engagement', hash=2624561525),
        Item('Prolonged Engagement', hash=1066772626),
        ]


class RapaciousAppetite(RollDefinition):
    """
    Stasis Submachine Gun, Aggressive Frame, Anti-Unstoppable, Craftable
    Source: Xûr
    https://www.light.gg/db/items/1081724548
    https://destiny.report/w/1081724548
    """
    item = Item('Rapacious Appetite', hash=1081724548)


class SeraphineHaze(RollDefinition):
    """
    Stasis Submachine Gun, Aggressive Frame, Anti-Unstoppable
    Source: Commander Zavala
    https://www.light.gg/db/items/1524387902
    https://destiny.report/w/1524387902
    """
    item = Item('Seraphine Haze', hash=1524387902)
    rolls = [
        Roll(
            'Super roll',
            [barrel.PolygonalRifling, AnyPerk],
            default_mags,
            [trait.LeadFromLight],
            [trait.Rimestealer],
            [trait.AttritionOrbs],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Stasis combo',
            [barrel.PolygonalRifling, AnyPerk],
            default_mags,
            [trait.Rimestealer],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Orb combo',
            [barrel.PolygonalRifling, AnyPerk],
            default_mags,
            [trait.LeadFromLight],
            [trait.AttritionOrbs],
            ),
        ]


class UnendingTempest(RollDefinition):
    """
    Stasis Submachine Gun, Precision Frame, Anti-Barrier
    Source: Crucible
    https://www.light.gg/db/items/2579239009
    https://destiny.report/w/2579239009
    """
    items = [
        Item('Unending Tempest', hash=2579239009),
        Item('Unending Tempest', hash=673621062),
        ]
    rolls = [
        Roll(
            'Super roll',
            [barrel.ArrowheadBrake, AnyPerk],
            default_mags,
            [trait.Demolitionist],
            [trait.AttritionOrbs],
            [trait.CrystallineCorpsebloom],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            default_mags,
            [trait.Demolitionist],
            [trait.CrystallineCorpsebloom],
            ),
        ]
