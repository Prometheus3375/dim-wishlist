from wishlist import *

_precision_strings = [bowstring.ElasticString, AnyPerk]
_precision_arrows = [arrow.CompactArrowShaft, AnyPerk]
_lightweight_strings = [bowstring.PolymerString, AnyPerk]
_lightweight_arrows = [arrow.FiberglassArrowShaft, AnyPerk]


class ConvenedRecurve(RollDefinition):
    """
    Void High-Impact Longbow, Anti-Unstoppable
    Source: Fireteam Ops
    https://www.light.gg/db/items/3667861447
    https://destiny.report/w/3667861447
    """
    items = [
        Item('Convened Recurve', hash=3667861447),
        Item('Convened Recurve', hash=2271714488),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            _precision_strings,
            _precision_arrows,
            [trait.RepulsorBrace],
            [trait.WitheringGaze],
            [trait.DestabilizingRounds],
            [trait.Demoralize],
            ),
        Roll(
            'Void combo',
            _precision_strings,
            _precision_arrows,
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds, trait.Demoralize],
            ),
        ]


class FortunateStar(RollDefinition):
    """
    Void Combat Bow, Lightweight Frame, Anti-Overload
    Source: Solstice
    https://www.light.gg/db/items/2631466936
    https://destiny.report/w/2631466936
    """
    items = [
        Item('Fortunate Star', hash=2631466936),
        Item('Fortunate Star', hash=591672323),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Ad clear',
            _lightweight_strings,
            _lightweight_arrows,
            [trait.ImpromptuAmmunition],
            [trait.RepulsorBrace],
            [trait.ArchersTempo],
            [trait.ExplosiveHead],
            [trait.DestabilizingRounds],
            [trait.Demoralize],
            ),
        Roll(
            'Void combo',
            _lightweight_strings,
            _lightweight_arrows,
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds, trait.Demoralize],
            ),
        ]


class Lethophobia(RollDefinition):
    """
    Void Combat Bow, Lightweight Frame, Anti-Overload, Craftable
    Source: Starcrossed
    https://www.light.gg/db/items/3710082365
    https://destiny.report/w/3710082365
    """
    item = Item('Lethophobia', hash=3710082365)


class UnderYourSkin(RollDefinition):
    """
    Void Combat Bow, Precision Frame, Anti-Barrier, Craftable
    Source: Vox Obscura
    https://www.light.gg/db/items/232928045
    https://destiny.report/w/232928045
    """
    item = Item('Under Your Skin', hash=232928045)
