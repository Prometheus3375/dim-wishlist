from wishlist import *
from . import *


class DoomedPetitioner(RollDefinition):
    """
    Void Linear Fusion Rifle, Adaptive Burst, Anti-Barrier, Craftable
    Source: Exotic mission "Starcrossed"
    https://www.light.gg/db/items/1501688142
    https://destiny.report/w/1501688142
    """
    item = Item('Doomed Petitioner', hash=1501688142)
    roll = Roll(
        'Damage dealing',
        default_barrels,
        [battery.EnhancedBattery, AnyPerk],
        [trait.EnviousAssassin],
        [trait.PrecisionInstrument],
        )


class EyesUnveiled(RollDefinition):
    """
    Void Linear Fusion Rifle, Precision Frame, Anti-Barrier
    Source: Dungeon "Pit of Heresy"
    https://www.light.gg/db/items/4147428506
    https://destiny.report/w/4147428506
    """
    item = Item('Eyes Unveiled', hash=4147428506)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            [battery.EnhancedBattery, AnyPerk],
            [trait.FourthTimesTheCharm],
            [trait.MegaKillClip],
            [trait.PrecisionInstrument],
            [trait.ElementalHoning],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            [battery.EnhancedBattery, AnyPerk],
            [trait.FourthTimesTheCharm, trait.MegaKillClip],
            [trait.PrecisionInstrument, trait.ElementalHoning],
            ),
        ]


class MistralLift(RollDefinition):
    """
    Void Linear Fusion Rifle, Adaptive Burst, Anti-Barrier
    Source: The Dawning
    https://www.light.gg/db/items/766122634
    https://destiny.report/w/766122634
    """
    items = [
        Item('Mistral Lift', hash=766122634),
        Item('Mistral Lift', hash=270610849),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_batteries,
            [trait.EnviousArsenal],
            [trait.Overflow],
            [trait.BaitAndSwitch],
            [trait.PrecisionInstrument],
            [origin.VeistStinger],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_batteries,
            [trait.Overflow, trait.EnviousArsenal],
            [trait.BaitAndSwitch, trait.PrecisionInstrument],
            [origin.VeistStinger],
            ),
        ]


class Taipan4fr(RollDefinition):
    """
    Void Linear Fusion Rifle, Precision Frame, Anti-Barrier, Craftable
    Source: Quest "Foundry Resonance"
    https://www.light.gg/db/items/1911060537
    https://destiny.report/w/1911060537
    """
    item = Item('Taipan-4fr', hash=1911060537)
    roll = Roll(
        'Damage dealing',
        default_barrels,
        default_batteries,
        [trait.TripleTap],
        [trait.FiringLine],
        )
