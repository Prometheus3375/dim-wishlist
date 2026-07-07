from wishlist import *

_default_barrels = [barrel.ArrowheadBrake, AnyPerk]
_default_mags = [magazine.FlaredMagwell, AnyPerk]


class AuricDisabler(RollDefinition):
    """
    Strand Auto Rifle, Precision Frame, Anti-Barrier
    Source: Saint-14
    https://www.light.gg/db/items/702001725
    https://destiny.report/w/702001725
    """
    item = Item('Auric Disabler', hash=702001725)
    rolls = [
        Roll(
            'Super roll',
            _default_barrels,
            _default_mags,
            [trait.Dragonfly],
            [trait.Hatchling],
            [trait.Slice],
            [trait.Tear],
            ),
        Roll(
            'Ad clear',
            _default_barrels,
            _default_mags,
            [trait.Dragonfly, trait.Hatchling],
            [trait.Tear],
            ),
        ]


class LethalAbundance(RollDefinition):
    """
    Strand Auto Rifle, High-Impact Frame, Anti-Unstoppable
    Source: Iron Banner
    https://www.light.gg/db/items/1884897339
    https://destiny.report/w/1884897339
    """
    item = Item('Lethal Abundance', hash=1884897339)
    rolls = [
        Roll(
            'Super roll',
            _default_barrels,
            _default_mags,
            [trait.Dragonfly],
            [trait.Hatchling],
            [trait.Slice],
            [trait.Tear],
            ),
        Roll(
            'Ad clear',
            _default_barrels,
            _default_mags,
            [trait.Dragonfly, trait.Hatchling],
            [trait.Tear],
            ),
        ]


class Perpetualis(RollDefinition):
    """
    Strand Auto Rifle, Adaptive Frame, Anti-Barrier, Craftable
    Source: NODE.OVRD.AVALON
    https://www.light.gg/db/items/392008588
    https://destiny.report/w/392008588
    """
    item = Item('Perpetualis', hash=392008588)


class RufussFury(RollDefinition):
    """
    Strand Auto Rifle, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Root of Nightmares
    https://www.light.gg/db/items/484515708
    https://destiny.report/w/484515708
    """
    items = [
        Item("Rufus's Fury", hash=484515708),
        Item("Rufus's Fury (Adept)", hash=342514437),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            _default_barrels,
            _default_mags,
            [trait.Reconstruction],
            [trait.Demolitionist],
            [trait.Slice],
            [trait.AdrenalineJunkie],
            [trait.Hatchling],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Ad clear',
            _default_barrels,
            _default_mags,
            [trait.Reconstruction],
            [trait.Hatchling, trait.ChaosReshaped],
            ),
        Roll(
            'Grenade combo',
            _default_barrels,
            _default_mags,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        ]


class TheForwardPath(RollDefinition):
    """
    Strand Auto Rifle, Adaptive Frame, Anti-Barrier
    Source: Iron Banner
    https://www.light.gg/db/items/1884897338
    https://destiny.report/w/1884897338
    """
    item = Item('The Forward Path', hash=1884897338)
    rolls = [
        Roll(
            'Super roll',
            _default_barrels,
            _default_mags,
            [trait.Slice],
            [trait.Demolitionist],
            [trait.Hatchling],
            [trait.Tear],
            ),
        Roll(
            'Strand combo',
            _default_barrels,
            _default_mags,
            [trait.Slice],
            [trait.Hatchling, trait.Tear],
            ),
        ]
