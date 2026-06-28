from wishlist import *


class CrowningDuologue(RollDefinition):
    """
    Strand Rocket Launcher, Precision Frame, Anti-Barrier
    Source:
    https://www.light.gg/db/items/1151307006
    https://destiny.report/w/1151307006
    """
    item = Item('Crowning Duologue', hash=1151307006)


class CruxCeleritasIV(RollDefinition):
    """
    Strand Rocket Launcher, Aggressive Frame, Anti-Unstoppable
    Source: Sparrow Racing League
    https://www.light.gg/db/items/391069235
    https://destiny.report/w/391069235
    """
    items = [
        Item('Crux Celeritas IV', hash=391069235),
        Item('Crux Celeritas IV', hash=2846261712),
        ]


class Cynosure(RollDefinition):
    """
    Strand Rocket Launcher, Adaptive Frame, Anti-Barrier
    Source: Fireteam Ops
    https://www.light.gg/db/items/2827141087
    https://destiny.report/w/2827141087
    """
    items = [
        Item('Cynosure', hash=2827141087),
        Item('Cynosure', hash=2511482352),
        ]


class Haliaetus(RollDefinition):
    """
    Strand Rocket Launcher, High-Impact Frame, Anti-Unstoppable
    Source: Banshee-44
    https://www.light.gg/db/items/2155534128
    https://destiny.report/w/2155534128
    """
    item = Item('Haliaetus', hash=2155534128)
    rolls = [
        Roll(
            'Damage dealing',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.ImpactCasing, AnyPerk],
            [trait.ClusterBomb, trait.AutoLoadingHolster],
            [trait.AggregateCharge, trait.ReapersTithe, trait.ElementalHoning],
            ),
        Roll(
            'Ad clear',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.AlloyCasing, AnyPerk],
            [trait.ClusterBomb, trait.ImpulseAmplifier],
            [trait.Bipod],
            ),
        ]
