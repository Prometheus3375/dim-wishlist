from wishlist import *
from . import *


class DawnFarOff(RollDefinition):
    """
    Solar Machine Gun, Aggressive Frame, Anti-Unstoppable
    Source: Solstice
    https://www.light.gg/db/items/1484294659
    https://destiny.report/w/1484294659
    """
    items = [
        Item('Dawn Far Off', hash=1484294659),
        Item('Dawn Far Off', hash=2770617440),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            flared_mag,
            [trait.BurningAmbition],
            [trait.ImpromptuAmmunition],
            [trait.AttritionOrbs],
            [trait.Incandescent],
            [trait.Redirection],
            [trait.Meganeura],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            flared_mag,
            [trait.ImpromptuAmmunition],
            [trait.Incandescent, trait.Redirection],
            ),
        Roll(
            'Solar combo',
            default_barrels,
            flared_mag,
            [trait.BurningAmbition],
            [trait.Incandescent],
            ),
        ]


class FixedOdds(RollDefinition):
    """
    Solar Machine Gun, High-Impact Frame, Anti-Unstoppable, Craftable
    Source: Dungeon "Duality"
    https://www.light.gg/db/items/2194955522
    https://destiny.report/w/2194955522
    """
    item = Item('Fixed Odds', hash=2194955522)
    roll = Roll(
        'Solar combo',
        default_barrels,
        appended_mag,
        [trait.FieldPrep],
        [trait.Incandescent],
        )


class Speleologist(RollDefinition):
    """
    Solar Machine Gun, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Exotic mission "Encore"
    https://www.light.gg/db/items/412251536
    https://destiny.report/w/412251536
    """
    item = Item('Speleologist', hash=412251536)


class TemporalClause(RollDefinition):
    """
    Solar Machine Gun, Aggressive Frame, Anti-Unstoppable
    Source: Nessus, Unstable Centaur
    https://www.light.gg/db/items/3132669561
    https://destiny.report/w/3132669561
    """
    item = Item('Temporal Clause', hash=3132669561)


class ThermalErosion(RollDefinition):
    """
    Solar Machine Gun, Rapid-Fire Frame, Anti-Overload
    Source: Europa
    https://www.light.gg/db/items/642545454
    https://destiny.report/w/642545454
    """
    item = Item('Thermal Erosion', hash=642545454)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            appended_mag,
            [trait.Incandescent],
            [trait.FeedingFrenzy],
            [trait.Demolitionist],
            [trait.BurningAmbition],
            [trait.MegaKillClip],
            [trait.Meganeura],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            appended_mag,
            [trait.Incandescent],
            [trait.Meganeura, trait.MegaKillClip],
            ),
        Roll(
            'Solar combo',
            default_barrels,
            appended_mag,
            [trait.Incandescent],
            [trait.BurningAmbition],
            ),
        ]


class UnwaveringDuty(RollDefinition):
    """
    Solar Machine Gun, Adaptive Frame, Anti-Barrier
    Source: Saint-14
    https://www.light.gg/db/items/3489054606
    https://destiny.report/w/3489054606
    """
    item = Item('Unwavering Duty', hash=3489054606)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            flared_mag,
            [trait.Incandescent],
            [trait.Rampage],
            [trait.BurningAmbition],
            [trait.KillingTally],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            flared_mag,
            [trait.Incandescent, trait.Rampage],
            [trait.KillingTally],
            ),
        Roll(
            'Solar combo',
            default_barrels,
            flared_mag,
            [trait.Incandescent],
            [trait.BurningAmbition],
            ),
        ]
