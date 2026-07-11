from wishlist import *
from . import *


class MykelsReverence(RollDefinition):
    """
    Strand Sidearm, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Raid "Root of Nightmares"
    https://www.light.gg/db/items/231031173
    https://destiny.report/w/231031173
    """
    items = [
        Item("Mykel's Reverence", hash=231031173),
        Item("Mykel's Reverence (Adept)", hash=1986287028),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.CollectiveDemolition],
            [trait.Slice],
            [trait.Hatchling],
            [trait.ParacausalAffinity],
            ),
        Roll(
            'Strand combo',
            default_barrels,
            default_mags,
            [trait.Slice],
            [trait.Hatchling],
            ),
        ]
