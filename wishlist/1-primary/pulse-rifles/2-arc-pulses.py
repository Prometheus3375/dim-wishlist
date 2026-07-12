from wishlist import *
from . import *


class Corrasion(RollDefinition):
    """
    Arc Pulse Rifle, Heavy Burst, Anti-Unstoppable, Craftable
    Source: Exotic mission "Encore"
    https://www.light.gg/db/items/2126178511
    https://destiny.report/w/2126178511
    """
    item = Item('Corrasion', hash=2126178511)


class CruelMercy(RollDefinition):
    """
    Arc Pulse Rifle, Heavy Burst, Anti-Unstoppable
    Source: Commander Zavala
    https://www.light.gg/db/items/4011513985
    https://destiny.report/w/4011513985
    """
    item = Item('Cruel Mercy', hash=4011513985)
    roll = Roll(
        'Grenade combo',
        default_barrels,
        default_mags,
        [trait.Demolitionist],
        [trait.AdrenalineJunkie],
        )


class HorrorsLeast(RollDefinition):
    """
    Arc Pulse Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Commander Zavala; Tenet of Bravery
    https://www.light.gg/db/items/827835657
    https://destiny.report/w/827835657
    """
    items = [
        Item("Horror's Least", hash=827835657),
        Item("Horror's Least", hash=1018012078),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.SuperchargedMagazine],
            [trait.Overflow],
            [trait.JoltingFeedback],
            [trait.Rampage],
            ),
        Roll(
            'Arc combo',
            default_barrels,
            default_mags,
            [trait.SuperchargedMagazine],
            [trait.JoltingFeedback],
            ),
        ]


class InfinitePaths8(RollDefinition):
    """
    Arc Pulse Rifle, Lightweight Frame, Anti-Overload
    Source: World
    https://www.light.gg/db/items/3176697588
    https://destiny.report/w/3176697588
    """
    item = Item('Infinite Paths 8', hash=3176697588)


class Insidious(RollDefinition):
    """
    Arc Pulse Rifle, Aggressive Burst, Anti-Unstoppable, Craftable
    Source: Raid "Vow of the Disciple"
    https://www.light.gg/db/items/3428521585
    https://destiny.report/w/3428521585
    """
    item = Item('Insidious', hash=3428521585)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Dragonfly],
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.Dragonfly],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Grenade combo',
            default_barrels,
            default_mags,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        ]


class OversoulEdict(RollDefinition):
    """
    Arc Pulse Rifle, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Raid "Crota's End"
    https://www.light.gg/db/items/1098171824
    https://destiny.report/w/1098171824
    """
    items = [
        Item('Oversoul Edict', hash=1098171824),
        Item('Oversoul Edict (Adept)', hash=578105049),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Demolitionist],
            [trait.SuperchargedMagazine],
            [trait.AdrenalineJunkie],
            [trait.JoltingFeedback],
            [trait.GearShift],
            ),
        Roll(
            'Arc combo',
            default_barrels,
            default_mags,
            [trait.SuperchargedMagazine],
            [trait.JoltingFeedback, trait.GearShift],
            ),
        Roll(
            'Grenade combo',
            default_barrels,
            default_mags,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        ]


class PhyllotacticSpiral(RollDefinition):
    """
    Arc Pulse Rifle, High-Impact Frame, Anti-Unstoppable, Craftable
    Source: Neomuna
    https://www.light.gg/db/items/3635821806
    https://destiny.report/w/3635821806
    """
    item = Item('Phyllotactic Spiral', hash=3635821806)


class ScalarPotential(RollDefinition):
    """
    Arc Pulse Rifle, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Exotic mission "Starcrossed"
    https://www.light.gg/db/items/2563668388
    https://destiny.report/w/2563668388
    """
    item = Item('Scalar Potential', hash=2563668388)


class TheThirdAxiom(RollDefinition):
    """
    Arc Pulse Rifle, Adaptive Frame, Anti-Barrier
    Source: Commander Zavala
    https://www.light.gg/db/items/3744058588
    https://destiny.report/w/3744058588
    """
    item = Item('The Third Axiom', hash=3744058588)
