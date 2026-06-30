from wishlist import *


class MirrorImago(RollDefinition):
    """
    Strand Submachine Gun, Adaptive Frame
    https://www.light.gg/db/items/3234363830
    """
    items = [
        Item('Mirror Imago', hash=3234363830),
        Item('Mirror Imago (Adept)', hash=302039451),
        # With Runneth Over
        Item('Mirror Imago', hash=3877448149),
        Item('Mirror Imago (Adept)', hash=4116546788),
        ]


class Anamnesis(RollDefinition):
    """
    Void Combat Bow, Lightweight Frame
    https://www.light.gg/db/items/2291392465
    """
    items = [
        Item('Anamnesis', hash=2291392465),
        Item('Anamnesis (Adept)', hash=1536325168),
        # With Runneth Over
        Item('Anamnesis', hash=3417731926),
        Item('Anamnesis (Adept)', hash=3949253499),
        ]
    rolls = [
        Roll(
            'Void combo',
            [bowstring.PolymerString, AnyPerk],
            [arrow.FiberglassArrowShaft, AnyPerk],
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds, trait.Demoralize],
            )
        ]


class Afterlight(RollDefinition):
    """
    Vois Fusion Rifle, Adaptive Frame
    https://www.light.gg/db/items/3228630258
    """
    items = [
        Item('Afterlight', hash=3228630258),
        Item('Afterlight (Adept)', hash=3953163559),
        # With Runneth Over
        Item('Afterlight', hash=1834313033),
        Item('Afterlight (Adept)', hash=861521336),
        ]


class Division(RollDefinition):
    """
    Arc Sidearm, Heavy Burst
    https://www.light.gg/db/items/2903168058
    """
    items = [
        Item('Division', hash=2903168058),
        Item('Division (Adept)', hash=3734001727),
        # With Runneth Over
        Item('Division', hash=2992463569),
        Item('Division (Adept)', hash=2501377328),
        ]
    roll = Roll(
        'PvE',
        [barrel.FlutedBarrel, AnyPerk],
        [magazine.FlaredMagwell, AnyPerk],
        [trait.EddyCurrent],
        [trait.Voltshot, trait.Surrounded],
        )


class FalsePromises(RollDefinition):
    """
    Stasis Auto Rifle, High-Impact Frame
    https://www.light.gg/db/items/1390080550
    """
    item = Item('False Promises', hash=1390080550)


class WhisperingSlab(RollDefinition):
    """
    Kinetic Combat Bow, Lightweight Frame
    https://www.light.gg/db/items/690341468
    """
    item = Item('Whispering Slab', hash=690341468)
    rolls = [
        Roll(
            'PvE',
            [bowstring.PolymerString, AnyPerk],
            [arrow.FiberglassArrowShaft, AnyPerk],
            [trait.ArchersTempo],
            [trait.VorpalWeapon],
            ),
        ]


class HollowWords(RollDefinition):
    """
    Arc Fusion Rifle, Precision Frame
    https://www.light.gg/db/items/342027677
    """
    item = Item('Hollow Words', hash=342027677)
