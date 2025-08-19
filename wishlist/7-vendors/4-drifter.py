from database import *


class Bygones(RollDefinition):
    """
    Kinetic Pulse Rifle, Adaptive Frame
    https://www.light.gg/db/items/2199554524
    """
    item = Item(name='Bygones', hash=2199554524)
    roll = Roll(
        'PvE',
        [traits.AttritionOrbs, traits.ShootToLoot],
        [traits.KineticTremors],
        )


class Backfang(RollDefinition):
    """
    Arc Rapid-Fire Glaive
    https://www.light.gg/db/items/267672635
    """
    item = Item(name='Backfang', hash=267672635)
    rolls = [
        Roll(
            'PvE',
            [hafts.AuxiliaryReserves, hafts.LowImpedanceWindings, AnyPerk],
            [magazines.AlloyMagazine, magazines.LightMag, AnyPerk],
            [traits.ReplenishingAegis],
            [traits.Voltshot, traits.Surrounded, traits.UnstoppableForce],
            ),
        Roll(
            'Melee damage',
            [hafts.AuxiliaryReserves, hafts.LowImpedanceWindings, AnyPerk],
            [magazines.AlloyMagazine, magazines.LightMag, AnyPerk],
            [traits.ReplenishingAegis],
            [traits.CloseToMelee],
            ),
        ]
