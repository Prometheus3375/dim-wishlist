from database import *


# Special


class Trachinus(RollDefinition):
    """
    Stasis Shotgun, Rapid Fire Slug
    https://www.light.gg/db/items/3635232671
    """
    items = [
        Item(name='Trachinus', hash=3635232671),
        Item(name='Trachinus', hash=2888021252),
        Item(name='Trachinus', hash=2888021253),
        ]


# Heavy


class Synanceia(RollDefinition):
    """
    Solar Sword, Wave Sword Frame
    https://www.light.gg/db/items/1823308496
    """
    items = [
        Item(name='Synanceia', hash=1823308496),
        Item(name='Synanceia', hash=2765451290),
        Item(name='Synanceia', hash=2765451291),
        ]
    rolls = [
        Roll(
            'Movement',
            [blades.JaggedEdge, AnyPerk],
            [guards.SwordmastersGuard, AnyPerk],
            [traits.AssassinsBlade],
            [traits.EagerEdge],
            ),
        Roll(
            'Ad clear',
            [blades.JaggedEdge, AnyPerk],
            [guards.SwordmastersGuard, AnyPerk],
            [traits.AssassinsBlade, traits.RelentlessStrikes],
            [traits.ChainReaction],
            ),
        Roll(
            'Damage dealing',
            [blades.JaggedEdge, AnyPerk],
            [guards.SwordmastersGuard, AnyPerk],
            [traits.RelentlessStrikes],
            [traits.Surrounded],
            ),
        ]
