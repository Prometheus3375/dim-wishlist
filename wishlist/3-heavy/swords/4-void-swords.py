from wishlist import *


class SullenClaw(RollDefinition):
    """
    Void Sword, Lightweight Frame, Anti-Overload
    Source: Equilibrium
    https://www.light.gg/db/items/1085743380
    https://destiny.report/w/1085743380
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
            'Movement',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.EagerEdge],
            [trait.AssassinsBlade],
            ),
        Roll(
            'Ad clear',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.ImpromptuAmmunition, trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        # Roll(
        #     'Damage blocking',
        #     [blade.JaggedEdge, AnyPerk],
        #     [guard.SwordmastersGuard, AnyPerk],
        #     [trait.FlashCounter],
        #     [trait.DestabilizingRounds],
        #     ),
        # Roll(
        #     'Melee damage increase',
        #     [blade.HungryEdge, AnyPerk],
        #     [guard.SwordmastersGuard, AnyPerk],
        #     [trait.ProximityPower],
        #     [trait.DestabilizingRounds],
        #     ),
        ]
