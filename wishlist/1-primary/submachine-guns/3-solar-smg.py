from wishlist import *
from . import *


class CALUSMiniTool(RollDefinition):
    """
    Solar Submachine Gun, MIDA Synergy, Anti-Overload, Craftable
    Source: Exotic mission "Presage"
    https://www.light.gg/db/items/2490988246
    https://destiny.report/w/2490988246
    """
    item = Item('CALUS Mini-Tool', hash=2490988246)
    roll = Roll(
        'Ad clear',
        [barrel.ArrowheadBrake, AnyPerk],
        default_mags,
        [trait.ThreatDetector],
        [trait.Incandescent],
        )


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
    Source: Banshee-44; Tenet of Bravery
    https://www.light.gg/db/items/3946054154
    https://destiny.report/w/3946054154
    """
    item = Item('MIDA Mini-Tool', hash=3946054154)
    roll = Roll(
        'Solar combo',
        [barrel.ArrowheadBrake, AnyPerk],
        default_mags,
        [trait.HealClip],
        [trait.Incandescent],
        )


class NoSurvivors(RollDefinition):
    """
    Solar Submachine Gun, Aggressive Frame, Anti-Unstoppable
    Source: Dungeon "Ghosts of the Deep"
    https://www.light.gg/db/items/3625452995
    https://destiny.report/w/3625452995
    """
    item = Item('No Survivors', hash=3625452995)
    rolls = [
        Roll(
            'Super roll',
            [barrel.ChamberedCompensator, AnyPerk],
            default_mags,
            [trait.HealClip],
            [trait.BurningAmbition],
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            [trait.Incandescent],
            ),
        Roll(
            'Solar combo',
            [barrel.ChamberedCompensator, AnyPerk],
            default_mags,
            [trait.HealClip, trait.BurningAmbition],
            [trait.Incandescent],
            ),
        Roll(
            'Grenade combo',
            [barrel.ChamberedCompensator, AnyPerk],
            default_mags,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        ]


class Parabellum(RollDefinition):
    """
    Solar Submachine Gun, Adaptive Frame, Anti-Barrier
    Source: European Dead Zone
    https://www.light.gg/db/items/3769072067
    https://destiny.report/w/3769072067
    """
    item = Item('Parabellum', hash=3769072067)
    roll = Roll(
        'Solar combo',
        [barrel.ArrowheadBrake, AnyPerk],
        default_mags,
        [trait.HealClip],
        [trait.Incandescent],
        )


class PerfectPitch(RollDefinition):
    """
    Solar Submachine Gun, Precision Frame, Anti-Barrier
    Source: Solo Ops
    https://www.light.gg/db/items/2191451996
    https://destiny.report/w/2191451996
    """
    item = Item('Perfect Pitch', hash=2191451996)
    roll = Roll(
        'Solar combo',
        [barrel.ArrowheadBrake, AnyPerk],
        default_mags,
        [trait.HealClip],
        [trait.Incandescent],
        )


class YeartideApex(RollDefinition):
    """
    Solar Submachine Gun, Lightweight Frame, Anti-Overload
    Source: Solstice
    https://www.light.gg/db/items/3293207827
    https://destiny.report/w/3293207827
    """
    items = [
        Item('Yeartide Apex', hash=3293207827),
        Item('Yeartide Apex', hash=2965080304),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.HealClip],
            [trait.Demolitionist],
            [trait.Incandescent],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Solar combo',
            default_barrels,
            default_mags,
            [trait.HealClip],
            [trait.Incandescent],
            ),
        ]
