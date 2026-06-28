from wishlist import *


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
