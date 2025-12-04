from wishlist import *


class PreAstyanaxIV(RollDefinition):
    """
    Solar Combat Bow, Precision Frame
    https://www.light.gg/db/items/471764396
    """
    item = Item('Pre Astyanax IV', hash=471764396)
    roll = Roll(
        'Solar combo',
        [bowstring.ElasticString, AnyPerk],
        [arrow.CompactArrowShaft, AnyPerk],
        [trait.Incandescent],
        [trait.BurningAmbition],
        )


class ForcedMemorializer(RollDefinition):
    """
    Kinetic Scout Rifle, Precision Frame
    https://www.light.gg/db/items/1197073834
    """
    item = Item('Forced Memorializer', hash=1197073834)
    rolls = [
        Roll(
            'PvE',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.ExplosivePayload, trait.BewilderingBurst],
            [trait.KineticTremors],
            ),
        Roll(
            'Missile combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.BewilderingBurst],
            [trait.AncillaryOrdinance],
            ),
        ]


class SeraphineHaze(RollDefinition):
    """
    Stasis Submachine Gun, Aggressive Frame
    https://www.light.gg/db/items/1524387902
    """
    item = Item('Seraphine Haze', hash=1524387902)
    rolls = [
        Roll(
            'Stasis combo',
            [barrel.PolygonalRifling, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Rimestealer, trait.Demolitionist],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Orb combo',
            [barrel.PolygonalRifling, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.LeadFromLight],
            [trait.AttritionOrbs],
            ),
        ]


class DutyBound(RollDefinition):
    """
    Kinetic Auto Rifle, Adaptive Frame
    https://www.light.gg/db/items/260532765
    """
    items = [
        Item('Duty Bound', hash=260532765),
        Item('Duty Bound', hash=89693562),
        ]


class HorrorsLeast(RollDefinition):
    """
    Arc Pulse Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/827835657
    """
    items = [
        Item("Horror's Least", hash=827835657),
        Item("Horror's Least", hash=1018012078),
        ]
    rolls = [
        Roll(
            'Arc combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.SuperchargedMagazine],
            [trait.JoltingFeedback],
            ),
        ]


class OxygenSR3(RollDefinition):
    """
    Solar Scout Rifle, Precision Frame
    https://www.light.gg/db/items/4104613038
    """
    items = [
        Item('Oxygen SR3', hash=4104613038),
        Item('Oxygen SR3', hash=444627789),
        ]
    rolls = [
        Roll(
            'PvE',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.HealClip],
            [trait.Meganeura],
            ),
        ]


class SarpedonD(RollDefinition):
    """
    Arc Hand Cannon, Spread Shot
    Random Perks: This item cannot be reacquired from Collections.
    https://www.light.gg/db/items/1242785638
    """
    items = [
        Item('Sarpedon-D', hash=1242785638),
        Item('Sarpedon-D', hash=3318545829),
        ]
    rolls = [
        Roll(
            'Melee damage increase',
            [barrel.BarrelShroud, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.EddyCurrent, trait.ImpromptuAmmunition],
            [trait.OneTwoPunch],
            ),
        Roll(
            'Ad clear',
            [barrel.BarrelShroud, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.EddyCurrent, trait.ImpromptuAmmunition],
            [trait.Voltshot],
            ),
        Roll(
            'Damage dealing',
            [barrel.BarrelShroud, AnyPerk],
            [magazine.AlloyMagazine, AnyPerk],
            [trait.TrickleCharge],
            [trait.TrenchBarrel],
            ),
        # Roll(
        #     'Melee regen',
        #     [barrel.BarrelShroud, AnyPerk],
        #     [magazine.AppendedMag, AnyPerk],
        #     [trait.EddyCurrent, trait.ImpromptuAmmunition, trait.TrickleCharge],
        #     [trait.CollectivePugilism],
        #     ),
        # Roll(
        #     'Infinite ammo',
        #     [barrel.BarrelShroud, AnyPerk],
        #     [magazine.AppendedMag, AnyPerk],
        #     [trait.TrickleCharge],
        #     [trait.RollingStorm],
        #     ),
        ]


# Special


class Lionfish4FR(RollDefinition):
    """
    Stasis Fusion Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/2423071981
    """
    item = Item('Lionfish-4FR', hash=2423071981)
    rolls = [
        Roll(
            'Chill Clip',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.EnhancedBattery, AnyPerk],
            [trait.Reconstruction],
            [trait.ChillClip],
            ),
        Roll(
            'Damage Dealing',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.EnhancedBattery, AnyPerk],
            [trait.Reconstruction],
            [trait.ControlledBurst, trait.ElementalHoning],
            ),
        ]


class MintRetrograde(RollDefinition):
    """
    Strand Pulse Rifle, Rocket-Assisted Frame
    https://www.light.gg/db/items/42435996
    """
    item = Item('Mint Retrograde', hash=42435996)
    rolls = [
        Roll(
            'Damage dealing',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.HighVelocityRounds, AnyPerk],
            [trait.RewindRounds],
            [trait.BaitAndSwitch, trait.ElementalHoning],
            ),
        Roll(
            'Ad clear',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds, AnyPerk],
            [trait.Hatchling],
            [trait.OneForAll],
            ),
        ]


class Theodolite(RollDefinition):
    """
    Arc Breechloaded Grenade Launcher, Micro-Missile Frame
    https://www.light.gg/db/items/4146673635
    """
    item = Item('Theodolite', hash=4146673635)
    rolls = [
        Roll(
            'PvE',
            [launcher_barrel.HardLaunch, AnyPerk],
            [magazine.SpikeGrenades, AnyPerk],
            [trait.Reconstruction],
            [trait.Frenzy, trait.ReapersTithe],
            ),
        ]


# Heavy


class OutrageousFortune(RollDefinition):
    """
    Solar Drum Grenade Launcher, Rapid-Fire Frame
    https://www.light.gg/db/items/4146673634
    """
    item = Item('Outrageous Fortune', hash=4146673634)
    rolls = [
        Roll(
            'Damage dealing',
            [launcher_barrel.HardLaunch, AnyPerk],
            [magazine.SpikeGrenades, AnyPerk],
            [trait.EnviousArsenal],
            [trait.BaitAndSwitch],
            ),
        Roll(
            'High DPS',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.SpikeGrenades, AnyPerk],
            [trait.EnviousArsenal],
            [trait.ExplosiveLight],
            ),
        Roll(
            'Ad clear',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighExplosiveOrdnance, AnyPerk],
            [trait.Incandescent],
            [trait.ChainReaction],
            ),
        ]


class AGoodShout(RollDefinition):
    """
    Void Crossbow, High-Impact Frame
    https://www.light.gg/db/items/3615748501
    """
    items = [
        Item('A Good Shout', hash=3615748501),
        Item('A Good Shout', hash=649691506),
        ]
    rolls = [
        Roll(
            'Ad clear',
            [rail.LowProfileRail, AnyPerk],
            [bolt.HeavyBolts, AnyPerk],
            [trait.BoltScavenger, trait.WitheringGaze],
            [trait.Butterfly],
            ),
        Roll(
            'Void combo',
            [rail.LowProfileRail, AnyPerk],
            [bolt.HeavyBolts, AnyPerk],
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Damage dealing',
            [rail.LowProfileRail, AnyPerk],
            [bolt.HeavyBolts, AnyPerk],
            [trait.EnviousArsenal, trait.WitheringGaze, trait.BoltScavenger],
            [trait.BoxBreathing, trait.HighGround],
            ),
        ]
