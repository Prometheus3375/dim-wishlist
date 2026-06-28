from wishlist import *


class ModifiedB7Pistol(RollDefinition):
    """
    Stasis Hand Cannon, Dynamic Heat Weapon, Anti-Overload
    Source: Renegades
    https://www.light.gg/db/items/3146657388
    https://destiny.report/w/3146657388
    """
    items = [
        Item('Modified B-7 Pistol', hash=3146657388),
        Item('Modified B-7 Pistol', hash=1872906663),
        ]
    rolls = [
        Roll(
            'Stasis combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.Rimestealer],
            [trait.CrystallineCorpsebloom, trait.Headstone],
            ),
        Roll(
            'Precision combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.Firefly],
            [trait.Headstone],
            ),
        Roll(
            'Demolitionist',
            [barrel.ArrowheadBrake, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.Demolitionist],
            [trait.CrystallineCorpsebloom, trait.Headstone],
            ),
        ]
