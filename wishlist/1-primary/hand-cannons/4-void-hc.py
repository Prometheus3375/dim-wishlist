from wishlist import *
from . import *


class AncientGospel(RollDefinition):
    """
    Void Hand Cannon, Adaptive Frame, Anti-Barrier, Craftable
    Source: Garden of Salvation
    https://www.light.gg/db/items/963574173
    https://destiny.report/w/963574173
    """
    item = Item('Ancient Gospel', hash=963574173)
    is_chosen = True
    roll = Roll(
        'Ad clear',
        default_barrels,
        default_mags,
        [trait.DestabilizingRounds],
        [trait.ExplosivePayload],
        )


class BottomDollar(RollDefinition):
    """
    Void Hand Cannon, Aggressive Frame, Anti-Unstoppable
    Source: The Drifter
    https://www.light.gg/db/items/2953199259
    https://destiny.report/w/2953199259
    """
    item = Item('Bottom Dollar', hash=2953199259)


class ExaltedTruth(RollDefinition):
    """
    Void Hand Cannon, Adaptive Frame, Anti-Barrier
    Source: Trials of Osiris
    https://www.light.gg/db/items/2776092653
    https://destiny.report/w/2776092653
    """
    item = Item('Exalted Truth', hash=2776092653)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.DestabilizingRounds],
            [trait.WitheringGaze],
            [trait.Demoralize],
            [trait.RepulsorBrace],
            ),
        Roll(
            'Void combo',
            default_barrels,
            default_mags,
            [trait.DestabilizingRounds],
            [trait.RepulsorBrace],
            ),
        ]


class IKELOS_HC_v103(RollDefinition):
    """
    Void Hand Cannon, Precision Frame, Anti-Barrier, Craftable
    Source: Seraph's Shield
    https://www.light.gg/db/items/1731355324
    https://destiny.report/w/1731355324
    """
    item = Item('IKELOS_HC_v1.0.3', hash=1731355324)


class KindledOrchid(RollDefinition):
    """
    Void Hand Cannon, Adaptive Frame, Anti-Barrier
    Source: Arena Ops
    https://www.light.gg/db/items/3961462214
    https://destiny.report/w/3961462214
    """
    items = [
        Item('Kindled Orchid', hash=3961462214),
        Item('Kindled Orchid', hash=334964261),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.RepulsorBrace],
            [trait.ShootToLoot],
            [trait.ImpromptuAmmunition],
            [trait.DestabilizingRounds],
            [trait.Demoralize],
            [trait.ExplosivePayload],
            ),
        Roll(
            'Void combo',
            default_barrels,
            default_mags,
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Shoot to Loot',
            default_barrels,
            default_mags,
            [trait.ShootToLoot],
            [trait.ExplosivePayload],
            ),
        ]


class MaahesHC4(RollDefinition):
    """
    Void Hand Cannon, Heavy Burst, Anti-Unstoppable
    Source: Banshee-44
    https://www.light.gg/db/items/734476286
    https://destiny.report/w/734476286
    """
    item = Item('Maahes HC4', hash=734476286)
    roll = Roll(
        'Void combo',
        default_barrels,
        [magazine.AlloyMagazine, AnyPerk],
        [trait.RepulsorBrace],
        [trait.DestabilizingRounds],
        ),


class MosAthanorIV(RollDefinition):
    """
    Void Hand Cannon, Aggressive Frame, Anti-Unstoppable
    Source: Lord Shaxx
    https://www.light.gg/db/items/4118334987
    https://destiny.report/w/4118334987
    """
    items = [
        Item('Mos Athanor IV', hash=4118334987),
        Item('Mos Athanor IV', hash=1288422452),
        ]


class Optative(RollDefinition):
    """
    Void Hand Cannon, Precision Frame, Anti-Barrier, Craftable
    Source: Starcrossed
    https://www.light.gg/db/items/2817683783
    https://destiny.report/w/2817683783
    """
    item = Item('Optative', hash=2817683783)


class TargetedRedaction(RollDefinition):
    """
    Void Hand Cannon, Aggressive Frame, Anti-Unstoppable, Craftable
    Source: Xûr
    https://www.light.gg/db/items/3890055324
    https://destiny.report/w/3890055324
    """
    item = Item('Targeted Redaction', hash=3890055324)


class WordOfCrota(RollDefinition):
    """
    Void Hand Cannon, Precision Frame, Anti-Barrier, Craftable
    Source: Crota's End
    https://www.light.gg/db/items/120706239
    https://destiny.report/w/120706239
    """
    items = [
        Item('Word of Crota', hash=120706239),
        Item('Word of Crota (Adept)', hash=3926103986),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.RepulsorBrace],
            [trait.Demolitionist],
            [trait.DestabilizingRounds],
            [trait.AdrenalineJunkie],
            ),
        Roll(
            'Void combo',
            default_barrels,
            default_mags,
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Grenade combo',
            default_barrels,
            default_mags,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        ]
