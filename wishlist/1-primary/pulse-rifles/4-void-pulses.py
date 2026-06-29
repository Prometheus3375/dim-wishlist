from wishlist import *


class ClawsOfTheWolf(RollDefinition):
    """
    Void Pulse Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Lord Saladin
    https://www.light.gg/db/items/3634548599
    https://destiny.report/w/3634548599
    """
    item = Item('Claws of the Wolf', hash=3634548599)


class ElsiesRifle(RollDefinition):
    """
    Void Pulse Rifle, High-Impact Frame, Anti-Unstoppable
    Source: Onslaught
    https://www.light.gg/db/items/381446446
    https://destiny.report/w/381446446
    """
    item = Item("Elsie's Rifle", hash=381446446)


class Gridskipper(RollDefinition):
    """
    Void Pulse Rifle, Rapid-Fire Frame, Anti-Overload
    Source: World
    https://www.light.gg/db/items/3176697589
    https://destiny.report/w/3176697589
    """
    item = Item('Gridskipper', hash=3176697589)


class HighTyrant(RollDefinition):
    """
    Void Pulse Rifle, Balanced Heat Weapon, Anti-Overload
    Source: Equilibrium
    https://www.light.gg/db/items/2873508409
    https://destiny.report/w/2873508409
    """
    item = Item('High Tyrant', hash=2873508409)
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.DestabilizingRounds, trait.Demolitionist],
            [trait.MasterOfArms, trait.Meganeura, trait.Demoralize],
            ),
        Roll(
            'Void combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.RepulsorBrace],
            [trait.Demoralize],
            ),
        Roll(
            'Withering Gaze',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.DestabilizingRounds],
            [trait.WitheringGaze],
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
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.RepulsorBrace, trait.Firefly],
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


class Yesteryear(RollDefinition):
    """
    Void Pulse Rifle, Adaptive Frame, Anti-Barrier
    Source: The Drifter
    https://www.light.gg/db/items/4028000428
    https://destiny.report/w/4028000428
    """
    item = Item('Yesteryear', hash=4028000428)
