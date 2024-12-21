from database import *


class AnonymousAutumn(RD):
    """
    Arc Sidearm, Lightweight Frame
    https://www.light.gg/db/items/1051949956
    """
    item = Item(name='Anonymous Autumn', hash=1051949956)
    roll = Roll(
        'PvE roll',
        [traits.EddyCurrent, traits.AttritionOrbs, traits.Demolitionist],
        [traits.Voltshot],
        )
