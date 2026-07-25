from wishlist import *


class UncivilDiscourse(RollDefinition):
    """
    Arc Hand Cannon, Dynamic Heat Weapon, Anti-Overload
    Source: Lawless Frontier
    https://www.light.gg/db/items/3146657389
    https://destiny.report/w/3146657389
    """
    items = [
        Item('Uncivil Discourse', hash=3146657389),
        Item('Uncivil Discourse', hash=2462965802),
        ]
    rolls = [
        Roll(
            'Super roll',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.AirTrigger],
            [trait.LoneWolf],
            [trait.CoolingBaubles],
            [trait.JoltingFeedback],
            [trait.PrecisionInstrument],
            [trait.OpeningShot],
            ),
        Roll(
            """
            Miniboss damage.
            Accelerated Assault with 130 Heat Gen and 100 Cooling Efficiency
            allows to shoot 14 rounds before overheating.
            With 120 Heat Gen it allows to shoot 15 instead.
            """,
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.AirTrigger, trait.CoolingBaubles],
            [trait.JoltingFeedback, trait.PrecisionInstrument],
            ),
        Roll(
            'PvP',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.LoneWolf],
            [trait.JoltingFeedback],
            [trait.OpeningShot],
            ),
        ]
