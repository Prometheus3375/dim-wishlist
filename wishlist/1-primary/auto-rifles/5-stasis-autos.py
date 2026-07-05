from wishlist import *

_default_barrels = [barrel.ArrowheadBrake, AnyPerk]
_default_mags = [magazine.FlaredMagwell, AnyPerk]


class FairJudgment(RollDefinition):
    """
    Stasis Auto Rifle, Precision Frame, Anti-Barrier
    Source: Solo Ops
    https://www.light.gg/db/items/4113452819
    https://destiny.report/w/4113452819
    """
    item = Item('Fair Judgment', hash=4113452819)
    rolls = [
        Roll(
            'Super roll',
            _default_barrels,
            _default_mags,
            [trait.Rimestealer],
            [trait.Deconstruct],
            [trait.Headstone],
            ),
        Roll(
            'Stasis combo',
            _default_barrels,
            _default_mags,
            [trait.Rimestealer],
            [trait.Headstone],
            ),
        ]


class HerodC(RollDefinition):
    """
    Stasis Auto Rifle, High-Impact Frame, Anti-Unstoppable
    Source: The Drifter
    https://www.light.gg/db/items/2065366342
    https://destiny.report/w/2065366342
    """
    item = Item('Herod-C', hash=2065366342)


class HorrorStory(RollDefinition):
    """
    Stasis Auto Rifle, Precision Frame, Anti-Barrier
    Source: Festival of the Lost
    https://www.light.gg/db/items/2884070594
    https://destiny.report/w/2884070594
    """
    item = Item('Horror Story', hash=2884070594)
    rolls = [
        Roll(
            'Super roll',
            _default_barrels,
            _default_mags,
            [trait.Demolitionist],
            [trait.Headstone],
            [trait.AdrenalineJunkie],
            ),
        Roll(
            'Grenade combo',
            _default_barrels,
            _default_mags,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        ]


class Intercalary(RollDefinition):
    """
    Stasis Auto Rifle, Adaptive Frame, Anti-Barrier
    Source: The Desert Perpetual (Both)
    https://www.light.gg/db/items/2725426834
    https://destiny.report/w/2725426834
    """
    item = Item('Intercalary', hash=2725426834)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            _default_barrels,
            _default_mags,
            [trait.Headstone],
            [trait.Demolitionist],
            [trait.Rimestealer],
            [trait.OneForAll],
            ),
        Roll(
            'Stasis combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Headstone],
            [trait.Rimestealer],
            ),
        Roll(
            'One for All',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Headstone, trait.Demolitionist],
            [trait.OneForAll],
            ),
        ]


class VeiledThreat(RollDefinition):
    """
    Stasis Auto Rifle, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Exotic mission "Encore"
    https://www.light.gg/db/items/3685470415
    https://destiny.report/w/3685470415
    """
    item = Item('Veiled Threat', hash=3685470415)
