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


class QullimsTerminus(RollDefinition):
    """
    Stasis Machine Gun, High-Impact Frame, Anti-Unstoppable, Craftable
    Source: King's Fall
    https://www.light.gg/db/items/1321506184
    https://destiny.report/w/1321506184
    """
    items = [
        Item("Qullim's Terminus", hash=1321506184),
        Item("Qullim's Terminus (Harrowed)", hash=3248429089),
        ]


class RecurrentImpact(RollDefinition):
    """
    Stasis Machine Gun, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Vox Obscura
    https://www.light.gg/db/items/1572896086
    https://destiny.report/w/1572896086
    """
    item = Item('Recurrent Impact', hash=1572896086)


class UlteriorObservation(RollDefinition):
    """
    Stasis Machine Gun, Aggressive Frame, Anti-Unstoppable
    Source: Kepler
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
