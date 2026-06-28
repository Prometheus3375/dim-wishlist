from wishlist import *


class OpaqueHourglass(RollDefinition):
    """
    Arc Crossbow, High-Impact Frame, Anti-Unstoppable
    Source: "The Desert Perpetual" Raid
    https://www.light.gg/db/items/1553681400
    https://destiny.report/w/1553681400
    """
    item = Item('Opaque Hourglass', hash=1553681400)
    rolls = [
        Roll(
            'Damage dealing',
            [rail.LowProfileRail, AnyPerk],
            [bolt.HeavyBolts, AnyPerk],
            [trait.ImpulseAmplifier, trait.BoltScavenger],
            [trait.ElementalHoning, trait.Frenzy],
            ),
        Roll(
            """
            Ad clear.
            Explosive Bolts prevent killing Elite combatants with precision hits.
            """,
            [rail.LowProfileRail, AnyPerk],
            [bolt.HeavyBolts, AnyPerk],
            [trait.Firefly],
            [trait.Dragonfly],
            ),
        ]
