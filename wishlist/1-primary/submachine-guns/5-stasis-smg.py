from wishlist import *


class M17FastTalker(RollDefinition):
    """
    Stasis Submachine Gun, Balanced Heat Weapon, Anti-Overload
    Source: Renegades
    https://www.light.gg/db/items/1419158093
    https://destiny.report/w/1419158093
    """
    items = [
        Item('M-17 "Fast Talker"', hash=1419158093),
        Item('M-17 "Fast Talker"', hash=2770035786),
        ]
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ChamberedCompensator, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.Demolitionist],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Damage dealing with Peacekeepers',
            [barrel.ChamberedCompensator, AnyPerk],
            [battery.IonizedHeatsink, AnyPerk],
            [trait.AttritionOrbs],
            [trait.TargetLock],
            ),
        Roll(
            'Damage dealing with Peacekeepers',
            [barrel.ChamberedCompensator, AnyPerk],
            [battery.OverclockedHeatsink, AnyPerk],
            [trait.CoolingBaubles],
            [trait.TargetLock],
            ),
        ]
