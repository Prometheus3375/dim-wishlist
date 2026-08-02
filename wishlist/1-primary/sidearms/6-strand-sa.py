from wishlist import *
from . import *


class Breachlight(RollDefinition):
    """
    Strand Sidearm, Heavy Burst, Anti-Unstoppable, Legacy
    Source: Xûr
    https://www.light.gg/db/items/2328923181
    https://destiny.report/w/2328923181
    """
    item = Item('Breachlight', hash=2328923181)
    rolls = [
        Roll(
            'Hatchling',
            [barrel.ArrowheadBrake, AnyPerk],
            default_mags,
            [trait.Pugilist, trait.Demolitionist, trait.ThreatDetector],
            [trait.Hatchling],
            ),
        Roll(
            """
            Desperate Measures.
            For this weapon Desperate Measures is better than Swashbuckler and Adrenaline Junkie
            because DM can be activated while stowed and lasts longer.
            """,
            [barrel.ArrowheadBrake, AnyPerk],
            default_mags,
            [trait.Pugilist, trait.Demolitionist, trait.ThreatDetector],
            [trait.DesperateMeasures],
            ),
        ]


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
