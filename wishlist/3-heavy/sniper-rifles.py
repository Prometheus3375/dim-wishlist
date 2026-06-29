from wishlist import *


class RefurbishedA499(RollDefinition):
    """
    Kinetic Sniper Rifle, Disruption Weapon, Anti-Barrier
    Source: Lawless Frontier
    https://www.light.gg/db/items/3661051060
    https://destiny.report/w/3661051060
    """
    items = [
        Item('Refurbished A499', hash=3661051060),
        Item('Refurbished A499', hash=593808239),
        ]
    rolls = [
        Roll(
            'Damage dealing',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.SnapshotSights, trait.GutshotStraight],
            [trait.AggregateCharge],
            ),
        Roll(
            'PvE',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.BewilderingBurst],
            [trait.AmbitiousAssassin, trait.AncillaryOrdinance],
            ),
        ]
