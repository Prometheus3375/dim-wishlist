from database import *


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


class AuricDisabler(RollDefinition):
    """
    Strand Auto Rifle, Precision Frame
    https://www.light.gg/db/items/702001725
    """
    item = Item(name='Auric Disabler', hash=702001725)
    roll = Roll(
        'PvE',
        [barrels.ArrowheadBrake, AnyPerk],
        [magazines.FlaredMagwell, AnyPerk],
        [traits.Hatchling],
        [traits.Tear, traits.SwordLogic, traits.DesperateMeasures],
        )


class AureusNeutralizer(RollDefinition):
    """
    Kinetic Hand Cannon, Spread Shot
    https://www.light.gg/db/items/3981920134
    """
    item = Item(name='Aureus Neutralizer', hash=3981920134)
    rolls = [
        Roll(
            'Damage dealing',
            [barrels.BarrelShroud, AnyPerk],
            [magazines.AppendedMag, AnyPerk],
            [traits.VorpalWeapon],
            [traits.TrenchBarrel, traits.CascadePoint],
            ),
        Roll(
            'Melee damage increase',
            [barrels.BarrelShroud, AnyPerk],
            [magazines.TacticalMag, AnyPerk],
            [traits.GraveRobber, traits.ThreatDetector],
            [traits.OneTwoPunch],
            ),
        Roll(
            'PvP',
            [barrels.Smallbore, AnyPerk],
            [magazines.AccurizedRounds, AnyPerk],
            [traits.BarrelConstrictor],
            [traits.ClosingTime, traits.OpeningShot],
            ),
        ]


class AishasEmbrace(RollDefinition):
    """
    Void Scout Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/3709368142
    """
    item = Item(name="Aisha's Embrace", hash=3709368142)
    rolls = [
        Roll(
            'Ad clear',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.TacticalMag, AnyPerk],
            [traits.RapidHit, traits.Demoralize],
            [traits.DestabilizingRounds],
            ),
        ]


class Forgiveness(RollDefinition):
    """
    Arc Sidearm, Heavy Burst
    https://www.light.gg/db/items/1552443158
    """
    item = Item(name='Forgiveness', hash=1552443158)


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


class UnwaveringDuty(RollDefinition):
    """
    Solar Machine Gun, Adaptive Frame
    https://www.light.gg/db/items/3489054606
    """
    item = Item(name='Unwavering Duty', hash=3489054606)
    rolls = [
        Roll(
            'Ad clear',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.AppendedMag, AnyPerk],
            [traits.Incandescent, traits.Rampage, traits.Incandescent],
            [traits.KillingTally],
            ),
        Roll(
            'Solar combo',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.AppendedMag, AnyPerk],
            [traits.Incandescent],
            [traits.BurningAmbition],
            ),
        ]
