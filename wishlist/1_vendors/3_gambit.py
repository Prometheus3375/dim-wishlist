from database import *


class Bygones(RD):
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
