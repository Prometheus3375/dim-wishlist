from wishlist import *
from . import *


class IterativeLoop(RollDefinition):
    """
    Arc Fusion Rifle, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Neomuna
    https://www.light.gg/db/items/1289796511
    https://destiny.report/w/1289796511
    """
    item = Item('Iterative Loop', hash=1289796511)


class LoadedQuestion(RollDefinition):
    """
    Arc Fusion Rifle, High-Impact Frame, Anti-Unstoppable
    Source: Commander Zavala
    https://www.light.gg/db/items/852069910
    https://destiny.report/w/852069910
    """
    items = [
        Item('Loaded Question', hash=852069910),
        Item('Loaded Question (Adept)', hash=2914913838),
        Item('Loaded Question', hash=3125454907),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_battery,
            [trait.EnviousAssassin],
            [trait.Demolitionist],
            [trait.ReservoirBurst],
            [trait.ControlledBurst],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_battery,
            [trait.EnviousAssassin],
            [trait.ControlledBurst],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_battery,
            [trait.Demolitionist],
            [trait.ReservoirBurst],
            ),
        ]


class MidhasReckoning(RollDefinition):
    """
    Arc Fusion Rifle, High-Impact Frame, Anti-Unstoppable, Craftable
    Source: Raid "King's Fall"
    https://www.light.gg/db/items/3969066556
    https://destiny.report/w/3969066556
    """
    items = [
        Item("Midha's Reckoning", hash=3969066556),
        Item("Midha's Reckoning (Harrowed)", hash=3904516037),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_battery,
            [trait.Cornered],
            [trait.Voltshot],
            [trait.Surrounded],
            [trait.ReservoirBurst],
            [trait.GearShift],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_battery,
            [trait.Cornered],
            [trait.Surrounded, trait.Surrounded],
            ),
        Roll(
            'Reload combo',
            default_barrels,
            default_battery,
            [trait.Voltshot],
            [trait.ReservoirBurst],
            ),
        ]


class MainIngredient(RollDefinition):
    """
    Arc Fusion Rifle, Precision Frame, Anti-Barrier
    Source: Fireteam Ops
    https://www.light.gg/db/items/4046741099
    https://destiny.report/w/4046741099
    """
    items = [
        Item('Main Ingredient', hash=4046741099),
        Item('Main Ingredient', hash=2901221332),
        ]


class PLUGONE1(RollDefinition):
    """
    Arc Fusion Rifle, Precision Frame, Anti-Barrier
    Source: Commander Zavala
    https://www.light.gg/db/items/852069911
    https://destiny.report/w/852069911
    """
    items = [
        Item('PLUG ONE.1', hash=852069911),
        Item('PLUG ONE.1 (Adept)', hash=3106557243),
        Item('PLUG ONE.1', hash=3293524502),
        ]


class TecheunForce(RollDefinition):
    """
    Arc Fusion Rifle, Adaptive Frame, Anti-Barrier, Craftable
    Source: Raid "Last Wish"
    https://www.light.gg/db/items/3591141932
    https://destiny.report/w/3591141932
    """
    item = Item('Techeun Force', hash=3591141932)


class TemperedDynamo(RollDefinition):
    """
    Arc Fusion Rifle, Aggressive Frame, Anti-Unstoppable
    Source: Arena Ops
    https://www.light.gg/db/items/2274706510
    https://destiny.report/w/2274706510
    """
    items = [
        Item('Tempered Dynamo', hash=2274706510),
        Item('Tempered Dynamo', hash=2925315757),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_battery,
            [trait.RewindRounds],
            [trait.ImpromptuAmmunition],
            [trait.SuperchargedMagazine],
            [trait.JoltingFeedback],
            [trait.Discord],
            [trait.Surrounded],
            ),
        Roll(
            'Arc combo',
            default_barrels,
            default_battery,
            [trait.SuperchargedMagazine],
            [trait.JoltingFeedback],
            ),
        ]


class TheWizenedRebuke(RollDefinition):
    """
    Arc Fusion Rifle, High-Impact Frame, Anti-Unstoppable
    Source: Iron Banner
    https://www.light.gg/db/items/293709641
    https://destiny.report/w/293709641
    """
    item = Item('The Wizened Rebuke', hash=293709641)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            [barrel.HammerForgedRifling, AnyPerk],
            [battery.ProjectionFuse, AnyPerk],
            [trait.UnderPressure],
            [trait.Discord],
            [trait.Overflow],
            [trait.ClosingTime],
            [trait.ControlledBurst],
            [trait.ReservoirBurst],
            ),
        Roll(
            'PvP',
            [barrel.HammerForgedRifling, AnyPerk],
            [battery.ProjectionFuse, AnyPerk],
            [trait.UnderPressure],
            [trait.ClosingTime],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_battery,
            [trait.Overflow],
            [trait.ControlledBurst],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_battery,
            [trait.Discord],
            [trait.ReservoirBurst],
            ),
        ]
