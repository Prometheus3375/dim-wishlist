from wishlist import *


class BadOmens(RollDefinition):
    """
    Void Rocket Launcher, Aggressive Frame, Anti-Unstoppable
    Source: Gambit
    https://www.light.gg/db/items/1996201272
    https://destiny.report/w/1996201272
    """
    item = Item('Bad Omens', hash=1996201272)


class BellowingGiant(RollDefinition):
    """
    Void Rocket Launcher, Adaptive Frame, Anti-Barrier
    Source: Arena Ops
    https://www.light.gg/db/items/412265080
    https://destiny.report/w/412265080
    """
    items = [
        Item('Bellowing Giant', hash=412265080),
        Item('Bellowing Giant', hash=1889005379),
        ]


class FaithKeeper(RollDefinition):
    """
    Void Rocket Launcher, Precision Frame, Anti-Barrier, Craftable
    Source: Exotic mission "Encore"
    https://www.light.gg/db/items/4195186942
    https://destiny.report/w/4195186942
    """
    item = Item('Faith-Keeper', hash=4195186942)


class FoldedRoot(RollDefinition):
    """
    Void Rocket Launcher, Aggressive Frame, Anti-Unstoppable
    Source: Reclamation Events
    https://www.light.gg/db/items/2725894221
    https://destiny.report/w/2725894221
    """
    items = [
        Item('Folded Root', hash=2725894221),
        Item('Folded Root', hash=3184457500),
        Item('Folded Root', hash=3184457501),
        Item('Folded Root', hash=3184457502),
        Item('Folded Root', hash=3184457503),
        ]
    roll = Roll(
        'Damage dealing',
        [launcher_barrel.QuickLaunch, AnyPerk],
        [magazine.ImpactCasing, AnyPerk],
        [trait.ClusterBomb],
        [trait.LastingImpression, trait.Frenzy],
        )


class RedHerring(RollDefinition):
    """
    Void Rocket Launcher, Adaptive Frame, Anti-Barrier, Craftable
    Source: Savathûn's Throne World
    https://www.light.gg/db/items/3175851496
    https://destiny.report/w/3175851496
    """
    item = Item('Red Herring', hash=3175851496)


class TomorrowsAnswer(RollDefinition):
    """
    Void Rocket Launcher, High-Impact Frame, Anti-Unstoppable
    Source: Trials of Osiris
    https://www.light.gg/db/items/1940352487
    https://destiny.report/w/1940352487
    """
    item = Item("Tomorrow's Answer", hash=1940352487)
