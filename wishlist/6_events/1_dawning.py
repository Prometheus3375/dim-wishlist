from database import *


class StayFrosty(RollDefinition):
    """
    Stasis Pulse Rifle, Lightweight Frame
    https://www.light.gg/db/items/1123433952
    """
    item = Item(name='Stay Frosty', hash=1123433952)
    roll = Roll(
        'Stasis combo',
        [barrels.ArrowheadBrake, AnyPerk],
        [
            magazines.TacticalMag,
            magazines.AppendedMag,
            magazines.AlloyMagazine,
            magazines.FlaredMagwell,
            ],
        [traits.Rimestealer],
        [traits.Headstone],
        )


class Glacioclasm(RollDefinition):
    """
    Void Fusion Rifle, High-Impact Frame
    https://www.light.gg/db/items/1183116657
    """
    item = Item(name='Glacioclasm', hash=1183116657)
    rolls = [
        Roll(
            """
            Ad clear.
            Reservoir Burst increases mag size to 7 and with Enhanced battery to 8 (max),
            but better to use just Reservoir Burst for one more empowered shot.
            """,
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.LiquidCoils, AnyPerk],
            [traits.Subsistence, traits.Overflow, traits.EnviousAssassin],
            [traits.ReservoirBurst],
            ),
        Roll(
            'Damage dealing. Enhanced Battery + Backup Mag mod give mag size of 8 (max)',
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.EnhancedBattery, AnyPerk],
            [traits.EnviousAssassin, traits.Overflow],
            [traits.ControlledBurst],
            [origin.OmolonFluidDynamics],
            ),
        Roll(
            'PvP',
            [barrels.Smallbore, barrels.ExtendedBarrel, barrels.ArrowheadBrake],
            [batteries.ProjectionFuse],
            [traits.UnderPressure],
            [traits.ClosingTime, traits.HighImpactReserves],
            ),
        ]


class MistralLift(RollDefinition):
    """
    Void Linear Fusion Rifle, Adaptive Burst
    https://www.light.gg/db/items/3483485727
    """
    item = Item(name='Mistral Lift', hash=3483485727)
    roll = Roll(
        'Damage dealing',
        [barrels.ArrowheadBrake, AnyPerk],
        [batteries.AcceleratedCoils, AnyPerk],
        [
            traits.EnviousArsenal,
            traits.EnviousAssassin,
            traits.Reconstruction,
            traits.WitheringGaze,
            ],
        [traits.BaitAndSwitch],
        [origin.VeistStinger],
        )


class Zephyr(RollDefinition):
    """
    Stasis Sword, Adaptive Frame
    https://www.light.gg/db/items/601948197
    """
    item = Item(name='Zephyr', hash=601948197)
    rolls = [
        Roll(
            'Damage dealing',
            [blades.JaggedEdge, AnyPerk],
            [guards.SwordmastersGuard, AnyPerk],
            [traits.RelentlessStrikes, traits.AttritionOrbs],
            [traits.WhirlwindBlade, traits.Surrounded],
            ),
        Roll(
            """
            Cold Steel.
            Rimestealer requires destroying a frozen target or a Stasis crystal
            which hard to achieve with Cold Steel
            """,
            [blades.JaggedEdge, AnyPerk],
            [guards.SwordmastersGuard, AnyPerk],
            [traits.RelentlessStrikes, traits.AttritionOrbs],
            [traits.ColdSteel],
            ),
        Roll(
            'Ad clear',
            [blades.JaggedEdge, AnyPerk],
            [guards.SwordmastersGuard, AnyPerk],
            [traits.TirelessBlade, traits.RelentlessStrikes],
            [traits.ChainReaction],
            ),
        ]
