from wishlist import *


class AbyssalEdge(RollDefinition):
    """
    Strand Sword, Wave Sword Frame, Anti-Unstoppable
    Source: Banshee-44
    https://www.light.gg/db/items/2599520828
    https://destiny.report/w/2599520828
    """
    item = Item('Abyssal Edge', hash=2599520828)


class DragoncultSickle(RollDefinition):
    """
    Strand Sword, Caster Frame, Anti-Barrier
    Source: Warlord's Ruin
    https://www.light.gg/db/items/2525261820
    https://destiny.report/w/2525261820
    """
    item = Item('Dragoncult Sickle', hash=2525261820)


class EightySix(RollDefinition):
    """
    Strand Sword, Vortex Frame, Anti-Overload
    Source: Banshee-44
    https://www.light.gg/db/items/2344383760
    https://destiny.report/w/2344383760
    """
    item = Item('Eighty-Six', hash=2344383760)
    rolls = [
        Roll(
            'Damage dealing',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.RelentlessStrikes],
            [trait.Redirection, trait.ElementalHoning],
            ),
        Roll(
            'Ability regen',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.RelentlessStrikes],
            [trait.AttritionOrbs],
            ),
        # Roll(
        #     'Ad clear',
        #     [blade.JaggedEdge, AnyPerk],
        #     [guard.SwordmastersGuard, AnyPerk],
        #     [trait.RelentlessStrikes, trait.TirelessBlade],
        #     [trait.ChainReaction, trait.Hatchling],
        #     ),
        # Roll(
        #     'Damage blocking',
        #     [blade.JaggedEdge, AnyPerk],
        #     [guard.SwordmastersGuard, AnyPerk],
        #     [trait.FlashCounter],
        #     [trait.Hatchling, trait.AttritionOrbs],
        #     ),
        ]


class ThinPrecipice(RollDefinition):
    """
    Strand Sword, Vortex Frame, Anti-Overload, Craftable
    Source:
    https://www.light.gg/db/items/4066778670
    https://destiny.report/w/4066778670
    """
    item = Item('Thin Precipice', hash=4066778670)
