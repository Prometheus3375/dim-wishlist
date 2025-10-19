from wishlist import *


class Bygones(RollDefinition):
    """
    Kinetic Pulse Rifle, Adaptive Frame
    https://www.light.gg/db/items/2199554524
    """
    item = Item(name='Bygones', hash=2199554524)
    roll = Roll(
        'PvE',
        [trait.AttritionOrbs, trait.ShootToLoot],
        [trait.KineticTremors],
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
            [haft.AuxiliaryReserves, haft.LowImpedanceWindings, AnyPerk],
            [magazine.AlloyMagazine, magazine.LightMag, AnyPerk],
            [trait.ReplenishingAegis],
            [trait.Voltshot, trait.Surrounded, trait.UnstoppableForce],
            ),
        Roll(
            'Melee damage',
            [haft.AuxiliaryReserves, haft.LowImpedanceWindings, AnyPerk],
            [magazine.AlloyMagazine, magazine.LightMag, AnyPerk],
            [trait.ReplenishingAegis],
            [trait.CloseToMelee],
            ),
        ]
