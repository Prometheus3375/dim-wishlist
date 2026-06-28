from wishlist import *


class GiversBlessing(RollDefinition):
    """
    Kinetic Auto Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/970034755
    """
    item = Item("Giver's Blessing", hash=970034755)
    rolls = [
        Roll(
            'Ammo generation',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.ImpromptuAmmunition],
            [trait.KineticTremors, trait.OneForAll],
            ),
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Demolitionist, trait.FeedingFrenzy],
            [trait.KineticTremors, trait.OneForAll],
            ),
        ]


class LastThursday(RollDefinition):
    """
    Strand Pulse Rifle, Adaptive Frame
    https://www.light.gg/db/items/3813721211
    """
    item = Item('Last Thursday', hash=3813721211)
    rolls = [
        Roll(
            'Slice',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Strategist],
            [trait.Slice],
            ),
        Roll(
            'Hatchling',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Demolitionist, trait.Strategist],
            [trait.Hatchling],
            ),
        ]


class Agape(RollDefinition):
    """
    Solar Hand Cannon, Heavy Burst
    https://www.light.gg/db/items/4124362340
    """
    item = Item('Agape', hash=4124362340)
    rolls = [
        Roll(
            'Lucky Pants combo',
            [barrel.ChamberedCompensator, AnyPerk],
            [magazine.AppendedMag, AnyPerk],
            [trait.RewindRounds],
            [trait.PrecisionInstrument],
            ),
        Roll(
            'Solar combo',
            [barrel.ChamberedCompensator, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.HealClip],
            [trait.Incandescent],
            ),
        ]


class Sublimation(RollDefinition):
    """
    Arc Scout Rifle, High-Impact Frame
    https://www.light.gg/db/items/1674692344
    """
    item = Item('Sublimation', hash=1674692344)


# Special


class Precipial(RollDefinition):
    """
    Void Shotgun, Precision Frame
    https://www.light.gg/db/items/367772693
    """
    item = Item('Precipial', hash=367772693)


# Heavy


class UlteriorObservation(RollDefinition):
    """
    Stasis Machine Gun, Aggressive Frame
    https://www.light.gg/db/items/1079872540
    """
    item = Item('Ulterior Observation', hash=1079872540)
    rolls = [
        Roll(
            'Stasis combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.AppendedMag, AnyPerk],
            [trait.Headstone],
            [trait.Rimestealer],
            ),
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.AppendedMag, AnyPerk],
            [trait.Subsistence, trait.Headstone],
            [trait.KillingTally],
            ),
        ]
