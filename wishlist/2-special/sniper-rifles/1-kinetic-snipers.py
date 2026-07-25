from wishlist import *
from . import *


class AloneAsAGod(RollDefinition):
    """
    Kinetic Sniper Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Pantheon
    https://www.light.gg/db/items/353884603
    https://destiny.report/w/353884603
    """
    items = [
        Item('Alone as a god', hash=353884603),
        Item('Alone as a god', hash=4278664152),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.StoppingPower],
            [trait.RewindRounds],
            [trait.LuckyShot],
            [trait.KineticTremors],
            [trait.AllStar],
            [trait.AggregateCharge],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.StoppingPower, trait.RewindRounds, trait.LuckyShot],
            [trait.AggregateCharge, trait.AllStar, trait.KineticTremors],
            ),
        ]


class BiteOfTheFox(RollDefinition):
    """
    Kinetic Sniper Rifle, Aggressive Frame, Anti-Unstoppable
    Source: Lord Saladin
    https://www.light.gg/db/items/2851703775
    https://destiny.report/w/2851703775
    """
    item = Item('Bite of the Fox', hash=2851703775)


class DefianceOfYasmin(RollDefinition):
    """
    Kinetic Sniper Rifle, Adaptive Frame, Anti-Barrier, Craftable
    Source: Raid "King's Fall"
    https://www.light.gg/db/items/3228096719
    https://destiny.report/w/3228096719
    """
    items = [
        Item('Defiance of Yasmin', hash=3228096719),
        Item('Defiance of Yasmin (Harrowed)', hash=3503019618),
        ]


class EyeOfSol(RollDefinition):
    """
    Kinetic Sniper Rifle, Adaptive Frame, Anti-Barrier
    Source: Trials of Osiris
    https://www.light.gg/db/items/2499834165
    https://destiny.report/w/2499834165
    """
    item = Item('Eye of Sol', hash=2499834165)


class PraedythsRevenge(RollDefinition):
    """
    Kinetic Sniper Rifle, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Raid "Vault of Glass"
    https://www.light.gg/db/items/3844610113
    https://destiny.report/w/3844610113
    """
    items = [
        Item("Praedyth's Revenge", hash=3844610113),
        Item("Praedyth's Revenge (Timelost)", hash=2362652544),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.FourthTimesTheCharm],
            [trait.KineticTremors],
            [trait.RewindRounds],
            [trait.ElementalHoning],
            [trait.BaitAndSwitch],
            [trait.AllStar],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.KineticTremors, trait.FourthTimesTheCharm, trait.RewindRounds],
            [trait.BaitAndSwitch, trait.ElementalHoning, trait.AllStar],
            ),
        ]


class SomethingSomething(RollDefinition):
    """
    Kinetic Sniper Rifle, Aggressive Frame, Anti-Unstoppable
    Source: Commander Zavala; Tenet of Bravery
    https://www.light.gg/db/items/3421075982
    https://destiny.report/w/3421075982
    """
    items = [
        Item('Something Something', hash=3421075982),
        Item('Something Something', hash=690412397),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.TripleTap],
            [trait.StoppingPower],
            [trait.Discord],
            [trait.ElementalHoning],
            [trait.KineticTremors],
            [trait.Redirection],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.TripleTap, trait.StoppingPower],
            [trait.Redirection, trait.KineticTremors, trait.ElementalHoning],
            ),
        Roll(
            'Stacking Redirection',
            default_barrels,
            default_mags,
            [trait.Discord],
            [trait.Redirection],
            ),
        ]


class Succession(RollDefinition):
    """
    Kinetic Sniper Rifle, Aggressive Frame, Anti-Unstoppable, Craftable
    Source: Raid "Deep Stone Crypt"
    https://www.light.gg/db/items/2990047042
    https://destiny.report/w/2990047042
    """
    item = Item('Succession', hash=2990047042)
    roll = Roll(
        'Support rifle',
        default_barrels,
        default_mags,
        [trait.Reconstruction],
        [trait.Recombination],
        )


class SuccessionOnslaught(RollDefinition):
    """
    Kinetic Sniper Rifle, Aggressive Frame, Anti-Unstoppable
    Source: Onslaught
    https://www.light.gg/db/items/2731922624
    https://destiny.report/w/2731922624
    """
    item = Item('Succession', hash=2731922624)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.KineticTremors],
            [trait.Reconstruction],
            [trait.Recombination],
            [trait.AggregateCharge],
            ),
        Roll(
            'Support rifle',
            default_barrels,
            default_mags,
            [trait.Reconstruction],
            [trait.Recombination],
            ),
        ]


class TheSupremacy(RollDefinition):
    """
    Kinetic Sniper Rifle, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Raid "Last Wish"
    https://www.light.gg/db/items/2884596447
    https://destiny.report/w/2884596447
    """
    item = Item('The Supremacy', hash=2884596447)
    roll = Roll(
        'Sniper spam',
        default_barrels,
        default_mags,
        [trait.RewindRounds],
        [trait.FourthTimesTheCharm],
        )


class Tranquility(RollDefinition):
    """
    Kinetic Sniper Rifle, Adaptive Frame, Anti-Barrier
    Source: The Moon
    https://www.light.gg/db/items/846241148
    https://destiny.report/w/846241148
    """
    item = Item('Tranquility', hash=846241148)
