from wishlist import *
from . import *


class Drang(RollDefinition):
    """
    Solar Sidearm, Together Forever, Anti-Barrier
    Source: Banshee-44; Tenet of Bravery
    https://www.light.gg/db/items/358190158
    https://destiny.report/w/358190158
    """
    item = Item('Drang', hash=358190158)
    roll = Roll(
        'Solar combo',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.TacticalMag, AnyPerk],
        [trait.HealClip],
        [trait.Incandescent],
        )


class DrangBaroque(RollDefinition):
    """
    Solar Sidearm, Together Forever, Anti-Barrier, Craftable
    Source: Exotic mission "Presage"
    https://www.light.gg/db/items/502356570
    https://destiny.report/w/502356570
    """
    item = Item('Drang (Baroque)', hash=502356570)


class EveningSI4(RollDefinition):
    """
    Solar Sidearm, Adaptive Burst, Anti-Barrier
    Source: Commander Zavala; Tenet of Bravery
    https://www.light.gg/db/items/1763361847
    https://destiny.report/w/1763361847
    """
    items = [
        Item('Evening SI4', hash=1763361847),
        Item('Evening SI4', hash=3618823368),
        ]
    rolls = [
        Roll(
            'Super roll',
            [barrel.ExtendedBarrel, AnyPerk],
            default_mags,
            [trait.HealClip],
            [trait.ImpromptuAmmunition],
            [trait.Incandescent],
            ),
        Roll(
            'Solar combo',
            [barrel.ExtendedBarrel, AnyPerk],
            default_mags,
            [trait.HealClip],
            [trait.Incandescent],
            ),
        ]


class HeliocentricQSc(RollDefinition):
    """
    Solar Sidearm, Lightweight Frame, Anti-Overload
    Source: World
    https://www.light.gg/db/items/1291040555
    https://destiny.report/w/1291040555
    """
    items = [
        Item('Heliocentric QSc', hash=1291040555),
        Item('Heliocentric QSc', hash=3998080529),
        ]
    rolls = [
        Roll(
            'Super roll',
            [barrel.ExtendedBarrel, AnyPerk],
            default_mags,
            [trait.HealClip],
            [trait.Demolitionist],
            [trait.Incandescent],
            [trait.AdrenalineJunkie],
            ),
        Roll(
            'Solar combo',
            [barrel.ExtendedBarrel, AnyPerk],
            default_mags,
            [trait.HealClip],
            [trait.Incandescent],
            ),
        Roll(
            'Grenade combo',
            [barrel.ExtendedBarrel, AnyPerk],
            default_mags,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        ]


class PunchingOut(RollDefinition):
    """
    Solar Sidearm, Rapid-Fire Frame, Anti-Overload
    Source: Fireteam Ops
    https://www.light.gg/db/items/1469372193
    https://destiny.report/w/1469372193
    """
    items = [
        Item('Punching Out', hash=1469372193),
        Item('Punching Out', hash=1409524486),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            [barrel.ExtendedBarrel, AnyPerk],
            default_mags,
            [trait.Overflow],
            [trait.HealClip],
            [trait.Demolitionist],
            [trait.Meganeura],
            [trait.Incandescent],
            [trait.AdrenalineJunkie],
            ),
        Roll(
            'Solar combo',
            [barrel.ExtendedBarrel, AnyPerk],
            default_mags,
            [trait.HealClip],
            [trait.Incandescent],
            ),
        Roll(
            'Grenade combo',
            [barrel.ExtendedBarrel, AnyPerk],
            default_mags,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        ]
