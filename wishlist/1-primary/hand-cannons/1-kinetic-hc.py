from wishlist import *


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
            'Melee damage increase',
            [barrel.BarrelShroud, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.ProximityPower, trait.GraveRobber, trait.ThreatDetector],
            [trait.OneTwoPunch],
            ),
        Roll(
            'Damage dealing',
            [barrel.BarrelShroud, AnyPerk],
            [magazine.AlloyMagazine, AnyPerk],
            [trait.VorpalWeapon],
            [trait.TrenchBarrel, trait.CascadePoint],
            ),
        Roll(
            'PvP',
            [barrel.Smallbore, AnyPerk],
            [magazine.AccurizedRounds, AnyPerk],
            [trait.ThreatDetector],
            [trait.OpeningShot, trait.ClosingTime],
            ),
        ]


class CrimilsDagger(RollDefinition):
    """
    Kinetic Hand Cannon, Aggressive Frame, Anti-Unstoppable
    Source: Iron Banner
    https://www.light.gg/db/items/1617917863
    https://destiny.report/w/1617917863
    """
    item = Item("Crimil's Dagger", hash=1617917863)


class DFA(RollDefinition):
    """
    Kinetic Hand Cannon, Adaptive Frame, Anti-Barrier
    Source: Pinnacle Ops
    https://www.light.gg/db/items/739029153
    https://destiny.report/w/739029153
    """
    items = [
        Item('D.F.A.', hash=739029153),
        Item('D.F.A.', hash=2920548486),
        ]


class Malediction(RollDefinition):
    """
    Kinetic Hand Cannon, Aggressive Frame, Anti-Unstoppable
    Source: Solo Ops
    https://www.light.gg/db/items/979721268
    https://destiny.report/w/979721268
    """
    item = Item('Malediction', hash=979721268)


class MidnightCoup(RollDefinition):
    """
    Kinetic Hand Cannon, Adaptive Frame, Anti-Barrier
    Source: Onslaught
    https://www.light.gg/db/items/2033531689
    https://destiny.report/w/2033531689
    """
    item = Item('Midnight Coup', hash=2033531689)


class Rose(RollDefinition):
    """
    Kinetic Hand Cannon, Lightweight Frame, Anti-Overload
    Source: Competitive Crucible
    https://www.light.gg/db/items/1041028434
    https://destiny.report/w/1041028434
    """
    item = Item('Rose', hash=1041028434)


class ServiceRevolver(RollDefinition):
    """
    Kinetic Hand Cannon, Precision Frame, Anti-Barrier
    Source: Fireteam Ops
    https://www.light.gg/db/items/3796682229
    https://destiny.report/w/3796682229
    """
    items = [
        Item('Service Revolver', hash=3796682229),
        Item('Service Revolver', hash=59060498),
        ]


class SeventhSeraphOfficerRevolver(RollDefinition):
    """
    Kinetic Hand Cannon, Precision Frame, Anti-Barrier
    Source: Unspecified
    https://www.light.gg/db/items/3490736392
    https://destiny.report/w/3490736392
    """
    item = Item('Seventh Seraph Officer Revolver', hash=3490736392)


class SurvivorsEpitaph(RollDefinition):
    """
    Kinetic Hand Cannon, Precision Frame, Anti-Barrier
    Source: Crucible
    https://www.light.gg/db/items/4059111040
    https://destiny.report/w/4059111040
    """
    items = [
        Item("Survivor's Epitaph", hash=4059111040),
        Item("Survivor's Epitaph", hash=2152350211),
        ]


class WardensLaw(RollDefinition):
    """
    Kinetic Hand Cannon, Heavy Burst, Anti-Unstoppable
    Source: Commander Zavala
    https://www.light.gg/db/items/2363113134
    https://destiny.report/w/2363113134
    """
    item = Item("Warden's Law", hash=2363113134)
