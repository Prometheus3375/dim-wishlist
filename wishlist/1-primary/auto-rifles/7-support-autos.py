from wishlist import *

default_barrels = [barrel.HammerForgedRifling, AnyPerk]
default_mags = [magazine.AlloyMagazine, AnyPerk]


class ChrysuraMelo(RollDefinition):
    """
    Arc Auto Rifle, Support Frame, Anti-Overload
    Source: Dungeon "The Shattered Throne"
    https://www.light.gg/db/items/1750388538
    https://destiny.report/w/1750388538
    """
    item = Item('Chrysura Melo', hash=1750388538)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Physic],
            [trait.JoltingFeedback],
            [trait.LeadFromLight],
            [trait.SuperchargedMagazine],
            [trait.AttritionOrbs],
            ),
        Roll(
            'Arc combo',
            default_barrels,
            default_mags,
            [trait.JoltingFeedback],
            [trait.SuperchargedMagazine],
            ),
        Roll(
            'Orb combo',
            default_barrels,
            default_mags,
            [trait.LeadFromLight],
            [trait.AttritionOrbs],
            ),
        ]


class NoHesitation(RollDefinition):
    """
    Solar Auto Rifle, Support Frame, Anti-Overload, Craftable
    Source: The Pale Heart
    https://www.light.gg/db/items/1801007332
    https://destiny.report/w/1801007332
    """
    item = Item('No Hesitation', hash=1801007332)
    is_chosen = True
    roll = Roll(
        'Self-healing',
        default_barrels,
        default_mags,
        [trait.Physic],
        [trait.Incandescent, trait.ChaosReshaped],
        )


class CuspSempiternal(RollDefinition):
    """
    Void Auto Rifle, Support Frame, Anti-Overload
    Source: Epic raid "The Desert Perpetual"
    https://www.light.gg/db/items/2579693381
    https://destiny.report/w/2579693381
    """
    item = Item('Cusp Sempiternal', hash=2579693381)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Reciprocity],
            [trait.RepulsorBrace],
            [trait.WitheringGaze],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Self-healing',
            default_barrels,
            default_mags,
            [trait.Reciprocity],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Void combo',
            default_barrels,
            default_mags,
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        ]


class DECATUR02(RollDefinition):
    """
    Stasis Auto Rifle, Support Frame, Anti-Overload
    Source: Distortions
    https://www.light.gg/db/items/1850748385
    https://destiny.report/w/1850748385
    """
    item = Item('DECATUR 02', hash=1850748385)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Physic],
            [trait.CrystallineCorpsebloom],
            [trait.Redirection],
            [trait.Reciprocity],
            [trait.Rimestealer],
            ),
        Roll(
            'Self-sustain',
            default_barrels,
            default_mags,
            [trait.Physic],
            [trait.Reciprocity],
            ),
        Roll(
            'Stasis combo',
            default_barrels,
            default_mags,
            [trait.CrystallineCorpsebloom],
            [trait.Rimestealer],
            ),
        Roll(
            'Origin trait combo',
            default_barrels,
            default_mags,
            [trait.CrystallineCorpsebloom],
            [trait.Redirection],
            ),
        ]


class Adamantite(RollDefinition):
    """
    Strand Auto Rifle, Support Frame, Anti-Overload
    Source: Dungeon "Pit of Heresy"
    https://www.light.gg/db/items/621450049
    https://destiny.report/w/621450049
    """
    item = Item('Adamantite', hash=621450049)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Reciprocity],
            [trait.ImpromptuAmmunition],
            [trait.Hatchling],
            [trait.Tear],
            ),
        Roll(
            'Self-healing',
            default_barrels,
            default_mags,
            [trait.Reciprocity],
            [trait.Hatchling],
            ),
        ]
