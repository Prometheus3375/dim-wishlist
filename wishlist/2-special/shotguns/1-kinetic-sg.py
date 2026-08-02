from wishlist import *
from . import *


class AstralHorizon(RollDefinition):
    """
    Kinetic Shotgun, Aggressive Frame, Anti-Unstoppable
    Source: Saint-14
    https://www.light.gg/db/items/2269779982
    https://destiny.report/w/2269779982
    """
    item = Item('Astral Horizon', hash=2269779982)


class Blasphemer(RollDefinition):
    """
    Kinetic Shotgun, Pinpoint Slug Frame, Anti-Barrier
    Source: Altars of Sorrow
    https://www.light.gg/db/items/2527058297
    https://destiny.report/w/2527058297
    """
    item = Item('Blasphemer', hash=2527058297)


class Fortissimo11(RollDefinition):
    """
    Kinetic Shotgun, Pinpoint Slug Frame, Anti-Barrier
    Source: Commander Zavala
    https://www.light.gg/db/items/963732595
    https://destiny.report/w/963732595
    """
    items = [
        Item('Fortissimo-11', hash=963732595),
        Item('Fortissimo-11', hash=2821430069),
        ]


class Heritage(RollDefinition):
    """
    Kinetic Shotgun, Pinpoint Slug Frame, Anti-Barrier, Craftable
    Source: Raid "Deep Stone Crypt"
    https://www.light.gg/db/items/4248569242
    https://destiny.report/w/4248569242
    """
    item = Item('Heritage', hash=4248569242)


class ImperialDecree(RollDefinition):
    """
    Kinetic Shotgun, Aggressive Frame, Anti-Unstoppable, Craftable
    Source: Xûr
    https://www.light.gg/db/items/318443586
    https://destiny.report/w/318443586
    """
    item = Item('Imperial Decree', hash=318443586)


class PerfectParadox(RollDefinition):
    """
    Kinetic Shotgun, Rapid-Fire Frame, Anti-Overload
    Source: World
    https://www.light.gg/db/items/4108648762
    https://destiny.report/w/4108648762
    """
    item = Item('Perfect Paradox', hash=4108648762)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            pve_barrels,
            pve_mags,
            [trait.ThreatDetector],
            [trait.StoppingPower],
            [trait.Pugilist],
            [trait.TrenchBarrel],
            [trait.OneTwoPunch],
            ),
        Roll(
            'Melee damage increase',
            pve_barrels,
            pve_mags,
            [trait.ThreatDetector],
            [trait.OneTwoPunch],
            ),
        Roll(
            'Melee combo',
            pve_barrels,
            pve_mags,
            [trait.Pugilist],
            [trait.TrenchBarrel],
            ),
        Roll(
            'Damage dealing',
            pve_barrels,
            pve_mags,
            [trait.StoppingPower],
            [trait.TrenchBarrel],
            ),
        ]


class RagnhildD(RollDefinition):
    """
    Kinetic Shotgun, Aggressive Frame, Anti-Unstoppable, Craftable
    Source: Banshee-44
    https://www.light.gg/db/items/4225322581
    https://destiny.report/w/4225322581
    """
    item = Item('Ragnhild-D', hash=4225322581)


class RecklessEndangerment(RollDefinition):
    """
    Kinetic Shotgun, Lightweight Frame, Anti-Overload
    Source: Solo Ops
    https://www.light.gg/db/items/3085559077
    https://destiny.report/w/3085559077
    """
    item = Item('Reckless Endangerment', hash=3085559077)


class Riiswalker(RollDefinition):
    """
    Kinetic Shotgun, Lightweight Frame, Anti-Overload
    Source: Lord Saladin
    https://www.light.gg/db/items/1435062001
    https://destiny.report/w/1435062001
    """
    items = [
        Item('Riiswalker', hash=1435062001),
        Item('Riiswalker', hash=557165046),
        ]
    roll = Roll(
        'PvP',
        pvp_barrels,
        pvp_mags,
        [trait.Discord, trait.KillingWind],
        [trait.OpeningShot, trait.FragileFocus],
        )


class Someday(RollDefinition):
    """
    Kinetic Shotgun, Precision Frame, Anti-Barrier, Craftable
    Source: The Pale Heart
    https://www.light.gg/db/items/3232203524
    https://destiny.report/w/3232203524
    """
    item = Item('Someday', hash=3232203524)


class ThreatLevel(RollDefinition):
    """
    Kinetic Shotgun, Rapid-Fire Frame, Anti-Overload
    Source: Pantheon
    https://www.light.gg/db/items/1523151869
    https://destiny.report/w/1523151869
    """
    items = [
        Item('Threat Level', hash=1523151869),
        Item('Threat Level', hash=950894542),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            pve_barrels,
            pve_mags,
            [trait.OneTwoPunch],
            [trait.BewilderingBurst],
            [trait.CascadePoint],
            [trait.TrenchBarrel],
            [trait.AllStar],
            [trait.AggregateCharge],
            ),
        Roll(
            'Melee damage increase',
            pve_barrels,
            pve_mags,
            [trait.OneTwoPunch],
            [trait.TrenchBarrel],
            ),
        Roll(
            'Ad clear',
            pve_barrels,
            pve_mags,
            [trait.BewilderingBurst],
            [trait.TrenchBarrel, trait.AllStar, ],
            ),
        Roll(
            'Damage dealing',
            pve_barrels,
            pve_mags,
            [trait.CascadePoint],
            [trait.AggregateCharge, trait.AllStar, trait.TrenchBarrel],
            ),
        ]


class WastelanderM5(RollDefinition):
    """
    Kinetic Shotgun, Lightweight Frame, Anti-Overload, Craftable
    Source: Eternity
    https://www.light.gg/db/items/1679868061
    https://destiny.report/w/1679868061
    """
    item = Item('Wastelander M5', hash=1679868061)
