from wishlist import *
from . import *


class A21Delirium(RollDefinition):
    """
    Arc Machine Gun, Rapid-Fire Frame, Anti-Overload
    Source: Gambit
    https://www.light.gg/db/items/3001598094
    https://destiny.report/w/3001598094
    """
    item = Item('21% Delirium', hash=3001598094)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Overflow],
            [trait.TrickleCharge],
            [trait.FeedingFrenzy],
            [trait.KillingTally],
            [trait.MegaKillClip],
            [trait.JoltingFeedback],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.FeedingFrenzy],
            [trait.MegaKillClip],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.Overflow, trait.TrickleCharge],
            [trait.KillingTally],
            ),
        ]


class AFineMemorial(RollDefinition):
    """
    Arc Machine Gun, Adaptive Frame, Anti-Barrier
    Source: The Moon
    https://www.light.gg/db/items/3211332727
    https://destiny.report/w/3211332727
    """
    item = Item('A Fine Memorial', hash=3211332727)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.ImpromptuAmmunition],
            [trait.MegaKillClip],
            [trait.JoltingFeedback],
            [trait.Meganeura],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.ImpromptuAmmunition],
            [trait.Meganeura],
            ),
        ]


class BitterEnd(RollDefinition):
    """
    Arc Machine Gun, Balanced Heat Weapon, Anti-Overload
    Source: Dungeon "Equilibrium"
    https://www.light.gg/db/items/954563454
    https://destiny.report/w/954563454
    """
    item = Item('Bitter End', hash=954563454)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            [barrel.ChamberedCompensator, AnyPerk],
            [battery.OverclockedHeatsink, AnyPerk],
            [trait.CoolingBaubles],
            [trait.AttritionOrbs],
            [trait.JoltingFeedback],
            [trait.OneForAll],
            [trait.KillingTally],
            ),
        Roll(
            """
            Ad clear.
            Using Overclocked over Ionized Heatsink
            because Cooling Baubles keep the weapon cool.
            """,
            [barrel.ChamberedCompensator, AnyPerk],
            [battery.OverclockedHeatsink, AnyPerk],
            [trait.CoolingBaubles],
            [trait.KillingTally, trait.JoltingFeedback, trait.OneForAll],
            ),
        ]


class EleaticPrinciple(RollDefinition):
    """
    Arc Machine Gun, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Xûr
    https://www.light.gg/db/items/105306149
    https://destiny.report/w/105306149
    """
    item = Item('Eleatic Principle', hash=105306149)


class PlancksStride(RollDefinition):
    """
    Arc Machine Gun, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Xûr
    https://www.light.gg/db/items/820890091
    https://destiny.report/w/820890091
    """
    item = Item("Planck's Stride", hash=820890091)


class SeventhSeraphSAW(RollDefinition):
    """
    Arc Machine Gun, High-Impact Frame, Anti-Unstoppable
    Source: Cosmodrome
    https://www.light.gg/db/items/2584201248
    https://destiny.report/w/2584201248
    """
    item = Item('Seventh Seraph SAW', hash=2584201248)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            [magazine.SeraphRounds, AnyPerk],
            [trait.AttritionOrbs],
            [trait.SuperchargedMagazine],
            [trait.JoltingFeedback],
            [trait.MegaKillClip],
            [trait.Meganeura],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            [magazine.SeraphRounds, AnyPerk],
            [trait.SuperchargedMagazine],
            [trait.Meganeura, trait.JoltingFeedback],
            ),
        ]


class SongOfIrYut(RollDefinition):
    """
    Arc Machine Gun, Adaptive Frame, Anti-Barrier, Craftable
    Source: Raid "Crota's End"
    https://www.light.gg/db/items/2828278545
    https://destiny.report/w/2828278545
    """
    items = [
        Item('Song of Ir Yût', hash=2828278545),
        Item('Song of Ir Yût (Adept)', hash=407511664),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.FeedingFrenzy],
            [trait.JoltingFeedback],
            [trait.MegaKillClip],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.JoltingFeedback, trait.FeedingFrenzy],
            [trait.MegaKillClip],
            ),
        ]


class TerminusHorizon(RollDefinition):
    """
    Arc Machine Gun, High-Impact Frame, Anti-Unstoppable
    Source: Dungeon "Spire of the Watcher"
    https://www.light.gg/db/items/3814261872
    https://destiny.report/w/3814261872
    """
    item = Item('Terminus Horizon', hash=3814261872)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Meganeura],
            [trait.SuperchargedMagazine],
            [trait.FeedingFrenzy],
            [trait.JoltingFeedback],
            [trait.MegaKillClip],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.Meganeura],
            [trait.MegaKillClip, trait.JoltingFeedback],
            ),
        ]


class WatchfulEye(RollDefinition):
    """
    Arc Machine Gun, Aggressive Frame, Anti-Unstoppable
    Source: Dungeon "Pit of Heresy"
    https://www.light.gg/db/items/3058845782
    https://destiny.report/w/3058845782
    """
    items = [
        Item('Watchful Eye', hash=3058845782),
        Item('Watchful Eye', hash=1757177186),
        Item('Watchful Eye (Adept)', hash=737409399),
        Item('Watchful Eye (Adept)', hash=2856225832),
        Item('Watchful Eye', hash=768610585),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Overflow],
            [trait.JoltingFeedback],
            [trait.KillingTally],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.Overflow],
            [trait.KillingTally, trait.JoltingFeedback],
            ),
        ]
