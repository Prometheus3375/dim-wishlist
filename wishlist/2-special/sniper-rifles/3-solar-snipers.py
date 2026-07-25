from wishlist import *
from . import *


class Beloved(RollDefinition):
    """
    Solar Sniper Rifle, Adaptive Frame, Anti-Barrier, Craftable
    Source: Exotic mission "Presage"
    https://www.light.gg/db/items/3107853529
    https://destiny.report/w/3107853529
    """
    item = Item('Beloved', hash=3107853529)


class IKELOS_SR_v103(RollDefinition):
    """
    Solar Sniper Rifle, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Exotic mission "Seraph's Shield"
    https://www.light.gg/db/items/2302346155
    https://destiny.report/w/2302346155
    """
    item = Item('IKELOS_SR_v1.0.3', hash=2302346155)
    roll = Roll(
        'Damage dealing',
        default_barrels,
        default_mags,
        [trait.FourthTimesTheCharm],
        [trait.FocusedFury],
        )


class KeenThistle(RollDefinition):
    """
    Solar Sniper Rifle, Aggressive Frame, Anti-Unstoppable
    Source: Trials of Osiris
    https://www.light.gg/db/items/2499834164
    https://destiny.report/w/2499834164
    """
    item = Item('Keen Thistle', hash=2499834164)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.EnviousArsenal],
            [trait.TripleTap],
            [trait.BaitAndSwitch],
            [trait.FourthTimesTheCharm],
            [trait.ElementalHoning],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.TripleTap, trait.EnviousArsenal],
            [trait.BaitAndSwitch, trait.ElementalHoning],
            ),
        Roll(
            'Sniper spam',
            default_barrels,
            default_mags,
            [trait.TripleTap],
            [trait.FourthTimesTheCharm],
            ),
        ]


class LastForay(RollDefinition):
    """
    Solar Sniper Rifle, Aggressive Frame, Anti-Unstoppable
    Source: European Dead Zone
    https://www.light.gg/db/items/4118936670
    https://destiny.report/w/4118936670
    """
    item = Item('Last Foray', hash=4118936670)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.RewindRounds],
            [trait.EnviousAssassin],
            [trait.PrecisionInstrument],
            [trait.BaitAndSwitch],
            [trait.TripleTap],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.RewindRounds, trait.EnviousAssassin],
            [trait.BaitAndSwitch, trait.PrecisionInstrument],
            ),
        Roll(
            'Sniper spam',
            default_barrels,
            default_mags,
            [trait.RewindRounds],
            [trait.TripleTap],
            ),
        ]


class OmniscientEye(RollDefinition):
    """
    Solar Sniper Rifle, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Raid "Garden of Salvation"
    https://www.light.gg/db/items/147444292
    https://destiny.report/w/147444292
    """
    item = Item('Omniscient Eye', hash=147444292)
    is_chosen = True
    roll = Roll(
        'Damage dealing',
        default_barrels,
        default_mags,
        [trait.FourthTimesTheCharm],
        [trait.PrecisionInstrument],
        )


class TwilightOath(RollDefinition):
    """
    Solar Sniper Rifle, Rapid-Fire Frame, Anti-Overload
    Source: The Dreaming City
    https://www.light.gg/db/items/268357178
    https://destiny.report/w/268357178
    """
    item = Item('Twilight Oath', hash=268357178)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.EnviousAssassin],
            [trait.LuckyShot],
            [trait.PrecisionInstrument],
            [trait.BaitAndSwitch],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.EnviousAssassin, trait.LuckyShot],
            [trait.BaitAndSwitch, trait.PrecisionInstrument],
            ),
        ]


class UzumeRR4(RollDefinition):
    """
    Solar Sniper Rifle, Adaptive Frame, Anti-Barrier
    Source: Commander Zavala
    https://www.light.gg/db/items/4037675261
    https://destiny.report/w/4037675261
    """
    item = Item('Uzume RR4', hash=4037675261)
