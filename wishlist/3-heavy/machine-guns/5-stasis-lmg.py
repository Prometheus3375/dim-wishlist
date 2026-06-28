from wishlist import *


class UlteriorObservation(RollDefinition):
    """
    Stasis Machine Gun, Aggressive Frame, Anti-Unstoppable
    Source: Exploring Kepler
    https://www.light.gg/db/items/1079872540
    https://destiny.report/w/1079872540
    """
    item = Item('Ulterior Observation', hash=1079872540)
    rolls = [
        Roll(
            'Stasis combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.AppendedMag, AnyPerk],
            [trait.Headstone],
            [trait.Rimestealer],
            ),
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.AppendedMag, AnyPerk],
            [trait.Subsistence, trait.Headstone],
            [trait.KillingTally],
            ),
        ]
