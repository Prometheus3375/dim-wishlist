from wishlist import *


class ChivalricFire(RollDefinition):
    """
    Void Sword, Caster Frame, Anti-Barrier
    Source: Solo Ops
    https://www.light.gg/db/items/938936806
    https://destiny.report/w/938936806
    """
    item = Item('Chivalric Fire', hash=938936806)


class DeathsRazor(RollDefinition):
    """
    Void Sword, Vortex Frame, Anti-Overload, Craftable
    Source: Xûr
    https://www.light.gg/db/items/3371413056
    https://destiny.report/w/3371413056
    """
    item = Item("Death's Razor", hash=3371413056)


class FallingGuillotine(RollDefinition):
    """
    Void Sword, Vortex Frame, Anti-Overload
    Source: Onslaught
    https://www.light.gg/db/items/2480871539
    https://destiny.report/w/2480871539
    """
    item = Item('Falling Guillotine', hash=2480871539)


class StrykersSureHand(RollDefinition):
    """
    Void Sword, Aggressive Frame, Anti-Unstoppable
    Source: Arena Ops
    https://www.light.gg/db/items/2490460292
    https://destiny.report/w/2490460292
    """
    items = [
        Item("Stryker's Sure-Hand", hash=2490460292),
        Item("Stryker's Sure-Hand", hash=2158575991),
        ]


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


class TheOtherHalf(RollDefinition):
    """
    Void Sword, Adaptive Frame, Anti-Barrier, Craftable
    Source: Eternity
    https://www.light.gg/db/items/3257091167
    https://destiny.report/w/3257091167
    """
    item = Item('The Other Half', hash=3257091167)
