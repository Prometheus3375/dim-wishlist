from wishlist import *


class PsiAeternaIV(RollDefinition):
    """
    Arc Pulse Rifle, Micro-Missile Frame, Anti-Unstoppable
    Source: Commander Zavala
    https://www.light.gg/db/items/3556730800
    https://destiny.report/w/3556730800
    """
    items = [
        Item('Psi Aeterna IV', hash=3556730800),
        Item('Psi Aeterna IV', hash=135971347),
        ]
    rolls = [
        Roll(
            'Super roll',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.HighVelocityRounds, AnyPerk],
            [trait.BlastDistributor],
            [trait.TrickleCharge],
            [trait.ElementalHoning],
            [trait.OneForAll],
            ),
        Roll(
            'Damage dealing',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.HighVelocityRounds, AnyPerk],
            [trait.TrickleCharge],
            [trait.ElementalHoning],
            ),
        Roll(
            'Blast Distributor',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds, AnyPerk],
            [trait.BlastDistributor],
            [trait.OneForAll, trait.ElementalHoning],
            ),
        ]


class VeillantifD(RollDefinition):
    """
    Solar Pulse Rifle, Micro-Missile Frame, Anti-Unstoppable
    Source: Sparrow Racing League
    https://www.light.gg/db/items/1361871430
    https://destiny.report/w/1361871430
    """
    items = [
        Item('Veillantif-D', hash=1361871430),
        Item('Veillantif-D', hash=406384293),
        ]


class MintRetrograde(RollDefinition):
    """
    Strand Pulse Rifle, Micro-Missile Frame, Anti-Unstoppable
    Source: Pinnacle Ops
    https://www.light.gg/db/items/1715391576
    https://destiny.report/w/1715391576
    """
    items = [
        Item('Mint Retrograde', hash=1715391576),
        Item('Mint Retrograde', hash=3285784871),
        ]
