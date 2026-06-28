from wishlist import *


class DEADHORSE04(RollDefinition):
    """
    Stasis Submachine Gun, Adaptive Frame, Anti-Barrier
    Source: Unspecified
    https://www.light.gg/db/items/822872238
    https://destiny.report/w/822872238
    """
    item = Item('DEADHORSE 04', hash=822872238)


class M17FastTalker(RollDefinition):
    """
    Stasis Submachine Gun, Balanced Heat Weapon, Anti-Overload
    Source: Renegades
    https://www.light.gg/db/items/1419158093
    https://destiny.report/w/1419158093
    """
    items = [
        Item('M-17 "Fast Talker"', hash=1419158093),
        Item('M-17 "Fast Talker"', hash=2770035786),
        ]
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ChamberedCompensator, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.Demolitionist],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Damage dealing with Peacekeepers',
            [barrel.ChamberedCompensator, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.AttritionOrbs],
            [trait.TargetLock],
            ),
        Roll(
            'Damage dealing with Peacekeepers',
            [barrel.ChamberedCompensator, AnyPerk],
            [battery.OverclockedHeatsink, AnyPerk],
            [trait.CoolingBaubles],
            [trait.TargetLock],
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
            'Stasis combo',
            [barrel.PolygonalRifling, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Rimestealer, trait.Demolitionist],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Orb combo',
            [barrel.PolygonalRifling, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.LeadFromLight],
            [trait.AttritionOrbs],
            ),
        ]


class UnendingTempest(RollDefinition):
    """
    Stasis Submachine Gun, Precision Frame, Anti-Barrier
    Source: Unspecified
    https://www.light.gg/db/items/2579239009
    https://destiny.report/w/2579239009
    """
    items = [
        Item('Unending Tempest', hash=2579239009),
        Item('Unending Tempest', hash=673621062),
        ]
