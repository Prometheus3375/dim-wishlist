from classes import Wishlist, roll
from database import *

wishlist = Wishlist(
    title='Wishlist made by Prometheus3375',
    description='Rolls on weapons and armor Prometheus3375 would like to have',
    )

# region Cassoid

wishlist.add(
    DedGramaryeIV,
    'Good PvE roll',
    [magazines.TacticalMag],
    [traits.ThreatDetector],
    [traits.ChainReaction, traits.Voltshot],
    )

# endregion

# region Omolon

wishlist.add(
    YarovitMG4,
    'Good PvE roll',
    [traits.Strategist, traits.EnlightenedAction],
    [traits.Headstone, traits.DesperateMeasures, traits.Surrounded],
    )

# endregion

# region Veist

wishlist.add_many(
    Suspectum4FR,
    roll(
        'Roll for damage dealing',
        [barrels.ArrowheadBrake, AnyPerk],
        # todo add mags when learnt which actually work
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
    )

# endregion

# region Vanguard

_scintillation_rolls = [
    roll(
        'Roll for damage dealing',
        [barrels.ArrowheadBrake, AnyPerk],
        [batteries.EnhancedBattery, batteries.AcceleratedCoils, AnyPerk],
        [traits.RewindRounds, traits.EnviousAssassin],
        [traits.BaitAndSwitch, traits.Surrounded],
        [origin.VeistStinger],
        ),
    roll(
        'ALH and BnS are good combo',
        [barrels.ArrowheadBrake, AnyPerk],
        [batteries.EnhancedBattery, batteries.AcceleratedCoils, AnyPerk],
        [traits.AutoLoadingHolster],
        [traits.BaitAndSwitch],
        [origin.VeistStinger],
        ),
    roll(
        'Rewind Rounds with Veist Stinger usually allows to fire all of the reserves. '
        'Unfortunately, any mag stat increase above 20 reduces reserves; '
        'Enhanced Battery is +20, Ionized Battery is +40',
        [batteries.IonizedBattery],
        is_trash=True,
        ),
    ]

wishlist.add_many(Scintillation, *_scintillation_rolls)
wishlist.add_many(ScintillationAdept, *_scintillation_rolls)

# endregion

# region The Pale Heart

_ergo_sum_blades = [blades.EnduringBlade, AnyPerk]
_ergo_sum_dmg_note = (
    'Roll for damage dealing. Blade and guard is not that important. '
    'Prefer Enduring Blade for more ammo. '
    'In any damage situation you should be transcendent '
    'which maximizes Charge Rate anyway.'
    'Aegis thoughts: https://youtu.be/bGTXGydS8uM'
)

wishlist.add_many(
    ErgoSum,
    roll(
        _ergo_sum_dmg_note,
        [unique.ErgoSum.ThePerfectFifth],
        [unique.ErgoSum.CasterFrame],
        _ergo_sum_blades,
        ),
    roll(
        _ergo_sum_dmg_note,
        [unique.ErgoSum.UnplannedReprieve],
        [unique.ErgoSum.LightweightFrame],
        _ergo_sum_blades,
        ),
    roll(
        'Roll to activate Wolfpack Rounds on swords. '
        'Lightweight Frame has fast heavy attack which consumes only 3 ammo',
        [unique.ErgoSum.WolfpackRounds],
        [unique.ErgoSum.LightweightFrame],
        _ergo_sum_blades,
        [guards.SwordmastersGuard, AnyPerk],
        ),
    roll(
        'Roll for ad clear',
        [unique.ErgoSum.ArcConductor],
        [
            unique.ErgoSum.LightweightFrame,
            unique.ErgoSum.WaveSwordFrame,
            unique.ErgoSum.CasterFrame,
            ],
        _ergo_sum_blades,
        [guards.SwordmastersGuard, AnyPerk],
        ),
    # roll(
    #     'Good roll to get ability energy from sword kills',
    #     [unique.ErgoSum.GatheringLight],
    #     [unique.ErgoSum.WaveSwordFrame],
    #     _ergo_sum_blades,
    #     ),
    roll(
        'Stormbringer requires 3 kills to activate and barely makes a difference in ad clear',
        [unique.ErgoSum.Stormbringer],
        is_trash=True,
        ),
    )

wishlist.add_many(
    Relativism,
    roll(
        'Combination Blow builds',
        [unique.SpiritOf.Assassin, unique.SpiritOf.Caliban],
        [unique.SpiritOf.Liar],
        ),
    roll(
        'Other melee builds; '
        'Synthoceps increase damage of Combination Blow very little',
        [unique.SpiritOf.Assassin, unique.SpiritOf.Caliban],
        [unique.SpiritOf.Synthoceps],
        ),
    roll(
        'Duskfield build',
        [unique.SpiritOf.Renewal],
        [unique.SpiritOf.Cyrtarachne],
        ),
    # roll(
    #     'Woven Mail builds',
    #     [unique.SpiritOf.InmostLight, unique.SpiritOf.Foetracer],
    #     [unique.SpiritOf.Cyrtarachne],
    #     ),
    # roll(
    #     'Dodge builds',
    #     [unique.SpiritOf.Dragon],
    #     [unique.SpiritOf.Coyote, unique.SpiritOf.Wormhusk],
    #     ),
    roll(
        'Super build',
        [unique.SpiritOf.Galanor],
        [unique.SpiritOf.StarEater],
        ),
    roll(
        'Super and weapon damage',
        [unique.SpiritOf.Foetracer],
        [unique.SpiritOf.StarEater],
        ),
    roll(
        'Ad clear and super damage',
        [unique.SpiritOf.Caliban],
        [unique.SpiritOf.StarEater],
        ),
    # roll(
    #     'Gyrfalcon builds',
    #     [unique.SpiritOf.Dragon, unique.SpiritOf.Foetracer],
    #     [unique.SpiritOf.Gyrfalcon],
    #     ),
    roll(
        'PvP build',
        [unique.SpiritOf.Ophidian],
        [unique.SpiritOf.Wormhusk],
        ),
    )

wishlist.add_many(
    Stoicism,
    roll(
        'Melee builds',
        [unique.SpiritOf.InmostLight, unique.SpiritOf.Assassin, unique.SpiritOf.Severance],
        [unique.SpiritOf.Synthoceps, unique.SpiritOf.Contact],
        ),
    roll(
        'Barricade builds',
        [unique.SpiritOf.Hoarfrost],
        [unique.SpiritOf.AlphaLupi, unique.SpiritOf.Horn],
        ),
    roll(
        # Verity buffs Unbreakable damage, check when dropped how usable it is
        'Unbreakable build',
        [unique.SpiritOf.Bear],
        [unique.SpiritOf.Armamentarium],
        ),
    roll(
        "Drengr's Lash build",
        [unique.SpiritOf.Abeyant],
        [unique.SpiritOf.Horn],
        ),
    roll(
        'Super and weapon damage',
        [unique.SpiritOf.EternalWarrior],
        [unique.SpiritOf.StarEater],
        ),
    roll(
        'PvP build',
        [unique.SpiritOf.Ophidian],
        [unique.SpiritOf.AlphaLupi],
        ),
    )

wishlist.add_many(
    Solipsism,
    roll(
        'Melee builds',
        [unique.SpiritOf.Necrotic, unique.SpiritOf.InmostLight, unique.SpiritOf.Assassin],
        [unique.SpiritOf.Synthoceps, unique.SpiritOf.Claw],
        ),
    # roll(
    #     'Grenade build',
    #     [unique.SpiritOf.Osmiomancy],
    #     [unique.SpiritOf.Verity],
    #     ),
    roll(
        'Empowered Rift combo',
        [unique.SpiritOf.Filaments],
        [unique.SpiritOf.Starfire],
        ),
    # roll(
    #     'Other Rift builds',
    #     [unique.SpiritOf.InmostLight, unique.SpiritOf.Stag],
    #     [unique.SpiritOf.Vesper],
    #     ),
    roll(
        'Super builds',
        [unique.SpiritOf.Apotheosis],
        [unique.SpiritOf.StarEater, unique.SpiritOf.Harmony],
        ),
    roll(
        'Song of Flame grenade build',
        [unique.SpiritOf.Apotheosis],
        [unique.SpiritOf.Verity],
        ),
    roll(
        'PvP build',
        [unique.SpiritOf.Ophidian],
        [unique.SpiritOf.Harmony],
        ),
    )

# endregion

# region Echoes

_breachlight_mags = [magazines.TacticalMag, magazines.FlaredMagwell, magazines.AppendedMag]

wishlist.add_many(
    Breachlight,
    roll(
        'PvE roll; '
        'Desperate Measures is better than Swashbuckler and Adrenaline Junkie '
        'because it can be activated while stowed and lasts longer',
        _breachlight_mags,
        [traits.Demolitionist, traits.Pugilist, traits.ThreatDetector],
        [traits.DesperateMeasures],
        ),
    roll(
        'Hatchling roll',
        _breachlight_mags,
        [traits.Demolitionist, traits.Pugilist, traits.ThreatDetector],
        [traits.Hatchling],
        ),
    )

wishlist.add_many(
    PatronOfLostCauses,
    roll(
        'Roll to get class ability energy from afar',
        [traits.Strategist],
        [traits.KineticTremors, traits.ExplosivePayload],
        ),
    roll(
        'Classic PvE roll for a scout rifle',
        [traits.RapidHit],
        [traits.KineticTremors, traits.ExplosivePayload],
        ),
    )

_perfect_paradox_barrels = [barrels.Smallbore, barrels.CorkscrewRifling, barrels.BarrelShroud]
_perfect_paradox_mags = [magazines.TacticalMag]

wishlist.add_many(
    PerfectParadox,
    roll(
        'Melee damage increase',
        _perfect_paradox_barrels,
        _perfect_paradox_mags,
        [traits.ThreatDetector, traits.FieldPrep],
        [traits.OneTwoPunch],
        ),
    roll(
        'Roll for damage dealing',
        _perfect_paradox_barrels,
        _perfect_paradox_mags,
        [traits.ThreatDetector, traits.DualLoader],
        [traits.TrenchBarrel],
        )
    )

wishlist.add_many(
    MartyrsRetribution,
    roll(
        'Clip combo',
        [barrels.VolatileLaunch],
        [magazines.HighVelocityRounds],
        [traits.HealClip],
        [traits.KillClip],
        ),
    roll(
        'Roll for grenade builds',
        [barrels.VolatileLaunch],
        [magazines.HighVelocityRounds],
        [traits.Demolitionist],
        [traits.AdrenalineJunkie],  # todo consider removing this roll
        ),
    roll(
        'Good PvE roll',
        [barrels.VolatileLaunch],
        [magazines.HighVelocityRounds],
        [traits.Demolitionist, traits.HealClip, traits.AutoLoadingHolster],
        [traits.DesperateMeasures, traits.Incandescent],
        ),
    )

wishlist.add(
    LineInTheSand,
    'Roll for damage dealing',
    [barrels.ArrowheadBrake, AnyPerk],
    # todo add mags when learn which actually work
    [batteries.AcceleratedCoils, AnyPerk],
    [traits.Demolitionist, traits.ClownCartridge],
    [traits.BaitAndSwitch],
    )

# endregion

if __name__ == '__main__':
    wishlist.to_dim_wishlist_file('wishlist.txt')
