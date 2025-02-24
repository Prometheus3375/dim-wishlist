from database import *


class Unloved(RD):
    """
    Strand Hand Cannon, Heavy Burst
    https://www.light.gg/db/items/2485881870
    """
    item = Item(name='Unloved', hash=2485881870)
    rolls = [
        Roll(
            'PvE',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, magazines.LightMag, magazines.AlloyMagazine, AnyPerk],
            [traits.Hatchling, traits.Dragonfly],
            [traits.Tear, traits.ParacausalAffinity],
            ),
        ]


class Unsworn(RD):
    """
    Strand Trace Rifle, Adaptive Frame
    https://www.light.gg/db/items/1303313141
    """
    item = Item(name='Unsworn', hash=1303313141)
    rolls = [
        Roll(
            'PvE',
            [barrels.Smallbore, AnyPerk],
            [batteries.TacticalBattery, AnyPerk],
            [traits.Tear],
            [traits.Hatchling, traits.DetonatorBeam],
            ),
        Roll(
            'Shoot to Loot',
            [barrels.Smallbore, AnyPerk],
            [batteries.TacticalBattery, AnyPerk],
            [traits.ShootToLoot],
            [traits.Hatchling, traits.DetonatorBeam],
            ),
        ]


class Unworthy(RD):
    """
    Arc Scout Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/2226158470
    """
    item = Item(name='Unworthy', hash=2226158470)
    roll = Roll(
        'PvE',
        [barrels.ArrowheadBrake, AnyPerk],
        [magazines.FlaredMagwell, AnyPerk],
        [traits.Firefly],
        [traits.Voltshot, traits.RollingStorm],
        )


class Unvoiced(RD):
    """
    Void Shotgun, Pinpoint Slug Frame
    https://www.light.gg/db/items/3360937899
    """
    item = Item(name='Unvoiced', hash=3360937899)
    roll = Roll(
        'Damage dealing',
        [barrels.ArrowheadBrake, AnyPerk],
        [magazines.TacticalMag, magazines.AssaultMag, magazines.LightMag],
        [traits.FourthTimesTheCharm, traits.EnviousArsenal],
        [traits.BaitAndSwitch, traits.VorpalWeapon],
        )
