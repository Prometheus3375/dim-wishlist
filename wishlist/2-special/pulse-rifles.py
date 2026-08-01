from wishlist import *

default_barrels = [launcher_barrel.VolatileLaunch, AnyPerk]
default_mags = [magazine.HighVelocityRounds, AnyPerk]


class PsiAeternaIV(RollDefinition):
    """
    Arc Pulse Rifle, Micro-Missile Frame, Anti-Unstoppable
    Source: Commander Zavala; Tenet of Bravery
    https://www.light.gg/db/items/3556730800
    https://destiny.report/w/3556730800
    """
    items = [
        Item('Psi Aeterna IV', hash=3556730800),
        Item('Psi Aeterna IV', hash=135971347),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.BlastDistributor],
            [trait.BeaconRounds],
            [trait.TrickleCharge],
            [trait.ElementalHoning],
            [trait.JoltingFeedback],
            [trait.OneForAll],
            ),
        Roll(
            'Miniboss damage',
            default_barrels,
            default_mags,
            [trait.TrickleCharge, trait.BeaconRounds],
            [trait.OneForAll, trait.JoltingFeedback],
            ),
        Roll(
            'Blast Distributor',
            default_barrels,
            default_mags,
            [trait.BlastDistributor],
            [trait.OneForAll, trait.JoltingFeedback],
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
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.HealClip],
            [trait.AirTrigger],
            [trait.BlastDistributor],
            [trait.ParacausalAffinity],
            [trait.Incandescent],
            [trait.SwordLogic],
            ),
        Roll(
            'Miniboss damage',
            default_barrels,
            default_mags,
            [trait.HealClip, trait.AirTrigger],
            [trait.SwordLogic, trait.ParacausalAffinity],
            ),
        Roll(
            'Blast Distributor',
            default_barrels,
            default_mags,
            [trait.BlastDistributor],
            [trait.SwordLogic, trait.ParacausalAffinity],
            ),
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
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.BeaconRounds],
            [trait.RewindRounds],
            [trait.Hatchling],
            [trait.ElementalHoning],
            [trait.MasterOfArms],
            ),
        Roll(
            'Miniboss damage',
            default_barrels,
            default_mags,
            [trait.BeaconRounds, trait.RewindRounds],
            [trait.MasterOfArms, trait.ElementalHoning],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.Hatchling],
            [trait.MasterOfArms, trait.ElementalHoning],
            ),
        ]


class MintRetrogradeOriginal(RollDefinition):
    """
    Strand Pulse Rifle, Micro-Missile Frame, Anti-Unstoppable
    Source: Unobtainable (Pinnacle Ops)
    https://www.light.gg/db/items/42435996
    https://destiny.report/w/42435996
    """
    item = Item('Mint Retrograde', hash=42435996)
    rolls = [
        Roll(
            'Miniboss damage',
            default_barrels,
            default_mags,
            [trait.BeaconRounds, trait.RewindRounds],
            [trait.OneForAll, trait.ElementalHoning],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.Hatchling],
            [trait.OneForAll, trait.ElementalHoning],
            ),
        ]
