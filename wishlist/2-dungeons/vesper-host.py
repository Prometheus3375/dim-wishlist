from wishlist import *


class PyroelectricPropellant(RollDefinition):
    """
    Arc Auto Rifle, Adaptive Frame
    https://www.light.gg/db/items/4232480042
    """
    item = Item(name='VS Pyroelectric Propellant', hash=4232480042)
    roll = Roll(
        'Ad clear',
        [trait.AttritionOrbs, trait.EddyCurrent, trait.Strategist],
        [trait.JoltingFeedback],
        )


class GraviticArrest(RollDefinition):
    """
    Void Fusion Rifle, Adaptive Frame
    https://www.light.gg/db/items/93061497
    """
    item = Item(name='VS Gravitic Arrest', hash=93061497)
    rolls = [
        Roll(
            'Withering Gaze',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.AcceleratedCoils, AnyPerk],
            [trait.Demolitionist],
            [trait.WitheringGaze],
            ),
        ]


class VelocityBaton(RollDefinition):
    """
    Void Breechloaded Grenade Launcher, Area Denial Frame
    https://www.light.gg/db/items/1762785663
    """
    item = Item(name='VS Velocity Baton', hash=1762785663)
    rolls = [
        Roll(
            'Attrition Orbs',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.Unrelenting, trait.Demolitionist],
            [trait.AttritionOrbs],
            ),
        Roll(
            'Ad clear',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.Unrelenting, trait.Demolitionist],
            [trait.DestabilizingRounds, trait.Adagio],
            ),
        Roll(
            'Void Combo',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        ]


class ChillInhibitor(RollDefinition):
    """
    Stasis Drum Grenade Launcher, Rapid-Fire Frame
    https://www.light.gg/db/items/1762785662
    """
    item = Item(name='VS Chill Inhibitor', hash=1762785662)
    rolls = [
        Roll(
            'Damage dealing',
            [launcher_barrel.HardLaunch, AnyPerk],
            [magazine.SpikeGrenades, AnyPerk],
            [trait.EnviousArsenal, trait.CascadePoint],
            [trait.BaitAndSwitch, trait.Surrounded],
            ),
        Roll(
            'High DPS',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.SpikeGrenades, AnyPerk],
            [trait.CascadePoint],
            [trait.ExplosiveLight],
            ),
        Roll(
            'Ad clear',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighExplosiveOrdnance, AnyPerk],
            [trait.DangerZone],
            [trait.ChainReaction, trait.Surrounded],
            ),
        ]
