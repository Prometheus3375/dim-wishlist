from wishlist import *


class MercuryA(RollDefinition):
    """
    Kinetic Combat Bow, High-Impact Longbow
    https://www.light.gg/db/items/2838279629
    """
    item = Item(name='Mercury-A', hash=2838279629)
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
    item = Item(name='Qua Nilus II', hash=190747610)
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
    item = Item(name='Jurisprudent', hash=4090134063)


class FaustusDecline(RollDefinition):
    """
    Stasis Sidearm, Lightweight Frame
    https://www.light.gg/db/items/1663482635
    """
    item = Item(name='Faustus Decline', hash=1663482635)
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
    item = Item(name='Ahab Char', hash=1411560894)
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
    item = Item(name='Drang', hash=358190158)
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
    item = Item(name='MIDA Mini-Tool', hash=3946054154)
    roll = Roll(
        'Solar combo',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.FlaredMagwell, AnyPerk],
        [trait.HealClip],
        [trait.Incandescent],
        )


# Special


class ShorelineDissident(RollDefinition):
    """
    Void Sniper Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/1193318082
    """
    item = Item(name='Shoreline Dissident', hash=1193318082)
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
    item = Item(name='Unfall', hash=738446555)
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


# Heavy


class Boomslang4FR(RollDefinition):
    """
    Arc Linear Fusion Rifle, Adaptive Burst
    https://www.light.gg/db/items/3926153598
    """
    item = Item(name='Boomslang-4FR', hash=3926153598)
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
    item = Item(name='Aurora Dawn', hash=2111625436)
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
    item = Item(name='Haliaetus', hash=2155534128)
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
