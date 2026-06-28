from wishlist import *


class WickedSister(RollDefinition):
    """
    Strand Drum Grenade Launcher, Adaptive Frame
    """
    item = Item('Wicked Sister', hash=2039776723)
    rolls = [
        Roll(
            'Damage dealing',
            [launcher_barrel.HardLaunch, AnyPerk],
            [magazine.SpikeGrenades, AnyPerk],
            [trait.EnviousArsenal, trait.EnviousAssassin, trait.AutoLoadingHolster],
            [trait.BaitAndSwitch],
            ),
        Roll(
            'High DPS',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.SpikeGrenades, AnyPerk],
            [trait.EnviousArsenal, trait.EnviousAssassin, trait.AutoLoadingHolster],
            [trait.ExplosiveLight],
            ),
        ]
