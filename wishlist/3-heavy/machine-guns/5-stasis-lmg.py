from wishlist import *


class ArchonsThunder(RollDefinition):
    """
    Stasis Machine Gun, High-Impact Frame, Anti-Unstoppable
    Source: Lord Saladin
    https://www.light.gg/db/items/91672792
    https://destiny.report/w/91672792
    """
    item = Item("Archon's Thunder", hash=91672792)


class ChainOfCommand(RollDefinition):
    """
    Stasis Machine Gun, Adaptive Frame, Anti-Barrier
    Source: Solo Ops
    https://www.light.gg/db/items/1716620044
    https://destiny.report/w/1716620044
    """
    item = Item('Chain of Command', hash=1716620044)


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
