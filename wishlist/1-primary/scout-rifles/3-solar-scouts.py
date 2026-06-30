from wishlist import *


class AdmetusD(RollDefinition):
    """
    Solar Scout Rifle, High-Impact Frame, Anti-Unstoppable
    Source: Banshee-44
    https://www.light.gg/db/items/3156551029
    https://destiny.report/w/3156551029
    """
    item = Item('Admetus-D', hash=3156551029)


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
            'PvE',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
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


class VisionOfConfluence(RollDefinition):
    """
    Solar Scout Rifle, Precision Frame, Anti-Barrier, Craftable
    Source: Vault of Glass
    https://www.light.gg/db/items/3444688218
    https://destiny.report/w/3444688218
    """
    items = [
        Item('Vision of Confluence', hash=3444688218),
        Item('Vision of Confluence (Timelost)', hash=337578911),
        ]
