from wishlist import *


class WickedSister(RollDefinition):
    """
    Strand Drum Grenade Launcher, Adaptive Frame
    """
    item = Item(name='Wicked Sister', hash=2039776723)
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


class Cynosure(RollDefinition):
    """
    Strand Rocket launcher, Adaptive Frame
    https://www.light.gg/db/items/694275488
    """
    item = Item(name='Cynosure', hash=694275488)
    roll = Roll(
        'Damage dealing',
        [launcher_barrel.QuickLaunch, AnyPerk],
        [magazine.ImpactCasing, AnyPerk],
        [trait.Reconstruction, trait.ClownCartridge, trait.EnviousArsenal, trait.Demolitionist],
        [trait.ExplosiveLight, trait.ElementalHoning],
        )
