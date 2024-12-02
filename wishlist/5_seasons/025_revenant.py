from database import *


class Liturgy(RD):
    item = Item(name='Liturgy', hash=2599338624)
    rolls = [
        roll(
            'Roll for damage rotations',
            [barrels.HardLaunch, AnyPerk],
            [magazines.SpikeGrenades],
            [traits.EnviousArsenal],
            [traits.ChillClip],
            ),
        roll(
            'Stasis combo',
            [barrels.HardLaunch, AnyPerk],
            [magazines.SpikeGrenades],
            [traits.Rimestealer],
            [traits.ChillClip],
            ),
        ]


# class Exuviae(RD):
#     item = Item(name='Exuviae', hash=2823644677)


class RedTape(RD):
    item = Item(name='Red Tape', hash=3423493037)
    _barrels = [barrels.ArrowheadBrake, AnyPerk]
    _mags = [
        magazines.TacticalMag,
        magazines.AppendedMag,
        magazines.AlloyMagazine,
        magazines.FlaredMagwell,
        ]
    rolls = roll(
        'PvE rolls',
        _barrels,
        _mags,
        [traits.Demolitionist, traits.Rimestealer],
        [traits.ExplosivePayload, traits.Headstone],
        ),


# class Insurmountable(RD):
#     item = Item(name='Insurmountable', hash=414045521)


class Sovereignty(RD):
    item = Item(name='Sovereignty', hash=3818198556)
    roll = roll(
        'Weaken support roll',
        [barrels.ArrowheadBrake, AnyPerk],
        [magazines.TacticalMag, magazines.AlloyMagazine, magazines.FlaredMagwell],
        [traits.Demolitionist, traits.NoDistractions],
        [traits.WitheringGaze],
        )


class VantagePoint(RD):
    item = Item(name='Vantage Point', hash=3830941962)
    _mags = [
        magazines.TacticalMag,
        magazines.AppendedMag,
        magazines.AlloyMagazine,
        magazines.FlaredMagwell,
        ]
    roll = roll(
        'Roll for ad clear',
        [barrels.ArrowheadBrake, AnyPerk],
        _mags,
        [traits.EddyCurrent],
        [traits.JoltingFeedback],
        )


class NoxiousVetiver(RD):
    item = Item(name='Noxious Vetiver', hash=825495813)
    _mags = [
        magazines.AlloyMagazine,
        magazines.FlaredMagwell,
        magazines.TacticalMag,
        magazines.AppendedMag,
        ]
    roll = roll(
        'Roll for ad clear',
        [barrels.ArrowheadBrake, AnyPerk],
        _mags,
        [traits.AttritionOrbs, traits.LooseChange, traits.Pugilist],
        [traits.JoltingFeedback],
        )


# class ScavengersFate(RD):
#     item = Item(name="Scavenger's Fate", hash=2913577176)


class BitterSweet(RD):
    item = Item(name='Bitter/Sweet', hash=2599338625)
    rolls = [
        roll(
            'Roll for damage dealing',
            [barrels.HardLaunch, AnyPerk],
            [magazines.SpikeGrenades, AnyPerk],
            [traits.EnviousArsenal],
            [traits.BaitAndSwitch],
            ),
        roll(
            'Roll with high DPS',
            [barrels.QuickLaunch, AnyPerk],
            [magazines.SpikeGrenades, AnyPerk],
            [traits.EnviousArsenal],
            [traits.ExplosiveLight],
            ),
        ]


class HereticsFervor(RD):
    item = Item(name="Heretic's Fervor", hash=4224667951)
    roll = roll(
        'Roll for damage dealing',
        [barrels.QuickLaunch, AnyPerk],
        [magazines.ImpactCasing, AnyPerk],
        [traits.AutoLoadingHolster],
        [traits.ExplosiveLight],
        )


class ChromaRush(RD):
    item = Item(name='Chroma Rush', hash=2598420927)
    _mags = [
        magazines.AlloyMagazine,
        magazines.FlaredMagwell,
        magazines.TacticalMag,
        magazines.AppendedMag,
        ]
    rolls = [
        roll(
            'Kinetic Tremor roll',
            [barrels.ArrowheadBrake, AnyPerk],
            _mags,
            [traits.Subsistence],
            [traits.KineticTremors],
            ),
        roll(
            "Good ol' roll",
            [barrels.ArrowheadBrake, AnyPerk],
            _mags,
            [traits.Subsistence],
            [traits.Rampage],
            ),
        ]


# class IgnitionCode(RD):
#     item = Item(name='Ignition Code', hash=2761869150)


# class Gridskipper(RD):
#     item=Item(name='Gridskipper', hash=3433930495)


class SojournersTale(RD):
    item = Item(name="Sojourner's Tale", hash=2130875369)
    roll = roll(
        'Roll for damage dealing',
        [barrels.ArrowheadBrake, AnyPerk],
        [magazines.AssaultMag, magazines.TacticalMag, magazines.LightMag],
        [traits.AutoLoadingHolster],
        [traits.PrecisionInstrument],
        )
