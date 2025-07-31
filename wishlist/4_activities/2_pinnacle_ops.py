from database import *


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


# Special


class Lionfish4FR(RollDefinition):
    """
    Stasis Fusion Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/2423071981
    """
    item = Item(name='Lionfish-4FR', hash=2838279629)
    rolls = [
        Roll(
            'Chill Clip',
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.AcceleratedCoils, AnyPerk],
            [traits.Reconstruction],
            [traits.ChillClip],
            ),
        Roll(
            'Damage Dealing',
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.AcceleratedCoils, AnyPerk],
            [traits.Reconstruction],
            [traits.ControlledBurst],
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
