from wishlist import *

_default_barrels = [barrel.ArrowheadBrake, AnyPerk]
_default_mags = [magazine.FlaredMagwell, AnyPerk]


class AgeOldBond(RollDefinition):
    """
    Void Auto Rifle, High-Impact Frame, Anti-Unstoppable, Craftable
    Source: Last Wish
    https://www.light.gg/db/items/424291879
    https://destiny.report/w/424291879
    """
    item = Item('Age-Old Bond', hash=424291879)
    roll = Roll(
        'Grenade combo',
        _default_barrels,
        _default_mags,
        [trait.Demolitionist],
        [trait.AdrenalineJunkie],
        )


class GnawingHunger(RollDefinition):
    """
    Void Auto Rifle, Adaptive Frame, Anti-Barrier
    Source: Gambit
    https://www.light.gg/db/items/214545213
    https://destiny.report/w/214545213
    """
    item = Item('Gnawing Hunger', hash=214545213)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            _default_barrels,
            _default_mags,
            [trait.Demolitionist],
            [trait.WitheringGaze],
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Void combo',
            _default_barrels,
            _default_mags,
            [trait.RepulsorBrace, trait.WitheringGaze],
            [trait.DestabilizingRounds],
            ),
        ]


class PositiveOutlook(RollDefinition):
    """
    Void Auto Rifle, Precision Frame, Anti-Barrier
    Source: Fireteam Ops
    https://www.light.gg/db/items/3625635456
    https://destiny.report/w/3625635456
    """
    items = [
        Item('Positive Outlook', hash=3625635456),
        Item('Positive Outlook', hash=1832481283),
        ]
    rolls = [
        Roll(
            'Super roll',
            _default_barrels,
            _default_mags,
            [trait.AmbitiousAssassin],
            [trait.RepulsorBrace],
            [trait.WitheringGaze],
            [trait.DestabilizingRounds],
            [trait.MegaKillClip],
            [trait.Dragonfly],
            ),
        Roll(
            'Void combo',
            _default_barrels,
            _default_mags,
            [trait.RepulsorBrace, trait.WitheringGaze],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Kill combo',
            _default_barrels,
            _default_mags,
            [trait.AmbitiousAssassin],
            [trait.MegaKillClip],
            ),
        ]


class RecklessOracle(RollDefinition):
    """
    Void Auto Rifle, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Garden of Salvation
    https://www.light.gg/db/items/1992309064
    https://destiny.report/w/1992309064
    """
    item = Item('Reckless Oracle', hash=1992309064)


class RecklessOraclePantheon(RollDefinition):
    """
    Void Auto Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Pantheon
    https://www.light.gg/db/items/4158265643
    https://destiny.report/w/4158265643
    """
    items = [
        Item('Reckless Oracle', hash=4158265643),
        Item('Reckless Oracle', hash=1802315656),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            _default_barrels,
            _default_mags,
            [trait.DestabilizingRounds],
            [trait.CollectiveAction],
            [trait.RepulsorBrace],
            [trait.ChaosReshaped],
            [trait.OneForAll],
            ),
        Roll(
            'Ad clear',
            _default_barrels,
            _default_mags,
            [trait.DestabilizingRounds],
            [trait.ChaosReshaped, trait.OneForAll],
            ),
        Roll(
            'Void combo',
            _default_barrels,
            _default_mags,
            [trait.DestabilizingRounds],
            [trait.RepulsorBrace],
            ),
        ]


class ReghusksPledge(RollDefinition):
    """
    Void Auto Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Iron Banner
    https://www.light.gg/db/items/2370525224
    https://destiny.report/w/2370525224
    """
    item = Item("Reghusk's Pledge", hash=2370525224)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            _default_barrels,
            _default_mags,
            [trait.Demoralize],
            [trait.DestabilizingRounds],
            [trait.ImpromptuAmmunition],
            [trait.AttritionOrbs],
            [trait.GoldenTricorn],
            [trait.RepulsorBrace],
            ),
        Roll(
            'Void combo',
            _default_barrels,
            _default_mags,
            [trait.DestabilizingRounds, trait.Demoralize],
            [trait.RepulsorBrace],
            ),
        Roll(
            'Ammo generation',
            _default_barrels,
            _default_mags,
            [trait.ImpromptuAmmunition],
            [trait.AttritionOrbs, trait.GoldenTricorn],
            ),
        ]


class TheRiposte(RollDefinition):
    """
    Void Auto Rifle, Lightweight Frame, Anti-Overload
    Source: Competitive Crucible
    https://www.light.gg/db/items/866434750
    https://destiny.report/w/866434750
    """
    item = Item('The Riposte', hash=866434750)
    rolls = [
        Roll(
            'Void combo',
            _default_barrels,
            _default_mags,
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            [stock.HandLaidStock, AnyPerk],
            ),
        ]
