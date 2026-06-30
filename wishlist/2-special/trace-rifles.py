from wishlist import *


class Keraunios(RollDefinition):
    """
    Arc Trace Rifle, Adaptive Frame, Anti-Barrier
    Source: Guardian Games
    https://www.light.gg/db/items/2386208942
    https://destiny.report/w/2386208942
    """
    items = [
        Item('Keraunios', hash=2386208942),
        Item('Keraunios', hash=981450701),
        ]
    rolls = [
        Roll(
            'Super roll',
            [barrel.Smallbore, AnyPerk],
            [battery.TacticalBattery, AnyPerk],
            [trait.FourthTimesTheCharm],
            [trait.SuperchargedMagazine],
            [trait.ShootToLoot],
            [trait.TargetLock],
            [trait.JoltingFeedback],
            [trait.DetonatorBeam],
            ),
        Roll(
            'Ad clear',
            [barrel.Smallbore, AnyPerk],
            [battery.TacticalBattery, AnyPerk],
            [trait.SuperchargedMagazine],
            [trait.JoltingFeedback, trait.DetonatorBeam],
            ),
        Roll(
            'Shoot To Loot',
            [barrel.Smallbore, AnyPerk],
            [battery.TacticalBattery, AnyPerk],
            [trait.ShootToLoot],
            [trait.DetonatorBeam, trait.JoltingFeedback],
            ),
        Roll(
            'Continuous damage',
            [barrel.Smallbore, AnyPerk],
            [battery.TacticalBattery, AnyPerk],
            [trait.FourthTimesTheCharm],
            [trait.TargetLock],
            ),
        ]


class PathOfLeastResistance(RollDefinition):
    """
    Arc Trace Rifle, Adaptive Frame, Anti-Barrier, Craftable
    Source: Seraph's Shield
    https://www.light.gg/db/items/2827764482
    https://destiny.report/w/2827764482
    """
    item = Item('Path of Least Resistance', hash=2827764482)


class AcasiasDejection(RollDefinition):
    """
    Solar Trace Rifle, Adaptive Frame, Anti-Barrier, Craftable
    Source: Root of Nightmares
    https://www.light.gg/db/items/1471212226
    https://destiny.report/w/1471212226
    """
    items = [
        Item("Acasia's Dejection", hash=1471212226),
        Item("Acasia's Dejection (Adept)", hash=3493494807),
        ]


class RetracedPath(RollDefinition):
    """
    Solar Trace Rifle, Adaptive Frame, Anti-Barrier, Craftable
    Source: Eternity
    https://www.light.gg/db/items/548958835
    https://destiny.report/w/548958835
    """
    item = Item('Retraced Path', hash=548958835)


class Chronophage(RollDefinition):
    """
    Void Trace Rifle, Adaptive Frame, Anti-Barrier, Craftable
    Source: Exotic mission "Encore"
    https://www.light.gg/db/items/1886840007
    https://destiny.report/w/1886840007
    """
    item = Item('Chronophage', hash=1886840007)


class HollowDenial(RollDefinition):
    """
    Void Trace Rifle, Adaptive Frame, Anti-Barrier, Craftable
    Source: Presage
    https://www.light.gg/db/items/2323544076
    https://destiny.report/w/2323544076
    """
    item = Item('Hollow Denial', hash=2323544076)


class ActionItem(RollDefinition):
    """
    Stasis Trace Rifle, Adaptive Frame, Anti-Barrier
    Source: Lawless Events
    https://www.light.gg/db/items/527989828
    https://destiny.report/w/527989828
    """
    items = [
        Item('Action Item', hash=527989828),
        Item('Action Item', hash=437854388),
        Item('Action Item', hash=437854389),
        Item('Action Item', hash=437854390),
        Item('Action Item', hash=437854391),
        ]
    rolls = [
        Roll(
            'Super roll',
            [barrel.Smallbore, AnyPerk],
            [battery.TacticalBattery, AnyPerk],
            [trait.Rimestealer],
            [trait.Deconstruct],
            [trait.Demolitionist],
            [trait.CrystallineCorpsebloom],
            [trait.DetonatorBeam],
            ),
        Roll(
            'Stasis combo',
            [barrel.Smallbore, AnyPerk],
            [battery.TacticalBattery, AnyPerk],
            [trait.Rimestealer],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Demolitionist',
            [barrel.Smallbore, AnyPerk],
            [battery.TacticalBattery, AnyPerk],
            [trait.Demolitionist],
            [trait.CrystallineCorpsebloom, trait.DetonatorBeam],
            ),
        Roll(
            'Deconstruct',
            [barrel.Smallbore, AnyPerk],
            [battery.TacticalBattery, AnyPerk],
            [trait.Deconstruct],
            [trait.CrystallineCorpsebloom, trait.DetonatorBeam],
            ),
        ]


class Appetence(RollDefinition):
    """
    Stasis Trace Rifle, Adaptive Frame, Anti-Barrier, Craftable
    Source: Starcrossed
    https://www.light.gg/db/items/4153087276
    https://destiny.report/w/4153087276
    """
    item = Item('Appetence', hash=4153087276)


class Ribbontail(RollDefinition):
    """
    Strand Trace Rifle, Adaptive Frame, Anti-Barrier
    Source: Reclamation Events
    https://www.light.gg/db/items/3576134513
    https://destiny.report/w/3576134513
    """
    items = [
        Item('Ribbontail', hash=3576134513),
        Item('Ribbontail', hash=407150808),
        Item('Ribbontail', hash=407150809),
        Item('Ribbontail', hash=407150810),
        Item('Ribbontail', hash=407150811),
        ]
    roll = Roll(
        'Ad clear',
        [barrel.Smallbore, AnyPerk],
        [battery.TacticalBattery, AnyPerk],
        [trait.Subsistence],
        [trait.Redirection, trait.DetonatorBeam],
        )


class Unsworn(RollDefinition):
    """
    Strand Trace Rifle, Adaptive Frame, Anti-Barrier
    Source: Sundered Doctrine
    https://www.light.gg/db/items/3462679024
    https://destiny.report/w/3462679024
    """
    item = Item('Unsworn', hash=3462679024)
