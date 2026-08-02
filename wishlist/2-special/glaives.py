from wishlist import *

default_haft = [haft.LowImpedanceWindings, AnyPerk]
rapid_haft = [haft.AuxiliaryReserves, AnyPerk]
default_mag = [magazine.AlloyMagazine, AnyPerk]


class AlbedoWing(RollDefinition):
    """
    Arc Aggressive Glaive, Anti-Unstoppable
    Source: The Dawning
    https://www.light.gg/db/items/2274629609
    https://destiny.report/w/2274629609
    """
    items = [
        Item('Albedo Wing', hash=2274629609),
        Item('Albedo Wing', hash=1845372864),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_haft,
            default_mag,
            [trait.GraveRobber],
            [trait.ReplenishingAegis],
            [trait.DesperateMeasures],
            [trait.CloseToMelee],
            ),
        Roll(
            'Damage blocking',
            default_haft,
            default_mag,
            [trait.ReplenishingAegis, trait.GraveRobber],
            [trait.DesperateMeasures],
            ),
        Roll(
            'Melee damage',
            default_haft,
            default_mag,
            [trait.GraveRobber],
            [trait.CloseToMelee],
            ),
        ]


class Backfang(RollDefinition):
    """
    Arc Rapid-Fire Glaive, Anti-Overload
    Source: The Drifter
    https://www.light.gg/db/items/1277470844
    https://destiny.report/w/1277470844
    """
    items = [
        Item('Backfang', hash=1277470844),
        Item('Backfang', hash=267672635),
        ]
    rolls = [
        Roll(
            'Super roll',
            rapid_haft,
            default_mag,
            [trait.MeleeMomentum],
            [trait.ReplenishingAegis],
            [trait.JoltingFeedback],
            [trait.CloseToMelee],
            ),
        Roll(
            'Damage blocking',
            rapid_haft,
            default_mag,
            [trait.ReplenishingAegis, trait.MeleeMomentum],
            [trait.JoltingFeedback],
            ),
        Roll(
            'Melee damage',
            rapid_haft,
            default_mag,
            [trait.MeleeMomentum],
            [trait.CloseToMelee],
            ),
        ]


class NezarecsWhisper(RollDefinition):
    """
    Arc Adaptive Glaive, Anti-Barrier, Craftable
    Source: Exotic mission "Presage"
    https://www.light.gg/db/items/254636484
    https://destiny.report/w/254636484
    """
    item = Item("Nezarec's Whisper", hash=254636484)


class GreasyLuck(RollDefinition):
    """
    Solar Rapid-Fire Glaive, Anti-Overload
    Source: Dungeon "Ghosts of the Deep"
    https://www.light.gg/db/items/4274165888
    https://destiny.report/w/4274165888
    """
    item = Item('Greasy Luck', hash=4274165888)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            rapid_haft,
            default_mag,
            [trait.MeleeMomentum],
            [trait.Reconstruction],
            [trait.ChaosReshaped],
            [trait.ChainReaction],
            [trait.CloseToMelee],
            [trait.Incandescent],
            ),
        Roll(
            'Damage blocking',
            rapid_haft,
            default_mag,
            [trait.Reconstruction, trait.ChaosReshaped],
            [trait.Incandescent, trait.ChainReaction],
            ),
        Roll(
            'Melee damage',
            rapid_haft,
            default_mag,
            [trait.MeleeMomentum, trait.ChaosReshaped],
            [trait.CloseToMelee],
            ),
        ]


class JudgmentOfKelgorath(RollDefinition):
    """
    Solar Aggressive Glaive, Anti-Unstoppable, Craftable
    Source: Exotic mission "Seraph's Shield"
    https://www.light.gg/db/items/2978226043
    https://destiny.report/w/2978226043
    """
    item = Item('Judgment of Kelgorath', hash=2978226043)
    roll = Roll(
        'Damage blocking',
        default_haft,
        default_mag,
        [trait.ImmovableObject],
        [trait.Incandescent],
        )


class LubraesRuin(RollDefinition):
    """
    Solar Adaptive Glaive, Anti-Barrier, Craftable
    Source: Raid "Vow of the Disciple"
    https://www.light.gg/db/items/2534546147
    https://destiny.report/w/2534546147
    """
    items = [
        Item("Lubrae's Ruin", hash=2534546147),
        Item("Lubrae's Ruin (Adept)", hash=1466006054),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_haft,
            default_mag,
            [trait.GraveRobber],
            [trait.Frenzy],
            [trait.CloseToMelee],
            [trait.Swashbuckler],
            [trait.Incandescent],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Melee damage',
            default_haft,
            default_mag,
            [trait.CloseToMelee],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Double damage bonus',
            default_haft,
            default_mag,
            [trait.Frenzy],
            [trait.Swashbuckler, trait.ChaosReshaped],
            ),
        ]


class EclipticDistaff(RollDefinition):
    """
    Void Adaptive Glaive, Anti-Barrier
    Source: Solo Ops
    https://www.light.gg/db/items/1942143745
    https://destiny.report/w/1942143745
    """
    item = Item('Ecliptic Distaff', hash=1942143745)
    rolls = [
        Roll(
            'Super roll',
            default_haft,
            default_mag,
            [trait.ReplenishingAegis],
            [trait.GraveRobber],
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            [trait.ChaosReshaped],
            [trait.WitheringGaze],
            ),
        Roll(
            'Damage blocking',
            default_haft,
            default_mag,
            [trait.ReplenishingAegis],
            [trait.ChaosReshaped, trait.DestabilizingRounds, trait.WitheringGaze],
            ),
        Roll(
            """
            Void shield;
            Repulsor Brace can be gained via melee kills
            with Suppressing Glaive from NPA Repulsion Regulator.
            """,
            default_haft,
            default_mag,
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds, trait.ChaosReshaped, trait.WitheringGaze],
            ),
        ]


class ForthcomingDeviance(RollDefinition):
    """
    Void Rapid-Fire Glaive, Anti-Overload, Craftable
    Source: Raid "Salvation's Edge"
    https://www.light.gg/db/items/535198113
    https://destiny.report/w/535198113
    """
    items = [
        Item('Forthcoming Deviance', hash=535198113),
        Item('Forthcoming Deviance (Adept)', hash=3123651616),
        ]
    rolls = [
        Roll(
            'Super roll',
            rapid_haft,
            default_mag,
            [trait.GraveRobber],
            [trait.ReplenishingAegis],
            [trait.RepulsorBrace],
            [trait.CloseToMelee],
            [trait.DestabilizingRounds],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Damage blocking',
            rapid_haft,
            default_mag,
            [trait.ReplenishingAegis],
            [trait.ChaosReshaped, trait.DestabilizingRounds],
            ),
        Roll(
            'Melee damage',
            rapid_haft,
            default_mag,
            [trait.GraveRobber],
            [trait.CloseToMelee],
            ),
        Roll(
            """
            Void shield;
            Repulsor Brace can be gained via melee kills
            with Suppressing Glaive from NPA Repulsion Regulator.
            """,
            rapid_haft,
            default_mag,
            [trait.RepulsorBrace],
            [trait.CloseToMelee, trait.DestabilizingRounds, trait.ChaosReshaped],
            ),
        ]


class TheEnigma(RollDefinition):
    """
    Void Adaptive Glaive, Anti-Barrier, Craftable
    Source: Savathûn's Throne World
    https://www.light.gg/db/items/2595497736
    https://destiny.report/w/2595497736
    """
    item = Item('The Enigma', hash=2595497736)


class TheHeron(RollDefinition):
    """
    Void Aggressive Glaive, Anti-Unstoppable
    Source: Events during season "Lawless"
    https://www.light.gg/db/items/2246386812
    https://destiny.report/w/2246386812
    """
    items = [
        Item('The Heron', hash=2246386812),
        Item('The Heron', hash=617566156),
        Item('The Heron', hash=617566157),
        Item('The Heron', hash=617566158),
        Item('The Heron', hash=617566159),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_haft,
            default_mag,
            [trait.ProximityPower],
            [trait.ReplenishingAegis],
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            [trait.Redirection],
            [trait.CloseToMelee],
            ),
        Roll(
            'Damage blocking',
            default_haft,
            default_mag,
            [trait.ReplenishingAegis],
            [trait.Redirection, trait.DestabilizingRounds],
            ),
        Roll(
            'Melee damage',
            default_haft,
            default_mag,
            [trait.ProximityPower],
            [trait.CloseToMelee],
            ),
        Roll(
            """
            Void shield;
            Repulsor Brace can be gained via melee kills
            with Suppressing Glaive from NPA Repulsion Regulator.
            """,
            default_haft,
            default_mag,
            [trait.RepulsorBrace],
            [trait.CloseToMelee, trait.DestabilizingRounds, trait.Redirection],
            ),
        ]


class RakeAngle(RollDefinition):
    """
    Stasis Aggressive Glaive, Anti-Unstoppable
    Source: Commander Zavala
    https://www.light.gg/db/items/2201323795
    https://destiny.report/w/2201323795
    """
    items = [
        Item('Rake Angle', hash=2201323795),
        Item('Rake Angle', hash=2298039571),
        Item('Rake Angle (Adept)', hash=3997086838),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_haft,
            default_mag,
            [trait.ReplenishingAegis],
            [trait.ChillClip],
            [trait.CloseToMelee],
            ),
        Roll(
            'Damage blocking',
            default_haft,
            default_mag,
            [trait.ReplenishingAegis],
            [trait.ChillClip],
            ),
        ]


class RefusalOfTheCall(RollDefinition):
    """
    Strand Adaptive Glaive, Anti-Barrier
    Source: Dungeon "Pit of Heresy"
    https://www.light.gg/db/items/1541324871
    https://destiny.report/w/1541324871
    """
    item = Item('Refusal of the Call', hash=1541324871)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_haft,
            default_mag,
            [trait.CloseToMelee],
            [trait.Slice],
            [trait.ChainReaction],
            [trait.ReplenishingAegis],
            [trait.DesperateMeasures],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Damage blocking',
            default_haft,
            default_mag,
            [trait.ChainReaction, trait.Slice],
            [trait.ReplenishingAegis],
            ),
        Roll(
            'Melee damage',
            default_haft,
            default_mag,
            [trait.CloseToMelee],
            [trait.ChaosReshaped, trait.DesperateMeasures],
            ),
        ]


class RefusalOfTheCallOriginal(RollDefinition):
    """
    Strand Adaptive Glaive, Anti-Barrier, Legacy
    Source: Unobtainable (Heresy)
    https://www.light.gg/db/items/25228802
    https://destiny.report/w/25228802
    """
    items = [
        Item('Refusal of the Call (Adept)', hash=25228802),
        Item('Refusal of the Call', hash=3269398063),
        Item('Refusal of the Call', hash=2671849376),
        Item('Refusal of the Call (Adept)', hash=2755584425),
        ]
    roll = Roll(
        'Damage blocking',
        default_haft,
        default_mag,
        [trait.ReplenishingAegis],
        [trait.MeleeMomentum],
        )
