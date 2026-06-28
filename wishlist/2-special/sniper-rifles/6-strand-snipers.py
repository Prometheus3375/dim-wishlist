from wishlist import *


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
    Source: "The Desert Perpetual" Raid
    https://www.light.gg/db/items/688593230
    https://destiny.report/w/688593230
    """
    item = Item('Lance Ephemeral', hash=688593230)
    rolls = [
        Roll(
            'Damage dealing',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.RewindRounds, trait.FourthTimesTheCharm],
            [trait.BaitAndSwitch, trait.Redirection, trait.ElementalHoning],
            ),
        ]


class NaeemsLance(RollDefinition):
    """
    Strand Sniper Rifle, Rapid-Fire Frame, Anti-Overload
    Source: "Warlord's Ruin" Dungeon
    https://www.light.gg/db/items/4119503981
    https://destiny.report/w/4119503981
    """
    item = Item("Naeem's Lance", hash=4119503981)
