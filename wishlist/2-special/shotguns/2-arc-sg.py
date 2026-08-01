from wishlist import *
from . import *


class ArcaneEmbrace(RollDefinition):
    """
    Arc Shotgun, Heavy Burst, Anti-Unstoppable
    Source: Festival of the Lost
    https://www.light.gg/db/items/1813474267
    https://destiny.report/w/1813474267
    """
    items = [
        Item('Arcane Embrace', hash=3328019216),
        Item('Arcane Embrace', hash=1813474267),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.FourthTimesTheCharm],
            [trait.EnviousArsenal],
            [trait.Surrounded],
            [trait.AggregateCharge],
            ),
        Roll(
            'Damage dealing',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.EnviousArsenal, trait.FourthTimesTheCharm],
            [trait.AggregateCharge, trait.Surrounded],
            ),
        ]


class DedGramaryeIV(RollDefinition):
    """
    Arc Shotgun, Lightweight Frame, Anti-Overload
    Source: Banshee-44
    https://www.light.gg/db/items/870893339
    https://destiny.report/w/870893339
    """
    item = Item('Ded Gramarye IV', hash=870893339)
    rolls = [
        Roll(
            'Super roll',
            [barrel.Smallbore, AnyPerk],
            [magazine.LightMag, AnyPerk],
            [trait.ThreatDetector],
            [trait.Discord],
            [trait.Voltshot],
            [trait.ChainReaction],
            ),
        Roll(
            'Ad clear',
            [barrel.Smallbore, AnyPerk],
            [magazine.LightMag, AnyPerk],
            [trait.Discord],
            [trait.ChainReaction],
            ),
        Roll(
            'Ad clear',
            [barrel.Smallbore, AnyPerk],
            [magazine.LightMag, AnyPerk],
            [trait.ThreatDetector],
            [trait.Voltshot],
            ),
        Roll(
            'Discord does not combo with Voltshot',
            [trait.Discord],
            [trait.Voltshot],
            is_trash=True,
            ),
        ]


class FoundVerdict(RollDefinition):
    """
    Arc Shotgun, Aggressive Frame, Anti-Unstoppable, Craftable
    Source: Raid "Vault of Glass"
    https://www.light.gg/db/items/694500607
    https://destiny.report/w/694500607
    """
    items = [
        Item('Found Verdict', hash=694500607),
        Item('Found Verdict (Timelost)', hash=851296754),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            [barrel.Smallbore, AnyPerk],
            [magazine.AccurizedRounds, AnyPerk],
            [trait.ThreatDetector],
            [trait.AggregateCharge],
            [trait.TrenchBarrel],
            [trait.OpeningShot],
            ),
        Roll(
            'PvP',
            [barrel.Smallbore, AnyPerk],
            [magazine.AccurizedRounds, AnyPerk],
            [trait.ThreatDetector],
            [trait.OpeningShot],
            ),
        Roll(
            'Damage dealing',
            [barrel.Smallbore, AnyPerk],
            [magazine.AssaultMag, AnyPerk],
            [trait.AggregateCharge],
            [trait.TrenchBarrel],
            ),
        ]


class Matador64(RollDefinition):
    """
    Arc Shotgun, Precision Frame, Anti-Barrier
    Source: Dungeon "Grasp of Avarice"
    https://www.light.gg/db/items/1518956169
    https://destiny.report/w/1518956169
    """
    item = Item('Matador 64', hash=1518956169)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            pvp_barrels,
            pvp_mags,
            [trait.LoneWolf],
            [trait.ThreatDetector],
            [trait.ClosingTime],
            [trait.OpeningShot],
            ),
        Roll(
            'PvP',
            pvp_barrels,
            pvp_mags,
            [trait.ThreatDetector],
            [trait.OpeningShot],
            ),
        Roll(
            'PvP',
            pvp_barrels,
            pvp_mags,
            [trait.LoneWolf],
            [trait.ClosingTime],
            ),
        ]


class MIDAMacroTool(RollDefinition):
    """
    Arc Shotgun, MIDA Synergy, Anti-Unstoppable
    Source: Lord Shaxx; Tenet of Bravery
    https://www.light.gg/db/items/2699423382
    https://destiny.report/w/2699423382
    """
    item = Item('MIDA Macro-Tool', hash=2699423382)
    rolls = [
        Roll(
            'Super roll',
            pvp_barrels,
            pvp_mags,
            [trait.LoneWolf],
            [trait.ThreatDetector],
            [trait.ClosingTime],
            [trait.OpeningShot],
            ),
        Roll(
            'PvP',
            pvp_barrels,
            pvp_mags,
            [trait.ThreatDetector],
            [trait.OpeningShot],
            ),
        Roll(
            'PvP',
            pvp_barrels,
            pvp_mags,
            [trait.LoneWolf],
            [trait.ClosingTime],
            ),
        ]


class ProphetOfDoom(RollDefinition):
    """
    Arc Shotgun, Precision Frame, Anti-Barrier, Craftable
    Source: Raid "Garden of Salvation"
    https://www.light.gg/db/items/2145441168
    https://destiny.report/w/2145441168
    """
    item = Item('Prophet of Doom', hash=2145441168)
    roll = Roll(
        'PvP',
        pvp_barrels,
        pvp_mags,
        [trait.ThreatDetector],
        [trait.OpeningShot],
        )


class TheDeicide(RollDefinition):
    """
    Arc Shotgun, Rapid-Fire Frame, Anti-Overload
    Source: Nessus, Unstable Centaur
    https://www.light.gg/db/items/1517780158
    https://destiny.report/w/1517780158
    """
    item = Item('The Deicide', hash=1517780158)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            [barrel.Smallbore, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.DualLoader],
            [trait.ThreatDetector],
            [trait.AutoLoadingHolster],
            [trait.OneTwoPunch],
            [trait.TrenchBarrel],
            [trait.Voltshot],
            ),
        Roll(
            'Melee damage increase',
            [barrel.Smallbore, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.ThreatDetector],
            [trait.OneTwoPunch],
            ),
        Roll(
            'Ad clear',
            [barrel.Smallbore, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.DualLoader],
            [trait.Voltshot],
            ),
        Roll(
            'Damage dealing',
            [barrel.Smallbore, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.AutoLoadingHolster],
            [trait.TrenchBarrel],
            ),
        ]


class TheInquisitor(RollDefinition):
    """
    Arc Shotgun, Pinpoint Slug Frame, Anti-Barrier
    Source: Trials of Osiris
    https://www.light.gg/db/items/1185633760
    https://destiny.report/w/1185633760
    """
    item = Item('The Inquisitor', hash=1185633760)


class XenoclastIV(RollDefinition):
    """
    Arc Shotgun, Lightweight Frame, Anti-Overload
    Source: Commander Zavala
    https://www.light.gg/db/items/963732594
    https://destiny.report/w/963732594
    """
    item = Item('Xenoclast IV', hash=963732594)
