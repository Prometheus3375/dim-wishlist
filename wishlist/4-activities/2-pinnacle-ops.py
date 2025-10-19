from wishlist import *


class PreAstyanaxIV(RollDefinition):
    """
    Solar Combat Bow, Precision Frame
    https://www.light.gg/db/items/471764396
    """
    item = Item(name='Pre Astyanax IV', hash=471764396)
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
    item = Item(name='Forced Memorializer', hash=1197073834)
    rolls = [
        Roll(
            'PvE',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.ExplosivePayload],
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
    item = Item(name='Seraphine Haze', hash=1524387902)
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


# Special


class Lionfish4FR(RollDefinition):
    """
    Stasis Fusion Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/2423071981
    """
    item = Item(name='Lionfish-4FR', hash=2423071981)
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
    item = Item(name='Mint Retrograde', hash=42435996)
    rolls = [
        Roll(
            'Ad clear',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.TacticalMag, magazine.FlaredMagwell, AnyPerk],
            [trait.Hatchling],
            [trait.OneForAll, trait.ChainReaction],
            ),
        Roll(
            'Damage dealing',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.RewindRounds],
            [trait.BaitAndSwitch, trait.ElementalHoning],
            ),
        ]


class Theodolite(RollDefinition):
    """
    Arc Breechloaded Grenade Launcher, Micro-Missile Frame
    https://www.light.gg/db/items/4146673635
    """
    item = Item(name='Theodolite', hash=4146673635)
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
    item = Item(name='Outrageous Fortune', hash=4146673634)
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
