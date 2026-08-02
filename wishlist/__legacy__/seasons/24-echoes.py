from wishlist import *


class MartyrsRetribution(RollDefinition):
    """
    Solar Breechloaded Grenade Launcher, Wave Frame
    https://www.light.gg/db/items/2584830733
    """
    item = Item("Martyr's Retribution", hash=2584830733)
    rolls = [
        Roll(
            """
            Incandescent.
            The preferred roll as there is already a Solar Wave Frame GL
            with damage increase perks: Explosive Personality with One for All
            """,
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.Demolitionist, trait.HealClip],
            [trait.Incandescent],
            ),
        Roll(
            'Clip combo',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.HealClip],
            [trait.KillClip],
            ),
        Roll(
            """
            Adrenaline Junkie.
            For this weapon Adrenaline Junkie is better than Desperate Measures
            because AJ can achieve max stacks easily with 1-2 shots,
            while DM requires two ability kills
            """,
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.Demolitionist, trait.HealClip],
            [trait.AdrenalineJunkie],
            ),
        ]
