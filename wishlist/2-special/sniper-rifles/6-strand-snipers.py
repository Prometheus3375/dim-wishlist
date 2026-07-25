from wishlist import *
from . import *


class ALLEN05(RollDefinition):
    """
    Strand Sniper Rifle, Adaptive Frame, Anti-Barrier
    Source: Distortions
    https://www.light.gg/db/items/423677697
    https://destiny.report/w/423677697
    """
    item = Item('ALLEN 05', hash=423677697)


class LanceEphemeral(RollDefinition):
    """
    Strand Sniper Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Raid "The Desert Perpetual"
    https://www.light.gg/db/items/688593230
    https://destiny.report/w/688593230
    """
    item = Item('Lance Ephemeral', hash=688593230)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.FourthTimesTheCharm],
            [trait.RewindRounds],
            [trait.BaitAndSwitch],
            [trait.Deconstruct],
            [trait.ElementalHoning],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.FourthTimesTheCharm, trait.RewindRounds],
            [trait.BaitAndSwitch, trait.ElementalHoning],
            ),
        ]


class NaeemsLance(RollDefinition):
    """
    Strand Sniper Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Dungeon "Warlord's Ruin"
    https://www.light.gg/db/items/4119503981
    https://destiny.report/w/4119503981
    """
    item = Item("Naeem's Lance", hash=4119503981)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Deconstruct],
            [trait.RewindRounds],
            [trait.ElementalHoning],
            [trait.PrecisionInstrument],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.RewindRounds],
            [trait.PrecisionInstrument, trait.ElementalHoning],
            ),
        ]


class VoltaBracket(RollDefinition):
    """
    Strand Sniper Rifle, Aggressive Frame, Anti-Unstoppable, Craftable
    Source: Neomuna
    https://www.light.gg/db/items/3920310144
    https://destiny.report/w/3920310144
    """
    item = Item('Volta Bracket', hash=3920310144)
    roll = Roll(
        'Sniper spam',
        default_barrels,
        default_mags,
        [trait.TripleTap],
        [trait.RewindRounds],
        )
