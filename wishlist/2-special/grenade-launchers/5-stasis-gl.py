from wishlist import *


class LingeringDread(RollDefinition):
    """
    Stasis Breechloaded Grenade Launcher, Lightweight Frame, Anti-Overload
    Source: Dungeon "Duality"
    https://www.light.gg/db/items/1745368385
    https://destiny.report/w/1745368385
    """
    item = Item('Lingering Dread', hash=1745368385)


class Liturgy(RollDefinition):
    """
    Stasis Breechloaded Grenade Launcher, Double Fire, Anti-Unstoppable
    Source: World
    https://www.light.gg/db/items/3377522331
    https://destiny.report/w/3377522331
    """
    item = Item('Liturgy', hash=3377522331)


class NewPacificEpitaph(RollDefinition):
    """
    Stasis Breechloaded Grenade Launcher, Wave Frame, Anti-Unstoppable
    Source: "Ghosts of the Deep" Dungeon
    https://www.light.gg/db/items/2988180391
    https://destiny.report/w/2988180391
    """
    item = Item('New Pacific Epitaph', hash=2988180391)


class OusterEngine(RollDefinition):
    """
    Stasis Breechloaded Grenade Launcher, Area Denial Frame, Anti-Overload
    Source: Pinnacle Ops
    https://www.light.gg/db/items/2223968549
    https://destiny.report/w/2223968549
    """
    items = [
        Item('Ouster Engine', hash=2223968549),
        Item('Ouster Engine', hash=3718184802),
        ]


class Permafrost(RollDefinition):
    """
    Stasis Breechloaded Grenade Launcher, Wave Frame, Anti-Unstoppable
    Source: The Dawning
    https://www.light.gg/db/items/2922964484
    https://destiny.report/w/2922964484
    """
    items = [
        Item('Permafrost', hash=2922964484),
        Item('Permafrost', hash=2316331767),
        ]
    rolls = [
        Roll(
            'Stasis combo',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.Rimestealer],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Ad clear',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.ImpromptuAmmunition, trait.Demolitionist],
            [trait.CrystallineCorpsebloom, trait.ReapersTithe, trait.OneForAll],
            ),
        Roll(
            'Grenade combo',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        ]
