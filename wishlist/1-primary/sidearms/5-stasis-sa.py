from wishlist import *


class FaustusDecline(RollDefinition):
    """
    Stasis Sidearm, Lightweight Frame, Anti-Overload
    Source: Banshee-44
    https://www.light.gg/db/items/1663482635
    https://destiny.report/w/1663482635
    """
    item = Item('Faustus Decline', hash=1663482635)
    roll = Roll(
        'PvE',
        [barrel.Smallbore, AnyPerk],
        [magazine.FlaredMagwell, AnyPerk],
        [trait.Demolitionist, trait.Rimestealer],
        [trait.Headstone],
        )


class LiminalVigil(RollDefinition):
    """
    Stasis Sidearm, Heavy Burst, Anti-Unstoppable
    Source: "Spire of the Watcher" Dungeon
    https://www.light.gg/db/items/355893876
    https://destiny.report/w/355893876
    """
    item = Item('Liminal Vigil', hash=355893876)


class Peacebond(RollDefinition):
    """
    Stasis Sidearm, Adaptive Burst, Anti-Barrier
    Source: Unspecified
    https://www.light.gg/db/items/247984829
    https://destiny.report/w/247984829
    """
    item = Item('Peacebond', hash=247984829)
