from wishlist import *


class Agape(RollDefinition):
    """
    Solar Hand Cannon, Heavy Burst, Anti-Unstoppable
    Source: Exploring Kepler
    https://www.light.gg/db/items/4124362340
    https://destiny.report/w/4124362340
    """
    item = Item('Agape', hash=4124362340)
    rolls = [
        Roll(
            'Lucky Pants combo',
            [barrel.ChamberedCompensator, AnyPerk],
            [magazine.AppendedMag, AnyPerk],
            [trait.RewindRounds],
            [trait.PrecisionInstrument],
            ),
        Roll(
            'Solar combo',
            [barrel.ChamberedCompensator, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.HealClip],
            [trait.Incandescent],
            ),
        ]


class EpochalIntegration(RollDefinition):
    """
    Solar Hand Cannon, Adaptive Frame, Anti-Barrier
    Source: Terminal Overload
    https://www.light.gg/db/items/3851394887
    https://destiny.report/w/3851394887
    """
    item = Item('Epochal Integration', hash=3851394887)


class FiniteImpactor(RollDefinition):
    """
    Solar Hand Cannon, Adaptive Frame, Anti-Barrier
    Source: Iron Banner
    https://www.light.gg/db/items/1917334929
    https://destiny.report/w/1917334929
    """
    item = Item('Finite Impactor', hash=1917334929)


class FrontiersCry(RollDefinition):
    """
    Solar Hand Cannon, Precision Frame, Anti-Barrier
    Source: Lord Saladin
    https://www.light.gg/db/items/3203303472
    https://destiny.report/w/3203303472
    """
    item = Item("Frontier's Cry", hash=3203303472)


class IgneousHammer(RollDefinition):
    """
    Solar Hand Cannon, Aggressive Frame, Anti-Unstoppable
    Source: Trials of Osiris
    https://www.light.gg/db/items/2776092652
    https://destiny.report/w/2776092652
    """
    item = Item('Igneous Hammer', hash=2776092652)


class LunasHowl(RollDefinition):
    """
    Solar Hand Cannon, Precision Frame, Anti-Barrier
    Source: Onslaught
    https://www.light.gg/db/items/2033531688
    https://destiny.report/w/2033531688
    """
    item = Item("Luna's Howl", hash=2033531688)


class PhoneutriaFera(RollDefinition):
    """
    Solar Hand Cannon, Spread Shot, Anti-Overload
    Source: Reclamation Events
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
            [magazine.TacticalMag, AnyPerk],
            [trait.ProximityPower, trait.ThreatDetector],
            [trait.OneTwoPunch],
            ),
        Roll(
            'Damage dealing',
            [barrel.FlutedBarrel, AnyPerk],
            [magazine.AppendedMag, AnyPerk],
            [trait.ThreatDetector],
            [trait.Surrounded],
            ),
        # Roll(
        #     'Ad clear',
        #     [barrel.FlutedBarrel, AnyPerk],
        #     [magazine.TacticalMag, AnyPerk],
        #     [trait.ThreatDetector],
        #     [trait.Incandescent],
        #     ),
        ]


class Trust(RollDefinition):
    """
    Solar Hand Cannon, Precision Frame, Anti-Barrier
    Source: Gambit
    https://www.light.gg/db/items/810474118
    https://destiny.report/w/810474118
    """
    item = Item('Trust', hash=810474118)


class ZaoulisBane(RollDefinition):
    """
    Solar Hand Cannon, Adaptive Frame, Anti-Barrier
    Source: Pantheon
    https://www.light.gg/db/items/3647341740
    https://destiny.report/w/3647341740
    """
    items = [
        Item("Zaouli's Bane", hash=3647341740),
        Item("Zaouli's Bane", hash=3066945855),
        ]
