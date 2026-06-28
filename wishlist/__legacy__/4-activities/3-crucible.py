from wishlist import *


class StarsInShadow(RollDefinition):
    """
    Solar Pulse Rifle, High-Impact Frame
    https://www.light.gg/db/items/3602242905
    """
    item = Item('Stars In Shadow', hash=3602242905)


class MosAthanorIV(RollDefinition):
    """
    Void Hand Cannon, Aggressive Frame
    https://www.light.gg/db/items/4118334987
    """
    items = [
        Item('Mos Athanor IV', hash=4118334987),
        Item('Mos Athanor IV', hash=1288422452),
        ]


# Special


class PureRecollection(RollDefinition):
    """
    Void Shotgun, Heavy Burst
    https://www.light.gg/db/items/1956186483
    """
    item = Item('Void Shotgun', hash=1956186483)


class ReturnedMemory(RollDefinition):
    """
    Solar Sidearm, Rocket-Assisted Frame
    https://www.light.gg/db/items/4049127142
    """
    item = Item('Returned Memory', hash=4049127142)
    rolls = [
        Roll(
            """
            PvE.
            Note for Redirection: stacks are granted and consumed for every hit,
            i.e., 2 * (1 [impact] + #[targets hit by an explosion]).
            If a target dies to impact, explosion doesn't hit it.
            Multiplier 2 is replaced with 3 for consumption if perk is not enhanced.
            """,
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.HealClip, trait.ImpulseAmplifier],
            [trait.Incandescent, trait.OneForAll, trait.Redirection],
            ),
        ]


class MIDAMacroTool(RollDefinition):
    """
    Arc Shotgun, Precision Frame
    https://www.light.gg/db/items/2699423382
    """
    item = Item('MIDA Macro-Tool', hash=2699423382)
    roll = Roll(
        'PvP',
        [barrel.Smallbore, barrel.CorkscrewRifling, barrel.BarrelShroud],
        [magazine.AccurizedRounds, magazine.LightMag],
        [trait.ThreatDetector],
        [trait.ClosingTime, trait.OpeningShot],
        )


class Riptide(RollDefinition):
    """
    Stasis Fusion Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/2297554989
    """
    items = [
        Item('Riptide', hash=2297554989),
        Item('Riptide', hash=1323862250),
        ]
    rolls = [
        Roll(
            'Chill Clip',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.EnhancedBattery, AnyPerk],
            [trait.Overflow, trait.AutoLoadingHolster],
            [trait.ChillClip],
            ),
        Roll(
            'Damage dealing',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.EnhancedBattery, AnyPerk],
            [trait.Overflow, trait.AutoLoadingHolster],
            [trait.ControlledBurst],
            ),
        ]


# Heavy


class QuaVinctusIV(RollDefinition):
    """
    Strand Machine Gun, High-Impact Frame
    https://www.light.gg/db/items/337893613
    """
    items = [
        Item('Qua Vinctus IV', hash=337893613),
        Item('Qua Vinctus IV', hash=4176551594),
        ]
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.AppendedMag, AnyPerk],
            [trait.Hatchling, trait.Demolitionist],
            [trait.Meganeura, trait.KillingTally, trait.Tear],
            ),
        ]
