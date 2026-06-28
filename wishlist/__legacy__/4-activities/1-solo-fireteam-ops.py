from wishlist import *


class Jurisprudent(RollDefinition):
    """
    Stasis Scout Rifle, High-Impact Frame
    https://www.light.gg/db/items/4090134063
    """
    item = Item('Jurisprudent', hash=4090134063)


class FaustusDecline(RollDefinition):
    """
    Stasis Sidearm, Lightweight Frame
    https://www.light.gg/db/items/1663482635
    """
    item = Item('Faustus Decline', hash=1663482635)
    roll = Roll(
        'PvE',
        [barrel.Smallbore, AnyPerk],
        [magazine.FlaredMagwell, AnyPerk],
        [trait.Demolitionist, trait.Rimestealer],
        [trait.Headstone],
        )


class AhabChar(RollDefinition):
    """
    Solar Auto Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/1411560894
    """
    item = Item('Ahab Char', hash=1411560894)
    roll = Roll(
        'PvE',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.FlaredMagwell, AnyPerk],
        [trait.HealClip],
        [trait.BurningAmbition, trait.KillClip],
        )


class Drang(RollDefinition):
    """
    Solar Sidearm, Adaptive Frame
    https://www.light.gg/db/items/358190158
    """
    item = Item('Drang', hash=358190158)
    roll = Roll(
        'Solar combo',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.TacticalMag, AnyPerk],
        [trait.HealClip],
        [trait.Incandescent],
        )


class MIDAMiniTool(RollDefinition):
    """
    Solar Submachine Gun, Lightweight Frame
    https://www.light.gg/db/items/3946054154
    """
    item = Item('MIDA Mini-Tool', hash=3946054154)
    roll = Roll(
        'Solar combo',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.FlaredMagwell, AnyPerk],
        [trait.HealClip],
        [trait.Incandescent],
        )


# Special


class ShorelineDissident(RollDefinition):
    """
    Void Sniper Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/1193318082
    """
    item = Item('Shoreline Dissident', hash=1193318082)
    roll = Roll(
        'Damage dealing',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.TacticalMag, AnyPerk],
        [trait.TripleTap],
        [trait.PrecisionInstrument],
        )


class HawthornesFieldForgedShotgun(RollDefinition):
    """
    Stasis Shotgun, Lightweight Frame
    https://www.light.gg/db/items/1402874079
    """
    item = Item("Hawthorne's Field-Forged Shotgun", hash=1402874079)
    rolls = [
        Roll(
            'PvP',
            [barrel.Smallbore, barrel.CorkscrewRifling, barrel.BarrelShroud],
            [magazine.AccurizedRounds, magazine.LightMag],
            [trait.ThreatDetector, trait.LoneWolf],
            [trait.OpeningShot, trait.ClosingTime],
            ),
        Roll(
            'Ad clear',
            [barrel.BarrelShroud, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.ThreatDetector],
            [trait.CrystallineCorpsebloom],
            ),
        ]


class Monody44(RollDefinition):
    """
    Void Fusion Rifle, High-Impact Frame
    https://www.light.gg/db/items/3201200906
    """
    item = Item('Monody-44', hash=3201200906)


class Motif41(RollDefinition):
    """
    Solar Breechloaded Grenade Launcher, Area Denial Frame
    https://www.light.gg/db/items/1685533876
    """
    item = Item('Motif-41', hash=1685533876)
    rolls = [
        Roll(
            'Ad clear',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.HealClip, trait.AutoLoadingHolster],
            [trait.Incandescent],
            ),
        Roll(
            'Demolitionist',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.HealClip, trait.AutoLoadingHolster],
            [trait.Demolitionist],
            ),
        Roll(
            'Attrition Orbs',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.HealClip, trait.AutoLoadingHolster],
            [trait.AttritionOrbs],
            ),
        ]


# Heavy


class Haliaetus(RollDefinition):
    """
    Strand Rocket Launcher, High-Impact Frame
    https://www.light.gg/db/items/2155534128
    """
    item = Item('Haliaetus', hash=2155534128)
    rolls = [
        Roll(
            'Damage dealing',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.ImpactCasing, AnyPerk],
            [trait.ClusterBomb, trait.AutoLoadingHolster],
            [trait.AggregateCharge, trait.ReapersTithe, trait.ElementalHoning],
            ),
        Roll(
            'Ad clear',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.AlloyCasing, AnyPerk],
            [trait.ClusterBomb, trait.ImpulseAmplifier],
            [trait.Bipod],
            ),
        ]


class EightySix(RollDefinition):
    """
    Strand Sword, Vortex Frame
    https://www.light.gg/db/items/2344383760
    """
    item = Item('Eighty-Six', hash=2344383760)
    rolls = [
        Roll(
            'Damage dealing',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.RelentlessStrikes],
            [trait.Redirection, trait.ElementalHoning],
            ),
        Roll(
            'Ability regen',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.RelentlessStrikes],
            [trait.AttritionOrbs],
            ),
        # Roll(
        #     'Ad clear',
        #     [blade.JaggedEdge, AnyPerk],
        #     [guard.SwordmastersGuard, AnyPerk],
        #     [trait.RelentlessStrikes, trait.TirelessBlade],
        #     [trait.ChainReaction, trait.Hatchling],
        #     ),
        # Roll(
        #     'Damage blocking',
        #     [blade.JaggedEdge, AnyPerk],
        #     [guard.SwordmastersGuard, AnyPerk],
        #     [trait.FlashCounter],
        #     [trait.Hatchling, trait.AttritionOrbs],
        #     ),
        ]
