from wishlist import *

default_barrels = [barrel.Smallbore, AnyPerk]
default_batteries = [battery.TacticalBattery, AnyPerk]


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
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_batteries,
            [trait.SuperchargedMagazine],
            [trait.ShootToLoot],
            [trait.JoltingFeedback],
            [trait.DetonatorBeam],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_batteries,
            [trait.SuperchargedMagazine],
            [trait.JoltingFeedback, trait.DetonatorBeam],
            ),
        Roll(
            'Shoot To Loot',
            default_barrels,
            default_batteries,
            [trait.ShootToLoot],
            [trait.DetonatorBeam, trait.JoltingFeedback],
            ),
        ]


class PathOfLeastResistance(RollDefinition):
    """
    Arc Trace Rifle, Adaptive Frame, Anti-Barrier, Craftable
    Source: Exotic mission "Seraph's Shield"
    https://www.light.gg/db/items/2827764482
    https://destiny.report/w/2827764482
    """
    item = Item('Path of Least Resistance', hash=2827764482)
    roll = Roll(
        'Shoot To Loot',
        default_barrels,
        default_batteries,
        [trait.ShootToLoot],
        [trait.Dragonfly],
        )


class AcasiasDejection(RollDefinition):
    """
    Solar Trace Rifle, Adaptive Frame, Anti-Barrier, Craftable
    Source: Raid "Root of Nightmares"
    https://www.light.gg/db/items/1471212226
    https://destiny.report/w/1471212226
    """
    items = [
        Item("Acasia's Dejection", hash=1471212226),
        Item("Acasia's Dejection (Adept)", hash=3493494807),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_batteries,
            [trait.FieldPrep],
            [trait.Reconstruction],
            [trait.BurningAmbition],
            [trait.Incandescent],
            [trait.DetonatorBeam],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_batteries,
            [trait.FieldPrep, trait.Reconstruction],
            [trait.Incandescent, trait.DetonatorBeam, trait.ChaosReshaped],
            ),
        Roll(
            'Solar combo',
            default_barrels,
            default_batteries,
            [trait.BurningAmbition],
            [trait.Incandescent],
            ),
        ]


class RetracedPath(RollDefinition):
    """
    Solar Trace Rifle, Adaptive Frame, Anti-Barrier, Craftable
    Source: Eternity
    https://www.light.gg/db/items/548958835
    https://destiny.report/w/548958835
    """
    item = Item('Retraced Path', hash=548958835)
    roll = Roll(
        'Shoot To Loot',
        [barrel.ExtendedBarrel, AnyPerk],
        default_batteries,
        [trait.ShootToLoot],
        [trait.Incandescent],
        )


class Chronophage(RollDefinition):
    """
    Void Trace Rifle, Adaptive Frame, Anti-Barrier, Craftable
    Source: Exotic mission "Encore"
    https://www.light.gg/db/items/1886840007
    https://destiny.report/w/1886840007
    """
    item = Item('Chronophage', hash=1886840007)
    is_chosen = True
    roll = Roll(
        'Void combo',
        default_barrels,
        default_batteries,
        [trait.RepulsorBrace],
        [trait.DestabilizingRounds],
        )


class HollowDenial(RollDefinition):
    """
    Void Trace Rifle, Adaptive Frame, Anti-Barrier, Craftable
    Source: Exotic mission "Presage"
    https://www.light.gg/db/items/2323544076
    https://destiny.report/w/2323544076
    """
    item = Item('Hollow Denial', hash=2323544076)


class ActionItem(RollDefinition):
    """
    Stasis Trace Rifle, Adaptive Frame, Anti-Barrier
    Source: Events during season "Lawless"
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
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_batteries,
            [trait.Rimestealer],
            [trait.Deconstruct],
            [trait.Demolitionist],
            [trait.CrystallineCorpsebloom],
            [trait.DetonatorBeam],
            ),
        Roll(
            'Stasis combo',
            default_barrels,
            default_batteries,
            [trait.Rimestealer],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Deconstruct',
            default_barrels,
            default_batteries,
            [trait.Deconstruct],
            [trait.CrystallineCorpsebloom],
            ),
        ]


class Appetence(RollDefinition):
    """
    Stasis Trace Rifle, Adaptive Frame, Anti-Barrier, Craftable
    Source: Exotic mission "Starcrossed"
    https://www.light.gg/db/items/4153087276
    https://destiny.report/w/4153087276
    """
    item = Item('Appetence', hash=4153087276)


class Ribbontail(RollDefinition):
    """
    Strand Trace Rifle, Adaptive Frame, Anti-Barrier
    Source: Events during season "Reclamation"
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
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_batteries,
            [trait.Subsistence],
            [trait.DetonatorBeam],
            [trait.Redirection],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_batteries,
            [trait.Subsistence],
            [trait.Redirection, trait.DetonatorBeam],
            ),
        ]


class Unsworn(RollDefinition):
    """
    Strand Trace Rifle, Adaptive Frame, Anti-Barrier
    Source: Dungeon "Sundered Doctrine"
    https://www.light.gg/db/items/3462679024
    https://destiny.report/w/3462679024
    """
    item = Item('Unsworn', hash=3462679024)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_batteries,
            [trait.ShootToLoot],
            [trait.Tear],
            [trait.DetonatorBeam],
            [trait.Hatchling],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Strand combo',
            default_barrels,
            default_batteries,
            [trait.Tear],
            [trait.Hatchling],
            ),
        Roll(
            'Shoot To loot',
            default_barrels,
            default_batteries,
            [trait.ShootToLoot],
            [trait.DetonatorBeam],
            ),
        ]
