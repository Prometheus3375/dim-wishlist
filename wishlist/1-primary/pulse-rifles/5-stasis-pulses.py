from wishlist import *
from . import *


class Disparity(RollDefinition):
    """
    Stasis Pulse Rifle, Aggressive Burst, Anti-Unstoppable, Craftable
    Source: Exotic mission "Seraph's Shield"
    https://www.light.gg/db/items/1751893422
    https://destiny.report/w/1751893422
    """
    item = Item('Disparity', hash=1751893422)


class HailingConfusion(RollDefinition):
    """
    Stasis Pulse Rifle, Adaptive Frame, Anti-Barrier
    Source: Europa
    https://www.light.gg/db/items/4236134153
    https://destiny.report/w/4236134153
    """
    item = Item('Hailing Confusion', hash=4236134153)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Headstone],
            [trait.Rimestealer],
            [trait.Demolitionist],
            [trait.CrystallineCorpsebloom],
            [trait.DesperateMeasures],
            [trait.Meganeura],
            ),
        Roll(
            'Stasis combo',
            default_barrels,
            default_mags,
            [trait.Rimestealer, trait.Headstone],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Precision combo',
            default_barrels,
            default_mags,
            [trait.Headstone],
            [trait.Meganeura],
            ),
        Roll(
            'Ability combo',
            default_barrels,
            default_mags,
            [trait.Demolitionist],
            [trait.DesperateMeasures],
            ),
        ]


class NewPurpose(RollDefinition):
    """
    Stasis Pulse Rifle, High-Impact Frame, Anti-Unstoppable
    Source: Dungeon "Duality"
    https://www.light.gg/db/items/1400385226
    https://destiny.report/w/1400385226
    """
    item = Item('New Purpose', hash=1400385226)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Headstone],
            [trait.Rimestealer],
            [trait.Meganeura],
            ),
        Roll(
            'Stasis combo',
            default_barrels,
            default_mags,
            [trait.Headstone],
            [trait.Rimestealer],
            ),
        Roll(
            'Precision combo',
            default_barrels,
            default_mags,
            [trait.Headstone],
            [trait.Meganeura],
            ),
        ]


class RedrixsEstoc(RollDefinition):
    """
    Stasis Pulse Rifle, Legacy PR-55 Frame, Anti-Barrier
    Source: Competitive Crucible
    https://www.light.gg/db/items/747743636
    https://destiny.report/w/747743636
    """
    item = Item("Redrix's Estoc", hash=747743636)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Rimestealer],
            [trait.Firefly],
            [trait.CrystallineCorpsebloom],
            [trait.Headstone],
            [stock.HandLaidStock, AnyPerk],
            ),
        Roll(
            'Stasis combo',
            default_barrels,
            default_mags,
            [trait.Rimestealer, trait.CrystallineCorpsebloom],
            [trait.Headstone],
            [stock.HandLaidStock, AnyPerk],
            ),
        Roll(
            'Precision combo',
            default_barrels,
            default_mags,
            [trait.Firefly],
            [trait.Headstone],
            [stock.HandLaidStock, AnyPerk],
            ),
        ]


class StayFrosty(RollDefinition):
    """
    Stasis Pulse Rifle, Lightweight Frame, Anti-Overload
    Source: The Dawning
    https://www.light.gg/db/items/3910523587
    https://destiny.report/w/3910523587
    """
    item = Item('Stay Frosty', hash=3910523587)
    roll = Roll(
        'Stasis combo',
        default_barrels,
        default_mags,
        [trait.Rimestealer],
        [trait.Headstone],
        )


class Syncopation53(RollDefinition):
    """
    Stasis Pulse Rifle, Adaptive Frame, Anti-Barrier, Craftable
    Source: Banshee-44
    https://www.light.gg/db/items/2856514843
    https://destiny.report/w/2856514843
    """
    item = Item('Syncopation-53', hash=2856514843)


class TheTimeWornSpire(RollDefinition):
    """
    Stasis Pulse Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Iron Banner
    https://www.light.gg/db/items/2204165992
    https://destiny.report/w/2204165992
    """
    item = Item('The Time-Worn Spire', hash=2204165992)
    roll = Roll(
        'Precision combo',
        default_barrels,
        default_mags,
        [trait.Firefly],
        [trait.Headstone],
        )
