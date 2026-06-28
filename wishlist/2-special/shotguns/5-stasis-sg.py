from wishlist import *


class Deadlock(RollDefinition):
    """
    Stasis Shotgun, Precision Frame, Anti-Barrier
    Source: Competitive Crucible
    https://www.light.gg/db/items/3926987546
    https://destiny.report/w/3926987546
    """
    item = Item('Deadlock', hash=3926987546)


class Fractethyst(RollDefinition):
    """
    Stasis Shotgun, Precision Frame, Anti-Barrier
    Source:
    https://www.light.gg/db/items/2993995118
    https://destiny.report/w/2993995118
    """
    item = Item('Fractethyst', hash=2993995118)


class HawthornesFieldForgedShotgun(RollDefinition):
    """
    Stasis Shotgun, Lightweight Frame, Anti-Overload
    Source: Banshee-44
    https://www.light.gg/db/items/1402874079
    https://destiny.report/w/1402874079
    """
    item = Item("Hawthorne's Field-Forged Shotgun", hash=1402874079)
    rolls = [
        Roll(
            'PvP',
            [barrel.Smallbore, barrel.CorkscrewRifling, barrel.BarrelShroud],
            [magazine.AccurizedRounds, magazine.LightMag],
            [trait.ThreatDetector, trait.LoneWolf],
            [trait.OpeningShot, trait.ClosingTime],
            ),
        Roll(
            'Ad clear',
            [barrel.BarrelShroud, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.ThreatDetector],
            [trait.CrystallineCorpsebloom],
            ),
        ]


class OneSmallStep(RollDefinition):
    """
    Stasis Shotgun, Rapid-Fire Frame, Anti-Overload
    Source: Unspecified
    https://www.light.gg/db/items/2527058296
    https://destiny.report/w/2527058296
    """
    item = Item('One Small Step', hash=2527058296)
