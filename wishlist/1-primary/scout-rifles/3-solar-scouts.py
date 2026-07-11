from wishlist import *
from . import *


class AdmetusD(RollDefinition):
    """
    Solar Scout Rifle, High-Impact Frame, Anti-Unstoppable
    Source: Banshee-44
    https://www.light.gg/db/items/3156551029
    https://destiny.report/w/3156551029
    """
    item = Item('Admetus-D', hash=3156551029)
    roll = Roll(
        'Solar combo',
        default_barrels,
        default_mags,
        [trait.HealClip],
        [trait.Incandescent],
        )


class OxygenSR3(RollDefinition):
    """
    Solar Scout Rifle, Precision Frame, Anti-Barrier
    Source: Commander Zavala
    https://www.light.gg/db/items/4104613038
    https://destiny.report/w/4104613038
    """
    items = [
        Item('Oxygen SR3', hash=4104613038),
        Item('Oxygen SR3', hash=444627789),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.HealClip],
            [trait.ShootToLoot],
            [trait.Meganeura],
            [trait.OneForAll],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.HealClip],
            [trait.Meganeura],
            ),
        ]


class TimewornWayfarer(RollDefinition):
    """
    Solar Scout Rifle, Aggressive Frame, Anti-Unstoppable, Craftable
    Source: Exotic mission "Encore"
    https://www.light.gg/db/items/1058098236
    https://destiny.report/w/1058098236
    """
    item = Item('Timeworn Wayfarer', hash=1058098236)
    is_chosen = True
    roll = Roll(
        'Solar combo',
        default_barrels,
        default_mags,
        [trait.HealClip],
        [trait.Incandescent],
        )


class Trustee(RollDefinition):
    """
    Solar Scout Rifle, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Raid "Deep Stone Crypt"
    https://www.light.gg/db/items/1392919471
    https://destiny.report/w/1392919471
    """
    item = Item('Trustee', hash=1392919471)
    rolls = [
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.Reconstruction],
            [trait.Meganeura, trait.Redirection],
            ),
        Roll(
            'Solar combo',
            default_barrels,
            default_mags,
            [trait.HealClip],
            [trait.Incandescent],
            ),
        ]


class VisionOfConfluence(RollDefinition):
    """
    Solar Scout Rifle, Precision Frame, Anti-Barrier, Craftable
    Source: Raid "Vault of Glass"
    https://www.light.gg/db/items/3444688218
    https://destiny.report/w/3444688218
    """
    items = [
        Item('Vision of Confluence', hash=3444688218),
        Item('Vision of Confluence (Timelost)', hash=337578911),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.HealClip],
            [trait.Incandescent],
            [trait.Firefly],
            [trait.BurningAmbition],
            ),
        Roll(
            'Solar combo',
            default_barrels,
            default_mags,
            [trait.Incandescent],
            [trait.BurningAmbition],
            ),
        Roll(
            'Reload combo',
            default_barrels,
            default_mags,
            [trait.HealClip],
            [trait.Firefly],
            ),
        ]
