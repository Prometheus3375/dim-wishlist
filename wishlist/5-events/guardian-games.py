from wishlist import *


class Taraxippos(RollDefinition):
    """
    Strand Scout Rifle, Lightweight Frame
    https://www.light.gg/db/items/2595813005
    """
    item = Item('Taraxippos', hash=2595813005)


class Title(RollDefinition):
    """
    Void Submachine Gun, Aggressive Frame
    https://www.light.gg/db/items/55393445
    """
    item = Item('The Title', hash=55393445)
    rolls = [
        Roll(
            'Void combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Classic combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.ThreatDetector],
            [trait.Surrounded],
            ),
        ]


class TripleLaureate(RollDefinition):
    """
    Stasis Hand Cannon, Spread Shot
    https://www.light.gg/db/items/1605599021
    """
    items = [
        Item('Triple Laureate', hash=1605599021),
        Item('Triple Laureate', hash=2908653246),
        ]
    rolls = [
        Roll(
            'Super roll',
            [barrel.BarrelShroud, AnyPerk],
            [magazine.AppendedMag, AnyPerk],
            [trait.GraveRobber],
            [trait.AmbitiousAssassin],
            [trait.CrystallineCorpsebloom],
            [trait.TrenchBarrel],
            [trait.OneTwoPunch],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Melee damage increase',
            [barrel.BarrelShroud, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.GraveRobber],
            [trait.OneTwoPunch],
            ),
        Roll(
            'Ad clear',
            [barrel.BarrelShroud, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.CrystallineCorpsebloom],
            [trait.ChaosReshaped],
            ),
        ]


# Special


class Keraunios(RollDefinition):
    """
    Arc Trace Rifle, Adaptive Frame
    https://www.light.gg/db/items/2386208942
    """
    items = [
        Item('Keraunios', hash=2386208942),
        Item('Keraunios', hash=981450701),
        ]
    rolls = [
        Roll(
            'Super roll',
            [barrel.Smallbore, AnyPerk],
            [battery.TacticalBattery, AnyPerk],
            [trait.FourthTimesTheCharm],
            [trait.SuperchargedMagazine],
            [trait.ShootToLoot],
            [trait.TargetLock],
            [trait.JoltingFeedback],
            [trait.DetonatorBeam],
            ),
        Roll(
            'Ad clear',
            [barrel.Smallbore, AnyPerk],
            [battery.TacticalBattery, AnyPerk],
            [trait.SuperchargedMagazine],
            [trait.JoltingFeedback, trait.DetonatorBeam],
            ),
        Roll(
            'Shoot To Loot',
            [barrel.Smallbore, AnyPerk],
            [battery.TacticalBattery, AnyPerk],
            [trait.ShootToLoot],
            [trait.JoltingFeedback, trait.DetonatorBeam],
            ),
        Roll(
            'Continuous damage',
            [barrel.Smallbore, AnyPerk],
            [battery.TacticalBattery, AnyPerk],
            [trait.FourthTimesTheCharm],
            [trait.TargetLock],
            ),
        ]


class TheBeacon(RollDefinition):
    """
    Solar Fusion Rifle, Rapid-Fire Frame
    Source: Guardian Games
    https://www.light.gg/db/items/2161618499
    """
    items = [
        Item('The Beacon', hash=2161618499),
        Item('The Beacon', hash=76739872),
        ]
    rolls = [
        Roll(
            'Super roll',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.EnhancedBattery, AnyPerk],
            [trait.LeadFromGold],
            [trait.RewindRounds],
            [trait.Demolitionist],
            [trait.Deconstruct],
            [trait.ControlledBurst],
            [trait.BaitAndSwitch],
            ),
        Roll(
            'Damage dealing',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.EnhancedBattery, AnyPerk],
            [trait.RewindRounds],
            [trait.BaitAndSwitch, trait.ControlledBurst],
            ),
        Roll(
            'Deconstruct',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.EnhancedBattery, AnyPerk],
            [trait.RewindRounds],
            [trait.Deconstruct],
            ),
        ]


# Heavy


class Hullabaloo(RollDefinition):
    """
    Arc Drum Grenade Launcher, Compressed Wave Frame
    https://www.light.gg/db/items/2666273249
    """
    item = Item('Hullabaloo', hash=2666273249)
    rolls = [
        Roll(
            'Ad clear',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.Voltshot, trait.Demolitionist],
            [trait.ChainReaction, trait.OneForAll],
            ),
        Roll(
            'Damage dealing',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.EnviousAssassin],
            [trait.OneForAll],
            ),
        ]
