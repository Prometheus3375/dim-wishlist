from wishlist import *


class NatureReclaimed(RollDefinition):
    """
    Solar Scout Rifle, Lightweight Frame
    https://www.light.gg/db/items/2639921391
    """
    item = Item('Nature Reclaimed', hash=2639921391)
    rolls = [
        Roll(
            'Shoot to Loot',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.ShootToLoot],
            [trait.ExplosivePayload],
            ),
        Roll(
            'Solar combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.HealClip],
            [trait.Incandescent],
            ),
        ]


class WarlordsSpear(RollDefinition):
    """
    Arc Trace Rifle, Adaptive Frame
    https://www.light.gg/db/items/1968711238
    """
    item = Item("Warlord's Spear", hash=1968711238)
    rolls = [
        Roll(
            'Jolting Feedback',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.TacticalBattery, AnyPerk],
            [trait.RewindRounds, trait.LooseChange],
            [trait.JoltingFeedback],
            ),
        Roll(
            'Detonator Beam',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.TacticalBattery, AnyPerk],
            [trait.RewindRounds],
            [trait.DetonatorBeam],
            ),
        ]
