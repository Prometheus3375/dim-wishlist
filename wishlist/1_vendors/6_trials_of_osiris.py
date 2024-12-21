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
