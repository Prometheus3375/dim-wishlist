from wishlist import *


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
