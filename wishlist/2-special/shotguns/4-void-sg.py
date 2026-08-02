from wishlist import *
from . import *


class ASuddenDeath(RollDefinition):
    """
    Void Shotgun, Aggressive Frame, Anti-Unstoppable
    Source: Dungeon "Prophecy"
    https://www.light.gg/db/items/2489016648
    https://destiny.report/w/2489016648
    """
    item = Item('A Sudden Death', hash=2489016648)


class BassoOstinato(RollDefinition):
    """
    Void Shotgun, Rapid-Fire Frame, Anti-Overload
    Source: Terminal Overload
    https://www.light.gg/db/items/2353274446
    https://destiny.report/w/2353274446
    """
    item = Item('Basso Ostinato', hash=2353274446)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            pve_barrels,
            pve_mags,
            [trait.GraveRobber],
            [trait.ProximityPower],
            [trait.Discord],
            [trait.OneTwoPunch],
            [trait.DestabilizingRounds],
            [trait.TrenchBarrel],
            ),
        Roll(
            'Melee damage increase',
            pve_barrels,
            pve_mags,
            [trait.ProximityPower, trait.GraveRobber],
            [trait.OneTwoPunch],
            ),
        Roll(
            'Ad clear',
            pve_barrels,
            pve_mags,
            [trait.Discord],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Damage dealing',
            pve_barrels,
            pve_mags,
            [trait.GraveRobber],
            [trait.TrenchBarrel],
            ),
        ]


class Bonechiller(RollDefinition):
    """
    Void Shotgun, Pinpoint Slug Frame, Anti-Barrier
    Source: Europa
    https://www.light.gg/db/items/1529367715
    https://destiny.report/w/1529367715
    """
    item = Item('Bonechiller', hash=1529367715)


class NessasOblation(RollDefinition):
    """
    Void Shotgun, Pinpoint Slug Frame, Anti-Barrier, Craftable
    Source: Raid "Root of Nightmares"
    https://www.light.gg/db/items/135029084
    https://destiny.report/w/135029084
    """
    items = [
        Item("Nessa's Oblation", hash=135029084),
        Item("Nessa's Oblation (Adept)", hash=522366885),
        ]


class Precipial(RollDefinition):
    """
    Void Shotgun, Precision Frame, Anti-Barrier
    Source: Kepler
    https://www.light.gg/db/items/367772693
    https://destiny.report/w/367772693
    """
    item = Item('Precipial', hash=367772693)
    is_chosen = True
    roll = Roll(
        'PvP',
        pvp_barrels,
        pvp_mags,
        [trait.ThreatDetector],
        [trait.OpeningShot],
        )


class PureRecollection(RollDefinition):
    """
    Void Shotgun, Heavy Burst, Anti-Unstoppable
    Source: Lord Shaxx; Tenet of Bravery
    https://www.light.gg/db/items/1956186483
    https://destiny.report/w/1956186483
    """
    item = Item('Pure Recollection', hash=1956186483)
    rolls = [
        Roll(
            'Damage dealing',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.ArmorPiercingRounds, AnyPerk],
            [trait.EnviousArsenal],
            [trait.BaitAndSwitch],
            ),
        ]


class Python(RollDefinition):
    """
    Void Shotgun, Aggressive Frame, Anti-Unstoppable
    Source: Gambit
    https://www.light.gg/db/items/4276696962
    https://destiny.report/w/4276696962
    """
    item = Item('Python', hash=4276696962)


class RetoldTale(RollDefinition):
    """
    Void Shotgun, Precision Frame, Anti-Barrier
    Source: The Dreaming City
    https://www.light.gg/db/items/3442151842
    https://destiny.report/w/3442151842
    """
    item = Item('Retold Tale', hash=3442151842)
    rolls = [
        Roll(
            'Super roll',
            pvp_barrels,
            pvp_mags,
            [trait.ThreatDetector],
            [trait.LoneWolf],
            [trait.ClosingTime],
            ),
        Roll(
            'PvP',
            pvp_barrels,
            pvp_mags,
            [trait.ThreatDetector, trait.LoneWolf],
            [trait.ClosingTime],
            ),
        ]


class Retrofuturist(RollDefinition):
    """
    Void Shotgun, Lightweight Frame, Anti-Overload
    Source: Lord Shaxx
    https://www.light.gg/db/items/3688176697
    https://destiny.report/w/3688176697
    """
    items = [
        Item('Retrofuturist', hash=3688176697),
        Item('Retrofuturist', hash=1612781792),
        ]


class Unvoiced(RollDefinition):
    """
    Void Shotgun, Pinpoint Slug Frame, Anti-Barrier
    Source: Dungeon "Sundered Doctrine"
    https://www.light.gg/db/items/2213885190
    https://destiny.report/w/2213885190
    """
    item = Item('Unvoiced', hash=2213885190)
