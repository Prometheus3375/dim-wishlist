from database import *


class YesterdaysQuestion(RD):
    items = [
        Item(name="Yesterday's Question", hash=2300143112),
        Item(name="Yesterday's Question (Adept)", hash=2378785953),
        ]
    roll = roll(
        'Roll for Lucky Pants',
        [traits.FourthTimesTheCharm, traits.RapidHit],
        [traits.VorpalWeapon],
        )


class TomorrowsAnswer(RD):
    items = [
        Item(name="Tomorrow's Answer", hash=3009199534),
        Item(name="Tomorrow's Answer (Adept)", hash=303107619),
        ]
    rolls = [
        roll(
            'Roll for damage dealing; High-Impact Frame is bad for burst damage,'
            ' but there is no other good Void RL',
            [barrels.QuickLaunch, AnyPerk],
            [magazines.ImpactCasing, AnyPerk],
            [traits.EnviousArsenal, traits.WitheringGaze],
            [traits.BaitAndSwitch, traits.ExplosiveLight],
            ),
        roll(
            'Roll for ad clear',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.AlloyCasing, AnyPerk],
            [traits.DangerZone, traits.AirTrigger],
            [traits.Bipod, traits.ChainReaction],
            ),
        ]
