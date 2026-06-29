from wishlist import *


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
    roll = Roll(
        'Damage dealing',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.TacticalMag, AnyPerk],
        [trait.FourthTimesTheCharm],
        [trait.AggregateCharge, trait.PrecisionInstrument, trait.Surrounded],
        )


class DedGramaryeIV(RollDefinition):
    """
    Arc Shotgun, Lightweight Frame, Anti-Overload
    Source: Banshee-44
    https://www.light.gg/db/items/870893339
    https://destiny.report/w/870893339
    """
    item = Item('Ded Gramarye IV', hash=870893339)


class Matador64(RollDefinition):
    """
    Arc Shotgun, Precision Frame, Anti-Barrier
    Source: Grasp of Avarice
    https://www.light.gg/db/items/1518956169
    https://destiny.report/w/1518956169
    """
    item = Item('Matador 64', hash=1518956169)


class MIDAMacroTool(RollDefinition):
    """
    Arc Shotgun, MIDA Synergy, Anti-Unstoppable
    Source: Lord Shaxx
    https://www.light.gg/db/items/2699423382
    https://destiny.report/w/2699423382
    """
    item = Item('MIDA Macro-Tool', hash=2699423382)
    roll = Roll(
        'PvP',
        [barrel.Smallbore, barrel.CorkscrewRifling, barrel.BarrelShroud],
        [magazine.AccurizedRounds, magazine.LightMag],
        [trait.ThreatDetector],
        [trait.ClosingTime, trait.OpeningShot],
        )


class TheDeicide(RollDefinition):
    """
    Arc Shotgun, Rapid-Fire Frame, Anti-Overload
    Source: Nessus, Unstable Centaur
    https://www.light.gg/db/items/1517780158
    https://destiny.report/w/1517780158
    """
    item = Item('The Deicide', hash=1517780158)


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
