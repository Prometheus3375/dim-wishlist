from database import *


class WickedSister(RD):
    """
    Strand Power Grenade Launcher, Adaptive Frame
    """
    item = Item(name='Wicked Sister', hash=2039776723)
    rolls = [
        Roll(
            'Damage dealing',
            [barrels.HardLaunch, AnyPerk],
            [magazines.SpikeGrenades, AnyPerk],
            [traits.EnviousArsenal, traits.EnviousAssassin, traits.AutoLoadingHolster],
            [traits.BaitAndSwitch],
            ),
        Roll(
            'High DPS',
            [barrels.QuickLaunch, AnyPerk],
            [magazines.SpikeGrenades, AnyPerk],
            [traits.EnviousArsenal, traits.EnviousAssassin, traits.AutoLoadingHolster],
            [traits.ExplosiveLight],
            ),
        ]


class Cynosure(RD):
    """
    Strand Rocket launcher, Adaptive Frame
    https://www.light.gg/db/items/694275488
    """
    item = Item(name='Cynosure', hash=694275488)
    roll = Roll(
        'Damage dealing',
        [barrels.QuickLaunch, AnyPerk],
        [magazines.ImpactCasing, AnyPerk],
        [traits.Reconstruction, traits.ClownCartridge, traits.EnviousArsenal, traits.Demolitionist],
        [traits.ExplosiveLight, traits.LastingImpression],
        )


# Nightfalls


class Palindrome(RD):
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
        [barrels.Smallbore, AnyPerk],
        [magazines.FlaredMagwell, magazines.TacticalMag, AnyPerk],
        [traits.ExplosivePayload],
        [traits.MasterOfArms, traits.RollingStorm],
        [origin.WildCard],
        )


class RakeAngle(RD):
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
        [hafts.LowImpedanceWindings, AnyPerk],
        [magazines.AlloyMagazine, magazines.LightMag, AnyPerk],
        [traits.ReplenishingAegis, traits.Overflow],
        [traits.ChillClip],
        )


class LotusEater(RD):
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
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.AppendedMag, magazines.HighVelocityRounds, AnyPerk],
            [traits.RepulsorBrace],
            [traits.DestabilizingRounds],
            ),
        Roll(
            'Ad clear',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.AppendedMag, magazines.HighVelocityRounds, AnyPerk],
            [traits.Reconstruction],
            [traits.OneForAll],
            ),
        Roll(
            'Withering Gaze',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.AppendedMag, magazines.HighVelocityRounds, AnyPerk],
            [traits.Reconstruction, traits.RepulsorBrace],
            [traits.WitheringGaze],
            ),
        ]


class Scintillation(RD):
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
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.EnhancedBattery, batteries.AcceleratedCoils, AnyPerk],
            [traits.RewindRounds, traits.EnviousAssassin],
            [traits.BaitAndSwitch, traits.Surrounded],
            [origin.VeistStinger],
            ),
        Roll(
            """
            Rewind Rounds with Veist Stinger usually allows to fire all reserves.
            Unfortunately, any mag stat increase above 20 reduces reserves;
            Enhanced Battery is +20, Ionized Battery is +40
            """,
            [batteries.IonizedBattery],
            is_trash=True,
            ),
        ]
