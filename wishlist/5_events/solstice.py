from database import *


class FortunateStar(RollDefinition):
    """
    Combat Bow, Lightweight Frame
    https://www.light.gg/db/items/2631466936
    """
    items = [
        Item(name='Fortunate Star', hash=2631466936),
        Item(name='Fortunate Star', hash=591672323),
        ]
    rolls = [
        Roll(
            'Ad clear',
            [strings.PolymerString, AnyPerk],
            [arrows.FiberglassArrowShaft, AnyPerk],
            [traits.Dragonfly, traits.ArchersTempo],
            [traits.DestabilizingRounds],
            ),
        Roll(
            'Void combo',
            [strings.PolymerString, AnyPerk],
            [arrows.FiberglassArrowShaft, AnyPerk],
            [traits.RepulsorBrace],
            [traits.DestabilizingRounds, traits.Demoralize],
            ),
        ]


class YeartideApex(RollDefinition):
    """
    Solar Submachine Gun, Lightweight Frame
    https://www.light.gg/db/items/3293207827
    """
    items = [
        Item(name='Yeartide Apex', hash=3293207827),
        Item(name='Yeartide Apex', hash=2965080304),
        ]
    rolls = [
        Roll(
            'Ad clear',
            [barrels.Smallbore, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.HealClip, traits.Demolitionist],
            [traits.Incandescent, traits.ChaosReshaped],
            ),
        Roll(
            'Super regen',
            [barrels.Smallbore, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.AttritionOrbs],
            [traits.ChaosReshaped, traits.TargetLock],
            ),
        ]


# Special


class FestivalFlight(RollDefinition):
    """
    Breechloaded Grenade Launcher, Area Denial Frame
    https://www.light.gg/db/items/4019651319
    """
    items = [
        Item(name='Festival Flight', hash=4019651319),
        Item(name='Festival Flight', hash=3977654524),
        ]
    rolls = [
        Roll(
            'Ad clear',
            [barrels.QuickLaunch, AnyPerk],
            [magazines.HighVelocityRounds],
            [traits.AmbitiousAssassin, traits.Demolitionist, traits.Slice],
            [traits.OneForAll, traits.Hatchling],
            ),
        Roll(
            'Damage rotations',
            [barrels.Countermass, AnyPerk],
            [magazines.HighVelocityRounds],
            [traits.EnviousArsenal],
            [traits.ElementalHoning],
            ),
        ]
