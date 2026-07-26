from wishlist import *

default_barrels = [launcher_barrel.VolatileLaunch, AnyPerk]
default_mags = [magazine.HighVelocityRounds]


class Hullabaloo(RollDefinition):
    """
    Arc Drum Grenade Launcher, Compressed Wave Frame, Anti-Unstoppable
    Source: Guardian Games
    https://www.light.gg/db/items/2449096504
    https://destiny.report/w/2449096504
    """
    items = [
        Item('Hullabaloo', hash=2449096504),
        Item('Hullabaloo', hash=2666273249),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.FieldPrep],
            [trait.EnviousArsenal],
            [trait.ChainReaction],
            [trait.OneForAll],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.FieldPrep],
            [trait.ChainReaction, trait.OneForAll],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.EnviousArsenal],
            [trait.OneForAll],
            ),
        ]


class LoveAndDeath(RollDefinition):
    """
    Solar Drum Grenade Launcher, Compressed Wave Frame, Anti-Unstoppable
    Source: The Moon
    https://www.light.gg/db/items/3482299617
    https://destiny.report/w/3482299617
    """
    item = Item('Love and Death', hash=3482299617)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Incandescent],
            [trait.ImpromptuAmmunition],
            [trait.EnviousArsenal],
            [trait.ChainReaction],
            [trait.ExplosiveLight],
            [trait.AggregateCharge],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.Incandescent, trait.ImpromptuAmmunition],
            [trait.ChainReaction],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.EnviousArsenal],
            [trait.ExplosiveLight, trait.AggregateCharge],
            ),
        ]


class DimensionalHypotrochoid(RollDefinition):
    """
    Stasis Drum Grenade Launcher, Compressed Wave Frame, Anti-Unstoppable, Craftable
    Source: Neomuna
    https://www.light.gg/db/items/1311684613
    https://destiny.report/w/1311684613
    """
    item = Item('Dimensional Hypotrochoid', hash=1311684613)
    is_chosen = True
    roll = Roll(
        'Ad clear',
        default_barrels,
        default_mags,
        [trait.Rimestealer],
        [trait.CrystallineCorpsebloom],
        )
