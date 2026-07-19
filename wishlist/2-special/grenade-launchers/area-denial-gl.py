from wishlist import *

default_barrels = [launcher_barrel.QuickLaunch, AnyPerk]
default_magazine = [magazine.HighVelocityRounds]


class Psychopomp(RollDefinition):
    """
    Arc Breechloaded Grenade Launcher, Area Denial Frame, Anti-Overload
    Source: Dungeon "Pit of Heresy"
    https://www.light.gg/db/items/1835232052
    https://destiny.report/w/1835232052
    """
    item = Item('Psychopomp', hash=1835232052)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_magazine,
            [trait.ImpromptuAmmunition],
            [trait.BlastDistributor],
            [trait.AutoLoadingHolster],
            [trait.Voltshot],
            [trait.AttritionOrbs],
            [trait.AggregateCharge],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_magazine,
            [trait.ImpromptuAmmunition],
            [trait.Voltshot, trait.AttritionOrbs],
            ),
        Roll(
            'Damage rotations',
            default_barrels,
            default_magazine,
            [trait.AutoLoadingHolster],
            [trait.AggregateCharge],
            ),
        ]


class Motif41(RollDefinition):
    """
    Solar Breechloaded Grenade Launcher, Area Denial Frame, Anti-Overload
    Source: Banshee-44; Tenet of Bravery
    https://www.light.gg/db/items/1685533876
    https://destiny.report/w/1685533876
    """
    item = Item('Motif-41', hash=1685533876)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_magazine,
            [trait.HealClip],
            [trait.AutoLoadingHolster],
            [trait.Incandescent],
            [trait.AttritionOrbs],
            ),
        Roll(
            'Solar combo',
            default_barrels,
            default_magazine,
            [trait.HealClip],
            [trait.Incandescent],
            ),
        ]


class VSVelocityBaton(RollDefinition):
    """
    Void Breechloaded Grenade Launcher, Area Denial Frame, Anti-Overload
    Source: Dungeon "Vesper's Host"
    https://www.light.gg/db/items/2452936816
    https://destiny.report/w/2452936816
    """
    item = Item('VS Velocity Baton', hash=2452936816)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_magazine,
            [trait.RepulsorBrace],
            [trait.Unrelenting],
            [trait.Demolitionist],
            [trait.DestabilizingRounds],
            [trait.ChainReaction],
            [trait.AttritionOrbs],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_magazine,
            [trait.Unrelenting],
            [trait.ChainReaction, trait.DestabilizingRounds],
            ),
        Roll(
            'Void combo',
            default_barrels,
            default_magazine,
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        ]


class LostSignal(RollDefinition):
    """
    Stasis Breechloaded Grenade Launcher, Area Denial Frame, Anti-Overload, Craftable
    Source: Exotic mission "Encore"
    https://www.light.gg/db/items/1197771438
    https://destiny.report/w/1197771438
    """
    item = Item('Lost Signal', hash=1197771438)
    roll = Roll(
        'Void combo',
        default_barrels,
        default_magazine,
        [trait.AutoLoadingHolster],
        [trait.OneForAll],
        )


class OusterEngine(RollDefinition):
    """
    Stasis Breechloaded Grenade Launcher, Area Denial Frame, Anti-Overload
    Source: Pinnacle Ops
    https://www.light.gg/db/items/2223968549
    https://destiny.report/w/2223968549
    """
    items = [
        Item('Ouster Engine', hash=2223968549),
        Item('Ouster Engine', hash=3718184802),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_magazine,
            [trait.AutoLoadingHolster],
            [trait.Rimestealer],
            [trait.BlastDistributor],
            [trait.ChaosReshaped],
            [trait.CrystallineCorpsebloom],
            [trait.ChainReaction],
            ),
        Roll(
            'Maintaining Grenade bonus',
            default_barrels,
            default_magazine,
            [trait.BlastDistributor],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Stasis combo',
            default_barrels,
            default_magazine,
            [trait.Rimestealer],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Damage rotations',
            default_barrels,
            default_magazine,
            [trait.AutoLoadingHolster],
            [trait.ChaosReshaped],
            ),
        ]


class FestivalFlight(RollDefinition):
    """
    Strand Breechloaded Grenade Launcher, Area Denial Frame, Anti-Overload
    Source: Solstice
    https://www.light.gg/db/items/4019651319
    https://destiny.report/w/4019651319
    """
    items = [
        Item('Festival Flight', hash=4019651319),
        Item('Festival Flight', hash=3977654524),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_magazine,
            [trait.BlastDistributor],
            [trait.Demolitionist],
            [trait.Slice],
            [trait.OneForAll],
            [trait.AttritionOrbs],
            [trait.Hatchling],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_magazine,
            [trait.BlastDistributor, trait.Demolitionist],
            [trait.OneForAll, trait.Hatchling],
            ),
        Roll(
            'Strand combo',
            default_barrels,
            default_magazine,
            [trait.Slice],
            [trait.Hatchling],
            ),
        ]
