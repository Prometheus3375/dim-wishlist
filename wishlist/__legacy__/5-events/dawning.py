from wishlist import *


class Glacioclasm(RollDefinition):
    """
    Void Fusion Rifle, High-Impact Frame
    https://www.light.gg/db/items/1183116657
    """
    item = Item('Glacioclasm', hash=1183116657)
    rolls = [
        Roll(
            """
            Ad clear.
            Reservoir Burst increases mag size to 7 and with Enhanced battery to 8 (max),
            but better to use just Reservoir Burst for one more empowered shot.
            """,
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.LiquidCoils, AnyPerk],
            [trait.Subsistence, trait.Overflow, trait.EnviousAssassin],
            [trait.ReservoirBurst],
            ),
        Roll(
            'Damage dealing. Enhanced Battery + Backup Mag mod give mag size of 8 (max)',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.EnhancedBattery, AnyPerk],
            [trait.EnviousAssassin, trait.Overflow],
            [trait.ControlledBurst],
            [origin.OmolonFluidDynamics],
            ),
        Roll(
            'PvP',
            [barrel.Smallbore, barrel.ExtendedBarrel, barrel.ArrowheadBrake],
            [battery.ProjectionFuse],
            [trait.UnderPressure],
            [trait.ClosingTime, trait.HighImpactReserves],
            ),
        ]
