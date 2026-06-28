from wishlist import *


class QuaFurorV(RollDefinition):
    """
    Stasis Machine Gun, Aggressive Frame
    https://www.light.gg/db/items/751880654
    """
    item = Item('Qua Furor V', hash=751880654)
    roll = Roll(
        'PvE',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.FlaredMagwell, AnyPerk],
        [trait.FeedingFrenzy],
        [trait.OneForAll, trait.Dragonfly],
        )


class VeledaF(RollDefinition):
    """
    Void Sniper Rifle, Aggressive Frame
    https://www.light.gg/db/items/4200122994
    """
    item = Item('Veleda-F', hash=4200122994)
    roll = Roll(
        'Withering Gaze',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.TacticalMag, magazine.AlloyMagazine, magazine.FlaredMagwell],
        [trait.AirTrigger],
        [trait.WitheringGaze],
        )


class YarovitMG4(RollDefinition):
    """
    Stasis Submachine Gun, Lightweight Frame
    https://www.light.gg/db/items/3959549446
    """
    item = Item('Yarovit MG4', hash=3959549446)
    roll = Roll(
        'PvE',
        [trait.Strategist, trait.EnlightenedAction],
        [trait.Headstone, trait.Surrounded],
        )


class Legato11(RollDefinition):
    """
    Solar Shotgun, Pinpoint Slug Frame
    https://www.light.gg/db/items/3753063346
    """
    item = Item('Legato-11', hash=3753063346)
    roll = Roll(
        'Damage dealing',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.AssaultMag, magazine.TacticalMag, magazine.LightMag],
        [trait.AutoLoadingHolster, trait.TripleTap],
        [trait.VorpalWeapon],
        )


class CruorisFR4(RollDefinition):
    """
    Arc Fusion Rifle, Aggressive Frame
    https://www.light.gg/db/items/891996636
    """
    item = Item('Cruoris FR4', hash=891996636)


class BoondoggleMk55(RollDefinition):
    """
    Kinetic Submachine Gun, Aggressive Frame
    https://www.light.gg/db/items/32287609
    """
    item = Item('Boondoggle Mk. 55', hash=32287609)
    rolls = [
        Roll(
            'Hip-Fire',
            [barrel.Smallbore, barrel.CorkscrewRifling, AnyPerk],
            [magazine.RicochetRounds, magazine.LightMag, magazine.FlaredMagwell, AnyPerk],
            [trait.HipFireGrip, trait.Subsistence],
            [trait.OffhandStrike],
            ),
        ]


class Suspectum4FR(RollDefinition):
    """
    Stasis Linear Fusion Rifle, Precision Frame
    https://www.light.gg/db/items/3615421669
    """
    item = Item('Suspectum-4FR', hash=3615421669)
    rolls = [
        Roll(
            'Damage dealing',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.AcceleratedCoils, AnyPerk],
            [trait.EnviousAssassin, trait.EnlightenedAction],
            [trait.PrecisionInstrument],
            ),
        Roll(
            'FTTC does not regenerate ammo if mag is overflowed',
            [trait.EnviousAssassin],
            [trait.FourthTimesTheCharm],
            is_trash=True,
            ),
        ]
