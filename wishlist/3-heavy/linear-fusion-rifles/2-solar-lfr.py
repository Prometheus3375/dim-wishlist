from wishlist import *
from . import *


class BriarsContempt(RollDefinition):
    """
    Solar Linear Fusion Rifle, Adaptive Burst, Anti-Barrier, Craftable
    Source: Raid "Root of Nightmares"
    https://www.light.gg/db/items/1491665733
    https://destiny.report/w/1491665733
    """
    items = [
        Item("Briar's Contempt", hash=1491665733),
        Item("Briar's Contempt (Adept)", hash=2890082420),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.EnviousAssassin],
            [trait.RewindRounds],
            [trait.Surrounded],
            [trait.AggregateCharge],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.EnviousAssassin, trait.RewindRounds],
            [trait.AggregateCharge, trait.Surrounded],
            ),
        ]


class Cataclysmic(RollDefinition):
    """
    Solar Linear Fusion Rifle, Precision Frame, Anti-Barrier, Craftable
    Source: Raid "Vow of the Disciple"
    https://www.light.gg/db/items/999767358
    https://destiny.report/w/999767358
    """
    items = [
        Item('Cataclysmic', hash=999767358),
        Item('Cataclysmic (Adept)', hash=2886339027),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            [battery.EnhancedBattery, AnyPerk],
            [trait.FourthTimesTheCharm],
            [trait.BaitAndSwitch],
            [trait.AggregateCharge],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            [battery.EnhancedBattery, AnyPerk],
            [trait.FourthTimesTheCharm],
            [trait.AggregateCharge, trait.BaitAndSwitch],
            ),
        ]
