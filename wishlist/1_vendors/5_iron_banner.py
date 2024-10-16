from database import *


class TinashasMastery(RD):
    item = Item(name="Tinasha's Mastery", hash=480368036)
    rolls = [
        roll(
            'Chill Clip roll',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.TacticalMag, AnyPerk],
            [traits.ImpulseAmplifier, traits.LooseChange],
            [traits.ChillClip],
            ),
        roll(
            'Roll for ad clear',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.TacticalMag, AnyPerk],
            [traits.ImpulseAmplifier],
            [traits.OneForAll, traits.Adagio],
            ),
        ]


class ArchonsThunder(RD):
    item = Item(name="Archon's Thunder", hash=2896109856)
    _mags = [
        magazines.AppendedMag,
        magazines.AlloyMagazine,
        magazines.FlaredMagwell,
        magazines.TacticalMag,
        ]
    roll = roll(
        'Roll for ad clear',
        [barrels.ArrowheadBrake, AnyPerk],
        _mags,
        [traits.Rimestealer, traits.AirTrigger],
        [traits.Headstone],
        )
