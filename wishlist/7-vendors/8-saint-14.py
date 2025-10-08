from wishlist import *


class YesterdaysQuestion(RollDefinition):
    """
    Arc Hand Cannon, Heavy Burst
    https://www.light.gg/db/items/2300143112
    """
    items = [
        Item(name="Yesterday's Question", hash=2300143112),
        Item(name="Yesterday's Question (Adept)", hash=2378785953),
        ]
    roll = Roll(
        'Damage dealing with Lucky Pants',
        [traits.FourthTimesTheCharm, traits.RapidHit],
        [traits.VorpalWeapon],
        )


class ExaltedTruth(RollDefinition):
    """
    Void Hand Cannon, Adaptive Frame
    https://www.light.gg/db/items/3436626079
    """
    items = [
        Item(name='Exalted Truth', hash=3436626079),
        Item(name='Exalted Truth (Adept)', hash=1201528146),
        ]
    rolls = [
        Roll(
            'PvE',
            [barrels.Smallbore, AnyPerk],
            [magazines.FlaredMagwell, magazines.TacticalMag, AnyPerk],
            [traits.DestabilizingRounds, traits.WitheringGaze],
            [traits.RepulsorBrace, traits.Demoralize],
            )
        ]


# Special


class KeenThistle(RollDefinition):
    """
    Solar Sniper Rifle, Aggressive Frame
    https://www.light.gg/db/items/1893967086
    """
    items = [
        Item(name='Keen Thistle', hash=1893967086),
        Item(name='Keen Thistle (Adept)', hash=3503560035),
        ]


class Inquisitor(RollDefinition):
    """
    Arc Shotgun, Pinpoint Slug Frame
    https://www.light.gg/db/items/51129316
    """
    items = [
        Item(name='The Inquisitor', hash=51129316),
        Item(name='The Inquisitor (Adept)', hash=2330860573),
        ]


# Heavy


class TomorrowsAnswer(RollDefinition):
    """
    Void Rocket Launcher, High-Impact Frame
    https://www.light.gg/db/items/3009199534
    """
    items = [
        Item(name="Tomorrow's Answer", hash=3009199534),
        Item(name="Tomorrow's Answer (Adept)", hash=303107619),
        ]
    rolls = [
        Roll(
            """
            Damage dealing.
            High-Impact Frame is bad for this,
            but there is no other good Void RL
            """,
            [barrels.QuickLaunch, AnyPerk],
            [magazines.ImpactCasing, AnyPerk],
            [traits.EnviousArsenal, traits.WitheringGaze],
            [traits.BaitAndSwitch, traits.ExplosiveLight],
            ),
        Roll(
            'Ad clear',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.AlloyCasing, AnyPerk],
            [traits.DangerZone, traits.AirTrigger],
            [traits.Bipod, traits.ChainReaction],
            ),
        ]
