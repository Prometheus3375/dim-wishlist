from wishlist import *


class OpaqueHourglass(RollDefinition):
    """
    Arc Crossbow, High-Impact Frame, Anti-Unstoppable
    Source: The Desert Perpetual (Both)
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


class AGoodShout(RollDefinition):
    """
    Void Crossbow, High-Impact Frame, Anti-Unstoppable
    Source: Commander Zavala
    https://www.light.gg/db/items/3615748501
    https://destiny.report/w/3615748501
    """
    items = [
        Item('A Good Shout', hash=3615748501),
        Item('A Good Shout', hash=649691506),
        ]
    rolls = [
        Roll(
            'Ad clear',
            [rail.LowProfileRail, AnyPerk],
            [bolt.HeavyBolts, AnyPerk],
            [trait.BoltScavenger, trait.WitheringGaze],
            [trait.Butterfly],
            ),
        Roll(
            'Void combo',
            [rail.LowProfileRail, AnyPerk],
            [bolt.HeavyBolts, AnyPerk],
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Damage dealing',
            [rail.LowProfileRail, AnyPerk],
            [bolt.HeavyBolts, AnyPerk],
            [trait.EnviousArsenal, trait.WitheringGaze, trait.BoltScavenger],
            [trait.BoxBreathing, trait.HighGround],
            ),
        ]


class Submersion(RollDefinition):
    """
    Stasis Crossbow, High-Impact Frame, Anti-Unstoppable
    Source: Reclamation Events
    https://www.light.gg/db/items/3524386983
    https://destiny.report/w/3524386983
    """
    items = [
        Item('Submersion', hash=3524386983),
        Item('Submersion', hash=1724104236),
        ]
    rolls = [
        Roll(
            'Damage dealing',
            [rail.LowProfileRail, AnyPerk],
            [bolt.HeavyBolts, AnyPerk],
            [trait.ImpulseAmplifier, trait.BoltScavenger, trait.AutoLoadingHolster],
            [trait.AggregateCharge, trait.HighGround, trait.FiringLine],
            ),
        Roll(
            """
            Chill Clip.
            Both Serrated Bolts and Explosive Bolts shatter targets frozen by Chill Clip.
            """,
            [rail.LowProfileRail, AnyPerk],
            [bolt.SerratedBolts, bolt.ExplosiveBolts, bolt.HeavyBolts, AnyPerk],
            [trait.ImpulseAmplifier, trait.BoltScavenger, trait.AutoLoadingHolster],
            [trait.ChillClip],
            ),
        Roll(
            """
            Headstone.
            Explosive Bolts do not explode Stasis crystals on Ultimatum.
            They also prevent killing Elite combatants with precision hits.
            Anyway, crystals can explode instantly because of the movement of a killing bolt.
            """,
            [rail.LowProfileRail, AnyPerk],
            [bolt.HeavyBolts, AnyPerk],
            [trait.ImpulseAmplifier, trait.BoltScavenger, trait.AutoLoadingHolster],
            [trait.Headstone],
            ),
        ]
