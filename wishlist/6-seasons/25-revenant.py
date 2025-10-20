from wishlist import *


class Exuviae(RollDefinition):
    """
    Stasis Hand Cannon, Aggressive Frame
    https://www.light.gg/db/items/2823644677
    """
    item = Item('Exuviae', hash=2823644677)


class Insurmountable(RollDefinition):
    """
    Void Sidearm, Precision Frame
    https://www.light.gg/db/items/414045521
    """
    item = Item('Insurmountable', hash=414045521)


class VantagePoint(RollDefinition):
    """
    Arc Pulse Rifle, Adaptive Frame
    https://www.light.gg/db/items/3830941962
    """
    item = Item('Vantage Point', hash=3830941962)
    _mags = [
        magazine.TacticalMag,
        magazine.AppendedMag,
        magazine.AlloyMagazine,
        magazine.FlaredMagwell,
        ]
    roll = Roll(
        'Ad clear',
        [barrel.ArrowheadBrake, AnyPerk],
        _mags,
        [trait.EddyCurrent],
        [trait.JoltingFeedback],
        )


class Liturgy(RollDefinition):
    """
    Stasis Breechloaded Grenade Launcher, Double Fire
    https://www.light.gg/db/items/2599338624
    """
    item = Item('Liturgy', hash=2599338624)
    rolls = [
        Roll(
            'Damage rotations combo',
            [launcher_barrel.HardLaunch, AnyPerk],
            [magazine.SpikeGrenades],
            [trait.EnviousArsenal],
            [trait.ChillClip],
            ),
        ]


class Sovereignty(RollDefinition):
    """
    Void Sniper Rifle, Adaptive Frame
    https://www.light.gg/db/items/3818198556
    """
    item = Item('Sovereignty', hash=3818198556)
    roll = Roll(
        'Withering Gaze. Appended Mag + Backup Mag mod increase mag size to 7',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.AppendedMag, magazine.TacticalMag, magazine.AlloyMagazine,
         magazine.FlaredMagwell],
        [trait.Demolitionist, trait.NoDistractions],
        [trait.WitheringGaze],
        )


class BitterSweet(RollDefinition):
    """
    Arc Drum Grenade Launcher, Adaptive Frame
    https://www.light.gg/db/items/2599338625
    """
    item = Item('Bitter/Sweet', hash=2599338625)
    rolls = [
        Roll(
            'Damage dealing',
            [launcher_barrel.HardLaunch, AnyPerk],
            [magazine.SpikeGrenades, AnyPerk],
            [trait.EnviousArsenal],
            [trait.BaitAndSwitch],
            ),
        Roll(
            'High DPS',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.SpikeGrenades, AnyPerk],
            [trait.EnviousArsenal],
            [trait.ExplosiveLight],
            ),
        ]


class NoxiousVetiver(RollDefinition):
    """
    Arc Submachine Gun, Precision Frame
    https://www.light.gg/db/items/825495813
    """
    item = Item('Noxious Vetiver', hash=825495813)
    _mags = [
        magazine.AlloyMagazine,
        magazine.FlaredMagwell,
        magazine.TacticalMag,
        magazine.AppendedMag,
        ]
    roll = Roll(
        'Roll for ad clear',
        [barrel.ArrowheadBrake, AnyPerk],
        _mags,
        [trait.AttritionOrbs, trait.LooseChange, trait.Pugilist],
        [trait.JoltingFeedback],
        )


class ScavengersFate(RollDefinition):
    """
    Void Shotgun, Precision Frame
    https://www.light.gg/db/items/2913577176
    """
    item = Item("Scavenger's Fate", hash=2913577176)
    roll = Roll(
        'PvP',
        [barrel.BarrelShroud, barrel.CorkscrewRifling, barrel.FullChoke],
        [magazine.AccurizedRounds, magazine.LightMag],
        [trait.LoneWolf],
        [trait.ClosingTime],
        )


class RedTape(RollDefinition):
    """
    Stasis Scout Rifle, Lightweight Frame
    https://www.light.gg/db/items/3423493037
    """
    item = Item('Red Tape', hash=3423493037)
    _barrels = [barrel.ArrowheadBrake, AnyPerk]
    _mags = [
        magazine.TacticalMag,
        magazine.AppendedMag,
        magazine.AlloyMagazine,
        magazine.FlaredMagwell,
        ]
    rolls = [
        Roll(
            'Explosive Payload',
            _barrels,
            _mags,
            [trait.Demolitionist],
            [trait.ExplosivePayload],
            ),
        Roll(
            'Headstone',
            _barrels,
            _mags,
            [trait.Demolitionist, trait.Rimestealer],
            [trait.Headstone],
            ),
        ]


class HereticsFervor(RollDefinition):
    """
    Stasis Rocket Launcher, Aggressive Frame
    https://www.light.gg/db/items/4224667951
    """
    item = Item("Heretic's Fervor", hash=4224667951)
    roll = Roll(
        'Damage dealing',
        [launcher_barrel.QuickLaunch, AnyPerk],
        [magazine.ImpactCasing, AnyPerk],
        [trait.AutoLoadingHolster],
        [trait.ExplosiveLight],
        )


class ChromaRush(RollDefinition):
    """
    Kinetic Auto Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/2598420927
    """
    item = Item('Chroma Rush', hash=2598420927)
    _mags = [
        magazine.AlloyMagazine,
        magazine.FlaredMagwell,
        magazine.TacticalMag,
        magazine.AppendedMag,
        ]
    rolls = [
        Roll(
            'Kinetic Tremor roll',
            [barrel.ArrowheadBrake, AnyPerk],
            _mags,
            [trait.Subsistence],
            [trait.KineticTremors],
            ),
        Roll(
            "Good ol' roll",
            [barrel.ArrowheadBrake, AnyPerk],
            _mags,
            [trait.Subsistence],
            [trait.Rampage],
            ),
        ]


class Gridskipper(RollDefinition):
    """
    Void Pulse Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/3433930495
    """
    item = Item('Gridskipper', hash=3433930495)
    roll = Roll(
        'PvE',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.FlaredMagwell, AnyPerk],
        [trait.RepulsorBrace],
        [trait.DestabilizingRounds],
        )


class IgnitionCode(RollDefinition):
    """
    Kinetic Breechloaded Grenade Launcher, Lightweight Frame
    https://www.light.gg/db/items/2761869150
    """
    item = Item('Ignition Code', hash=2761869150)


class SojournersTale(RollDefinition):
    """
    Solar Shotgun, Pinpoint Slug Frame
    https://www.light.gg/db/items/2130875369
    """
    item = Item("Sojourner's Tale", hash=2130875369)
    roll = Roll(
        'Damage dealing',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.AssaultMag, magazine.TacticalMag, magazine.LightMag],
        [trait.AutoLoadingHolster],
        [trait.PrecisionInstrument],
        )
