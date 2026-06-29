from wishlist import *


class AbideTheReturn(RollDefinition):
    """
    Solar Sword, Adaptive Frame, Anti-Barrier
    Source: The Dreaming City
    https://www.light.gg/db/items/1291270049
    https://destiny.report/w/1291270049
    """
    item = Item('Abide the Return', hash=1291270049)


class SolasScar(RollDefinition):
    """
    Solar Sword, Caster Frame, Anti-Barrier
    Source: Trials of Osiris
    https://www.light.gg/db/items/4089030727
    https://destiny.report/w/4089030727
    """
    item = Item("Sola's Scar", hash=4089030727)


class Synanceia(RollDefinition):
    """
    Solar Sword, Wave Sword Frame, Anti-Unstoppable
    Source: Reclamation Events
    https://www.light.gg/db/items/1823308496
    https://destiny.report/w/1823308496
    """
    items = [
        Item('Synanceia', hash=1823308496),
        Item('Synanceia', hash=2765451288),
        Item('Synanceia', hash=2765451289),
        Item('Synanceia', hash=2765451290),
        Item('Synanceia', hash=2765451291),
        ]
    rolls = [
        Roll(
            'Movement',
            [blade.HonedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.AssassinsBlade],
            [trait.EagerEdge],
            ),
        Roll(
            'Ad clear',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.RelentlessStrikes],
            [trait.ChainReaction],
            ),
        Roll(
            'Damage dealing',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.RelentlessStrikes],
            [trait.Surrounded, trait.ElementalHoning],
            ),
        ]


class Terciopelo4bl(RollDefinition):
    """
    Solar Sword, Lightweight Frame, Anti-Overload
    Source: Sparrow Racing League
    https://www.light.gg/db/items/393652859
    https://destiny.report/w/393652859
    """
    items = [
        Item('Terciopelo-4bl', hash=393652859),
        Item('Terciopelo-4bl', hash=2775462168),
        ]
