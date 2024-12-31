from database import *


class PyroelectricPropellant(RD):
    """
    Arc Auto Rifle, Adaptive Frame
    https://www.light.gg/db/items/4232480042
    """
    item = Item(name='VS Pyroelectric Propellant', hash=4232480042)
    roll = Roll(
        'Ad clear',
        [traits.AttritionOrbs, traits.EddyCurrent],
        [traits.JoltingFeedback],
        )


class GraviticArrest(RD):
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
            [traits.Demolitionist, traits.RepulsorBrace],
            [traits.WitheringGaze],
            ),
        Roll(
            'Ad clear',
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.AcceleratedCoils, AnyPerk],
            [traits.Demolitionist, traits.RepulsorBrace],
            [traits.ChainReaction],
            )
        ]


class VelocityBaton(RD):
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
            [traits.Demolitionist, traits.Unrelenting, traits.RepulsorBrace],
            [traits.AttritionOrbs],
            ),
        Roll(
            'Ad clear',
            [barrels.QuickLaunch, AnyPerk],
            [magazines.HighVelocityRounds],
            [traits.Demolitionist, traits.Unrelenting, traits.RepulsorBrace],
            [traits.Adagio, traits.DestabilizingRounds],
            ),
        ]


class ChillInhibitor(RD):
    """
    Stasis Power Grenade Launcher, Rapid-Fire Frame
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
            [traits.EnviousArsenal, traits.CascadePoint],
            [traits.ExplosiveLight],
            ),
        Roll(
            'Ad clear',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.HighExplosiveOrdnance, AnyPerk],
            [traits.DangerZone, traits.Demolitionist],
            [traits.Surrounded, traits.ChainReaction],
            ),
        ]
