from wishlist import *
from . import *


class ForcedMemorializer(RollDefinition):
    """
    Kinetic Scout Rifle, Precision Frame, Anti-Barrier
    Source: Commander Zavala; Tenet of Bravery
    https://www.light.gg/db/items/1197073834
    https://destiny.report/w/1197073834
    """
    item = Item('Forced Memorializer', hash=1197073834)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.BewilderingBurst],
            [trait.ExplosivePayload],
            [trait.ShootToLoot],
            [trait.AncillaryOrdinance],
            [trait.KineticTremors],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.ExplosivePayload, trait.BewilderingBurst],
            [trait.KineticTremors],
            ),
        ]


class HungJurySR4(RollDefinition):
    """
    Kinetic Scout Rifle, Precision Frame, Anti-Barrier
    Source: Onslaught
    https://www.light.gg/db/items/697459665
    https://destiny.report/w/697459665
    """
    item = Item('Hung Jury SR4', hash=697459665)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Demolitionist],
            [trait.KineticTremors],
            [trait.ShootToLoot],
            [trait.ExplosivePayload],
            [trait.Firefly],
            [trait.AncillaryOrdinance],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.KineticTremors],
            [trait.Firefly, trait.ExplosivePayload],
            ),
        Roll(
            'Shoot to Loot',
            default_barrels,
            default_mags,
            [trait.ShootToLoot],
            [trait.ExplosivePayload],
            ),
        ]


class Imperative(RollDefinition):
    """
    Kinetic Scout Rifle, High-Impact Frame, Anti-Unstoppable, Craftable
    Source: Exotic mission "Starcrossed"
    https://www.light.gg/db/items/2045811635
    https://destiny.report/w/2045811635
    """
    item = Item('Imperative', hash=2045811635)
    roll = Roll(
        'Ad clear',
        default_barrels,
        default_mags,
        [trait.RapidHit],
        [trait.KineticTremors],
        )


class InboundSurveillance(RollDefinition):
    """
    Kinetic Scout Rifle, High-Impact Frame, Anti-Unstoppable
    Source: World
    https://www.light.gg/db/items/2776506837
    https://destiny.report/w/2776506837
    """
    item = Item('Inbound Surveillance', hash=2776506837)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.StoppingPower],
            [trait.ShootToLoot],
            [trait.BewilderingBurst],
            [trait.ExplosivePayload],
            [trait.KineticTremors],
            [trait.Redirection],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.StoppingPower],
            [trait.KineticTremors, trait.Redirection],
            ),
        Roll(
            'Shoot to Loot',
            default_barrels,
            default_mags,
            [trait.ShootToLoot],
            [trait.ExplosivePayload],
            ),
        ]


class LastRite(RollDefinition):
    """
    Kinetic Scout Rifle, Aggressive Frame, Anti-Unstoppable
    Source: Solo Ops
    https://www.light.gg/db/items/3708636616
    https://destiny.report/w/3708636616
    """
    item = Item('Last Rite', hash=3708636616)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.StoppingPower],
            [trait.BewilderingBurst],
            [trait.ShootToLoot],
            [trait.Firefly],
            [trait.AdhesiveOrdnance],
            [trait.ExplosivePayload],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.BewilderingBurst],
            [trait.Firefly, trait.ExplosivePayload],
            ),
        Roll(
            'Shoot to Loot',
            default_barrels,
            default_mags,
            [trait.ShootToLoot],
            [trait.ExplosivePayload, trait.AdhesiveOrdnance],
            ),
        ]


class NamelessMidnight(RollDefinition):
    """
    Kinetic Scout Rifle, Precision Frame, Anti-Barrier
    Source: Fireteam Ops
    https://www.light.gg/db/items/1957301533
    https://destiny.report/w/1957301533
    """
    items = [
        Item('Nameless Midnight', hash=1957301533),
        Item('Nameless Midnight', hash=3470514298),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.ShootToLoot],
            [trait.RapidHit],
            [trait.KineticTremors],
            [trait.ExplosivePayload],
            [trait.AllStar],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.RapidHit],
            [trait.ExplosivePayload],
            ),
        Roll(
            'Shoot to Loot',
            default_barrels,
            default_mags,
            [trait.ShootToLoot],
            [trait.ExplosivePayload, trait.AllStar],
            ),
        ]


class NightWatch(RollDefinition):
    """
    Kinetic Scout Rifle, Lightweight Frame, Anti-Overload
    Source: The Drifter
    https://www.light.gg/db/items/2916547559
    https://destiny.report/w/2916547559
    """
    item = Item('Night Watch', hash=2916547559)
    roll = Roll(
        'Ad clear',
        default_barrels,
        default_mags,
        [trait.RapidHit],
        [trait.ExplosivePayload],
        )


class PatronOfLostCauses(RollDefinition):
    """
    Kinetic Scout Rifle, Lightweight Frame, Anti-Overload
    Source: Banshee-44
    https://www.light.gg/db/items/3156551030
    https://destiny.report/w/3156551030
    """
    items = [
        Item('Patron of Lost Causes', hash=3156551030),
        Item('Patron of Lost Causes', hash=2249996761),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.RapidHit],
            [trait.Strategist],
            [trait.ExplosivePayload],
            [trait.KineticTremors],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.RapidHit],
            [trait.KineticTremors, trait.ExplosivePayload],
            ),
        ]


class RandysThrowingKnife(RollDefinition):
    """
    Kinetic Scout Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Crucible
    https://www.light.gg/db/items/4176824345
    https://destiny.report/w/4176824345
    """
    items = [
        Item("Randy's Throwing Knife", hash=4176824345),
        Item("Randy's Throwing Knife", hash=3975115486),
        ]
    roll = Roll(
        'Ad clear',
        default_barrels,
        default_mags,
        [trait.RapidHit],
        [trait.KineticTremors, trait.Firefly],
        )


class TearsOfContrition(RollDefinition):
    """
    Kinetic Scout Rifle, Precision Frame, Anti-Barrier, Craftable
    Source: Exotic mission "Presage"
    https://www.light.gg/db/items/1366394399
    https://destiny.report/w/1366394399
    """
    item = Item('Tears of Contrition', hash=1366394399)


class Transfiguration(RollDefinition):
    """
    Kinetic Scout Rifle, High-Impact Frame, Anti-Unstoppable, Craftable
    Source: Raid "Last Wish"
    https://www.light.gg/db/items/3885259140
    https://destiny.report/w/3885259140
    """
    item = Item('Transfiguration', hash=3885259140)
    rolls = [
        Roll(
            'Grenade combo',
            default_barrels,
            default_mags,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        Roll(
            'Collective combo',
            default_barrels,
            default_mags,
            [trait.CollectiveDemolition],
            [trait.CollectiveAction],
            ),
        ]
