from wishlist import *
from . import *


class ArchonsThunder(RollDefinition):
    """
    Stasis Machine Gun, High-Impact Frame, Anti-Unstoppable
    Source: Lord Saladin
    https://www.light.gg/db/items/91672792
    https://destiny.report/w/91672792
    """
    items = [
        Item("Archon's Thunder", hash=91672792),
        Item("Archon's Thunder", hash=2896109856),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            appended_mag,
            [trait.AirTrigger],
            [trait.Rimestealer],
            [trait.Headstone],
            ),
        Roll(
            'Stasis combo',
            default_barrels,
            appended_mag,
            [trait.Rimestealer],
            [trait.Headstone],
            ),
        ]


class ChainOfCommand(RollDefinition):
    """
    Stasis Machine Gun, Adaptive Frame, Anti-Barrier
    Source: Solo Ops
    https://www.light.gg/db/items/1716620044
    https://destiny.report/w/1716620044
    """
    item = Item('Chain of Command', hash=1716620044)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            flared_mag,
            [trait.AdrenalineJunkie],
            [trait.Overflow],
            [trait.Headstone],
            [trait.Demolitionist],
            [trait.KillingTally],
            [trait.Meganeura],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            flared_mag,
            [trait.Overflow, trait.AdrenalineJunkie],
            [trait.KillingTally],
            ),
        Roll(
            'Precision combo',
            default_barrels,
            flared_mag,
            [trait.Headstone],
            [trait.Meganeura],
            ),
        Roll(
            'Grenade combo',
            default_barrels,
            flared_mag,
            [trait.AdrenalineJunkie],
            [trait.Demolitionist],
            ),
        ]


class QullimsTerminus(RollDefinition):
    """
    Stasis Machine Gun, High-Impact Frame, Anti-Unstoppable, Craftable
    Source: Raid "King's Fall"
    https://www.light.gg/db/items/1321506184
    https://destiny.report/w/1321506184
    """
    items = [
        Item("Qullim's Terminus", hash=1321506184),
        Item("Qullim's Terminus (Harrowed)", hash=3248429089),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            appended_mag,
            [trait.Unrelenting],
            [trait.CrystallineCorpsebloom],
            [trait.MegaKillClip],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            appended_mag,
            [trait.Unrelenting],
            [trait.CrystallineCorpsebloom, trait.MegaKillClip],
            ),
        ]


class RecurrentImpact(RollDefinition):
    """
    Stasis Machine Gun, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Exotic mission "Vox Obscura"
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
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            appended_mag,
            [trait.Subsistence],
            [trait.Headstone],
            [trait.Rimestealer],
            [trait.KillingTally],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            appended_mag,
            [trait.Subsistence, trait.Headstone],
            [trait.KillingTally],
            ),
        Roll(
            'Stasis combo',
            default_barrels,
            appended_mag,
            [trait.Headstone],
            [trait.Rimestealer],
            ),
        ]
