from database import *


class StayFrosty(RD):
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


class Glacioclasm(RD):
    """
    Void Fusion Rifle, High-Impact Frame
    https://www.light.gg/db/items/1183116657
    """
    item = Item(name='Glacioclasm', hash=1183116657)
    rolls = [
        Roll(
            'Ad clear. Enhanced Battery + Reservoir Burst give mag size of 8 (max)',
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.EnhancedBattery, AnyPerk],
            [traits.Subsistence, traits.Overflow],
            [traits.ReservoirBurst],
            ),
        Roll(
            'Damage dealing',
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.EnhancedBattery, AnyPerk],
            [traits.Overflow],
            [traits.ControlledBurst],
            ),
        Roll(
            'Withering Gaze',
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.EnhancedBattery, AnyPerk],
            [traits.Overflow],
            [traits.WitheringGaze],
            ),
        Roll(
            'PvP',
            [barrels.Smallbore],
            [batteries.ProjectionFuse],
            [traits.UnderPressure],
            [traits.ClosingTime, traits.HighImpactReserves],
            ),
        ]


class MistralLift(RD):
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
        [traits.BaitAndSwitch, traits.PrecisionInstrument],
        [origin.VeistStinger],
        )


class Zephyr(RD):
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
            [traits.TirelessBlade, traits.RelentlessStrikes, traits.AttritionOrbs],
            [traits.ChainReaction],
            ),
        ]
