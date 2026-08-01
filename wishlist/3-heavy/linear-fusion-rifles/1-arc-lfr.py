from wishlist import *
from . import *


class Boomslang4FR(RollDefinition):
    """
    Arc Linear Fusion Rifle, Adaptive Burst, Anti-Barrier
    Source: Commander Zavala; Tenet of Bravery
    https://www.light.gg/db/items/3926153598
    https://destiny.report/w/3926153598
    """
    item = Item('Boomslang-4FR', hash=3926153598)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.EnviousArsenal],
            [trait.RapidHit],
            [trait.PrecisionInstrument],
            [origin.VeistStinger],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.EnviousArsenal, trait.RapidHit],
            [trait.PrecisionInstrument],
            [origin.VeistStinger],
            ),
        ]


class SailspyPitchglass(RollDefinition):
    """
    Arc Linear Fusion Rifle, Precision Frame, Anti-Barrier, Craftable
    Source: Xûr
    https://www.light.gg/db/items/1184309824
    https://destiny.report/w/1184309824
    """
    item = Item('Sailspy Pitchglass', hash=1184309824)


class Stormchaser(RollDefinition):
    """
    Arc Linear Fusion Rifle, Adaptive Burst, Anti-Barrier
    Source: Dungeon "Duality"
    https://www.light.gg/db/items/2862666249
    https://destiny.report/w/2862666249
    """
    item = Item('Stormchaser', hash=2862666249)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.AutoLoadingHolster],
            [trait.SuperchargedMagazine],
            [trait.JoltingFeedback],
            [trait.GearShift],
            [trait.AggregateCharge],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.JoltingFeedback, trait.SuperchargedMagazine, trait.AutoLoadingHolster],
            [trait.AggregateCharge, trait.GearShift],
            ),
        ]


class WillfulHamartia(RollDefinition):
    """
    Arc Linear Fusion Rifle, Adaptive Burst, Anti-Barrier
    Source: Trials of Osiris
    https://www.light.gg/db/items/1952295804
    https://destiny.report/w/1952295804
    """
    item = Item('Willful Hamartia', hash=1952295804)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.AutoLoadingHolster],
            [trait.SuperchargedMagazine],
            [trait.JoltingFeedback],
            [trait.GearShift],
            [trait.AggregateCharge],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.JoltingFeedback, trait.SuperchargedMagazine, trait.AutoLoadingHolster],
            [trait.AggregateCharge, trait.GearShift],
            ),
        ]


class LineInTheSand(RollDefinition):
    """
    Arc Linear Fusion Rifle, Precision Frame, Anti-Barrier, Legacy
    Source: Xûr
    https://www.light.gg/db/items/2450049485
    https://destiny.report/w/2450049485
    """
    item = Item('Line in the Sand', hash=2450049485)
    is_chosen = True
    roll = Roll(
        'Damage dealing',
        default_barrels,
        [battery.EnhancedBattery, AnyPerk],
        [trait.ClownCartridge, trait.Deconstruct],
        [trait.BaitAndSwitch],
        )
