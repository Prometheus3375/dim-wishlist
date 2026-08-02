from wishlist import *
from . import *


class BugOutBag(RollDefinition):
    """
    Void Submachine Gun, Adaptive Frame, Anti-Barrier
    Source: Gambit
    https://www.light.gg/db/items/3327901954
    https://destiny.report/w/3327901954
    """
    item = Item('Bug-Out Bag', hash=3327901954)
    rolls = [
        Roll(
            'Super roll',
            [barrel.ExtendedBarrel, AnyPerk],
            default_mags,
            [trait.ThreatDetector],
            [trait.RepulsorBrace],
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Void combo',
            [barrel.ExtendedBarrel, AnyPerk],
            default_mags,
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Grenade combo',
            [barrel.ExtendedBarrel, AnyPerk],
            default_mags,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        ]


class EveryWakingMoment(RollDefinition):
    """
    Void Submachine Gun, Precision Frame, Anti-Barrier
    Source: The Moon
    https://www.light.gg/db/items/1487476133
    https://destiny.report/w/1487476133
    """
    item = Item('Every Waking Moment', hash=1487476133)
    rolls = [
        Roll(
            'Super roll',
            [barrel.ArrowheadBrake, AnyPerk],
            default_mags,
            [trait.DestabilizingRounds],
            [trait.RepulsorBrace],
            [trait.Meganeura],
            [trait.Demoralize],
            ),
        Roll(
            'Void combo',
            [barrel.ArrowheadBrake, AnyPerk],
            default_mags,
            [trait.DestabilizingRounds, trait.RepulsorBrace],
            [trait.Demoralize],
            ),
        ]


class ShayurasWrath(RollDefinition):
    """
    Void Submachine Gun, Precision Frame, Anti-Barrier
    Source: Trials of Osiris
    https://www.light.gg/db/items/3747667917
    https://destiny.report/w/3747667917
    """
    item = Item("Shayura's Wrath", hash=3747667917)
    roll = Roll(
        'Void combo',
        [barrel.FlutedBarrel, AnyPerk],
        default_mags,
        [trait.RepulsorBrace, trait.Demoralize],
        [trait.DestabilizingRounds],
        )


class TheHerosBurden(RollDefinition):
    """
    Void Submachine Gun, Adaptive Frame, Anti-Barrier
    Source: Lord Saladin
    https://www.light.gg/db/items/4222913208
    https://destiny.report/w/4222913208
    """
    item = Item("The Hero's Burden", hash=4222913208)


class TheRecluse(RollDefinition):
    """
    Void Submachine Gun, Lightweight Frame, Anti-Overload
    Source: Onslaught
    https://www.light.gg/db/items/3257283337
    https://destiny.report/w/3257283337
    """
    item = Item('The Recluse', hash=3257283337)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.CollectivePugilism],
            [trait.RepulsorBrace],
            [trait.DimensionalShift],
            [trait.CollectiveAction],
            [trait.DestabilizingRounds],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Void combo',
            default_barrels,
            default_mags,
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Collective combo',
            default_barrels,
            default_mags,
            [trait.CollectivePugilism, trait.DimensionalShift],
            [trait.CollectiveAction],
            ),
        ]


class TheTitle(RollDefinition):
    """
    Void Submachine Gun, Aggressive Frame, Anti-Unstoppable
    Source: Guardian Games
    https://www.light.gg/db/items/4106258882
    https://destiny.report/w/4106258882
    """
    item = Item('The Title', hash=4106258882)
    rolls = [
        Roll(
            'Super roll',
            [barrel.ExtendedBarrel, AnyPerk],
            default_mags,
            [trait.RepulsorBrace],
            [trait.ThreatDetector],
            [trait.DestabilizingRounds],
            [trait.Demoralize],
            ),
        Roll(
            'Void combo',
            [barrel.ExtendedBarrel, AnyPerk],
            default_mags,
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds, trait.Demoralize],
            ),
        ]


class Unforgiven(RollDefinition):
    """
    Void Submachine Gun, Aggressive Frame, Anti-Unstoppable
    Source: Dungeon "Duality"
    https://www.light.gg/db/items/234411205
    https://destiny.report/w/234411205
    """
    item = Item('Unforgiven', hash=234411205)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            [barrel.ChamberedCompensator, AnyPerk],
            default_mags,
            [trait.DestabilizingRounds],
            [trait.Demolitionist],
            [trait.AttritionOrbs],
            [trait.RepulsorBrace],
            [trait.AdrenalineJunkie],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Ad clear',
            [barrel.ChamberedCompensator, AnyPerk],
            default_mags,
            [trait.DestabilizingRounds],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Void combo',
            [barrel.ChamberedCompensator, AnyPerk],
            default_mags,
            [trait.DestabilizingRounds],
            [trait.RepulsorBrace],
            ),
        Roll(
            'Grenade combo',
            [barrel.ChamberedCompensator, AnyPerk],
            default_mags,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        ]


class VikalaSMG4(RollDefinition):
    """
    Void Submachine Gun, Balanced Heat Weapon, Anti-Overload
    Source: Sparrow Racing League
    https://www.light.gg/db/items/3210792817
    https://destiny.report/w/3210792817
    """
    items = [
        Item('Vikala SMG4', hash=3210792817),
        Item('Vikala SMG4', hash=1229624538),
        ]
    rolls = [
        Roll(
            'Super roll',
            [barrel.ExtendedBarrel, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.CoolingBaubles],
            [trait.Slideways],
            [trait.DimensionalShift],
            [trait.DestabilizingRounds],
            [trait.CollectiveAction],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Collective combo',
            [barrel.ExtendedBarrel, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.CoolingBaubles, trait.DimensionalShift],
            [trait.CollectiveAction],
            ),
        ]
