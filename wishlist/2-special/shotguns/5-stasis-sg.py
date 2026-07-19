from wishlist import *
from . import *


class Deadlock(RollDefinition):
    """
    Stasis Shotgun, Precision Frame, Anti-Barrier
    Source: Competitive Crucible
    https://www.light.gg/db/items/3926987546
    https://destiny.report/w/3926987546
    """
    item = Item('Deadlock', hash=3926987546)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            pvp_barrels,
            pvp_mags,
            [trait.LoneWolf],
            [trait.ThreatDetector],
            [trait.ClosingTime],
            [trait.OpeningShot],
            ),
        Roll(
            'PvP',
            pvp_barrels,
            pvp_mags,
            [trait.ThreatDetector],
            [trait.OpeningShot],
            ),
        Roll(
            'PvP',
            pvp_barrels,
            pvp_mags,
            [trait.LoneWolf],
            [trait.ClosingTime],
            ),
        ]


class Fractethyst(RollDefinition):
    """
    Stasis Shotgun, Precision Frame, Anti-Barrier
    Source: Dungeon "The Shattered Throne"
    https://www.light.gg/db/items/2993995118
    https://destiny.report/w/2993995118
    """
    item = Item('Fractethyst', hash=2993995118)


class HawthornesFieldForgedShotgun(RollDefinition):
    """
    Stasis Shotgun, Lightweight Frame, Anti-Overload
    Source: Banshee-44; Tenet of Bravery
    https://www.light.gg/db/items/1402874079
    https://destiny.report/w/1402874079
    """
    item = Item("Hawthorne's Field-Forged Shotgun", hash=1402874079)
    rolls = [
        Roll(
            'Super roll',
            pvp_barrels,
            pvp_mags,
            [trait.LoneWolf],
            [trait.ThreatDetector],
            [trait.ClosingTime],
            [trait.OpeningShot],
            ),
        Roll(
            'PvP',
            pvp_barrels,
            pvp_mags,
            [trait.ThreatDetector],
            [trait.OpeningShot],
            ),
        Roll(
            'PvP',
            pvp_barrels,
            pvp_mags,
            [trait.LoneWolf],
            [trait.ClosingTime],
            ),
        ]


class NoReprieve(RollDefinition):
    """
    Stasis Shotgun, Pinpoint Slug Frame, Anti-Barrier, Craftable
    Source: Xûr
    https://www.light.gg/db/items/2531963421
    https://destiny.report/w/2531963421
    """
    item = Item('No Reprieve', hash=2531963421)


class OneSmallStep(RollDefinition):
    """
    Stasis Shotgun, Rapid-Fire Frame, Anti-Overload
    Source: The Moon
    https://www.light.gg/db/items/2527058296
    https://destiny.report/w/2527058296
    """
    item = Item('One Small Step', hash=2527058296)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            pve_barrels,
            pve_mags,
            [trait.ProximityPower],
            [trait.Rimestealer],
            [trait.GraveRobber],
            [trait.OneTwoPunch],
            [trait.TrenchBarrel],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Melee damage increase',
            pve_barrels,
            pve_mags,
            [trait.ProximityPower, trait.GraveRobber],
            [trait.GraveRobber],
            ),
        Roll(
            'Stasis combo',
            pve_barrels,
            pve_mags,
            [trait.Rimestealer],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Damage dealing',
            pve_barrels,
            pve_mags,
            [trait.GraveRobber],
            [trait.TrenchBarrel],
            ),
        ]


class Trachinus(RollDefinition):
    """
    Stasis Shotgun, Rapid Fire Slug, Anti-Overload
    Source: Events during season "Reclamation"
    https://www.light.gg/db/items/3635232671
    https://destiny.report/w/3635232671
    """
    items = [
        Item('Trachinus', hash=3635232671),
        Item('Trachinus', hash=2888021252),
        Item('Trachinus', hash=2888021253),
        Item('Trachinus', hash=2888021254),
        Item('Trachinus', hash=2888021255),
        ]
    rolls = [
        Roll(
            'Super roll',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.AssaultMag, AnyPerk],
            [trait.LeadFromGold],
            [trait.Rimestealer],
            [trait.RapidHit],
            [trait.Headstone],
            [trait.ChillClip],
            [trait.PrecisionInstrument],
            ),
        Roll(
            'Stasis combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.AssaultMag, AnyPerk],
            [trait.Rimestealer],
            [trait.Headstone],
            ),
        Roll(
            'Chill Clip',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.AssaultMag, AnyPerk],
            [trait.RapidHit, trait.LeadFromGold],
            [trait.ChillClip],
            ),
        Roll(
            'Damage dealing',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.AssaultMag, AnyPerk],
            [trait.RapidHit],
            [trait.PrecisionInstrument],
            ),
        ]
