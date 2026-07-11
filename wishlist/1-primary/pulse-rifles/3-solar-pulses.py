from wishlist import *
from . import *


class Adhortative(RollDefinition):
    """
    Solar Pulse Rifle, Adaptive Frame, Anti-Barrier, Craftable
    Source: Exotic mission "Starcrossed"
    https://www.light.gg/db/items/2993554824
    https://destiny.report/w/2993554824
    """
    item = Item('Adhortative', hash=2993554824)
    roll = Roll(
        'Solar combo',
        default_barrels,
        default_mags,
        [trait.HealClip],
        [trait.Incandescent],
        )


class BxR55Battler(RollDefinition):
    """
    Solar Pulse Rifle, Legacy PR-55 Frame, Anti-Barrier, Craftable
    Source: Eternity
    https://www.light.gg/db/items/2708806099
    https://destiny.report/w/2708806099
    """
    item = Item('BxR-55 Battler', hash=2708806099)
    is_chosen = True
    roll = Roll(
        'PvP with grapple melee',
        [barrel.HammerForgedRifling],
        [magazine.AccurizedRounds],
        [trait.Demolitionist],
        [trait.BluntExecutionRounds],
        )


class DarkestBefore(RollDefinition):
    """
    Solar Pulse Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Dungeon "Prophecy"
    https://www.light.gg/db/items/2831259642
    https://destiny.report/w/2831259642
    """
    item = Item('Darkest Before', hash=2831259642)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.HealClip],
            [trait.AttritionOrbs],
            [trait.Incandescent],
            [trait.KillClip],
            ),
        Roll(
            'Solar combo',
            default_barrels,
            default_mags,
            [trait.HealClip],
            [trait.Incandescent],
            ),
        ]


class JorumsClaw(RollDefinition):
    """
    Solar Pulse Rifle, Adaptive Frame, Anti-Barrier
    Source: Lord Saladin
    https://www.light.gg/db/items/3634548598
    https://destiny.report/w/3634548598
    """
    item = Item("Jorum's Claw", hash=3634548598)


class Nullify(RollDefinition):
    """
    Solar Pulse Rifle, Heavy Burst, Anti-Unstoppable, Craftable
    Source: Raid "Salvation's Edge"
    https://www.light.gg/db/items/859869931
    https://destiny.report/w/859869931
    """
    items = [
        Item('Nullify', hash=859869931),
        Item('Nullify (Adept)', hash=892183998),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Firefly],
            [trait.HealClip],
            [trait.BurningAmbition],
            [trait.ChaosReshaped],
            [trait.Incandescent],
            [trait.Meganeura],
            ),
        Roll(
            'Solar combo',
            default_barrels,
            default_mags,
            [trait.BurningAmbition, trait.HealClip],
            [trait.Incandescent],
            ),
        Roll(
            'Precision combo',
            default_barrels,
            default_mags,
            [trait.Firefly],
            [trait.Meganeura],
            ),
        ]


class OgmaPR6(RollDefinition):
    """
    Solar Pulse Rifle, Lightweight Frame, Anti-Overload
    Source: Banshee-44
    https://www.light.gg/db/items/324584912
    https://destiny.report/w/324584912
    """
    item = Item('Ogma PR6', hash=324584912)


class StarsInShadow(RollDefinition):
    """
    Solar Pulse Rifle, High-Impact Frame, Anti-Unstoppable
    Source: Lord Shaxx
    https://www.light.gg/db/items/3602242905
    https://destiny.report/w/3602242905
    """
    item = Item('Stars In Shadow', hash=3602242905)
    rolls = [
        Roll(
            'Super roll',
            [barrel.PolygonalRifling, AnyPerk],
            [magazine.AccurizedRounds],
            [trait.HealClip],
            [trait.KeepAway],
            [trait.Headseeker],
            [trait.KillClip],
            ),
        Roll(
            'PvP',
            [barrel.PolygonalRifling, AnyPerk],
            [magazine.AccurizedRounds],
            [trait.KeepAway],
            [trait.Headseeker, trait.KillClip],
            ),
        Roll(
            'Clip combo',
            [barrel.PolygonalRifling, AnyPerk],
            [magazine.AccurizedRounds],
            [trait.HealClip],
            [trait.KillClip],
            ),
        ]
