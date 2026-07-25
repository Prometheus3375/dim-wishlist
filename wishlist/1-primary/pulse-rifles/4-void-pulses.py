from wishlist import *
from . import *


class ClawsOfTheWolf(RollDefinition):
    """
    Void Pulse Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Lord Saladin
    https://www.light.gg/db/items/3634548599
    https://destiny.report/w/3634548599
    """
    item = Item('Claws of the Wolf', hash=3634548599)
    roll = Roll(
        'Void combo',
        default_barrels,
        default_mags,
        [trait.RepulsorBrace],
        [trait.DestabilizingRounds],
        )


class ElsiesRifle(RollDefinition):
    """
    Void Pulse Rifle, High-Impact Frame, Anti-Unstoppable
    Source: Onslaught
    https://www.light.gg/db/items/381446446
    https://destiny.report/w/381446446
    """
    item = Item("Elsie's Rifle", hash=381446446)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.DimensionalShift],
            [trait.RepulsorBrace],
            [trait.CollectiveDemolition],
            [trait.Demoralize],
            [trait.CollectiveAction],
            [trait.DestabilizingRounds],
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
            [trait.CollectiveDemolition, trait.DimensionalShift],
            [trait.CollectiveAction],
            ),
        ]


class Gridskipper(RollDefinition):
    """
    Void Pulse Rifle, Rapid-Fire Frame, Anti-Overload
    Source: World
    https://www.light.gg/db/items/3176697589
    https://destiny.report/w/3176697589
    """
    item = Item('Gridskipper', hash=3176697589)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.DimensionalShift],
            [trait.Demoralize],
            [trait.Demolitionist],
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            [trait.DesperateMeasures],
            ),
        Roll(
            'Void combo',
            default_barrels,
            default_mags,
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Ability combo',
            default_barrels,
            default_mags,
            [trait.Demolitionist],
            [trait.DesperateMeasures],
            ),
        ]


class HighTyrant(RollDefinition):
    """
    Void Pulse Rifle, Balanced Heat Weapon, Anti-Overload
    Source: Dungeon "Equilibrium"
    https://www.light.gg/db/items/2873508409
    https://destiny.report/w/2873508409
    """
    item = Item('High Tyrant', hash=2873508409)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            [battery.IonizedHeatsink, AnyPerk],
            [trait.RepulsorBrace],
            [trait.CoolingBaubles],
            [trait.DestabilizingRounds],
            [trait.WitheringGaze],
            [trait.Demoralize],
            [trait.Meganeura],
            ),
        Roll(
            'Void combo',
            default_barrels,
            [battery.IonizedHeatsink, AnyPerk],
            [trait.RepulsorBrace, trait.DestabilizingRounds],
            [trait.Demoralize],
            ),
        ]


class JoxersLongsword(RollDefinition):
    """
    Void Pulse Rifle, Heavy Burst, Anti-Unstoppable
    Source: Crucible
    https://www.light.gg/db/items/2150012406
    https://destiny.report/w/2150012406
    """
    items = [
        Item("Joxer's Longsword", hash=2150012406),
        Item("Joxer's Longsword", hash=3538003989),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Demolitionist],
            [trait.Dragonfly],
            [trait.RepulsorBrace],
            [trait.AdrenalineJunkie],
            [trait.DestabilizingRounds],
            [trait.Demoralize],
            ),
        Roll(
            'Void combo',
            default_barrels,
            default_mags,
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds, trait.Demoralize],
            ),
        Roll(
            'Grenade combo',
            default_barrels,
            default_mags,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        ]


class LastPerdition(RollDefinition):
    """
    Void Pulse Rifle, Adaptive Frame, Anti-Barrier
    Source: Lord Shaxx
    https://www.light.gg/db/items/3364253967
    https://destiny.report/w/3364253967
    """
    item = Item('Last Perdition', hash=3364253967)


class Premonition(RollDefinition):
    """
    Void Pulse Rifle, High-Impact Frame, Anti-Unstoppable
    Source: The Moon
    https://www.light.gg/db/items/1969802090
    https://destiny.report/w/1969802090
    """
    item = Item('Premonition', hash=1969802090)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.RepulsorBrace],
            [trait.Firefly],
            [trait.Demoralize],
            [trait.DestabilizingRounds],
            [trait.Meganeura],
            ),
        Roll(
            'Void combo',
            default_barrels,
            default_mags,
            [trait.RepulsorBrace, trait.Demoralize],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Precision combo',
            default_barrels,
            default_mags,
            [trait.Firefly],
            [trait.Meganeura],
            ),
        ]


class TheMartlet(RollDefinition):
    """
    Void Pulse Rifle, Lightweight Frame, Anti-Overload
    Source: Saint-14
    https://www.light.gg/db/items/877384
    https://destiny.report/w/877384
    """
    item = Item('The Martlet', hash=877384)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.RepulsorBrace],
            [trait.Firefly],
            [trait.DestabilizingRounds],
            [trait.WitheringGaze],
            ),
        Roll(
            'Void combo',
            default_barrels,
            default_mags,
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        ]


class VelesX(RollDefinition):
    """
    Void Pulse Rifle, Aggressive Burst, Anti-Unstoppable
    Source: Solo Ops
    https://www.light.gg/db/items/438540299
    https://destiny.report/w/438540299
    """
    item = Item('Veles-X', hash=438540299)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.RepulsorBrace],
            [trait.Demoralize],
            [trait.DestabilizingRounds],
            [trait.Firefly],
            ),
        Roll(
            'Void combo',
            default_barrels,
            default_mags,
            [trait.RepulsorBrace, trait.Demoralize],
            [trait.DestabilizingRounds],
            ),
        ]


class Yesteryear(RollDefinition):
    """
    Void Pulse Rifle, Adaptive Frame, Anti-Barrier
    Source: The Drifter
    https://www.light.gg/db/items/4028000428
    https://destiny.report/w/4028000428
    """
    item = Item('Yesteryear', hash=4028000428)
