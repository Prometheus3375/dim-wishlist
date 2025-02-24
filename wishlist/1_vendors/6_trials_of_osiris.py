from database import *


class YesterdaysQuestion(RD):
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


class ExaltedTruth(RD):
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


class KeenThistle(RD):
    """
    Solar Sniper Rifle, Aggressive Frame
    https://www.light.gg/db/items/1893967086
    """
    items = [
        Item(name='Keen Thistle', hash=1893967086),
        Item(name='Keen Thistle (Adept)', hash=3503560035),
        ]


class TomorrowsAnswer(RD):
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
