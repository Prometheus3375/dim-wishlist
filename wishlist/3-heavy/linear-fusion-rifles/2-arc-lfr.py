from wishlist import *


class Boomslang4FR(RollDefinition):
    """
    Arc Linear Fusion Rifle, Adaptive Burst, Anti-Barrier
    Source: Commander Zavala
    https://www.light.gg/db/items/3926153598
    https://destiny.report/w/3926153598
    """
    item = Item('Boomslang-4FR', hash=3926153598)
    roll = Roll(
        'Damage dealing',
        [barrel.ArrowheadBrake, AnyPerk],
        [battery.AcceleratedCoils, AnyPerk],
        [trait.EnviousArsenal, trait.RapidHit],
        [trait.PrecisionInstrument],
        )


class SailspyPitchglass(RollDefinition):
    """
    Arc Linear Fusion Rifle, Precision Frame, Anti-Barrier, Craftable
    Source: Xûr
    https://www.light.gg/db/items/1184309824
    https://destiny.report/w/1184309824
    """
    item = Item('Sailspy Pitchglass', hash=1184309824)


class Stormchaser(RollDefinition):
    """
    Arc Linear Fusion Rifle, Adaptive Burst, Anti-Barrier
    Source: Dungeon "Duality"
    https://www.light.gg/db/items/2862666249
    https://destiny.report/w/2862666249
    """
    item = Item('Stormchaser', hash=2862666249)


class WillfulHamartia(RollDefinition):
    """
    Arc Linear Fusion Rifle, Adaptive Burst, Anti-Barrier
    Source: Trials of Osiris
    https://www.light.gg/db/items/1952295804
    https://destiny.report/w/1952295804
    """
    item = Item('Willful Hamartia', hash=1952295804)
