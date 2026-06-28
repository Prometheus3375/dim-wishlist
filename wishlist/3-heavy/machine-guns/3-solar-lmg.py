from wishlist import *


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


class TemporalClause(RollDefinition):
    """
    Solar Machine Gun, Aggressive Frame, Anti-Unstoppable
    Source: Unspecified
    https://www.light.gg/db/items/3132669561
    https://destiny.report/w/3132669561
    """
    item = Item('Temporal Clause', hash=3132669561)


class ThermalErosion(RollDefinition):
    """
    Solar Machine Gun, Rapid-Fire Frame, Anti-Overload
    Source: Unspecified
    https://www.light.gg/db/items/642545454
    https://destiny.report/w/642545454
    """
    item = Item('Thermal Erosion', hash=642545454)


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
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.AppendedMag, AnyPerk],
            [trait.Incandescent, trait.Rampage, trait.Incandescent],
            [trait.KillingTally],
            ),
        Roll(
            'Solar combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.AppendedMag, AnyPerk],
            [trait.Incandescent],
            [trait.BurningAmbition],
            ),
        ]
