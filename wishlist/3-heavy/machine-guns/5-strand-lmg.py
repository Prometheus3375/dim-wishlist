from wishlist import *


class CircularLogic(RollDefinition):
    """
    Strand Machine Gun, Adaptive Frame, Anti-Barrier
    Source: Terminal Overload
    https://www.light.gg/db/items/2528793321
    https://destiny.report/w/2528793321
    """
    item = Item('Circular Logic', hash=2528793321)


class DIABLERETS06(RollDefinition):
    """
    Strand Machine Gun, Rapid-Fire Frame, Anti-Overload
    Source: Distortions
    https://www.light.gg/db/items/1120206506
    https://destiny.report/w/1120206506
    """
    item = Item('DIABLERETS 06', hash=1120206506)


class ProMemoria(RollDefinition):
    """
    Strand Machine Gun, Aggressive Frame, Anti-Unstoppable, Craftable
    Source: The Pale Heart
    https://www.light.gg/db/items/3605603507
    https://destiny.report/w/3605603507
    """
    item = Item('Pro Memoria', hash=3605603507)


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
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.AppendedMag, AnyPerk],
            [trait.Hatchling, trait.Demolitionist],
            [trait.Meganeura, trait.KillingTally, trait.Tear],
            ),
        ]
