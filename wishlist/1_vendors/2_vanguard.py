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
            'ALH and BnS are good combo',
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.EnhancedBattery, batteries.AcceleratedCoils, AnyPerk],
            [traits.AutoLoadingHolster],
            [traits.BaitAndSwitch],
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
        Adept Mag mod adds 2 ammo.
        I suggest Alloy Magazine + Adept Mag for mag size of 7 and faster reload at 3 ammo
        """,
        [hafts.LowImpedanceWindings, AnyPerk],
        [magazines.AlloyMagazine, magazines.LightMag, AnyPerk],
        [traits.ReplenishingAegis, traits.Overflow],
        [traits.ChillClip],
        )
