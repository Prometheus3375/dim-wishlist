from database import *


class StayFrosty(RD):
    """
    Stasis Pulse Rifle, Lightweight Frame
    https://www.light.gg/db/items/1123433952
    """
    item = Item(name='Stay Frosty', hash=1123433952)
    _mags = [
        magazines.TacticalMag,
        magazines.AppendedMag,
        magazines.AlloyMagazine,
        magazines.FlaredMagwell,
        ]
    roll = Roll(
        'Headstone roll',
        [barrels.ArrowheadBrake, AnyPerk],
        _mags,
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
            'Roll for ad clear',
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.AcceleratedCoils, AnyPerk],
            [traits.Subsistence, traits.Overflow],
            [traits.ReservoirBurst],
            ),
        Roll(
            'Roll for damage dealing',
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.AcceleratedCoils, AnyPerk],
            [traits.Overflow],
            [traits.ControlledBurst],
            ),
        Roll(
            'Weaken support roll',
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.AcceleratedCoils, AnyPerk],
            [traits.Overflow],
            [traits.WitheringGaze],
            ),
        Roll(
            'PvP roll',
            [barrels.Smallbore],
            [batteries.ProjectionFuse],
            [traits.UnderPressure],
            [traits.HighImpactReserves, traits.ClosingTime],
            ),
        ]


class MistralLift(RD):
    """
    Void Linear Fusion Rifle, Adaptive Burst
    https://www.light.gg/db/items/3483485727
    """
    item = Item(name='Mistral Lift', hash=3483485727)
    roll = Roll(
        'Roll for damage dealing',
        [barrels.ArrowheadBrake, AnyPerk],
        [batteries.AcceleratedCoils, AnyPerk],
        [traits.Reconstruction, traits.EnviousAssassin, traits.ClownCartridge,
         traits.WitheringGaze],
        [traits.PrecisionInstrument, traits.BaitAndSwitch],
        )


class Zephyr(RD):
    """
    Stasis Sword, Adaptive Frame
    https://www.light.gg/db/items/601948197
    """
    item = Item(name='Zephyr', hash=601948197)
    rolls = [
        Roll(
            'Roll for damage dealing',
            [blades.JaggedEdge, AnyPerk],
            [guards.SwordmastersGuard, AnyPerk],
            [traits.RelentlessStrikes, traits.AttritionOrbs],
            [traits.WhirlwindBlade, traits.Surrounded],
            ),
        Roll(
            'Cold Steel roll',
            [blades.JaggedEdge, AnyPerk],
            [guards.SwordmastersGuard, AnyPerk],
            # Rimestealer requires destroying a frozen target or Stasis crystal
            # which hard to achieve with Cold Steel.
            [traits.RelentlessStrikes, traits.AttritionOrbs],
            [traits.ColdSteel],
            ),
        Roll(
            'Roll for ad clear',
            [blades.JaggedEdge, AnyPerk],
            [guards.SwordmastersGuard, AnyPerk],
            [traits.TirelessBlade, traits.AttritionOrbs],
            [traits.ChainReaction],
            ),
        ]
