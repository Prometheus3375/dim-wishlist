from database import *


class Bygones(RD):
    item = Item(name='Bygones', hash=2199554524)
    roll = roll(
        'PvE rolls',
        [traits.AttritionOrbs, traits.ShootToLoot],
        [traits.KineticTremors],
        )
