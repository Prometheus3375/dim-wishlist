from wishlist import *


class ForcedMemorializer(RollDefinition):
    """
    Kinetic Scout Rifle, Precision Frame, Anti-Barrier
    Source: Commander Zavala
    https://www.light.gg/db/items/1197073834
    https://destiny.report/w/1197073834
    """
    item = Item('Forced Memorializer', hash=1197073834)
    rolls = [
        Roll(
            'PvE',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.ExplosivePayload, trait.BewilderingBurst],
            [trait.KineticTremors],
            ),
        Roll(
            'Missile combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.BewilderingBurst],
            [trait.AncillaryOrdinance],
            ),
        ]


class InboundSurveillance(RollDefinition):
    """
    Kinetic Scout Rifle, High-Impact Frame, Anti-Unstoppable
    Source: The Edge of Fate Campaign
    https://www.light.gg/db/items/2776506837
    https://destiny.report/w/2776506837
    """
    item = Item('Inbound Surveillance', hash=2776506837)


class HungJurySR4(RollDefinition):
    """
    Kinetic Scout Rifle, Precision Frame, Anti-Barrier
    Source: Unspecified
    https://www.light.gg/db/items/697459665
    https://destiny.report/w/697459665
    """
    item = Item('Hung Jury SR4', hash=697459665)


class LastRite(RollDefinition):
    """
    Kinetic Scout Rifle, Aggressive Frame, Anti-Unstoppable
    Source: Solo Ops
    https://www.light.gg/db/items/3708636616
    https://destiny.report/w/3708636616
    """
    item = Item('Last Rite', hash=3708636616)


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


class NightWatch(RollDefinition):
    """
    Kinetic Scout Rifle, Lightweight Frame, Anti-Overload
    Source: Unspecified
    https://www.light.gg/db/items/2916547559
    https://destiny.report/w/2916547559
    """
    item = Item('Night Watch', hash=2916547559)


class PatronOfLostCauses(RollDefinition):
    """
    Kinetic Scout Rifle, Lightweight Frame, Anti-Overload
    Source: Unspecified
    https://www.light.gg/db/items/3156551030
    https://destiny.report/w/3156551030
    """
    item = Item('Patron of Lost Causes', hash=3156551030)


class RandysThrowingKnife(RollDefinition):
    """
    Kinetic Scout Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Unspecified
    https://www.light.gg/db/items/4176824345
    https://destiny.report/w/4176824345
    """
    items = [
        Item("Randy's Throwing Knife", hash=4176824345),
        Item("Randy's Throwing Knife", hash=3975115486),
        ]
