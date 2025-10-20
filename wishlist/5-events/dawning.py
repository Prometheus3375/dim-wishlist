from wishlist import *


class StayFrosty(RollDefinition):
    """
    Stasis Pulse Rifle, Lightweight Frame
    https://www.light.gg/db/items/1123433952
    """
    item = Item('Stay Frosty', hash=1123433952)
    roll = Roll(
        'Stasis combo',
        [barrel.ArrowheadBrake, AnyPerk],
        [
            magazine.TacticalMag,
            magazine.AppendedMag,
            magazine.AlloyMagazine,
            magazine.FlaredMagwell,
            ],
        [trait.Rimestealer],
        [trait.Headstone],
        )


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


class MistralLift(RollDefinition):
    """
    Void Linear Fusion Rifle, Adaptive Burst
    https://www.light.gg/db/items/3483485727
    """
    item = Item('Mistral Lift', hash=3483485727)
    roll = Roll(
        'Damage dealing',
        [barrel.ArrowheadBrake, AnyPerk],
        [battery.AcceleratedCoils, AnyPerk],
        [
            trait.EnviousArsenal,
            trait.EnviousAssassin,
            trait.Reconstruction,
            trait.WitheringGaze,
            ],
        [trait.BaitAndSwitch],
        [origin.VeistStinger],
        )


class Zephyr(RollDefinition):
    """
    Stasis Sword, Adaptive Frame
    https://www.light.gg/db/items/601948197
    """
    item = Item('Zephyr', hash=601948197)
    rolls = [
        Roll(
            'Damage dealing',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.RelentlessStrikes, trait.AttritionOrbs],
            [trait.WhirlwindBlade, trait.Surrounded],
            ),
        Roll(
            """
            Cold Steel.
            Rimestealer requires destroying a frozen target or a Stasis crystal
            which hard to achieve with Cold Steel
            """,
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.RelentlessStrikes, trait.AttritionOrbs],
            [trait.ColdSteel],
            ),
        Roll(
            'Ad clear',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.TirelessBlade, trait.RelentlessStrikes],
            [trait.ChainReaction],
            ),
        ]
