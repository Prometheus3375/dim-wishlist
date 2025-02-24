from database import *


# region Cassoid
class DedGramaryeIV(RD):
    """
    Ark Shotgun, Lightweight Frame
    https://www.light.gg/db/items/499245245
    """
    item = Item(name='Ded Gramarye IV', hash=499245245)
    _barrels = [barrels.BarrelShroud, barrels.CorkscrewRifling, barrels.Smallbore]
    rolls = [
        Roll(
            'Ad clear',
            _barrels,
            [magazines.AssaultMag, magazines.LightMag, magazines.TacticalMag],
            [traits.Discord, traits.ThreatDetector],
            [traits.ChainReaction],
            ),
        Roll(
            """
            Voltshot.
            Mag increasing perks are not good with Voltshot
            as with them reserves deplete earlier.
            Discord is not an option as it refills mag, does not reload;
            thus, it does not activate Voltshot
            """,
            _barrels,
            [magazines.AssaultMag, magazines.LightMag],
            [traits.ThreatDetector],
            [traits.Voltshot],
            ),
        ]


class QuaFurorV(RD):
    """
    Stasis Machine Gun, Aggressive Frame
    https://www.light.gg/db/items/751880654
    """
    item = Item(name='Qua Furor V', hash=751880654)
    roll = Roll(
        'PvE',
        [barrels.ArrowheadBrake, AnyPerk],
        [magazines.FlaredMagwell, AnyPerk],
        [traits.FeedingFrenzy],
        [traits.OneForAll, traits.Dragonfly],
        )


# endregion
# region Field forged
class LiveFire(RD):
    """
    Stasis Scout Rifle, Precision Frame
    https://www.light.gg/db/items/3612142623
    """
    item = Item(name='Live Fire', hash=3612142623)
    rolls = [
        Roll(
            'Shoot to Loot',
            [traits.RapidHit],
            [traits.ShootToLoot],
            ),
        Roll(
            'Headstone. Prefer Red Tape for Rimestealer + Headstone',
            [traits.Rimestealer, traits.RapidHit],
            [traits.Headstone],
            ),
        ]


# endregion
# region Hakke
class VeledaF(RD):
    """
    Void Sniper Rifle, Aggressive Frame
    https://www.light.gg/db/items/4200122994
    """
    item = Item(name='Veleda-F', hash=4200122994)
    roll = Roll(
        'Withering Gaze',
        [barrels.ArrowheadBrake, AnyPerk],
        [magazines.TacticalMag, magazines.AlloyMagazine, magazines.FlaredMagwell],
        [traits.AirTrigger],
        [traits.WitheringGaze],
        )


class AdmetusD(RD):
    """
    Void Scout Rifle, High-Impact Frame
    https://www.light.gg/db/items/3776430252
    """
    item = Item(name='Admetus-D', hash=3776430252)
    roll = Roll(
        'Withering Gaze',
        [barrels.ArrowheadBrake, AnyPerk],
        [magazines.FlaredMagwell, AnyPerk],
        [traits.RepulsorBrace],
        [traits.WitheringGaze],
        )


# endregion
# region Omolon
class YarovitMG4(RD):
    """
    Stasis Submachine Gun, Lightweight Frame
    https://www.light.gg/db/items/3959549446
    """
    item = Item(name='Yarovit MG4', hash=3959549446)
    roll = Roll(
        'PvE',
        [traits.Strategist, traits.EnlightenedAction],
        [traits.Headstone, traits.Surrounded],
        )


# endregion
# SUROS
class Legato11(RD):
    """
    Solar Shotgun, Pinpoint Slug Frame
    https://www.light.gg/db/items/3753063346
    """
    item = Item(name='Legato-11', hash=3753063346)
    roll = Roll(
        'Damage dealing',
        [barrels.ArrowheadBrake, AnyPerk],
        [magazines.AssaultMag, magazines.TacticalMag, magazines.LightMag],
        [traits.AutoLoadingHolster, traits.TripleTap],
        [traits.VorpalWeapon],
        )


class CruorisFR4(RD):
    """
    Arc Fusion Rifle, Aggressive Frame
    https://www.light.gg/db/items/891996636
    """
    item = Item(name='Cruoris FR4', hash=891996636)


# endregion
# region Tex Mechanica
class BoondoggleMk55(RD):
    """
    Kinetic Submachine Gun, Aggressive Frame
    https://www.light.gg/db/items/32287609
    """
    item = Item(name='Boondoggle Mk. 55', hash=32287609)
    rolls = [
        Roll(
            'Hip-Fire',
            [barrels.ExtendedBarrel, barrels.ArrowheadBrake, AnyPerk],
            [magazines.RicochetRounds, magazines.LightMag, magazines.FlaredMagwell, AnyPerk],
            [traits.HipFireGrip, traits.Subsistence],
            [traits.OffhandStrike],
            ),
        ]


# endregion
# region Veist
class Suspectum4FR(RD):
    """
    Stasis Linear Fusion Rifle, Precision Frame
    https://www.light.gg/db/items/3615421669
    """
    item = Item(name='Suspectum-4FR', hash=3615421669)
    rolls = [
        Roll(
            'Damage dealing',
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.AcceleratedCoils, AnyPerk],
            [traits.EnviousAssassin, traits.EnlightenedAction],
            [traits.PrecisionInstrument],
            ),
        Roll(
            'FTTC does not regenerate ammo if mag is overflowed',
            [traits.EnviousAssassin],
            [traits.FourthTimesTheCharm],
            is_trash=True,
            ),
        ]
# endregion
