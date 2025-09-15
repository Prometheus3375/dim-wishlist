from database import *


# Special


class RomanticDeath(RollDefinition):
    """
    Void Breechloaded Grenade Launcher, Wave Frame
    https://www.light.gg/db/items/4169082039
    """
    items = [
        Item(name='Romantic Death', hash=4169082039),
        Item(name='Romantic Death', hash=2979965244),
        Item(name='Romantic Death', hash=2979965245),
        Item(name='Romantic Death', hash=2979965246),
        Item(name='Romantic Death', hash=2979965247),
        ]
    rolls = [
        Roll(
            'Ad clear',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.HighVelocityRounds],
            [traits.ThreatDetector, traits.FeedingFrenzy],
            [traits.DestabilizingRounds, traits.OneForAll, traits.ChainReaction],
            ),
        Roll(
            'Void combo',
            [barrels.VolatileLaunch, AnyPerk],
            [magazines.HighVelocityRounds],
            [traits.RepulsorBrace],
            [traits.DestabilizingRounds],
            ),
        ]


# Heavy


class FoldedRoot(RollDefinition):
    """
    Void Rocket Launcher, Aggressive Frame
    https://www.light.gg/db/items/2725894221
    """
    items = [
        Item(name='Folded Root', hash=2725894221),
        Item(name='Folded Root', hash=3184457500),
        Item(name='Folded Root', hash=3184457501),
        Item(name='Folded Root', hash=3184457502),
        Item(name='Folded Root', hash=3184457503),
        ]
    roll = Roll(
        'Damage dealing',
        [barrels.QuickLaunch, AnyPerk],
        [magazines.ImpactCasing, AnyPerk],
        [traits.ClusterBomb],
        [traits.LastingImpression, traits.Frenzy],
        )


class Submersion(RollDefinition):
    """
    Stasis Crossbow, High-Impact Frame
    https://www.light.gg/db/items/3524386983
    """
    items = [
        Item(name='Submersion', hash=3524386983),
        Item(name='Submersion', hash=1724104236),
        ]
    rolls = [
        Roll(
            'Ad clear',
            [rails.LowProfileRail, AnyPerk],
            [bolts.ExplosiveBolts, AnyPerk],
            [traits.AutoLoadingHolster, traits.ImpulseAmplifier, traits.BoltScavenger],
            [traits.Headstone],
            ),
        Roll(
            'Chill Clip',
            [rails.LowProfileRail, AnyPerk],
            [bolts.SerratedBolts, AnyPerk],
            [traits.AutoLoadingHolster, traits.ImpulseAmplifier, traits.BoltScavenger],
            [traits.ChillClip],
            ),
        Roll(
            'Damage dealing',
            [rails.LowProfileRail, AnyPerk],
            [bolts.HeavyBolts, AnyPerk],
            [traits.AutoLoadingHolster, traits.ImpulseAmplifier, traits.BoltScavenger],
            [traits.AggregateCharge, traits.HighGround, traits.FiringLine],
            ),
        ]
