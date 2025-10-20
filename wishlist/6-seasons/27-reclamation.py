from wishlist import *


# Special


class RomanticDeath(RollDefinition):
    """
    Void Breechloaded Grenade Launcher, Wave Frame
    https://www.light.gg/db/items/4169082039
    """
    items = [
        Item('Romantic Death', hash=4169082039),
        Item('Romantic Death', hash=2979965244),
        Item('Romantic Death', hash=2979965245),
        Item('Romantic Death', hash=2979965246),
        Item('Romantic Death', hash=2979965247),
        ]
    rolls = [
        Roll(
            'Ad clear',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.ThreatDetector, trait.FeedingFrenzy],
            [trait.DestabilizingRounds, trait.OneForAll, trait.ChainReaction],
            ),
        Roll(
            'Void combo',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        ]


# Heavy


class FoldedRoot(RollDefinition):
    """
    Void Rocket Launcher, Aggressive Frame
    https://www.light.gg/db/items/2725894221
    """
    items = [
        Item('Folded Root', hash=2725894221),
        Item('Folded Root', hash=3184457500),
        Item('Folded Root', hash=3184457501),
        Item('Folded Root', hash=3184457502),
        Item('Folded Root', hash=3184457503),
        ]
    roll = Roll(
        'Damage dealing',
        [launcher_barrel.QuickLaunch, AnyPerk],
        [magazine.ImpactCasing, AnyPerk],
        [trait.ClusterBomb],
        [trait.LastingImpression, trait.Frenzy],
        )


class Submersion(RollDefinition):
    """
    Stasis Crossbow, High-Impact Frame
    https://www.light.gg/db/items/3524386983
    """
    items = [
        Item('Submersion', hash=3524386983),
        Item('Submersion', hash=1724104236),
        ]
    rolls = [
        Roll(
            'Ad clear',
            [rail.LowProfileRail, AnyPerk],
            [bolt.ExplosiveBolts, AnyPerk],
            [trait.AutoLoadingHolster, trait.ImpulseAmplifier, trait.BoltScavenger],
            [trait.Headstone],
            ),
        Roll(
            'Chill Clip',
            [rail.LowProfileRail, AnyPerk],
            [bolt.SerratedBolts, AnyPerk],
            [trait.AutoLoadingHolster, trait.ImpulseAmplifier, trait.BoltScavenger],
            [trait.ChillClip],
            ),
        Roll(
            'Damage dealing',
            [rail.LowProfileRail, AnyPerk],
            [bolt.HeavyBolts, AnyPerk],
            [trait.AutoLoadingHolster, trait.ImpulseAmplifier, trait.BoltScavenger],
            [trait.AggregateCharge, trait.HighGround, trait.FiringLine],
            ),
        ]
