from wishlist import *


class Drang(RollDefinition):
    """
    Solar Sidearm, Together Forever, Anti-Barrier
    Source: Banshee-44
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
    Source: The Derelict Leviathan
    https://www.light.gg/db/items/502356570
    https://destiny.report/w/502356570
    """
    item = Item('Drang (Baroque)', hash=502356570)


class EveningSI4(RollDefinition):
    """
    Solar Sidearm, Adaptive Burst, Anti-Barrier
    Source: Commander Zavala
    https://www.light.gg/db/items/1763361847
    https://destiny.report/w/1763361847
    """
    items = [
        Item('Evening SI4', hash=1763361847),
        Item('Evening SI4', hash=3618823368),
        ]
    rolls = [
        Roll(
            'Solar combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.HealClip],
            [trait.Incandescent],
            ),
        Roll(
            'Impromptu Ammunition',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.ImpromptuAmmunition],
            [trait.Incandescent],
            ),
        # Roll(
        #     'Melee regen',
        #     [barrel.ArrowheadBrake, AnyPerk],
        #     [magazine.FlaredMagwell, AnyPerk],
        #     [trait.HealClip],
        #     [trait.CollectivePugilism],
        #     ),
        ]


class HeliocentricQSc(RollDefinition):
    """
    Solar Sidearm, Lightweight Frame, Anti-Overload
    Source: World
    https://www.light.gg/db/items/1291040555
    https://destiny.report/w/1291040555
    """
    item = Item('Heliocentric QSc', hash=1291040555)


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
