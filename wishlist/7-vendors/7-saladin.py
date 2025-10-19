from wishlist import *


class Peacebond(RollDefinition):
    """
    Stasis Sidearm, Adaptive Burst
    https://www.light.gg/db/items/3437370193
    """
    item = Item(name='Peacebond', hash=3437370193)
    roll = Roll(
        'PvE',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.FlaredMagwell, magazine.TacticalMag, AnyPerk],
        [trait.Headstone],
        [trait.Rimestealer],
        )


class NatureReclaimed(RollDefinition):
    """
    Solar Scout Rifle, Lightweight Frame
    https://www.light.gg/db/items/2639921391
    """
    item = Item(name='Nature Reclaimed', hash=2639921391)
    rolls = [
        Roll(
            'Shoot to Loot',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.ShootToLoot],
            [trait.ExplosivePayload],
            ),
        Roll(
            'Solar combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.HealClip],
            [trait.Incandescent],
            ),
        ]


# Special


class TinashasMastery(RollDefinition):
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
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighExplosiveOrdnance, magazine.TacticalMag, AnyPerk],
            [trait.ImpulseAmplifier, trait.AirTrigger, trait.LooseChange],
            [trait.ChillClip],
            ),
        Roll(
            f'Ad clear{_mag_note}',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighExplosiveOrdnance, magazine.TacticalMag, AnyPerk],
            [trait.ImpulseAmplifier, trait.AirTrigger],
            [trait.OneForAll, trait.Adagio],
            ),
        ]


class WarlordsSpear(RollDefinition):
    """
    Arc Trace Rifle, Adaptive Frame
    https://www.light.gg/db/items/1968711238
    """
    item = Item(name="Warlord's Spear", hash=1968711238)
    rolls = [
        Roll(
            'Jolting Feedback',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.TacticalBattery, AnyPerk],
            [trait.RewindRounds, trait.LooseChange],
            [trait.JoltingFeedback],
            ),
        Roll(
            'Detonator Beam',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.TacticalBattery, AnyPerk],
            [trait.RewindRounds],
            [trait.DetonatorBeam],
            ),
        ]


# Heavy


class ArchonsThunder(RollDefinition):
    """
    Stasis Machine Gun, High-Impact Frame
    https://www.light.gg/db/items/2896109856
    """
    item = Item(name="Archon's Thunder", hash=2896109856)
    _mags = [
        magazine.AppendedMag,
        magazine.AlloyMagazine,
        magazine.FlaredMagwell,
        magazine.TacticalMag,
        ]
    roll = Roll(
        'Ad clear',
        [barrel.ArrowheadBrake, AnyPerk],
        _mags,
        [trait.Rimestealer, trait.AirTrigger],
        [trait.Headstone],
        )
