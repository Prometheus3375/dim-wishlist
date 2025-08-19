from database import *


class MercuryA(RollDefinition):
    """
    Kinetic Combat Bow, High-Impact Longbow
    https://www.light.gg/db/items/2838279629
    """
    item = Item(name='Mercury-A', hash=2838279629)
    roll = Roll(
        "Hit combo; hits with Kinetic Tremors grant progress for Attrition Orbs",
        [strings.ElasticString, AnyPerk],
        [arrows.CompactArrowShaft, AnyPerk],
        [traits.AttritionOrbs],
        [traits.KineticTremors],
        )


class QuaNilusII(RollDefinition):
    """
    Strand Submachine Gun, Adaptive Frame
    https://www.light.gg/db/items/190747610
    """
    item = Item(name='Qua Nilus II', hash=190747610)
    roll = Roll(
        'PvE',
        [barrels.ArrowheadBrake, AnyPerk],
        [magazines.FlaredMagwell, AnyPerk],
        [traits.Slice],
        [traits.Hatchling, traits.Surrounded],
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
        [barrels.Smallbore, AnyPerk],
        [magazines.FlaredMagwell, AnyPerk],
        [traits.Demolitionist, traits.Rimestealer],
        [traits.Headstone],
        )


class AhabChar(RollDefinition):
    """
    Solar Auto Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/1411560894
    """
    item = Item(name='Ahab Char', hash=1411560894)
    roll = Roll(
        'PvE',
        [barrels.ArrowheadBrake, AnyPerk],
        [magazines.FlaredMagwell, AnyPerk],
        [traits.HealClip],
        [traits.BurningAmbition, traits.KillClip],
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
        [barrels.ArrowheadBrake, AnyPerk],
        [magazines.TacticalMag, AnyPerk],
        [traits.TripleTap],
        [traits.PrecisionInstrument],
        )


# Heavy


class Boomslang4FR(RollDefinition):
    """
    Arc Linear Fusion Rifle, Adaptive Burst
    https://www.light.gg/db/items/3926153598
    """
    item = Item(name='Boomslang-4FR', hash=3926153598)
    roll = Roll(
        'Damage dealing',
        [barrels.ArrowheadBrake, AnyPerk],
        [batteries.AcceleratedCoils, AnyPerk],
        [traits.EnviousArsenal],
        [traits.PrecisionInstrument],
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
            [blades.JaggedEdge, AnyPerk],
            [guards.SwordmastersGuard, AnyPerk],
            [traits.TirelessBlade, traits.Unrelenting],
            [traits.OneForAll, traits.ColdSteel],
            ),
        Roll(
            'Damage dealing with Ergo Sum',
            [blades.JaggedEdge, AnyPerk],
            [guards.SwordmastersGuard, AnyPerk],
            [traits.SharpHarvest],
            [traits.WhirlwindBlade],
            ),
        Roll(
            'Damage blocking. Flash Counter applies Cold Steel',
            [blades.JaggedEdge, AnyPerk],
            [guards.SwordmastersGuard, AnyPerk],
            [traits.FlashCounter],
            [traits.ColdSteel],
            ),
        ]
