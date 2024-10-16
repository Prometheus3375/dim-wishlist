from database import *


# region Cassoid
class DedGramaryeIV(RD):
    item = Item(name='Ded Gramarye IV', hash=499245245)
    _barrels = [barrels.BarrelShroud, barrels.CorkscrewRifling, barrels.Smallbore]
    rolls = [
        roll(
            'Chain Reaction roll',
            _barrels,
            [magazines.AssaultMag, magazines.LightMag, magazines.TacticalMag],
            [traits.Discord, traits.ThreatDetector],
            [traits.ChainReaction],
            ),
        roll(
            'Voltshot roll; '
            'mag increasing perks are not good with Voltshot '
            'as with them reserves deplete earlier; '
            'Discord is not an option as it refills mag, does not reload; '
            'thus, it does not activate Voltshot',
            _barrels,
            [magazines.AssaultMag, magazines.LightMag],
            [traits.ThreatDetector],
            [traits.Voltshot],
            ),
        ]


# endregion
# region Omolon
class YarovitMG4(RD):
    item = Item(name='Yarovit MG4', hash=3959549446)
    roll = roll(
        'Good PvE roll',
        [traits.Strategist, traits.EnlightenedAction],
        [traits.Headstone, traits.DesperateMeasures, traits.Surrounded],
        )


# endregion
# region Veist
class Suspectum4FR(RD):
    item = Item(name='Suspectum-4FR', hash=3615421669)
    rolls = [
        roll(
            'Roll for damage dealing',
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.AcceleratedCoils, AnyPerk],
            [traits.EnviousAssassin, traits.EnlightenedAction],
            [traits.PrecisionInstrument],
            ),
        roll(
            'FTTC does not regenerate ammo if mag is overflowed',
            [traits.EnviousAssassin],
            [traits.FourthTimesTheCharm],
            is_trash=True,
            ),
        ]
# endregion
