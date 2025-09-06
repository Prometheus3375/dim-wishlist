from database import *


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
            [traits.LoneWolf],
            [traits.OpeningShot, traits.ClosingTime],
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


# Heavy


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
