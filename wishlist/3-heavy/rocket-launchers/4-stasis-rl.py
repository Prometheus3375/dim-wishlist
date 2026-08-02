from wishlist import *
from . import *


class BumpInTheNight(RollDefinition):
    """
    Stasis Rocket Launcher, Aggressive Frame, Anti-Unstoppable, Craftable
    Source: Exotic mission "Presage"
    https://www.light.gg/db/items/1959650777
    https://destiny.report/w/1959650777
    """
    item = Item('Bump in the Night', hash=1959650777)


class ColdComfort(RollDefinition):
    """
    Stasis Rocket Launcher, Aggressive Frame, Anti-Unstoppable
    Source: Dungeon "Ghosts of the Deep"
    https://www.light.gg/db/items/2287287549
    https://destiny.report/w/2287287549
    """
    item = Item('Cold Comfort', hash=2287287549)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.ChillClip],
            [trait.EnviousAssassin],
            [trait.Bipod],
            [trait.ReapersTithe],
            [trait.AggregateCharge],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.EnviousAssassin],
            [trait.ReapersTithe, trait.AggregateCharge],
            ),
        ]


class ColdComfortRotN(RollDefinition):
    """
    Stasis Rocket Launcher, Aggressive Frame, Anti-Unstoppable, Legacy
    Source: Unobtainable (Rite of the Nine)
    https://www.light.gg/db/items/1817605554
    https://destiny.report/w/1817605554
    """
    items = [
        Item('Cold Comfort (Adept)', hash=1817605554),
        Item('Cold Comfort', hash=291447487),
        Item('Cold Comfort (Adept)', hash=2126543269),
        Item('Cold Comfort', hash=2760833884),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.EnviousArsenal],
            [trait.BaitAndSwitch, trait.ElementalHoning],
            ),
        ]


class PalmyraB(RollDefinition):
    """
    Stasis Rocket Launcher, Precision Frame, Anti-Barrier, Craftable
    Source: Banshee-44
    https://www.light.gg/db/items/3489657138
    https://destiny.report/w/3489657138
    """
    item = Item('Palmyra-B', hash=3489657138)
    roll = Roll(
        'Damage dealing',
        default_barrels,
        default_mags,
        [trait.AutoLoadingHolster],
        [trait.LastingImpression],
        )


class TheWhenAndWhere(RollDefinition):
    """
    Stasis Rocket Launcher, Adaptive Frame, Anti-Barrier
    Source: Raid "The Desert Perpetual"
    https://www.light.gg/db/items/1090936013
    https://destiny.report/w/1090936013
    """
    item = Item('The When And Where', hash=1090936013)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.ChillClip],
            [trait.ClownCartridge],
            [trait.Overflow],
            [trait.BaitAndSwitch],
            [trait.Surrounded],
            [trait.ReapersTithe],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.Overflow, trait.ClownCartridge],
            [trait.ReapersTithe, trait.BaitAndSwitch, trait.Surrounded],
            ),
        ]
