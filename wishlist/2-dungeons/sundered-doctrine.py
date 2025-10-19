from wishlist import *


class Unloved(RollDefinition):
    """
    Strand Hand Cannon, Heavy Burst
    https://www.light.gg/db/items/2485881870
    """
    item = Item(name='Unloved', hash=2485881870)
    rolls = [
        Roll(
            'PvE',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, magazine.LightMag, magazine.AlloyMagazine, AnyPerk],
            [trait.Hatchling, trait.Dragonfly],
            [trait.Tear, trait.ParacausalAffinity],
            ),
        ]


class Unsworn(RollDefinition):
    """
    Strand Trace Rifle, Adaptive Frame
    https://www.light.gg/db/items/1303313141
    """
    item = Item(name='Unsworn', hash=1303313141)
    rolls = [
        Roll(
            'PvE',
            [barrel.Smallbore, AnyPerk],
            [battery.TacticalBattery, AnyPerk],
            [trait.Tear],
            [trait.Hatchling, trait.DetonatorBeam],
            ),
        Roll(
            'Shoot to Loot',
            [barrel.Smallbore, AnyPerk],
            [battery.TacticalBattery, AnyPerk],
            [trait.ShootToLoot],
            [trait.Hatchling, trait.DetonatorBeam],
            ),
        ]


class Unworthy(RollDefinition):
    """
    Arc Scout Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/2226158470
    """
    item = Item(name='Unworthy', hash=2226158470)
    roll = Roll(
        'PvE',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.FlaredMagwell, AnyPerk],
        [trait.Firefly],
        [trait.Voltshot],
        )


class Unvoiced(RollDefinition):
    """
    Void Shotgun, Pinpoint Slug Frame
    https://www.light.gg/db/items/3360937899
    """
    item = Item(name='Unvoiced', hash=3360937899)
    roll = Roll(
        'Damage dealing',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.TacticalMag, magazine.AssaultMag, magazine.LightMag],
        [trait.Redirection, trait.FourthTimesTheCharm, trait.EnviousArsenal],
        [trait.BaitAndSwitch],
        )
