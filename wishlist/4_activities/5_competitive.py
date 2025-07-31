from database import *


class SolemnRemembrance(RollDefinition):
    """
    Stasis Hand Cannon, Precision Frame
    https://www.light.gg/db/items/4116518582
    """
    item = Item(name='Solemn Remembrance', hash=4116518582)
    rolls = [
        Roll(
            'Ad clear',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.TacticalMag, AnyPerk],
            [traits.Headstone],
            [traits.Firefly],
            [grips.PolymerGrip, AnyPerk],
            ),
        Roll(
            'Stasis combo',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.TacticalMag, AnyPerk],
            [traits.Headstone],
            [traits.Rimestealer],
            [grips.PolymerGrip, AnyPerk],
            ),
        ]


class RedrixsEstoc(RollDefinition):
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


# Special


class Deadlock(RollDefinition):
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
