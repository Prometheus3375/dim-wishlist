from wishlist import *


class BrassAttacks(RollDefinition):
    """
    Void Sidearm, Heavy Burst, Anti-Unstoppable
    Source: World
    https://www.light.gg/db/items/1291040554
    https://destiny.report/w/1291040554
    """
    item = Item('Brass Attacks', hash=1291040554)


class CompactDefender(RollDefinition):
    """
    Void Sidearm, Dynamic Heat Weapon, Anti-Overload
    Source: Lawless Frontier
    https://www.light.gg/db/items/2819552809
    https://destiny.report/w/2819552809
    """
    items = [
        Item('Compact Defender', hash=2819552809),
        Item('Compact Defender', hash=2659286158),
        ]
    roll = Roll(
        'Void combo',
        [barrel.ExtendedBarrel, AnyPerk],
        [battery.IonizedHeatsink, AnyPerk],
        [trait.DestabilizingRounds],
        [trait.RepulsorBrace],
        )


class Insurmountable(RollDefinition):
    """
    Void Sidearm, Precision Frame, Anti-Barrier
    Source: Banshee-44
    https://www.light.gg/db/items/2596736862
    https://destiny.report/w/2596736862
    """
    item = Item('Insurmountable', hash=2596736862)


class SeventhSeraphSI2(RollDefinition):
    """
    Void Sidearm, Lightweight Frame, Anti-Overload
    Source: Cosmodrome
    https://www.light.gg/db/items/453798564
    https://destiny.report/w/453798564
    """
    item = Item('Seventh Seraph SI-2', hash=453798564)
