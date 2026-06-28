from wishlist import *


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
    Source: Guardian Games 2025
    https://www.light.gg/db/items/3462679024
    https://destiny.report/w/3462679024
    """
    item = Item('Unsworn', hash=3462679024)
