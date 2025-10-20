from wishlist import *


class Intercalary(RollDefinition):
    """
    Stasis Auto Rifle, Adaptive Frame
    https://www.light.gg/db/items/2725426834
    """
    item = Item('Intercalary', hash=2725426834)
    rolls = [
        Roll(
            'Stasis Combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Headstone],
            [trait.Rimestealer],
            ),
        Roll(
            'One for All',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Headstone, trait.Demolitionist],
            [trait.OneForAll],
            ),
        ]


class Antedate(RollDefinition):
    """
    Arc Submachine Gun, Adaptive Frame
    https://www.light.gg/db/items/1435808083
    """
    item = Item('Antedate', hash=1435808083)
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Dragonfly],
            [trait.JoltingFeedback],
            ),
        Roll(
            'Super regen',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.RewindRounds],
            [trait.TargetLock],
            ),
        ]


class CuspSempiternal(RollDefinition):
    """
    Void Auto Rifle, Support Frame
    https://www.light.gg/db/items/2579693381
    """
    item = Item('Cusp Sempiternal', hash=2579693381)
    rolls = [
        Roll(
            'Self-healing',
            [barrel.FullBore, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Reciprocity],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Ad clear',
            [barrel.FullBore, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Reconstruction, trait.AttritionOrbs],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Void combo',
            [barrel.FullBore, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        ]


# Special


class LanceEphemeral(RollDefinition):
    """
    Strand Sniper Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/688593230
    """
    item = Item('Lance Ephemeral', hash=688593230)
    rolls = [
        Roll(
            'Damage dealing',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.RewindRounds, trait.FourthTimesTheCharm],
            [trait.BaitAndSwitch, trait.Redirection, trait.ElementalHoning],
            ),
        ]


class FiniteMaybe(RollDefinition):
    """
    Solar Fusion Rifle, Aggressive Frame
    https://www.light.gg/db/items/3241217409
    """
    item = Item('Finite Maybe', hash=3241217409)
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.AcceleratedCoils, AnyPerk],
            [trait.Incandescent],
            [trait.Discord],
            ),
        Roll(
            'Damage dealing',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.AcceleratedCoils, AnyPerk],
            [trait.Reconstruction],
            [trait.BaitAndSwitch, trait.ControlledBurst],
            ),
        ]


class StarscapeNull(RollDefinition):
    """
    Solar Shotgun, Lightweight Frame
    https://www.light.gg/db/items/3868973291
    """
    item = Item('Starscape Null', hash=3868973291)


# Heavy


class TheWhenAndWhere(RollDefinition):
    """
    Stasis Rocket Launcher, Adaptive Frame
    https://www.light.gg/db/items/1090936013
    """
    item = Item('The When And Where', hash=1090936013)
    rolls = [
        Roll(
            'Damage dealing',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.ImpactCasing, AnyPerk],
            [trait.Reconstruction, trait.Overflow, trait.ClownCartridge],
            [trait.BaitAndSwitch, trait.ElementalHoning, trait.ReapersTithe],
            ),
        ]


class OpaqueHourglass(RollDefinition):
    """
    Arc Crossbow, High-Impact Frame
    https://www.light.gg/db/items/1553681400
    """
    item = Item('Opaque Hourglass', hash=1553681400)
    rolls = [
        Roll(
            'Damage dealing',
            [rail.LowProfileRail, AnyPerk],
            [bolt.HeavyBolts, AnyPerk],
            [trait.ImpulseAmplifier, trait.BoltScavenger],
            [trait.ElementalHoning, trait.Frenzy],
            ),
        Roll(
            'Ad clear',
            [rail.LowProfileRail, AnyPerk],
            [bolt.ExplosiveBolts, AnyPerk],
            [trait.Firefly],
            [trait.Dragonfly],
            ),
        ]


class TheEverPresent(RollDefinition):
    """
    Strand Drum Grenade Launcher, Rapid-Fire Frame
    https://www.light.gg/db/items/3177074192
    """
    item = Item('The Ever-Present', hash=3177074192)
    rolls = [
        Roll(
            'Damage dealing',
            [launcher_barrel.HardLaunch, AnyPerk],
            [magazine.SpikeGrenades, AnyPerk],
            [trait.EnviousArsenal],
            [trait.AggregateCharge, trait.BaitAndSwitch, trait.ElementalHoning],
            ),
        Roll(
            'High DPS',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.SpikeGrenades, AnyPerk],
            [trait.AutoLoadingHolster],
            [trait.ExplosiveLight],
            ),
        Roll(
            'Ad clear',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.AlloyCasing, AnyPerk],
            [trait.Hatchling],
            [trait.ChainReaction],
            ),
        ]
