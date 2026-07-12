from wishlist import *
from . import *


class Antedate(RollDefinition):
    """
    Arc Submachine Gun, Adaptive Frame, Anti-Barrier
    Source: Raid "The Desert Perpetual"
    https://www.light.gg/db/items/1435808083
    https://destiny.report/w/1435808083
    """
    item = Item('Antedate', hash=1435808083)
    rolls = [
        Roll(
            'Super roll',
            [barrel.ExtendedBarrel, AnyPerk],
            default_mags,
            [trait.Dragonfly],
            [trait.Strategist],
            [trait.JoltingFeedback],
            [trait.ParacausalAffinity],
            ),
        Roll(
            'Ad clear',
            [barrel.ExtendedBarrel, AnyPerk],
            default_mags,
            [trait.Dragonfly],
            [trait.JoltingFeedback],
            ),
        ]


class IKELOS_SMG_v103(RollDefinition):
    """
    Arc Submachine Gun, Aggressive Frame, Anti-Unstoppable, Craftable
    Source: Exotic mission "Seraph's Shield"
    https://www.light.gg/db/items/2149683300
    https://destiny.report/w/2149683300
    """
    item = Item('IKELOS_SMG_v1.0.3', hash=2149683300)
    roll = Roll(
        'Ad clear',
        [barrel.ExtendedBarrel, AnyPerk],
        [magazine.SeraphRounds, AnyPerk],
        [trait.ThreatDetector],
        [trait.Voltshot],
        )


class OutOfBounds(RollDefinition):
    """
    Arc Submachine Gun, Lightweight Frame, Anti-Overload
    Source: Crucible
    https://www.light.gg/db/items/2579239008
    https://destiny.report/w/2579239008
    """
    items = [
        Item('Out of Bounds', hash=2579239008),
        Item('Out of Bounds', hash=3021407779),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Demolitionist],
            [trait.Voltshot],
            [trait.AdrenalineJunkie],
            [trait.JoltingFeedback],
            ),
        Roll(
            'Arc combo',
            default_barrels,
            default_mags,
            [trait.Voltshot],
            [trait.JoltingFeedback],
            ),
        Roll(
            'Grenade combo',
            default_barrels,
            default_mags,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        ]


class SeventhSeraphVY7(RollDefinition):
    """
    Arc Submachine Gun, Precision Frame, Anti-Barrier
    Source: Cosmodrome
    https://www.light.gg/db/items/1719169808
    https://destiny.report/w/1719169808
    """
    item = Item('Seventh Seraph VY-7', hash=1719169808)
    rolls = [
        Roll(
            'Super roll',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.SeraphRounds, AnyPerk],
            [trait.AmbitiousAssassin],
            [trait.SuperchargedMagazine],
            [trait.JoltingFeedback],
            [trait.GearShift],
            ),
        Roll(
            'Arc combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.SeraphRounds, AnyPerk],
            [trait.SuperchargedMagazine],
            [trait.JoltingFeedback, trait.GearShift],
            )
        ]


class Subjunctive(RollDefinition):
    """
    Arc Submachine Gun, Lightweight Frame, Anti-Overload, Craftable
    Source: Exotic mission "Starcrossed"
    https://www.light.gg/db/items/1447836603
    https://destiny.report/w/1447836603
    """
    item = Item('Subjunctive', hash=1447836603)
    roll = Roll(
        'Ad clear',
        [barrel.ExtendedBarrel, AnyPerk],
        default_mags,
        [trait.ThreatDetector],
        [trait.Voltshot],
        )


class Whatchamacallit(RollDefinition):
    """
    Arc Submachine Gun, Aggressive Burst, Anti-Unstoppable
    Source: Pinnacle Ops
    https://www.light.gg/db/items/357669417
    https://destiny.report/w/357669417
    """
    items = [
        Item('Whatchamacallit', hash=357669417),
        Item('Whatchamacallit', hash=149110926),
        ]
    rolls = [
        Roll(
            'Super roll',
            [barrel.ArrowheadBrake, AnyPerk],
            default_mags,
            [trait.LightTouch],
            [trait.CollectivePugilism],
            [trait.GearShift],
            [trait.JoltingFeedback],
            ),
        Roll(
            'Arc combo',
            [barrel.ArrowheadBrake, AnyPerk],
            default_mags,
            [trait.LightTouch],
            [trait.JoltingFeedback, trait.GearShift],
            )
        ]
