from wishlist import *

default_barrels = [barrel.BarrelShroud, AnyPerk]
default_mags = [magazine.AlloyMagazine, AnyPerk]


class AureusNeutralizer(RollDefinition):
    """
    Kinetic Hand Cannon, Spread Shot, Anti-Overload
    Source: Saint-14
    https://www.light.gg/db/items/3981920134
    https://destiny.report/w/3981920134
    """
    item = Item('Aureus Neutralizer', hash=3981920134)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.GraveRobber],
            [trait.ProximityPower],
            [trait.OneTwoPunch],
            [trait.TrenchBarrel],
            ),
        Roll(
            'Melee damage increase',
            default_barrels,
            default_mags,
            [trait.ProximityPower],
            [trait.OneTwoPunch],
            ),
        Roll(
            'PvP',
            [barrel.Smallbore, AnyPerk],
            [magazine.AccurizedRounds, AnyPerk],
            [trait.ThreatDetector],
            [trait.OpeningShot],
            ),
        ]


class SarpedonD(RollDefinition):
    """
    Arc Hand Cannon, Spread Shot, Anti-Overload
    Source: Commander Zavala; Tenet of Bravery
    https://www.light.gg/db/items/1242785638
    https://destiny.report/w/1242785638
    """
    items = [
        Item('Sarpedon-D', hash=1242785638),
        Item('Sarpedon-D', hash=3318545829),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.ImpromptuAmmunition],
            [trait.ProximityPower],
            [trait.OneTwoPunch],
            [trait.TrenchBarrel],
            ),
        Roll(
            'Melee damage increase',
            default_barrels,
            default_mags,
            [trait.ProximityPower],
            [trait.OneTwoPunch],
            ),
        ]


class PhoneutriaFera(RollDefinition):
    """
    Solar Hand Cannon, Spread Shot, Anti-Overload
    Source: Events during season "Reclamation"
    https://www.light.gg/db/items/3496887154
    https://destiny.report/w/3496887154
    """
    items = [
        Item('Phoneutria Fera', hash=3496887154),
        Item('Phoneutria Fera', hash=3804242792),
        Item('Phoneutria Fera', hash=3804242793),
        Item('Phoneutria Fera', hash=3804242794),
        Item('Phoneutria Fera', hash=3804242795),
        ]
    rolls = [
        Roll(
            'Melee damage increase',
            [barrel.FlutedBarrel, AnyPerk],
            default_mags,
            [trait.ProximityPower],
            [trait.OneTwoPunch],
            ),
        ]


class IRONWOOD03(RollDefinition):
    """
    Void Hand Cannon, Spread Shot, Anti-Overload
    Source: Distortions
    https://www.light.gg/db/items/2041617874
    https://destiny.report/w/2041617874
    """
    item = Item('IRONWOOD 03', hash=2041617874)
    roll = Roll(
        'Melee damage increase',
        default_barrels,
        default_mags,
        [trait.Pugilist],
        [trait.OneTwoPunch],
        )


class TripleLaureate(RollDefinition):
    """
    Stasis Hand Cannon, Spread Shot, Anti-Overload
    Source: Guardian Games
    https://www.light.gg/db/items/1605599021
    https://destiny.report/w/1605599021
    """
    items = [
        Item('Triple Laureate', hash=1605599021),
        Item('Triple Laureate', hash=2908653246),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.CrystallineCorpsebloom],
            [trait.GraveRobber],
            [trait.OneTwoPunch],
            [trait.ChaosReshaped],
            [trait.TrenchBarrel],
            ),
        Roll(
            'Melee damage increase',
            default_barrels,
            default_mags,
            [trait.GraveRobber],
            [trait.OneTwoPunch],
            ),
        ]
