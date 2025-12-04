from wishlist import *


class MercuryA(RollDefinition):
    """
    Kinetic Combat Bow, High-Impact Longbow
    https://www.light.gg/db/items/2838279629
    """
    item = Item('Mercury-A', hash=2838279629)
    roll = Roll(
        "Hit combo; hits with Kinetic Tremors grant progress for Attrition Orbs",
        [bowstring.ElasticString, AnyPerk],
        [arrow.CompactArrowShaft, AnyPerk],
        [trait.AttritionOrbs],
        [trait.KineticTremors],
        )


class QuaNilusII(RollDefinition):
    """
    Strand Submachine Gun, Adaptive Frame
    https://www.light.gg/db/items/190747610
    """
    item = Item('Qua Nilus II', hash=190747610)
    roll = Roll(
        'PvE',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.FlaredMagwell, AnyPerk],
        [trait.Slice],
        [trait.Hatchling, trait.Surrounded],
        )


class Jurisprudent(RollDefinition):
    """
    Stasis Scout Rifle, High-Impact Frame
    https://www.light.gg/db/items/4090134063
    """
    item = Item('Jurisprudent', hash=4090134063)


class FaustusDecline(RollDefinition):
    """
    Stasis Sidearm, Lightweight Frame
    https://www.light.gg/db/items/1663482635
    """
    item = Item('Faustus Decline', hash=1663482635)
    roll = Roll(
        'PvE',
        [barrel.Smallbore, AnyPerk],
        [magazine.FlaredMagwell, AnyPerk],
        [trait.Demolitionist, trait.Rimestealer],
        [trait.Headstone],
        )


class AhabChar(RollDefinition):
    """
    Solar Auto Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/1411560894
    """
    item = Item('Ahab Char', hash=1411560894)
    roll = Roll(
        'PvE',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.FlaredMagwell, AnyPerk],
        [trait.HealClip],
        [trait.BurningAmbition, trait.KillClip],
        )


class Drang(RollDefinition):
    """
    Solar Sidearm, Adaptive Frame
    https://www.light.gg/db/items/358190158
    """
    item = Item('Drang', hash=358190158)
    roll = Roll(
        'Solar combo',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.TacticalMag, AnyPerk],
        [trait.HealClip],
        [trait.Incandescent],
        )


class MIDAMiniTool(RollDefinition):
    """
    Solar Submachine Gun, Lightweight Frame
    https://www.light.gg/db/items/3946054154
    """
    item = Item('MIDA Mini-Tool', hash=3946054154)
    roll = Roll(
        'Solar combo',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.FlaredMagwell, AnyPerk],
        [trait.HealClip],
        [trait.Incandescent],
        )


class EveningSI4(RollDefinition):
    """
    Solar Sidearm, Adaptive Burst
    https://www.light.gg/db/items/1763361847
    """
    items = [
        Item('Evening SI4', hash=1763361847),
        Item('Evening SI4', hash=3618823368),
        ]
    rolls = [
        Roll(
            'Solar combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.HealClip],
            [trait.Incandescent],
            ),
        Roll(
            'Impromptu Ammunition',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.ImpromptuAmmunition],
            [trait.Incandescent],
            ),
        # Roll(
        #     'Melee regen',
        #     [barrel.ArrowheadBrake, AnyPerk],
        #     [magazine.FlaredMagwell, AnyPerk],
        #     [trait.HealClip],
        #     [trait.CollectivePugilism],
        #     ),
        ]


# Special


class ShorelineDissident(RollDefinition):
    """
    Void Sniper Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/1193318082
    """
    item = Item('Shoreline Dissident', hash=1193318082)
    roll = Roll(
        'Damage dealing',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.TacticalMag, AnyPerk],
        [trait.TripleTap],
        [trait.PrecisionInstrument],
        )


class Unfall(RollDefinition):
    """
    Arc Sidearm, Rocket-Assisted Frame
    https://www.light.gg/db/items/738446555
    """
    item = Item('Unfall', hash=738446555)
    rolls = [
        Roll(
            'Ad clear',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.ImpulseAmplifier],
            [trait.OneForAll, trait.JoltingFeedback],
            ),
        Roll(
            'Deconstruct',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.ImpulseAmplifier],
            [trait.Deconstruct],
            ),
        ]


class HawthornesFieldForgedShotgun(RollDefinition):
    """
    Stasis Shotgun, Lightweight Frame
    https://www.light.gg/db/items/1402874079
    """
    item = Item("Hawthorne's Field-Forged Shotgun", hash=1402874079)
    rolls = [
        Roll(
            'PvP',
            [barrel.Smallbore, barrel.CorkscrewRifling, barrel.BarrelShroud],
            [magazine.AccurizedRounds, magazine.LightMag],
            [trait.ThreatDetector, trait.LoneWolf],
            [trait.OpeningShot, trait.ClosingTime],
            ),
        Roll(
            'Ad clear',
            [barrel.BarrelShroud, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.ThreatDetector],
            [trait.CrystallineCorpsebloom],
            ),
        ]


class Monody44(RollDefinition):
    """
    Void Fusion Rifle, High-Impact Frame
    https://www.light.gg/db/items/3201200906
    """
    item = Item('Monody-44', hash=3201200906)


class Motif41(RollDefinition):
    """
    Solar Breechloaded Grenade Launcher, Area Denial Frame
    https://www.light.gg/db/items/1685533876
    """
    item = Item('Motif-41', hash=1685533876)
    rolls = [
        Roll(
            'Ad clear',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.HealClip, trait.AutoLoadingHolster],
            [trait.Incandescent],
            ),
        Roll(
            'Demolitionist',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.HealClip, trait.AutoLoadingHolster],
            [trait.Demolitionist],
            ),
        Roll(
            'Attrition Orbs',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.HealClip, trait.AutoLoadingHolster],
            [trait.AttritionOrbs],
            ),
        ]


class NoxSiderealIV(RollDefinition):
    """
    Stasis Fusion Rifle, Aggressive Frame
    Random Perks: This item cannot be reacquired from Collections.
    https://www.light.gg/db/items/2875763009
    """
    items = [
        Item('Nox Sidereal IV', hash=2875763009),
        Item('Nox Sidereal IV', hash=74733286),
        ]
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.EnhancedBattery, AnyPerk],
            [trait.AmbitiousAssassin, trait.ClownCartridge, trait.Demolitionist],
            [trait.CrystallineCorpsebloom, trait.ReservoirBurst],
            ),
        ]


class PsiAeternaIV(RollDefinition):
    """
    Arc Pulse Rifle, Micro-Missile Frame
    https://www.light.gg/db/items/3556730800
    """
    items = [
        Item('Psi Aeterna IV', hash=3556730800),
        Item('Psi Aeterna IV', hash=135971347),
        ]
    rolls = [
        Roll(
            'Damage dealing',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.HighVelocityRounds, AnyPerk],
            [trait.TrickleCharge],
            [trait.ElementalHoning],
            ),
        Roll(
            'Ad clear',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds, AnyPerk],
            [trait.StatsForAll, trait.EddyCurrent],
            [trait.OneForAll],
            ),
        Roll(
            'Blast Distributor',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds, AnyPerk],
            [trait.BlastDistributor],
            [trait.OneForAll, trait.ElementalHoning],
            ),
        # Roll(
        #     'Melee regen',
        #     [launcher_barrel.VolatileLaunch, AnyPerk],
        #     [magazine.HighVelocityRounds, AnyPerk],
        #     [trait.BlastDistributor, trait.EddyCurrent, trait.StatsForAll, trait.TrickleCharge],
        #     [trait.CollectivePugilism],
        #     ),
        # Roll(
        #     'Infinite ammo',
        #     [launcher_barrel.VolatileLaunch, AnyPerk],
        #     [magazine.HighVelocityRounds, AnyPerk],
        #     [trait.TrickleCharge],
        #     [trait.RollingStorm],
        #     ),
        ]


class SomethingSomething(RollDefinition):
    """
    Kinetic Sniper Rifle, Aggressive Frame
    https://www.light.gg/db/items/3421075982
    """
    items = [
        Item('Something Something', hash=3421075982),
        Item('Something Something', hash=690412397),
        ]


# Heavy


class Boomslang4FR(RollDefinition):
    """
    Arc Linear Fusion Rifle, Adaptive Burst
    https://www.light.gg/db/items/3926153598
    """
    item = Item('Boomslang-4FR', hash=3926153598)
    roll = Roll(
        'Damage dealing',
        [barrel.ArrowheadBrake, AnyPerk],
        [battery.AcceleratedCoils, AnyPerk],
        [trait.EnviousArsenal, trait.RapidHit],
        [trait.PrecisionInstrument],
        )


class AuroraDawn(RollDefinition):
    """
    Stasis Sword, Wave Sword Frame
    https://www.light.gg/db/items/2111625436
    """
    item = Item('Aurora Dawn', hash=2111625436)
    rolls = [
        Roll(
            'Ad clear',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.TirelessBlade, trait.Unrelenting],
            [trait.OneForAll, trait.ColdSteel],
            ),
        Roll(
            'Damage dealing with Ergo Sum',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.SharpHarvest],
            [trait.WhirlwindBlade],
            ),
        Roll(
            'Damage blocking. Flash Counter applies Cold Steel',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.FlashCounter],
            [trait.ColdSteel],
            ),
        ]


class Haliaetus(RollDefinition):
    """
    Strand Rocket Launcher, High-Impact Frame
    https://www.light.gg/db/items/2155534128
    """
    item = Item('Haliaetus', hash=2155534128)
    rolls = [
        Roll(
            'Damage dealing',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.ImpactCasing, AnyPerk],
            [trait.ClusterBomb, trait.AutoLoadingHolster],
            [trait.AggregateCharge, trait.ReapersTithe, trait.ElementalHoning],
            ),
        Roll(
            'Ad clear',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.AlloyCasing, AnyPerk],
            [trait.ClusterBomb, trait.ImpulseAmplifier],
            [trait.Bipod],
            ),
        ]


class EightySix(RollDefinition):
    """
    Strand Sword, Vortex Frame
    https://www.light.gg/db/items/2344383760
    """
    item = Item('Eighty-Six', hash=2344383760)
    rolls = [
        Roll(
            'Damage dealing',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard],
            [trait.RelentlessStrikes],
            [trait.Redirection, trait.ElementalHoning],
            ),
        Roll(
            'Ad clear',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard],
            [trait.RelentlessStrikes, trait.TirelessBlade],
            [trait.ChainReaction, trait.Hatchling],
            ),
        Roll(
            'Damage blocking',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard],
            [trait.FlashCounter],
            [trait.Hatchling, trait.AttritionOrbs],
            ),
        ]
