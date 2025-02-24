from database import *


class Peacebond(RD):
    """
    Stasis Sidearm, Adaptive Burst
    https://www.light.gg/db/items/3437370193
    """
    item = Item(name='Peacebond', hash=3437370193)
    roll = Roll(
        'PvE',
        [barrels.ArrowheadBrake, AnyPerk],
        [magazines.FlaredMagwell, magazines.TacticalMag, AnyPerk],
        [traits.Headstone],
        [traits.Rimestealer],
        )


class TinashasMastery(RD):
    """
    Stasis Sidearm, Rocket-Assisted Frame
    https://www.light.gg/db/items/480368036
    """
    item = Item(name="Tinasha's Mastery", hash=480368036)
    _mag_note = """.
        High-Explosive Ordnance with Backup Mag mod gives the maximum reserves,
        Tactical Mag with Backup Mag mod is the second best
        """

    rolls = [
        Roll(
            f'Chill Clip{_mag_note}',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.HighExplosiveOrdnance, magazines.TacticalMag, AnyPerk],
            [traits.ImpulseAmplifier, traits.AirTrigger, traits.LooseChange],
            [traits.ChillClip],
            ),
        Roll(
            f'Ad clear{_mag_note}',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.HighExplosiveOrdnance, magazines.TacticalMag, AnyPerk],
            [traits.ImpulseAmplifier, traits.AirTrigger],
            [traits.OneForAll, traits.Adagio],
            ),
        ]


class WarlordsSpear(RD):
    """
    Arc Trace Rifle, Adaptive Frame
    https://www.light.gg/db/items/2029899814
    """
    item = Item(name="Warlord's Spear", hash=1968711238)
    roll = Roll(
        'PvE',
        [barrels.Smallbore, AnyPerk],
        [batteries.TacticalBattery, AnyPerk],
        [traits.LooseChange],
        [traits.JoltingFeedback, traits.DetonatorBeam],
        )


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
        'Ad clear',
        [barrels.ArrowheadBrake, AnyPerk],
        _mags,
        [traits.Rimestealer, traits.AirTrigger],
        [traits.Headstone],
        )
