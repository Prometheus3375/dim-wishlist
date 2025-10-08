from wishlist import *


class GiversBlessing(RollDefinition):
    """
    Kinetic Auto Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/970034755
    """
    item = Item(name="Giver's Blessing", hash=970034755)
    rolls = [
        Roll(
            'Kinetic Tremors',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.RewindRounds, traits.Demolitionist],
            [traits.KineticTremors],
            ),
        Roll(
            'One for All',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.Demolitionist, traits.FeedingFrenzy],
            [traits.OneForAll],
            ),
        Roll(
            'Ammo generation',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.ImpromptuAmmunition],
            [traits.KineticTremors, traits.OneForAll],
            ),
        ]


class LastThursday(RollDefinition):
    """
    Strand Pulse Rifle, Adaptive Frame
    https://www.light.gg/db/items/3813721211
    """
    item = Item(name='Last Thursday', hash=3813721211)
    rolls = [
        Roll(
            'Slice',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.Strategist],
            [traits.Slice],
            ),
        Roll(
            'Hatchling',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.Demolitionist, traits.Strategist],
            [traits.Hatchling],
            ),
        ]


class Agape(RollDefinition):
    """
    Solar Hand Cannon, Heavy Burst
    https://www.light.gg/db/items/4124362340
    """
    item = Item(name='Agape', hash=4124362340)
    rolls = [
        Roll(
            'Lucky Pants combo',
            [barrels.ChamberedCompensator, AnyPerk],
            [magazines.AppendedMag, AnyPerk],
            [traits.RewindRounds],
            [traits.PrecisionInstrument, traits.VorpalWeapon],
            ),
        Roll(
            'Solar combo',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.HealClip],
            [traits.Incandescent],
            ),
        ]


class Sublimation(RollDefinition):
    """
    Arc Scout Rifle, High-Impact Frame
    https://www.light.gg/db/items/1674692344
    """
    item = Item(name='Sublimation', hash=1674692344)


# Special


class Precipial(RollDefinition):
    """
    Void Shotgun, Precision Frame
    https://www.light.gg/db/items/367772693
    """
    item = Item(name='Precipial', hash=367772693)


# Heavy


class UlteriorObservation(RollDefinition):
    """
    Stasis Machine Gun, Aggressive Frame
    https://www.light.gg/db/items/1079872540
    """
    item = Item(name='Ulterior Observation', hash=1079872540)
    rolls = [
        Roll(
            'Stasis combo',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.AppendedMag, AnyPerk],
            [traits.Headstone],
            [traits.Rimestealer],
            ),
        Roll(
            'Ad clear',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.AppendedMag, AnyPerk],
            [traits.Subsistence, traits.Headstone],
            [traits.KillingTally],
            ),
        ]
