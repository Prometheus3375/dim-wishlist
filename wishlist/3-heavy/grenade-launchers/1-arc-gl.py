from wishlist import *
from . import *


class Doomsday(RollDefinition):
    """
    Arc Drum Grenade Launcher, Adaptive Frame, Anti-Barrier
    Source: Gambit
    https://www.light.gg/db/items/713132408
    https://destiny.report/w/713132408
    """
    item = Item('Doomsday', hash=713132408)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.AutoLoadingHolster],
            [trait.SuperchargedMagazine],
            [trait.EnviousArsenal],
            [trait.BaitAndSwitch],
            [trait.ExplosiveLight],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_mags,
            [trait.SuperchargedMagazine, trait.EnviousArsenal, trait.AutoLoadingHolster],
            [trait.ExplosiveLight, trait.BaitAndSwitch],
            ),
        ]


class Tarnation(RollDefinition):
    """
    Arc Drum Grenade Launcher, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Wellspring Boss Vezuul, Lightflayer
    https://www.light.gg/db/items/2721157927
    https://destiny.report/w/2721157927
    """
    item = Item('Tarnation', hash=2721157927)
    roll = Roll(
        'Damage dealing',
        default_barrels,
        default_mags,
        [trait.EnviousAssassin],
        [trait.ExplosiveLight],
        )


class WendigoGL3(RollDefinition):
    """
    Arc Drum Grenade Launcher, Adaptive Frame, Anti-Barrier
    Source: Commander Zavala
    https://www.light.gg/db/items/4021098353
    https://destiny.report/w/4021098353
    """
    items = [
        Item('Wendigo GL3', hash=4021098353),
        Item('Wendigo GL3', hash=1854753404),
        Item('Wendigo GL3 (Adept)', hash=3915197957),
        Item('Wendigo GL3', hash=3183283212),
        Item('Wendigo GL3 (Adept)', hash=555148853),
        ]
    roll = Roll(
        'Damage dealing',
        default_barrels,
        default_mags,
        [trait.AutoLoadingHolster],
        [trait.ExplosiveLight],
        )
