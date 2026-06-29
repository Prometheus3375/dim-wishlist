from wishlist import *


class QuaNilusII(RollDefinition):
    """
    Strand Submachine Gun, Adaptive Frame, Anti-Barrier
    Source: Commander Zavala
    https://www.light.gg/db/items/190747610
    https://destiny.report/w/190747610
    """
    item = Item('Qua Nilus II', hash=190747610)
    roll = Roll(
        'PvE',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.FlaredMagwell, AnyPerk],
        [trait.Slice],
        [trait.Hatchling, trait.Surrounded],
        )


class SynchronicRoulette(RollDefinition):
    """
    Strand Submachine Gun, Precision Frame, Anti-Barrier
    Source: Terminal Overload
    https://www.light.gg/db/items/3752860091
    https://destiny.report/w/3752860091
    """
    item = Item('Synchronic Roulette', hash=3752860091)


class TheImmortal(RollDefinition):
    """
    Strand Submachine Gun, Aggressive Frame, Anti-Unstoppable
    Source: Saint-14
    https://www.light.gg/db/items/2872063099
    https://destiny.report/w/2872063099
    """
    item = Item('The Immortal', hash=2872063099)
    rolls = [
        Roll(
            'PvE',
            [barrel.PolygonalRifling, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Hatchling, trait.ThreatDetector],
            [trait.Demolitionist],
            ),
        Roll(
            'PvP',
            [barrel.HammerForgedRifling, barrel.ExtendedBarrel, barrel.Smallbore,
             barrel.CorkscrewRifling],
            [magazine.HighCaliberRounds, magazine.ArmorPiercingRounds, magazine.LightMag,
             magazine.RicochetRounds],
            [trait.DynamicSwayReduction, trait.Rangefinder],
            [trait.LoneWolf],
            ),
        ]
