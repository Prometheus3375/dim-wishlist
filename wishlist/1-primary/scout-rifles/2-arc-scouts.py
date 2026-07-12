from wishlist import *
from . import *


class LongArm(RollDefinition):
    """
    Arc Scout Rifle, Aggressive Frame, Anti-Unstoppable
    Source: Dungeon "Spire of the Watcher"
    https://www.light.gg/db/items/3418719964
    https://destiny.report/w/3418719964
    """
    item = Item('Long Arm', hash=3418719964)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.DualLoader],
            [trait.SuperchargedMagazine],
            [trait.LuckyShot],
            [trait.Meganeura],
            [trait.Redirection],
            [trait.ExplosivePayload],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.SuperchargedMagazine, trait.LuckyShot, trait.DualLoader],
            [trait.Meganeura, trait.Redirection],
            ),
        ]


class NoFeelings(RollDefinition):
    """
    Arc Scout Rifle, Precision Frame, Anti-Barrier
    Source: Arena Ops
    https://www.light.gg/db/items/1271275406
    https://destiny.report/w/1271275406
    """
    items = [
        Item('No Feelings', hash=1271275406),
        Item('No Feelings', hash=2979764077),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Voltshot],
            [trait.ImpromptuAmmunition],
            [trait.Meganeura],
            [trait.ExplosivePayload],
            [trait.GearShift],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.Voltshot],
            [trait.Meganeura, trait.GearShift],
            ),
        ]


class Sublimation(RollDefinition):
    """
    Arc Scout Rifle, High-Impact Frame, Anti-Unstoppable
    Source: Kepler
    https://www.light.gg/db/items/1674692344
    https://destiny.report/w/1674692344
    """
    item = Item('Sublimation', hash=1674692344)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.ImpromptuAmmunition],
            [trait.ShootToLoot],
            [trait.Voltshot],
            [trait.Redirection],
            [trait.ExplosivePayload],
            ),
        Roll(
            'Shoot to Loot',
            default_barrels,
            default_mags,
            [trait.ShootToLoot],
            [trait.ExplosivePayload],
            ),
        ]


class TarnishedMettle(RollDefinition):
    """
    Arc Scout Rifle, Lightweight Frame, Anti-Overload, Craftable
    Source: Xûr
    https://www.light.gg/db/items/2218569744
    https://destiny.report/w/2218569744
    """
    item = Item('Tarnished Mettle', hash=2218569744)
    roll = Roll(
        'Shoot to Loot',
        default_barrels,
        default_mags,
        [trait.ShootToLoot],
        [trait.ExplosivePayload],
        )


class Unworthy(RollDefinition):
    """
    Arc Scout Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Dungeon "Sundered Doctrine"
    https://www.light.gg/db/items/1700366811
    https://destiny.report/w/1700366811
    """
    item = Item('Unworthy', hash=1700366811)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Firefly],
            [trait.EddyCurrent],
            [trait.GearShift],
            [trait.Voltshot],
            ),
        Roll(
            'Reload combo',
            default_barrels,
            default_mags,
            [trait.Firefly],
            [trait.Voltshot],
            ),
        Roll(
            'Arc combo',
            default_barrels,
            default_mags,
            [trait.EddyCurrent],
            [trait.Voltshot, trait.GearShift],
            ),
        ]


class VoltaicShade(RollDefinition):
    """
    Arc Scout Rifle, Balanced Heat Weapon, Anti-Overload
    Source: Dungeon "Equilibrium"
    https://www.light.gg/db/items/71057630
    https://destiny.report/w/71057630
    """
    item = Item('Voltaic Shade', hash=71057630)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            [battery.IonizedHeatsink, AnyPerk],
            [trait.JoltingFeedback],
            [trait.ShootToLoot],
            [trait.Voltshot],
            [trait.Meganeura],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            [battery.IonizedHeatsink, AnyPerk],
            [trait.JoltingFeedback],
            [trait.Voltshot, trait.Meganeura],
            ),
        ]
