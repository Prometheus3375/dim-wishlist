from wishlist import *


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
