from database import *


# region Cassoid
class DedGramaryeIV(RD):
    item = Item(name='Ded Gramarye IV', hash=499245245)
    _barrels = [barrels.BarrelShroud, barrels.CorkscrewRifling, barrels.Smallbore]
    rolls = [
        Roll(
            'Chain Reaction roll',
            _barrels,
            [magazines.AssaultMag, magazines.LightMag, magazines.TacticalMag],
            [traits.Discord, traits.ThreatDetector],
            [traits.ChainReaction],
            ),
        Roll(
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
# region Field forged
class LiveFire(RD):
    item = Item(name='Live Fire', hash=3612142623)
    rolls = [
        Roll(
            'Shoot to Loot roll',
            [traits.RapidHit],
            [traits.ShootToLoot],
            ),
        Roll(
            'Headstone roll, prefer Red Tape for Rimestealer + Headstone',
            [traits.Rimestealer, traits.RapidHit],
            [traits.Headstone],
            ),
        ]


# endregion
# region Hakke
class VeledaF(RD):
    item = Item(name='Veleda F', hash=4200122994)
    roll = Roll(
        'Weaken support roll',
        [barrels.ArrowheadBrake, AnyPerk],
        [magazines.TacticalMag, magazines.AlloyMagazine, magazines.FlaredMagwell],
        [traits.AirTrigger],
        [traits.WitheringGaze],
        )


# endregion
# region Omolon
class YarovitMG4(RD):
    item = Item(name='Yarovit MG4', hash=3959549446)
    roll = Roll(
        'Good PvE roll',
        [traits.Strategist, traits.EnlightenedAction],
        [traits.Headstone, traits.DesperateMeasures, traits.Surrounded],
        )


# endregion
# SUROS
class Legato11(RD):
    item = Item(name='Legato-11', hash=3753063346)
    roll = Roll(
        'Roll for damage dealing',
        [barrels.ArrowheadBrake, AnyPerk],
        [magazines.AssaultMag, magazines.TacticalMag, magazines.LightMag],
        [traits.AutoLoadingHolster, traits.TripleTap],
        [traits.VorpalWeapon],
        )


# endregion
# region Veist
class Suspectum4FR(RD):
    item = Item(name='Suspectum-4FR', hash=3615421669)
    rolls = [
        Roll(
            'Roll for damage dealing',
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.AcceleratedCoils, AnyPerk],
            [traits.EnviousAssassin, traits.EnlightenedAction],
            [traits.PrecisionInstrument],
            ),
        Roll(
            'FTTC does not regenerate ammo if mag is overflowed',
            [traits.EnviousAssassin],
            [traits.FourthTimesTheCharm],
            is_trash=True,
            ),
        ]
# endregion
