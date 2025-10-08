from wishlist import *


class Exuviae(RollDefinition):
    """
    Stasis Hand Cannon, Aggressive Frame
    https://www.light.gg/db/items/2823644677
    """
    item = Item(name='Exuviae', hash=2823644677)


class Insurmountable(RollDefinition):
    """
    Void Sidearm, Precision Frame
    https://www.light.gg/db/items/414045521
    """
    item = Item(name='Insurmountable', hash=414045521)


class VantagePoint(RollDefinition):
    """
    Arc Pulse Rifle, Adaptive Frame
    https://www.light.gg/db/items/3830941962
    """
    item = Item(name='Vantage Point', hash=3830941962)
    _mags = [
        magazines.TacticalMag,
        magazines.AppendedMag,
        magazines.AlloyMagazine,
        magazines.FlaredMagwell,
        ]
    roll = Roll(
        'Ad clear',
        [barrels.ArrowheadBrake, AnyPerk],
        _mags,
        [traits.EddyCurrent],
        [traits.JoltingFeedback],
        )


class Liturgy(RollDefinition):
    """
    Stasis Breechloaded Grenade Launcher, Double Fire
    https://www.light.gg/db/items/2599338624
    """
    item = Item(name='Liturgy', hash=2599338624)
    rolls = [
        Roll(
            'Damage rotations combo',
            [barrels.HardLaunch, AnyPerk],
            [magazines.SpikeGrenades],
            [traits.EnviousArsenal],
            [traits.ChillClip],
            ),
        ]


class Sovereignty(RollDefinition):
    """
    Void Sniper Rifle, Adaptive Frame
    https://www.light.gg/db/items/3818198556
    """
    item = Item(name='Sovereignty', hash=3818198556)
    roll = Roll(
        'Withering Gaze. Appended Mag + Backup Mag mod increase mag size to 7',
        [barrels.ArrowheadBrake, AnyPerk],
        [magazines.AppendedMag, magazines.TacticalMag, magazines.AlloyMagazine,
         magazines.FlaredMagwell],
        [traits.Demolitionist, traits.NoDistractions],
        [traits.WitheringGaze],
        )


class BitterSweet(RollDefinition):
    """
    Arc Drum Grenade Launcher, Adaptive Frame
    https://www.light.gg/db/items/2599338625
    """
    item = Item(name='Bitter/Sweet', hash=2599338625)
    rolls = [
        Roll(
            'Damage dealing',
            [barrels.HardLaunch, AnyPerk],
            [magazines.SpikeGrenades, AnyPerk],
            [traits.EnviousArsenal],
            [traits.BaitAndSwitch],
            ),
        Roll(
            'High DPS',
            [barrels.QuickLaunch, AnyPerk],
            [magazines.SpikeGrenades, AnyPerk],
            [traits.EnviousArsenal],
            [traits.ExplosiveLight],
            ),
        ]


class NoxiousVetiver(RollDefinition):
    """
    Arc Submachine Gun, Precision Frame
    https://www.light.gg/db/items/825495813
    """
    item = Item(name='Noxious Vetiver', hash=825495813)
    _mags = [
        magazines.AlloyMagazine,
        magazines.FlaredMagwell,
        magazines.TacticalMag,
        magazines.AppendedMag,
        ]
    roll = Roll(
        'Roll for ad clear',
        [barrels.ArrowheadBrake, AnyPerk],
        _mags,
        [traits.AttritionOrbs, traits.LooseChange, traits.Pugilist],
        [traits.JoltingFeedback],
        )


class ScavengersFate(RollDefinition):
    """
    Void Shotgun, Precision Frame
    https://www.light.gg/db/items/2913577176
    """
    item = Item(name="Scavenger's Fate", hash=2913577176)
    roll = Roll(
        'PvP',
        [barrels.BarrelShroud, barrels.CorkscrewRifling, barrels.FullChoke],
        [magazines.AccurizedRounds, magazines.LightMag],
        [traits.LoneWolf],
        [traits.ClosingTime],
        )


class RedTape(RollDefinition):
    """
    Stasis Scout Rifle, Lightweight Frame
    https://www.light.gg/db/items/3423493037
    """
    item = Item(name='Red Tape', hash=3423493037)
    _barrels = [barrels.ArrowheadBrake, AnyPerk]
    _mags = [
        magazines.TacticalMag,
        magazines.AppendedMag,
        magazines.AlloyMagazine,
        magazines.FlaredMagwell,
        ]
    rolls = [
        Roll(
            'Explosive Payload',
            _barrels,
            _mags,
            [traits.Demolitionist],
            [traits.ExplosivePayload],
            ),
        Roll(
            'Headstone',
            _barrels,
            _mags,
            [traits.Demolitionist, traits.Rimestealer],
            [traits.Headstone],
            ),
        ]


class HereticsFervor(RollDefinition):
    """
    Stasis Rocket Launcher, Aggressive Frame
    https://www.light.gg/db/items/4224667951
    """
    item = Item(name="Heretic's Fervor", hash=4224667951)
    roll = Roll(
        'Damage dealing',
        [barrels.QuickLaunch, AnyPerk],
        [magazines.ImpactCasing, AnyPerk],
        [traits.AutoLoadingHolster],
        [traits.ExplosiveLight],
        )


class ChromaRush(RollDefinition):
    """
    Kinetic Auto Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/2598420927
    """
    item = Item(name='Chroma Rush', hash=2598420927)
    _mags = [
        magazines.AlloyMagazine,
        magazines.FlaredMagwell,
        magazines.TacticalMag,
        magazines.AppendedMag,
        ]
    rolls = [
        Roll(
            'Kinetic Tremor roll',
            [barrels.ArrowheadBrake, AnyPerk],
            _mags,
            [traits.Subsistence],
            [traits.KineticTremors],
            ),
        Roll(
            "Good ol' roll",
            [barrels.ArrowheadBrake, AnyPerk],
            _mags,
            [traits.Subsistence],
            [traits.Rampage],
            ),
        ]


class Gridskipper(RollDefinition):
    """
    Void Pulse Rifle, Rapid-Fire Frame
    https://www.light.gg/db/items/3433930495
    """
    item = Item(name='Gridskipper', hash=3433930495)
    roll = Roll(
        'PvE',
        [barrels.ArrowheadBrake, AnyPerk],
        [magazines.FlaredMagwell, AnyPerk],
        [traits.RepulsorBrace],
        [traits.DestabilizingRounds],
        )


class IgnitionCode(RollDefinition):
    """
    Kinetic Breechloaded Grenade Launcher, Lightweight Frame
    https://www.light.gg/db/items/2761869150
    """
    item = Item(name='Ignition Code', hash=2761869150)


class SojournersTale(RollDefinition):
    """
    Solar Shotgun, Pinpoint Slug Frame
    https://www.light.gg/db/items/2130875369
    """
    item = Item(name="Sojourner's Tale", hash=2130875369)
    roll = Roll(
        'Damage dealing',
        [barrels.ArrowheadBrake, AnyPerk],
        [magazines.AssaultMag, magazines.TacticalMag, magazines.LightMag],
        [traits.AutoLoadingHolster],
        [traits.PrecisionInstrument],
        )
