from wishlist import *


class AuricDisabler(RollDefinition):
    """
    Strand Auto Rifle, Precision Frame
    https://www.light.gg/db/items/702001725
    """
    item = Item('Auric Disabler', hash=702001725)
    roll = Roll(
        'PvE',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.FlaredMagwell, AnyPerk],
        [trait.Hatchling],
        [trait.Tear, trait.SwordLogic, trait.DesperateMeasures],
        )


class AureusNeutralizer(RollDefinition):
    """
    Kinetic Hand Cannon, Spread Shot
    https://www.light.gg/db/items/3981920134
    """
    item = Item('Aureus Neutralizer', hash=3981920134)
    rolls = [
        Roll(
            'Damage dealing',
            [barrel.BarrelShroud, AnyPerk],
            [magazine.AppendedMag, AnyPerk],
            [trait.VorpalWeapon],
            [trait.TrenchBarrel, trait.CascadePoint],
            ),
        Roll(
            'Melee damage increase',
            [barrel.BarrelShroud, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.GraveRobber, trait.ThreatDetector],
            [trait.OneTwoPunch],
            ),
        Roll(
            'PvP',
            [barrel.Smallbore, AnyPerk],
            [magazine.AccurizedRounds, AnyPerk],
            [trait.ThreatDetector],
            [trait.OpeningShot, trait.ClosingTime],
            ),
        ]


class EverburningGlitz(RollDefinition):
    """
    Kinetic Auto Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/2857870254
    """
    item = Item('Everburning Glitz', hash=2857870254)
    rolls = [
        Roll(
            'Attrition Orbs',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.AttritionOrbs],
            [trait.KineticTremors, trait.OneForAll],
            ),
        Roll(
            'Missile combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.BewilderingBurst],
            [trait.AncillaryOrdinance],
            ),
        ]


class AishasEmbrace(RollDefinition):
    """
    Void Scout Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/3709368142
    """
    item = Item("Aisha's Embrace", hash=3709368142)
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.RapidHit, trait.Demoralize],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Withering Gaze',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.RapidHit, trait.Demoralize],
            [trait.WitheringGaze],
            ),
        ]


class Forgiveness(RollDefinition):
    """
    Arc Sidearm, Heavy Burst
    https://www.light.gg/db/items/1552443158
    """
    item = Item('Forgiveness', hash=1552443158)


# Special


class BurdenOfGuilt(RollDefinition):
    """
    Stasis Fusion Rifle, Adaptive Frame
    https://www.light.gg/db/items/976459525
    """
    item = Item('Burden Of Guilt', hash=976459525)
    rolls = [
        Roll(
            'Stasis combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.AcceleratedCoils, AnyPerk],
            [trait.Rimestealer],
            [trait.CrystallineCorpsebloom],
            ),
        ]


# Heavy


class UnwaveringDuty(RollDefinition):
    """
    Solar Machine Gun, Adaptive Frame
    https://www.light.gg/db/items/3489054606
    """
    item = Item('Unwavering Duty', hash=3489054606)
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.AppendedMag, AnyPerk],
            [trait.Incandescent, trait.Rampage, trait.Incandescent],
            [trait.KillingTally],
            ),
        Roll(
            'Solar combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.AppendedMag, AnyPerk],
            [trait.Incandescent],
            [trait.BurningAmbition],
            ),
        ]
