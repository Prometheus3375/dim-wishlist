from classes import Wishlist
from database import *

wishlist = Wishlist(
    title='Wishlist made by Prometheus3375',
    description='Rolls on weapons and armor Prometheus3375 would like to have',
    )

# region Omolon

wishlist.add(
    'Yarovit MG4 rolls',
    YarovitMG4,
    {traits.RewindRounds, traits.Strategist, traits.EnlightenedAction},
    {traits.Surrounded, traits.DesperateMeasures, traits.Headstone},
    notes='Good PvE rolls',
    )

# endregion

# region Veist

wishlist.add(
    'Spectrum-4FR DPS rolls',
    Suspectum4FR,
    {barrels.ArrowheadBrake},
    {traits.EnlightenedAction, traits.EnviousAssassin},
    {traits.PrecisionInstrument},
    notes='Rolls for DPS',
    )

wishlist.add(
    'Spectrum-4FR bad combo',
    Suspectum4FR,
    {traits.EnviousAssassin},
    {traits.FourthTimesTheCharm},
    notes='FTTC does not regenerate ammo if mag is overflowed',
    trash=True,
    )

# endregion

# region The Pale Heart

_es_blades = {blades.EnduringBlade, blades.HungryEdge, blades.TemperedEdge}

wishlist.add(
    'Ergo Sum Wolfpack Rounds',
    ErgoSum,
    {unique.ES_WolfpackRounds},
    _es_blades,
    {unique.ES_LightweightFrame},
    notes='Roll to activate Wolfpack Rounds on swords. '
          'Lightweight Frame has fast heavy attack which consumes only 3 ammo',
    )

wishlist.add(
    'Ergo Sum Gathering Light',
    ErgoSum,
    {unique.ES_GatheringLight},
    _es_blades,
    {unique.ES_WaveSwordFrame},
    notes='Good roll to get ability energy from sword kills',
    )

# endregion

# region Echoes

wishlist.add(
    'Breachlight grenade roll',
    Breachlight,
    {traits.Demolitionist},
    {traits.AdrenalineJunkie},
    notes='Roll for grenade builds',
    )

wishlist.add(
    'Breachlight melee roll',
    Breachlight,
    {traits.Pugilist},
    {traits.Swashbuckler},
    notes='Roll for melee builds and synergy with the origin trait',
    )

wishlist.add(
    'Breachlight Strand roll',
    Breachlight,
    {traits.Slice},
    {traits.Hatchling},
    notes='Roll for Strand builds',
    )

wishlist.add(
    'Breachlight rolls',
    Breachlight,
    {traits.ThreatDetector, traits.Demolitionist},
    {traits.DesperateMeasures, traits.Hatchling},
    notes='Good PvE rolls',
    )

wishlist.add(
    'Patron of Lost Causes class ability rolls',
    PatronOfLostCauses,
    {traits.Strategist},
    {traits.ExplosivePayload, traits.KineticTremors},
    notes='Rolls to get class ability energy from afar',
    )

wishlist.add(
    'Patron of Lost Causes classic rolls',
    PatronOfLostCauses,
    {traits.RapidHit},
    {traits.ExplosivePayload, traits.KineticTremors},
    notes='Classic PvE rolls for a scout rifle',
    )

_perfect_paradox_barrels = {barrels.Smallbore, barrels.CorkscrewRifling, barrels.BarrelShroud}
_perfect_paradox_mags = {magazines.TacticalMag}

wishlist.add(
    'Perfect Paradox melee rolls',
    PerfectParadox,
    _perfect_paradox_barrels,
    _perfect_paradox_mags,
    {traits.FieldPrep},
    {traits.OneTwoPunch},
    notes='Special rolls for melee damage increase',
    )

wishlist.add(
    'Perfect Paradox DPS rolls',
    PerfectParadox,
    _perfect_paradox_barrels,
    _perfect_paradox_mags,
    {traits.ThreatDetector, traits.FieldPrep},
    {traits.TrenchBarrel},
    notes='Rolls for shotgun DPS',
    )

wishlist.add(
    "Martyr's Retribution Clip roll",
    MartyrsRetribution,
    {barrels.VolatileLaunch},
    {magazines.HighVelocityRounds},
    {traits.HealClip},
    {traits.KillClip},
    notes='Special Clip combo',
    )

wishlist.add(
    "Martyr's Retribution grenade roll",
    MartyrsRetribution,
    {barrels.VolatileLaunch},
    {magazines.HighVelocityRounds},
    {traits.Demolitionist},
    {traits.AdrenalineJunkie},
    notes='Roll for grenade builds',
    )

wishlist.add(
    "Martyr's Retribution regular rolls",
    MartyrsRetribution,
    {barrels.VolatileLaunch},
    {magazines.HighVelocityRounds},
    {traits.Demolitionist, traits.HealClip, traits.AutoLoadingHolster},
    {traits.DesperateMeasures, traits.Incandescent},
    notes='Good PvE rolls',
    )

wishlist.add(
    'Line in the Sand DPS rolls',
    LineInTheSand,
    {barrels.ArrowheadBrake},
    {traits.Demolitionist, traits.ClownCartridge},
    {traits.BaitAndSwitch},
    notes='DPS rolls'
    )

# endregion

if __name__ == '__main__':
    wishlist.to_dim_wishlist_file('wishlist.txt')
