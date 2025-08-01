from database import *


class PyroelectricPropellant(RollDefinition):
    """
    Arc Auto Rifle, Adaptive Frame
    https://www.light.gg/db/items/4232480042
    """
    item = Item(name='VS Pyroelectric Propellant', hash=4232480042)
    roll = Roll(
        'Ad clear',
        [traits.AttritionOrbs, traits.EddyCurrent, traits.Strategist],
        [traits.JoltingFeedback],
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
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.AcceleratedCoils, AnyPerk],
            [traits.Demolitionist],
            [traits.WitheringGaze],
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
            [barrels.QuickLaunch, AnyPerk],
            [magazines.HighVelocityRounds],
            [traits.Unrelenting, traits.Demolitionist],
            [traits.AttritionOrbs],
            ),
        Roll(
            'Ad clear',
            [barrels.QuickLaunch, AnyPerk],
            [magazines.HighVelocityRounds],
            [traits.Unrelenting, traits.Demolitionist],
            [traits.DestabilizingRounds, traits.Adagio],
            ),
        Roll(
            'Void Combo',
            [barrels.QuickLaunch, AnyPerk],
            [magazines.HighVelocityRounds],
            [traits.RepulsorBrace],
            [traits.DestabilizingRounds],
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
            [barrels.HardLaunch, AnyPerk],
            [magazines.SpikeGrenades, AnyPerk],
            [traits.EnviousArsenal, traits.CascadePoint],
            [traits.BaitAndSwitch, traits.Surrounded],
            ),
        Roll(
            'High DPS',
            [barrels.QuickLaunch, AnyPerk],
            [magazines.SpikeGrenades, AnyPerk],
            [traits.CascadePoint],
            [traits.ExplosiveLight],
            ),
        Roll(
            'Ad clear',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.HighExplosiveOrdnance, AnyPerk],
            [traits.DangerZone],
            [traits.ChainReaction, traits.Surrounded],
            ),
        ]
