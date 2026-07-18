from wishlist import *
from . import *


class AurvandilFR6(RollDefinition):
    """
    Stasis Fusion Rifle, High-Impact Frame, Anti-Unstoppable
    Source: Banshee-44
    https://www.light.gg/db/items/3786215462
    https://destiny.report/w/3786215462
    """
    item = Item('Aurvandil FR6', hash=3786215462)
    rolls = [
        Roll(
            'Debuff support',
            default_barrels,
            default_battery,
            [trait.Reconstruction],
            [trait.ChillClip],
            ),
        ]


class BurdenOfGuilt(RollDefinition):
    """
    Stasis Fusion Rifle, Adaptive Frame, Anti-Barrier
    Source: Saint-14
    https://www.light.gg/db/items/976459525
    https://destiny.report/w/976459525
    """
    item = Item('Burden Of Guilt', hash=976459525)
    rolls = [
        Roll(
            'Stasis combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.AcceleratedCoils, AnyPerk],
            [trait.Rimestealer],
            [trait.CrystallineCorpsebloom],
            ),
        ]


class Deliverance(RollDefinition):
    """
    Stasis Fusion Rifle, Precision Frame, Anti-Barrier, Craftable
    Source: Raid "Vow of the Disciple"
    https://www.light.gg/db/items/768621510
    https://destiny.report/w/768621510
    """
    items = [
        Item('Deliverance', hash=768621510),
        Item('Deliverance (Adept)', hash=2943293195),
        ]


class Lionfish4FR(RollDefinition):
    """
    Stasis Fusion Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Commander Zavala; Tenet of Bravery
    https://www.light.gg/db/items/2423071981
    https://destiny.report/w/2423071981
    """
    item = Item('Lionfish-4FR', hash=2423071981)
    is_chosen = True
    rolls = [
        Roll(
            'Debuff support',
            default_barrels,
            [battery.AcceleratedCoils, AnyPerk],
            [trait.Reconstruction],
            [trait.ChillClip],
            [origin.VeistStinger],
            ),
        ]


class NoxSiderealIV(RollDefinition):
    """
    Stasis Fusion Rifle, Aggressive Frame, Anti-Unstoppable
    Source: Commander Zavala; Tenet of Bravery
    https://www.light.gg/db/items/2875763009
    https://destiny.report/w/2875763009
    """
    items = [
        Item('Nox Sidereal IV', hash=2875763009),
        Item('Nox Sidereal IV', hash=74733286),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_battery,
            [trait.AmbitiousAssassin],
            [trait.Demolitionist],
            [trait.CrystallineCorpsebloom],
            [trait.ReservoirBurst],
            [trait.AdrenalineJunkie],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_battery,
            [trait.AmbitiousAssassin],
            [trait.CrystallineCorpsebloom, trait.ReservoirBurst],
            ),
        Roll(
            'Grenade combo',
            default_barrels,
            default_battery,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        ]


class Riptide(RollDefinition):
    """
    Stasis Fusion Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Lord Shaxx; Tenet of Bravery
    https://www.light.gg/db/items/2297554989
    https://destiny.report/w/2297554989
    """
    items = [
        Item('Riptide', hash=2297554989),
        Item('Riptide', hash=1323862250),
        ]
    rolls = [
        Roll(
            'Debuff support',
            default_barrels,
            [battery.AcceleratedCoils, AnyPerk],
            [trait.Overflow, trait.AutoLoadingHolster],
            [trait.ChillClip],
            ),
        ]
