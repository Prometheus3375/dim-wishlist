from wishlist import *


class EmptyVessel(RollDefinition):
    """
    Solar Breechloaded Grenade Launcher, Lightweight Frame, Anti-Overload
    Source: Commander Zavala
    https://www.light.gg/db/items/198068259
    https://destiny.report/w/198068259
    """
    item = Item('Empty Vessel', hash=198068259)


class ExplosivePersonality(RollDefinition):
    """
    Solar Breechloaded Grenade Launcher, Wave Frame, Anti-Unstoppable, Craftable
    Source: Season of the Risen
    https://www.light.gg/db/items/4096943616
    https://destiny.report/w/4096943616
    """
    item = Item('Explosive Personality', hash=4096943616)


class Motif41(RollDefinition):
    """
    Solar Breechloaded Grenade Launcher, Area Denial Frame, Anti-Overload
    Source: Banshee-44
    https://www.light.gg/db/items/1685533876
    https://destiny.report/w/1685533876
    """
    item = Item('Motif-41', hash=1685533876)
    rolls = [
        Roll(
            'Ad clear',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.HealClip, trait.AutoLoadingHolster],
            [trait.Incandescent],
            ),
        Roll(
            'Demolitionist',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.HealClip, trait.AutoLoadingHolster],
            [trait.Demolitionist],
            ),
        Roll(
            'Attrition Orbs',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.HealClip, trait.AutoLoadingHolster],
            [trait.AttritionOrbs],
            ),
        ]


class WildStyle(RollDefinition):
    """
    Solar Breechloaded Grenade Launcher, Double Fire, Anti-Unstoppable
    Source: Commander Zavala
    https://www.light.gg/db/items/4021098352
    https://destiny.report/w/4021098352
    """
    item = Item('Wild Style', hash=4021098352)
