from wishlist import *
from . import *


class BoldEndings(RollDefinition):
    """
    Stasis Hand Cannon, Heavy Burst, Anti-Unstoppable, Craftable
    Source: The Pale Heart
    https://www.light.gg/db/items/496728945
    https://destiny.report/w/496728945
    """
    item = Item('Bold Endings', hash=496728945)
    roll = Roll(
        'Stasis combo',
        [barrel.ChamberedCompensator, AnyPerk],
        default_mags,
        [trait.Rimestealer, trait.Headstone],
        [trait.CrystallineCorpsebloom],
        )


class Eyasluna(RollDefinition):
    """
    Stasis Hand Cannon, Adaptive Frame, Anti-Barrier
    Source: Grasp of Avarice
    https://www.light.gg/db/items/386864872
    https://destiny.report/w/386864872
    """
    item = Item('Eyasluna', hash=386864872)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            [magazine.AlloyMagazine, AnyPerk],
            [trait.Firefly],
            [trait.Meganeura],
            [trait.Headstone],
            [trait.ChaosReshaped],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Precision combo',
            default_barrels,
            [magazine.AlloyMagazine, AnyPerk],
            [trait.Meganeura, trait.Firefly],
            [trait.Headstone],
            ),
        ]


class Judgment(RollDefinition):
    """
    Stasis Hand Cannon, Adaptive Frame, Anti-Barrier
    Source: Dungeon "Prophecy"
    https://www.light.gg/db/items/1567585973
    https://destiny.report/w/1567585973
    """
    item = Item('Judgment', hash=1567585973)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Headstone],
            [trait.Demolitionist],
            [trait.CrystallineCorpsebloom],
            [trait.TimedPayload],
            [trait.AdrenalineJunkie],
            [trait.Rimestealer],
            ),
        Roll(
            'Stasis combo',
            default_barrels,
            default_mags,
            [trait.Headstone, trait.CrystallineCorpsebloom],
            [trait.Rimestealer],
            ),
        Roll(
            'Grenade combo',
            default_barrels,
            default_mags,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        ]


class LoudLullaby(RollDefinition):
    """
    Stasis Hand Cannon, Aggressive Frame, Anti-Unstoppable
    Source: The Moon
    https://www.light.gg/db/items/868076517
    https://destiny.report/w/868076517
    """
    item = Item('Loud Lullaby', hash=868076517)


class ModifiedB7Pistol(RollDefinition):
    """
    Stasis Hand Cannon, Dynamic Heat Weapon, Anti-Overload
    Source: Lawless Frontier
    https://www.light.gg/db/items/3146657388
    https://destiny.report/w/3146657388
    """
    items = [
        Item('Modified B-7 Pistol', hash=3146657388),
        Item('Modified B-7 Pistol', hash=1872906663),
        ]
    rolls = [
        Roll(
            'Super roll',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.Rimestealer],
            [trait.Firefly],
            [trait.Demolitionist],
            [trait.Headstone],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Stasis combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.Rimestealer],
            [trait.Headstone, trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Precision combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.Firefly],
            [trait.Headstone],
            ),
        ]


class SolemnRemembrance(RollDefinition):
    """
    Stasis Hand Cannon, Precision Frame, Anti-Barrier
    Source: Competitive Crucible
    https://www.light.gg/db/items/4116518582
    https://destiny.report/w/4116518582
    """
    item = Item('Solemn Remembrance', hash=4116518582)
    rolls = [
        Roll(
            'Super roll',
            [barrel.ArrowheadBrake, AnyPerk],
            default_mags,
            [trait.ImpromptuAmmunition],
            [trait.Headstone],
            [trait.Firefly],
            [trait.Rimestealer],
            [grip.CombatGrip, AnyPerk],
            ),
        Roll(
            'Precision combo',
            [barrel.ArrowheadBrake, AnyPerk],
            default_mags,
            [trait.Headstone],
            [trait.Firefly],
            [grip.CombatGrip, AnyPerk],
            ),
        Roll(
            'Stasis combo',
            [barrel.ArrowheadBrake, AnyPerk],
            default_mags,
            [trait.Headstone],
            [trait.Rimestealer],
            [grip.CombatGrip, AnyPerk],
            ),
        ]


class SomethingNew(RollDefinition):
    """
    Stasis Hand Cannon, Aggressive Frame, Anti-Unstoppable
    Source: Solstice
    https://www.light.gg/db/items/1705150753
    https://destiny.report/w/1705150753
    """
    items = [
        Item('Something New', hash=1705150753),
        Item('Something New', hash=2877020298),
        ]


class SpareRations(RollDefinition):
    """
    Stasis Hand Cannon, Lightweight Frame, Anti-Overload
    Source: Gambit
    https://www.light.gg/db/items/810474119
    https://destiny.report/w/810474119
    """
    item = Item('Spare Rations', hash=810474119)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Firefly],
            [trait.CrystallineCorpsebloom],
            [trait.OneForAll],
            [trait.ExplosivePayload],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.Firefly, trait.CrystallineCorpsebloom],
            [trait.OneForAll],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.CrystallineCorpsebloom],
            [trait.ExplosivePayload],
            ),
        ]


class Vulpecula(RollDefinition):
    """
    Stasis Hand Cannon, Precision Frame, Anti-Barrier
    Source: The Shattered Throne
    https://www.light.gg/db/items/3245446311
    https://destiny.report/w/3245446311
    """
    item = Item('Vulpecula', hash=3245446311)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.ShootToLoot],
            [trait.Headstone],
            [trait.Rimestealer],
            [trait.ExplosivePayload],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Stasis combo',
            default_barrels,
            default_mags,
            [trait.Headstone, trait.Rimestealer],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Shoot to Loot',
            default_barrels,
            default_mags,
            [trait.ShootToLoot],
            [trait.ExplosivePayload],
            ),
        ]
