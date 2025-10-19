from wishlist import *


class RedrixsEstoc(RollDefinition):
    """
    Stasis Pulse Rifle, Legacy PR-55 Frame
    https://www.light.gg/db/items/3218364298
    """
    item = Item(name="Redrix's Estoc", hash=3218364298)
    rolls = [
        Roll(
            'PvP',
            [barrel.ArrowheadBrake, barrel.ExtendedBarrel],
            [magazine.AccurizedRounds],
            [trait.LoneWolf],
            [trait.Headseeker],
            [stock.HandLaidStock, AnyPerk],
            ),
        Roll(
            'PvP hip fire',
            [barrel.ArrowheadBrake, barrel.ExtendedBarrel],
            [magazine.AccurizedRounds],
            [trait.OffhandStrike],
            [trait.Desperado],
            [stock.ShortActionStock, AnyPerk],
            ),
        Roll(
            'PvE',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, magazine.TacticalMag, AnyPerk],
            [trait.Rimestealer, trait.Demolitionist],
            [trait.Headstone],
            ),
        ]


# Special


class Deadlock(RollDefinition):
    """
    Stasis Shotgun, Precision Frame
    https://www.light.gg/db/items/2035738085
    """
    item = Item(name='Deadlock', hash=2035738085)
    roll = Roll(
        'PvP',
        [barrel.BarrelShroud, barrel.CorkscrewRifling, barrel.FullChoke],
        [magazine.AccurizedRounds, magazine.LightMag],
        [trait.ThreatDetector],
        [trait.ClosingTime],
        [stock.ShortActionStock, AnyPerk],
        )
