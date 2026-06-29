from wishlist import *


class SarpedonD(RollDefinition):
    """
    Arc Hand Cannon, Spread Shot, Anti-Overload
    Source: Commander Zavala
    https://www.light.gg/db/items/1242785638
    https://destiny.report/w/1242785638
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
            [trait.ProximityPower, trait.ImpromptuAmmunition, trait.EddyCurrent],
            [trait.OneTwoPunch],
            ),
        Roll(
            'Damage dealing',
            [barrel.BarrelShroud, AnyPerk],
            [magazine.AlloyMagazine, AnyPerk],
            [trait.TrickleCharge],
            [trait.TrenchBarrel],
            ),
        # Roll(
        #     'Ad clear',
        #     [barrel.BarrelShroud, AnyPerk],
        #     [magazine.TacticalMag, AnyPerk],
        #     [trait.ImpromptuAmmunition, trait.EddyCurrent],
        #     [trait.Voltshot],
        #     ),
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


class SolemnLie(RollDefinition):
    """
    Arc Hand Cannon, Lightweight Frame, Anti-Overload
    Source: Competitive Crucible
    https://www.light.gg/db/items/1041028435
    https://destiny.report/w/1041028435
    """
    item = Item('Solemn Lie', hash=1041028435)


class ThePalindrome(RollDefinition):
    """
    Arc Hand Cannon, Adaptive Frame, Anti-Barrier
    Source: Pinnacle Ops
    https://www.light.gg/db/items/739029152
    https://destiny.report/w/739029152
    """
    items = [
        Item('The Palindrome', hash=739029152),
        Item('The Palindrome', hash=3303271523),
        ]


class TrueProphecy(RollDefinition):
    """
    Arc Hand Cannon, Aggressive Frame, Anti-Unstoppable
    Source: Nessus, Unstable Centaur
    https://www.light.gg/db/items/960948343
    https://destiny.report/w/960948343
    """
    item = Item('True Prophecy', hash=960948343)


class WakingVigil(RollDefinition):
    """
    Arc Hand Cannon, Lightweight Frame, Anti-Overload
    Source: The Dreaming City
    https://www.light.gg/db/items/1727550459
    https://destiny.report/w/1727550459
    """
    item = Item('Waking Vigil', hash=1727550459)


class YesterdaysQuestion(RollDefinition):
    """
    Arc Hand Cannon, Heavy Burst, Anti-Unstoppable
    Source: Saint-14
    https://www.light.gg/db/items/1803480512
    https://destiny.report/w/1803480512
    """
    item = Item("Yesterday's Question", hash=1803480512)
