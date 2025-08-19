from database import *


class WickedSister(RollDefinition):
    """
    Strand Drum Grenade Launcher, Adaptive Frame
    """
    item = Item(name='Wicked Sister', hash=2039776723)
    rolls = [
        Roll(
            'Damage dealing',
            [barrels.HardLaunch, AnyPerk],
            [magazines.SpikeGrenades, AnyPerk],
            [traits.EnviousArsenal, traits.EnviousAssassin, traits.AutoLoadingHolster],
            [traits.BaitAndSwitch],
            ),
        Roll(
            'High DPS',
            [barrels.QuickLaunch, AnyPerk],
            [magazines.SpikeGrenades, AnyPerk],
            [traits.EnviousArsenal, traits.EnviousAssassin, traits.AutoLoadingHolster],
            [traits.ExplosiveLight],
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
        [barrels.QuickLaunch, AnyPerk],
        [magazines.ImpactCasing, AnyPerk],
        [traits.Reconstruction, traits.ClownCartridge, traits.EnviousArsenal, traits.Demolitionist],
        [traits.ExplosiveLight, traits.ElementalHoning],
        )
