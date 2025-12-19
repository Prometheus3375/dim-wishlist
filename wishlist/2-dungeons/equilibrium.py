from wishlist import *


class HighTyrant(RollDefinition):
    """
    Void Pulse Rifle, Balanced Heat Weapon
    https://www.light.gg/db/items/2873508409
    """
    item = Item('High Tyrant', hash=2873508409)
    rolls = [
        Roll(
            'PvE',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.DestabilizingRounds, trait.Demolitionist],
            [trait.MasterOfArms, trait.Demoralize],
            ),
        Roll(
            'Void combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.RepulsorBrace],
            [trait.Demoralize],
            ),
        Roll(
            'Withering Gaze',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.DestabilizingRounds],
            [trait.WitheringGaze],
            ),
        ]


class VoltaicShade(RollDefinition):
    """
    Arc Scout Rifle, Balanced Heat Weapon
    https://www.light.gg/db/items/71057630
    """
    item = Item('Voltaic Shade', hash=71057630)
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.JoltingFeedback],
            [trait.Voltshot, trait.Meganeura],
            ),
        ]


class ZealousIdeal(RollDefinition):
    """
    Solar Auto Rifle, Balanced Heat Weapon
    https://www.light.gg/db/items/1863583117
    """
    item = Item('Zealous Ideal', hash=1863583117)
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ChamberedCompensator, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.HealClip],
            [trait.Incandescent, trait.OneForAll],
            ),
        ]


class ConspiracyHoned(RollDefinition):
    """
    Stasis Sniper Rifle, Dynamic Heat Weapon
    https://www.light.gg/db/items/4062069077
    """
    item = Item('Conspiracy Honed', hash=4062069077)
    rolls = [
        Roll(
            'Damage dealing',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.OverclockedHeatsink, battery.IonizedHeatsink, AnyPerk],
            [trait.VorpalWeapon, trait.CoolingBaubles],
            [trait.BaitAndSwitch],
            ),
        ]


class BitterEnd(RollDefinition):
    """
    Arc Machine Gun, Balanced Heat Weapon
    https://www.light.gg/db/items/954563454
    """
    item = Item('Bitter End', hash=954563454)
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ChamberedCompensator, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.EddyCurrent, trait.AttritionOrbs],
            [trait.KillingTally, trait.OneForAll, trait.JoltingFeedback],
            ),
        Roll(
            'Damage dealing',
            [barrel.ChamberedCompensator, AnyPerk],
            [battery.OverclockedHeatsink, AnyPerk],
            [trait.TrickleCharge],
            [trait.KillingTally],
            ),
        ]


class SullenClaw(RollDefinition):
    """
    Void Sword, Lightweight Frame
    https://www.light.gg/db/items/1085743380
    """
    item = Item('Sullen Claw', hash=1085743380)
    rolls = [
        Roll(
            'Damage dealing',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.VorpalWeapon, trait.RelentlessStrikes],
            [trait.WhirlwindBlade],
            ),
        Roll(
            'Ad clear',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.ImpromptuAmmunition, trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Damage blocking',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.FlashCounter],
            [trait.DestabilizingRounds],
            ),
        # Roll(
        #     'Melee damage increase',
        #     [blade.HungryEdge, AnyPerk],
        #     [guard.SwordmastersGuard, AnyPerk],
        #     [trait.ProximityPower],
        #     [trait.DestabilizingRounds],
        #     ),
        ]
