from database import *


class PyroelectricPropellant(RD):
    item = Item(name='VS Pyroelectric Propellant', hash=4232480042)
    roll = roll(
        'Roll for ad clear',
        [traits.AttritionOrbs, traits.EddyCurrent],
        [traits.JoltingFeedback],
        )


class GraviticArrest(RD):
    item = Item(name='VS Gravitic Arrest', hash=93061497)
    rolls = [
        roll(
            'Weaken support roll',
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.AcceleratedCoils, AnyPerk],
            [traits.Demolitionist, traits.RepulsorBrace],
            [traits.WitheringGaze],
            ),
        roll(
            'Roll for ad clear',
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.AcceleratedCoils, AnyPerk],
            [traits.Demolitionist, traits.RepulsorBrace],
            [traits.ChainReaction],
            )
        ]


class VelocityBaton(RD):
    item = Item(name='VS Velocity Baton', hash=1762785663)
    rolls = [
        roll(
            'Attrition Orbs roll',
            [barrels.QuickLaunch, AnyPerk],
            [magazines.HighVelocityRounds],
            [traits.Demolitionist, traits.RepulsorBrace],
            [traits.AttritionOrbs],
            ),
        roll(
            'Roll for ad clear',
            [barrels.QuickLaunch, AnyPerk],
            [magazines.HighVelocityRounds],
            [traits.Demolitionist, traits.RepulsorBrace],
            [traits.Adagio, traits.DestabilizingRounds],
            ),
        ]


class ChillInhibitor(RD):
    item = Item(name='VS Chill Inhibitor', hash=1762785662)
    rolls = [
        roll(
            'Roll for damage dealing',
            [barrels.HardLaunch, AnyPerk],
            [magazines.SpikeGrenades, AnyPerk],
            [traits.EnviousArsenal, traits.CascadePoint],
            [traits.BaitAndSwitch, traits.Surrounded, traits.ExplosiveLight],
            ),
        roll(
            'Roll for ad clear',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.HighExplosiveOrdnance, AnyPerk],
            [traits.DangerZone, traits.Demolitionist],
            [traits.Surrounded, traits.ChainReaction],
            ),
        ]
