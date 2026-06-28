from wishlist import *


class UncivilDiscourse(RollDefinition):
    """
    Arc Hand Cannon, Dynamic Heat Weapon, Anti-Overload
    Source: Renegades
    https://www.light.gg/db/items/3146657389
    https://destiny.report/w/3146657389
    """
    items = [
        Item('Uncivil Discourse', hash=3146657389),
        Item('Uncivil Discourse', hash=2462965802),
        ]
    rolls = [
        Roll(
            """
            Damage dealing with Lucky Pants.
            Accelerated Assault with 130 Heat Gen and 100 Cooling Efficiency
            allows to shoot 14 rounds before overheating.
            With 120 Heat Gen it allows to shoot 15 instead.
            """,
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.EnhancedHeatsink, battery.IonizedHeatsink, AnyPerk],
            [trait.AirTrigger, AnyPerk],
            [trait.PrecisionInstrument],
            ),
        ]
