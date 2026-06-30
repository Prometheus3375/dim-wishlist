from wishlist import *


class ADistantPull(RollDefinition):
    """
    Stasis Sniper Rifle, Rapid-Fire Frame, Anti-Overload, Craftable
    Source:
    https://www.light.gg/db/items/1769847435
    https://destiny.report/w/1769847435
    """
    item = Item('A Distant Pull', hash=1769847435)


class ConspiracyHoned(RollDefinition):
    """
    Stasis Sniper Rifle, Dynamic Heat Weapon, Anti-Overload
    Source: Equilibrium
    https://www.light.gg/db/items/4062069077
    https://destiny.report/w/4062069077
    """
    item = Item('Conspiracy Honed', hash=4062069077)
    rolls = [
        Roll(
            """
            Damage dealing.
            410 Heat Gen allows to shoot 4 rounds before overheating.
            """,
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.VorpalWeapon, trait.CoolingBaubles],
            [trait.BaitAndSwitch],
            ),
        ]


class CriticalAnomaly(RollDefinition):
    """
    Stasis Sniper Rifle, Aggressive Frame, Anti-Unstoppable, Craftable
    Source: "Salvation's Edge" Raid
    https://www.light.gg/db/items/445197843
    https://destiny.report/w/445197843
    """
    items = [
        Item('Critical Anomaly', hash=445197843),
        Item('Critical Anomaly (Adept)', hash=172461430),
        ]


class LocusLocutus(RollDefinition):
    """
    Stasis Sniper Rifle, Adaptive Frame, Anti-Barrier, Craftable
    Source: Season of the Witch
    https://www.light.gg/db/items/4132072834
    https://destiny.report/w/4132072834
    """
    item = Item('Locus Locutus', hash=4132072834)


class Thoughtless(RollDefinition):
    """
    Stasis Sniper Rifle, Adaptive Frame, Anti-Barrier, Craftable
    Source: Season Pass Reward
    https://www.light.gg/db/items/4067556514
    https://destiny.report/w/4067556514
    """
    item = Item('Thoughtless', hash=4067556514)
