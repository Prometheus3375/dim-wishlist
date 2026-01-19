from wishlist import *


class AllOrNothing(RollDefinition):
    """
    Strand Pulse Rifle, Dynamic Heat Weapon
    https://www.light.gg/db/items/3984776322
    """
    items = [
        Item('All or Nothing', hash=3984776322),
        Item('All or Nothing', hash=2023002233),
        ]
    rolls = [
        Roll(
            'Precision combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.Firefly],
            [trait.Hatchling, trait.Tear],
            ),
        ]


class CompactDefender(RollDefinition):
    """
    Void Sidearm, Dynamic Heat Weapon
    https://www.light.gg/db/items/2819552809
    """
    items = [
        Item('Compact Defender', hash=2819552809),
        Item('Compact Defender', hash=2659286158),
        ]
    roll = Roll(
        'Void combo',
        [barrel.ExtendedBarrel, AnyPerk],
        [battery.IonizedHeatsink, AnyPerk],
        [trait.DestabilizingRounds],
        [trait.RepulsorBrace]
        )


class M17FastTalker(RollDefinition):
    """
    Stasis Submachine Gun, Balanced Heat Weapon
    https://www.light.gg/db/items/1419158093
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
            [trait.CrystallineCorpsebloom]
            ),
        Roll(
            'Damage dealing with Peacekeepers',
            [barrel.ChamberedCompensator, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.CoolingBaubles, trait.AttritionOrbs],
            [trait.TargetLock]
            ),
        ]


class ModifiedB7Pistol(RollDefinition):
    """
    Stasis Hand Cannon, Dynamic Heat Weapon
    https://www.light.gg/db/items/3146657388
    """
    items = [
        Item('Modified B-7 Pistol', hash=3146657388),
        Item('Modified B-7 Pistol', hash=1872906663),
        ]
    rolls = [
        Roll(
            'Stasis combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.Rimestealer],
            [trait.CrystallineCorpsebloom, trait.Headstone]
            ),
        Roll(
            'Precision combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.Firefly],
            [trait.Headstone]
            ),
        Roll(
            'Demolitionist',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.Demolitionist],
            [trait.CrystallineCorpsebloom, trait.Headstone]
            ),
        ]


# Special


class UncivilDiscourse(RollDefinition):
    """
    Arc Special Hand Cannon, Dynamic Heat Weapon
    https://www.light.gg/db/items/3146657389
    """
    items = [
        Item('Uncivil Discourse', hash=3146657389),
        Item('Uncivil Discourse', hash=2462965802),
        ]
    rolls = [
        Roll(
            'Damage dealing with Lucky Pants',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.CoolingBaubles, AnyPerk],
            [trait.PrecisionInstrument]
            ),
        ]


# Heavy


class RefurbishedA499(RollDefinition):
    """
    Kinetic Sniper Rifle, Disruption Weapon
    https://www.light.gg/db/items/3661051060
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
            [trait.GutshotStraight],
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
