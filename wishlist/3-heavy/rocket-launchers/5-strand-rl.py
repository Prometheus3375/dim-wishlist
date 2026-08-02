from wishlist import *
from . import *


class CrowningDuologue(RollDefinition):
    """
    Strand Rocket Launcher, Precision Frame, Anti-Barrier
    Source: Solstice
    https://www.light.gg/db/items/1151307006
    https://destiny.report/w/1151307006
    """
    items = [
        Item('Crowning Duologue', hash=1151307006),
        Item('Crowning Duologue', hash=4106757302),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.AutoLoadingHolster],
            [trait.Deconstruct],
            [trait.BaitAndSwitch],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.AutoLoadingHolster],
            [trait.BaitAndSwitch],
            ),
        Roll(
            'Anti-construct',
            default_barrels,
            default_mags,
            [trait.AutoLoadingHolster],
            [trait.Deconstruct],
            [origin.HakkeBreachArmaments],
            ),
        ]


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
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.ClownCartridge],
            [trait.Slideways],
            [trait.ReapersTithe],
            [trait.AggregateCharge],
            [trait.Surrounded],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.ClownCartridge],
            [trait.ReapersTithe, trait.AggregateCharge, trait.Surrounded],
            ),
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
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.EnviousArsenal],
            [trait.Overflow],
            [trait.Bipod],
            [trait.AggregateCharge],
            [trait.BaitAndSwitch],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.EnviousArsenal, trait.Overflow],
            [trait.AggregateCharge, trait.BaitAndSwitch],
            ),
        ]


class Haliaetus(RollDefinition):
    """
    Strand Rocket Launcher, High-Impact Frame, Anti-Unstoppable
    Source: Banshee-44; Tenet of Bravery
    https://www.light.gg/db/items/2155534128
    https://destiny.report/w/2155534128
    """
    item = Item('Haliaetus', hash=2155534128)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.AutoLoadingHolster],
            [trait.ClusterBomb],
            [trait.Bipod],
            [trait.ReapersTithe],
            [trait.AggregateCharge],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.ClusterBomb, trait.AutoLoadingHolster],
            [trait.ReapersTithe, trait.AggregateCharge],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.ClusterBomb],
            [trait.Bipod],
            ),
        ]


class Semiotician(RollDefinition):
    """
    Strand Rocket Launcher, High-Impact Frame, Anti-Unstoppable, Craftable
    Source: Xûr
    https://www.light.gg/db/items/2922749929
    https://destiny.report/w/2922749929
    """
    item = Item('Semiotician', hash=2922749929)
    roll = Roll(
        'Ad clear',
        [launcher_barrel.VolatileLaunch, AnyPerk],
        [magazine.HighVelocityRounds, AnyPerk],
        [trait.FieldPrep],
        [trait.Bipod],
        )
