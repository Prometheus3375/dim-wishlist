from wishlist import *


class Palindrome(RollDefinition):
    """
    Arc Hand Cannon, Adaptive Frame
    https://www.light.gg/db/items/2876244791
    """
    items = [
        Item(name='The Palindrome', hash=2876244791),
        Item(name='The Palindrome (Adept)', hash=4077588826),
        ]
    roll = Roll(
        'PvE',
        [barrel.Smallbore, AnyPerk],
        [magazine.FlaredMagwell, magazine.TacticalMag, AnyPerk],
        [trait.ExplosivePayload],
        [trait.MasterOfArms],
        [origin.WildCard],
        )


class CruelMercy(RollDefinition):
    """
    Arc Pulse Rifle, Heavy Burst
    https://www.light.gg/db/items/233635202
    """
    items = [
        Item(name='Cruel Mercy', hash=233635202),
        Item(name='Cruel Mercy (Adept)', hash=2347178967),
        ]
    rolls = [
        Roll(
            'PvE',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Dragonfly],
            [trait.Frenzy],
            ),
        # Roll(
        #     'Arc combo',
        #     [barrel.ArrowheadBrake, AnyPerk],
        #     [magazine.FlaredMagwell, AnyPerk],
        #     [trait.EddyCurrent],
        #     [trait.RollingStorm],
        #     ),
        ]


# Special


class RakeAngle(RollDefinition):
    """
    Stasis Aggressive Glaive
    https://www.light.gg/db/items/2298039571
    """
    items = [
        Item(name='Rake Angle', hash=2298039571),
        Item(name='Rake Angle (Adept)', hash=3997086838),
        ]
    roll = Roll(
        """
        Chill Clip.
        Appended Mag, Extended Mag and Backup Mag mod add 1 ammo,
        Adept Mag mod adds 2 ammo, Extended Mag + Adept Mag add 3 ammo.
        I suggest Alloy Magazine + Adept Mag for mag size of 7 and faster reload at 3 ammo
        """,
        [haft.LowImpedanceWindings, AnyPerk],
        [magazine.AlloyMagazine, magazine.LightMag, AnyPerk],
        [trait.ReplenishingAegis, trait.Overflow],
        [trait.ChillClip],
        )


class LotusEater(RollDefinition):
    """
    Void Sidearm, Rocket-Assisted Frame
    https://www.light.gg/db/items/3922217119
    """
    items = [
        Item(name='Lotus-Eater', hash=3922217119),
        Item(name='Lotus-Eater (Adept)', hash=2697143634),
        ]
    rolls = [
        Roll(
            'Void combo',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.AppendedMag, magazine.HighVelocityRounds, AnyPerk],
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Ad clear',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.AppendedMag, magazine.HighVelocityRounds, AnyPerk],
            [trait.Reconstruction],
            [trait.OneForAll],
            ),
        Roll(
            'Withering Gaze',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.AppendedMag, magazine.HighVelocityRounds, AnyPerk],
            [trait.Reconstruction, trait.RepulsorBrace],
            [trait.WitheringGaze],
            ),
        ]


# Heavy


class Scintillation(RollDefinition):
    """
    Strand Linear Fusion Rifle, Adaptive Burst
    https://www.light.gg/db/items/2591257541
    """
    items = [
        Item(name='Scintillation', hash=2591257541),
        Item(name='Scintillation (Adept)', hash=1492522228),
        ]
    rolls = [
        Roll(
            'Damage dealing',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.EnhancedBattery, battery.AcceleratedCoils, AnyPerk],
            [trait.RewindRounds, trait.EnviousAssassin],
            [trait.BaitAndSwitch, trait.Surrounded],
            [origin.VeistStinger],
            ),
        Roll(
            """
            Rewind Rounds with Veist Stinger usually allows to fire all reserves.
            Unfortunately, any mag stat increase above 20 reduces reserves;
            Enhanced Battery is +20, Ionized Battery is +40
            """,
            [battery.IonizedBattery],
            is_trash=True,
            ),
        ]
