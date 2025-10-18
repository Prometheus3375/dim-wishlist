from wishlist import *


class PreAstyanaxIV(RollDefinition):
    """
    Solar Combat Bow, Precision Frame
    https://www.light.gg/db/items/471764396
    """
    item = Item(name='Pre Astyanax IV', hash=471764396)
    roll = Roll(
        'Solar combo',
        [strings.ElasticString, AnyPerk],
        [arrows.CompactArrowShaft, AnyPerk],
        [traits.Incandescent],
        [traits.BurningAmbition],
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
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.ExplosivePayload],
            [traits.KineticTremors],
            ),
        Roll(
            'Missile combo',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.BewilderingBurst],
            [traits.AncillaryOrdinance],
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
            [barrels.PolygonalRifling, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.Rimestealer, traits.Demolitionist],
            [traits.CrystallineCorpsebloom],
            ),
        Roll(
            'Orb combo',
            [barrels.PolygonalRifling, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.LeadFromLight],
            [traits.AttritionOrbs],
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
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.EnhancedBattery, AnyPerk],
            [traits.Reconstruction],
            [traits.ChillClip],
            ),
        Roll(
            'Damage Dealing',
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.EnhancedBattery, AnyPerk],
            [traits.Reconstruction],
            [traits.ControlledBurst, traits.ElementalHoning],
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
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.TacticalMag, magazines.FlaredMagwell, AnyPerk],
            [traits.Hatchling],
            [traits.OneForAll, traits.ChainReaction],
            ),
        Roll(
            'Damage dealing',
            [barrels.QuickLaunch, AnyPerk],
            [magazines.TacticalMag, AnyPerk],
            [traits.RewindRounds],
            [traits.BaitAndSwitch, traits.ElementalHoning],
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
            [barrels.HardLaunch, AnyPerk],
            [magazines.SpikeGrenades, AnyPerk],
            [traits.Reconstruction],
            [traits.Frenzy, traits.ReapersTithe],
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
            [barrels.HardLaunch, AnyPerk],
            [magazines.SpikeGrenades, AnyPerk],
            [traits.EnviousArsenal],
            [traits.BaitAndSwitch],
            ),
        Roll(
            'High DPS',
            [barrels.QuickLaunch, AnyPerk],
            [magazines.SpikeGrenades, AnyPerk],
            [traits.EnviousArsenal],
            [traits.ExplosiveLight],
            ),
        Roll(
            'Ad clear',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.HighExplosiveOrdnance, AnyPerk],
            [traits.Incandescent],
            [traits.ChainReaction],
            ),
        ]
