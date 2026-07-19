from wishlist import *
from . import *


class Supercluster(RollDefinition):
    """
    Strand Shotgun, Pinpoint Slug Frame, Anti-Barrier, Craftable
    Source: Exotic mission "Starcrossed"
    https://www.light.gg/db/items/92459755
    https://destiny.report/w/92459755
    """
    item = Item('Supercluster', hash=92459755)


class Swordbreaker(RollDefinition):
    """
    Strand Shotgun, Lightweight Frame, Anti-Overload, Craftable
    Source: Raid "Crota's End"
    https://www.light.gg/db/items/3163900678
    https://destiny.report/w/3163900678
    """
    items = [
        Item('Swordbreaker', hash=3163900678),
        Item('Swordbreaker (Adept)', hash=1239700299),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            [barrel.BarrelShroud, AnyPerk],
            [magazine.AccurizedRounds, AnyPerk],
            [trait.Pugilist],
            [trait.ThreatDetector],
            [trait.ParacausalAffinity],
            [trait.OneTwoPunch],
            [trait.OpeningShot],
            [trait.Hatchling],
            ),
        Roll(
            'Melee damage increase',
            pve_barrels,
            pve_mags,
            [trait.ThreatDetector],
            [trait.OneTwoPunch],
            ),
        Roll(
            'PvP',
            pvp_barrels,
            pvp_mags,
            [trait.ThreatDetector],
            [trait.OneTwoPunch],
            ),
        Roll(
            'Ad clear',
            pve_barrels,
            pve_mags,
            [trait.Pugilist, trait.ParacausalAffinity],
            [trait.Hatchling],
            ),
        ]


class UntilItsReturn(RollDefinition):
    """
    Strand Shotgun, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Xûr
    https://www.light.gg/db/items/2883484461
    https://destiny.report/w/2883484461
    """
    item = Item('Until Its Return', hash=2883484461)
    roll = Roll(
        'Damage dealing',
        pve_barrels,
        pve_mags,
        [trait.Overflow],
        [trait.TrenchBarrel],
        )
