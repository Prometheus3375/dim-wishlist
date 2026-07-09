from wishlist import *
from . import *


class Austringer(RollDefinition):
    """
    Kinetic Hand Cannon, Adaptive Frame, Anti-Barrier, Craftable
    Source: Exotic mission "Presage"
    https://www.light.gg/db/items/3055790362
    https://destiny.report/w/3055790362
    """
    item = Item('Austringer', hash=3055790362)


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
    rolls = [
        Roll(
            'Super roll',
            [barrel.ChamberedCompensator, AnyPerk],
            default_mags,
            [trait.ExplosivePayload],
            [trait.OneForAll],
            [trait.AttritionOrbs],
            ),
        Roll(
            'Hit combo',
            [barrel.ChamberedCompensator, AnyPerk],
            default_mags,
            [trait.ExplosivePayload],
            [trait.AttritionOrbs],
            ),
        ]


class Fatebringer(RollDefinition):
    """
    Kinetic Hand Cannon, Adaptive Frame, Anti-Barrier, Craftable
    Source: Raid "Vault of Glass"
    https://www.light.gg/db/items/4184168210
    https://destiny.report/w/4184168210
    """
    items = [
        Item('Fatebringer', hash=4184168210),
        Item('Fatebringer (Timelost)', hash=4219826183),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.KineticTremors],
            [trait.ExplosivePayload],
            [trait.ImpromptuAmmunition],
            [trait.Firefly],
            [trait.OneForAll],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.KineticTremors],
            [trait.Firefly],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.KineticTremors, trait.ExplosivePayload],
            [trait.OneForAll],
            ),
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
    rolls = [
        Roll(
            'Super roll',
            [barrel.ArrowheadBrake, AnyPerk],
            default_mags,
            [trait.Firefly],
            [trait.ExplosivePayload],
            [trait.AttritionOrbs],
            [trait.KineticTremors],
            [trait.OneForAll],
            [trait.AncillaryOrdinance],
            ),
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            default_mags,
            [trait.Firefly, trait.ExplosivePayload],
            [trait.KineticTremors, trait.OneForAll],
            ),
        Roll(
            'Hit combo',
            [barrel.ArrowheadBrake, AnyPerk],
            default_mags,
            [trait.AttritionOrbs],
            [trait.KineticTremors],
            ),
        ]


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
    Source: Cosmodrome
    https://www.light.gg/db/items/3490736392
    https://destiny.report/w/3490736392
    """
    item = Item('Seventh Seraph Officer Revolver', hash=3490736392)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.SeraphRounds, AnyPerk],
            [trait.Reconstruction],
            [trait.BewilderingBurst],
            [trait.ShootToLoot],
            [trait.Redirection],
            [trait.ExplosivePayload],
            ),
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.SeraphRounds, AnyPerk],
            [trait.Reconstruction, trait.BewilderingBurst],
            [trait.Redirection, trait.ExplosivePayload],
            ),
        Roll(
            'Shoot to Loot',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.SeraphRounds, AnyPerk],
            [trait.ShootToLoot],
            [trait.ExplosivePayload],
            ),
        ]


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
    rolls = [
        Roll(
            'Miniboss damage dealing',
            [barrel.FlutedBarrel, AnyPerk],
            default_mags,
            [trait.FourthTimesTheCharm],
            [trait.VorpalWeapon],
            ),
        ]
