from wishlist import *


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
            [bowstring.PolymerString, AnyPerk],
            [arrow.FiberglassArrowShaft, AnyPerk],
            [trait.Dragonfly, trait.ArchersTempo],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Void combo',
            [bowstring.PolymerString, AnyPerk],
            [arrow.FiberglassArrowShaft, AnyPerk],
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds, trait.Demoralize],
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
            [barrel.Smallbore, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.HealClip, trait.Demolitionist],
            [trait.Incandescent, trait.ChaosReshaped],
            ),
        Roll(
            'Super regen',
            [barrel.Smallbore, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.AttritionOrbs],
            [trait.ChaosReshaped, trait.TargetLock],
            ),
        ]


# Special


class FestivalFlight(RollDefinition):
    """
    Strand Breechloaded Grenade Launcher, Area Denial Frame
    https://www.light.gg/db/items/4019651319
    """
    items = [
        Item(name='Festival Flight', hash=4019651319),
        Item(name='Festival Flight', hash=3977654524),
        ]
    rolls = [
        Roll(
            'Ad clear',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.AmbitiousAssassin, trait.Demolitionist, trait.Slice],
            [trait.OneForAll, trait.Hatchling],
            ),
        Roll(
            'Damage rotations',
            [launcher_barrel.Countermass, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.EnviousArsenal],
            [trait.ElementalHoning],
            ),
        ]
