from wishlist import *


class DeathAdder(RollDefinition):
    """
    Solar Submachine Gun, Lightweight Frame, Anti-Overload
    Source: World
    https://www.light.gg/db/items/2130249527
    https://destiny.report/w/2130249527
    """
    item = Item('Death Adder', hash=2130249527)


class MIDAMiniTool(RollDefinition):
    """
    Solar Submachine Gun, MIDA Synergy, Anti-Overload
    Source: Banshee-44
    https://www.light.gg/db/items/3946054154
    https://destiny.report/w/3946054154
    """
    item = Item('MIDA Mini-Tool', hash=3946054154)
    roll = Roll(
        'Solar combo',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.FlaredMagwell, AnyPerk],
        [trait.HealClip],
        [trait.Incandescent],
        )


class NoSurvivors(RollDefinition):
    """
    Solar Submachine Gun, Aggressive Frame, Anti-Unstoppable
    Source: "Ghosts of the Deep" Dungeon
    https://www.light.gg/db/items/3625452995
    https://destiny.report/w/3625452995
    """
    item = Item('No Survivors', hash=3625452995)


class Parabellum(RollDefinition):
    """
    Solar Submachine Gun, Adaptive Frame, Anti-Barrier
    Source: Unspecified
    https://www.light.gg/db/items/3769072067
    https://destiny.report/w/3769072067
    """
    item = Item('Parabellum', hash=3769072067)


class PerfectPitch(RollDefinition):
    """
    Solar Submachine Gun, Precision Frame, Anti-Barrier
    Source: Solo Ops
    https://www.light.gg/db/items/2191451996
    https://destiny.report/w/2191451996
    """
    item = Item('Perfect Pitch', hash=2191451996)
