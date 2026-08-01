from wishlist import *
from . import *


class CircularLogic(RollDefinition):
    """
    Strand Machine Gun, Adaptive Frame, Anti-Barrier
    Source: Terminal Overload
    https://www.light.gg/db/items/2528793321
    https://destiny.report/w/2528793321
    """
    item = Item('Circular Logic', hash=2528793321)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            flared_mag,
            [trait.AmbitiousAssassin],
            [trait.Firefly],
            [trait.MegaKillClip],
            [trait.Hatchling],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            flared_mag,
            [trait.AmbitiousAssassin],
            [trait.MegaKillClip],
            ),
        Roll(
            'Precision combo',
            default_barrels,
            flared_mag,
            [trait.Firefly],
            [trait.Hatchling],
            ),
        ]


class DIABLERETS06(RollDefinition):
    """
    Strand Machine Gun, Rapid-Fire Frame, Anti-Overload
    Source: Distortions
    https://www.light.gg/db/items/1120206506
    https://destiny.report/w/1120206506
    """
    item = Item('DIABLERETS 06', hash=1120206506)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            appended_mag,
            [trait.Hatchling],
            [trait.Subsistence],
            [trait.AttritionOrbs],
            [trait.Meganeura],
            [trait.Redirection],
            [trait.KillingTally],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            appended_mag,
            [trait.Hatchling],
            [trait.Redirection],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            appended_mag,
            [trait.Subsistence],
            [trait.KillingTally],
            ),
        Roll(
            'Precision combo',
            default_barrels,
            appended_mag,
            [trait.Hatchling],
            [trait.Meganeura],
            ),
        ]


class ProMemoria(RollDefinition):
    """
    Strand Machine Gun, Aggressive Frame, Anti-Unstoppable, Craftable
    Source: The Pale Heart
    https://www.light.gg/db/items/3605603507
    https://destiny.report/w/3605603507
    """
    item = Item('Pro Memoria', hash=3605603507)
    Roll(
        'Precision combo',
        default_barrels,
        flared_mag,
        [trait.Hatchling],
        [trait.MegaKillClip],
        )


class QuaVinctusIV(RollDefinition):
    """
    Strand Machine Gun, High-Impact Frame, Anti-Unstoppable
    Source: Crucible
    https://www.light.gg/db/items/337893613
    https://destiny.report/w/337893613
    """
    items = [
        Item('Qua Vinctus IV', hash=337893613),
        Item('Qua Vinctus IV', hash=4176551594),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            appended_mag,
            [trait.Hatchling],
            [trait.Demolitionist],
            [trait.Meganeura],
            [trait.KillingTally],
            ),
        Roll(
            'Precision combo',
            default_barrels,
            appended_mag,
            [trait.Hatchling],
            [trait.Meganeura],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            appended_mag,
            [trait.Hatchling],
            [trait.KillingTally],
            ),
        ]
