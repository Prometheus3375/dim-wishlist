from database import *


class Intercalary(RollDefinition):
    """
    Stasis Auto Rifle, Adaptive Frame
    https://www.light.gg/db/items/2725426834
    """
    item = Item(name='Intercalary', hash=2725426834)
    rolls = [
        Roll(
            'Stasis Combo',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.Headstone],
            [traits.Rimestealer],
            ),
        Roll(
            'One for All',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.Headstone, traits.Demolitionist],
            [traits.OneForAll],
            ),
        ]


class Antedate(RollDefinition):
    """
    Arc Submachine Gun, Adaptive Frame
    https://www.light.gg/db/items/1435808083
    """
    item = Item(name='Antedate', hash=1435808083)
    rolls = [
        Roll(
            'Ad clear',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.Dragonfly],
            [traits.JoltingFeedback],
            ),
        Roll(
            'Super regen',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.RewindRounds],
            [traits.TargetLock],
            ),
        ]


class CuspSempiternal(RollDefinition):
    """
    Void Auto Rifle, Support Frame
    https://www.light.gg/db/items/2579693381
    """
    item = Item(name='Cusp Sempiternal', hash=2579693381)
    rolls = [
        Roll(
            'Self-healing',
            [barrels.FullBore, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.Reciprocity],
            [traits.DestabilizingRounds],
            ),
        Roll(
            'Ad clear',
            [barrels.FullBore, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.Reconstruction, traits.AttritionOrbs],
            [traits.DestabilizingRounds],
            ),
        Roll(
            'Void combo',
            [barrels.FullBore, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.RepulsorBrace],
            [traits.DestabilizingRounds],
            ),
        ]


# Special


class LanceEphemeral(RollDefinition):
    """
    Strand Sniper Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/688593230
    """
    item = Item(name='Lance Ephemeral', hash=688593230)
    rolls = [
        Roll(
            'Damage dealing',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.TacticalMag, AnyPerk],
            [traits.RewindRounds, traits.FourthTimesTheCharm],
            [traits.BaitAndSwitch, traits.Redirection, traits.ElementalHoning],
            ),
        ]


class FiniteMaybe(RollDefinition):
    """
    Solar Fusion Rifle, Aggressive Frame
    https://www.light.gg/db/items/3241217409
    """
    item = Item(name='Finite Maybe', hash=3241217409)
    rolls = [
        Roll(
            'Ad clear',
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.AcceleratedCoils, AnyPerk],
            [traits.Incandescent],
            [traits.Discord],
            ),
        Roll(
            'Damage dealing',
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.AcceleratedCoils, AnyPerk],
            [traits.Reconstruction],
            [traits.BaitAndSwitch, traits.ControlledBurst],
            ),
        ]


class StarscapeNull(RollDefinition):
    """
    Solar Shotgun, Lightweight Frame
    https://www.light.gg/db/items/3868973291
    """
    item = Item(name='Starscape Null', hash=3868973291)


# Heavy


class TheWhenAndWhere(RollDefinition):
    """
    Stasis Rocket Launcher, Adaptive Frame
    https://www.light.gg/db/items/1090936013
    """
    item = Item(name='The When And Where', hash=1090936013)
    rolls = [
        Roll(
            'Damage dealing',
            [barrels.QuickLaunch, AnyPerk],
            [magazines.ImpactCasing, AnyPerk],
            [traits.Reconstruction, traits.Overflow, traits.ClownCartridge],
            [traits.BaitAndSwitch, traits.ElementalHoning, traits.ReapersTithe],
            ),
        ]


class OpaqueHourglass(RollDefinition):
    """
    Arc Crossbow, High-Impact Frame
    https://www.light.gg/db/items/1553681400
    """
    item = Item(name='Opaque Hourglass', hash=1553681400)
    rolls = [
        Roll(
            'Damage dealing',
            [rails.LowProfileRail, AnyPerk],
            [bolts.HeavyBolts, AnyPerk],
            [traits.ImpulseAmplifier, traits.BoltScavenger],
            [traits.ElementalHoning, traits.Frenzy],
            ),
        Roll(
            'Ad clear',
            [rails.LowProfileRail, AnyPerk],
            [bolts.ExplosiveBolts, AnyPerk],
            [traits.Firefly],
            [traits.Dragonfly],
            ),
        ]


class TheEverPresent(RollDefinition):
    """
    Strand Drum Grenade Launcher, Rapid-Fire Frame
    https://www.light.gg/db/items/3177074192
    """
    item = Item(name='The Ever-Present', hash=3177074192)
    rolls = [
        Roll(
            'Damage dealing',
            [barrels.HardLaunch, AnyPerk],
            [magazines.SpikeGrenades, AnyPerk],
            [traits.EnviousArsenal],
            [traits.AggregateCharge, traits.BaitAndSwitch, traits.ElementalHoning],
            ),
        Roll(
            'High DPS',
            [barrels.QuickLaunch, AnyPerk],
            [magazines.SpikeGrenades, AnyPerk],
            [traits.AutoLoadingHolster],
            [traits.ExplosiveLight],
            ),
        Roll(
            'Ad clear',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.AlloyCasing, AnyPerk],
            [traits.Hatchling],
            [traits.ChainReaction],
            ),
        ]
