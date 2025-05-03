from database import *


class AnonymousAutumn(RD):
    """
    Arc Sidearm, Lightweight Frame
    https://www.light.gg/db/items/1051949956
    """
    item = Item(name='Anonymous Autumn', hash=1051949956)
    roll = Roll(
        'PvE',
        [traits.EddyCurrent, traits.AttritionOrbs, traits.Demolitionist],
        [traits.Voltshot],
        )


class JoxersLongsword(RD):
    """
    Void Pulse Rifle, Heavy Burst
    https://www.light.gg/db/items/157601190
    """
    item = Item(name="Joxer's Longsword", hash=157601190)
    rolls = [
        Roll(
            'PvE',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.RepulsorBrace, traits.Dragonfly],
            [traits.DestabilizingRounds, traits.Demoralize],
            ),
        Roll(
            'Withering Gaze',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.Demolitionist],
            [traits.WitheringGaze],
            ),
        ]


# Competitive


class RedrixsEstoc(RD):
    """
    Stasis Pulse Rifle, Legacy PR-55 Frame
    https://www.light.gg/db/items/3218364298
    """
    item = Item(name="Redrix's Estoc", hash=3218364298)
    rolls = [
        Roll(
            'PvP',
            [barrels.ArrowheadBrake, barrels.ExtendedBarrel],
            [magazines.AccurizedRounds],
            [traits.LoneWolf],
            [traits.Headseeker],
            [stocks.HandLaidStock, AnyPerk],
            ),
        Roll(
            'PvP hip fire',
            [barrels.ArrowheadBrake, barrels.ExtendedBarrel],
            [magazines.AccurizedRounds],
            [traits.OffhandStrike],
            [traits.Desperado],
            [stocks.ShortActionStock, AnyPerk],
            ),
        Roll(
            'PvE',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, magazines.TacticalMag, AnyPerk],
            [traits.Rimestealer, traits.Demolitionist],
            [traits.Headstone],
            ),
        ]


class Deadlock(RD):
    """
    Stasis Shotgun, Precision Frame
    https://www.light.gg/db/items/2035738085
    """
    item = Item(name='Deadlock', hash=2035738085)
    roll = Roll(
        'PvP',
        [barrels.BarrelShroud, barrels.CorkscrewRifling, barrels.FullChoke],
        [magazines.AccurizedRounds, magazines.LightMag],
        [traits.LoneWolf],
        [traits.ClosingTime],
        [stocks.ShortActionStock, AnyPerk],
        )
