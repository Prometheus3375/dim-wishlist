from database import *


class TinashasMastery(RD):
    """
    Stasis Sidearm, Rocket-Assisted Frame
    https://www.light.gg/db/items/480368036
    """
    item = Item(name="Tinasha's Mastery", hash=480368036)
    _mag_note = """;
    High-Explosive Ordnance with Backup Mag mod gives the maximum reserves,
    Tactical Mag with Backup Mag mod is the second best
    """

    rolls = [
        Roll(
            f'Chill Clip roll{_mag_note}',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.HighExplosiveOrdnance, magazines.TacticalMag, AnyPerk],
            [traits.ImpulseAmplifier, traits.AirTrigger, traits.LooseChange],
            [traits.ChillClip],
            ),
        Roll(
            f'Roll for ad clear{_mag_note}',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.HighExplosiveOrdnance, magazines.TacticalMag, AnyPerk],
            [traits.ImpulseAmplifier, traits.AirTrigger],
            [traits.OneForAll, traits.Adagio],
            ),
        ]


class ArchonsThunder(RD):
    """
    Stasis Machine Gun, High-Impact Frame
    https://www.light.gg/db/items/2896109856
    """
    item = Item(name="Archon's Thunder", hash=2896109856)
    _mags = [
        magazines.AppendedMag,
        magazines.AlloyMagazine,
        magazines.FlaredMagwell,
        magazines.TacticalMag,
        ]
    roll = Roll(
        'Roll for ad clear',
        [barrels.ArrowheadBrake, AnyPerk],
        _mags,
        [traits.Rimestealer, traits.AirTrigger],
        [traits.Headstone],
        )
