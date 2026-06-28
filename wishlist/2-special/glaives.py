from wishlist import *


class AlbedoWing(RollDefinition):
    """
    Arc Aggressive Glaive, Anti-Unstoppable
    Source: The Dawning
    https://www.light.gg/db/items/2274629609
    https://destiny.report/w/2274629609
    """
    item = Item('Albedo Wing', hash=2274629609)


class Backfang(RollDefinition):
    """
    Arc Rapid-Fire Glaive, Anti-Overload
    Source: The Drifter (unavailable right now)
    https://www.light.gg/db/items/1277470844
    https://destiny.report/w/1277470844
    """
    item = Item('Backfang', hash=1277470844)


class GreasyLuck(RollDefinition):
    """
    Solar Rapid-Fire Glaive, Anti-Overload
    Source: "Ghosts of the Deep" Dungeon
    https://www.light.gg/db/items/4274165888
    https://destiny.report/w/4274165888
    """
    item = Item('Greasy Luck', hash=4274165888)


class EclipticDistaff(RollDefinition):
    """
    Void Adaptive Glaive, Anti-Barrier
    Source: Solo Ops
    https://www.light.gg/db/items/1942143745
    https://destiny.report/w/1942143745
    """
    item = Item('Ecliptic Distaff', hash=1942143745)


class TheHeron(RollDefinition):
    """
    Void Aggressive Glaive, Anti-Unstoppable
    Source: Lawless Events
    https://www.light.gg/db/items/2246386812
    https://destiny.report/w/2246386812
    """
    items = [
        Item('The Heron', hash=2246386812),
        Item('The Heron', hash=617566156),
        Item('The Heron', hash=617566157),
        Item('The Heron', hash=617566158),
        Item('The Heron', hash=617566159),
        ]
    rolls = [
        Roll(
            'Damage blocking',
            [haft.LowImpedanceWindings, AnyPerk],
            [magazine.AlloyMagazine, AnyPerk],
            [trait.ReplenishingAegis],
            [trait.Redirection, trait.DestabilizingRounds],
            ),
        Roll(
            'Melee damage',
            [haft.LowImpedanceWindings, AnyPerk],
            [magazine.AlloyMagazine, AnyPerk],
            [trait.ProximityPower],
            [trait.CloseToMelee],
            ),
        ]


class RakeAngle(RollDefinition):
    """
    Stasis Aggressive Glaive, Anti-Unstoppable
    Source: Commander Zavala
    https://www.light.gg/db/items/2201323795
    https://destiny.report/w/2201323795
    """
    item = Item('Rake Angle', hash=2201323795)


class RefusalOfTheCall(RollDefinition):
    """
    Strand Adaptive Glaive, Anti-Barrier
    Source:
    https://www.light.gg/db/items/1541324871
    https://destiny.report/w/1541324871
    """
    item = Item('Refusal of the Call', hash=1541324871)
