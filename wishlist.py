from classes import Wishlist
from database import *

wishlist = Wishlist(
    title='Wishlist made by Prometheus3375',
    description='Rolls on weapons and armor Prometheus3375 would like to have',
    )

# region Omolon

wishlist.add(
    YarovitMG4,
    'Good PvE rolls',
    {traits.RewindRounds, traits.Strategist, traits.EnlightenedAction},
    {traits.Surrounded, traits.DesperateMeasures, traits.Headstone},
    )

# endregion

# region Veist

wishlist.add(
    Suspectum4FR,
    'Rolls for DPS',
    {barrels.ArrowheadBrake},
    {traits.EnlightenedAction, traits.EnviousAssassin},
    {traits.PrecisionInstrument},
    )

wishlist.add(
    Suspectum4FR,
    'FTTC does not regenerate ammo if mag is overflowed',
    {traits.EnviousAssassin},
    {traits.FourthTimesTheCharm},
    trash=True,
    )

# endregion

# region The Pale Heart

_es_blades = {blades.EnduringBlade, blades.HungryEdge, blades.TemperedEdge}

wishlist.add(
    ErgoSum,
    'Roll to activate Wolfpack Rounds on swords. '
    'Lightweight Frame has fast heavy attack which consumes only 3 ammo',
    {unique.ErgoSum.WolfpackRounds},
    _es_blades,
    {unique.ErgoSum.LightweightFrame},
    )

wishlist.add(
    ErgoSum,
    'Good roll to get ability energy from sword kills',
    {unique.ErgoSum.GatheringLight},
    _es_blades,
    {unique.ErgoSum.WaveSwordFrame},
    )

# endregion

# region Echoes

wishlist.add(
    Breachlight,
    'Roll for grenade builds',
    {traits.Demolitionist},
    {traits.AdrenalineJunkie},
    )

wishlist.add(
    Breachlight,
    'Roll for melee builds and synergy with the origin trait',
    {traits.Pugilist},
    {traits.Swashbuckler},
    )

wishlist.add(
    Breachlight,
    'Roll for Strand builds',
    {traits.Slice},
    {traits.Hatchling},
    )

wishlist.add(
    Breachlight,
    'Good PvE rolls',
    {traits.ThreatDetector, traits.Demolitionist},
    {traits.DesperateMeasures, traits.Hatchling},
    )

wishlist.add(
    PatronOfLostCauses,
    'Rolls to get class ability energy from afar',
    {traits.Strategist},
    {traits.ExplosivePayload, traits.KineticTremors},
    )

wishlist.add(
    PatronOfLostCauses,
    'Classic PvE rolls for a scout rifle',
    {traits.RapidHit},
    {traits.ExplosivePayload, traits.KineticTremors},
    )

_perfect_paradox_barrels = {barrels.Smallbore, barrels.CorkscrewRifling, barrels.BarrelShroud}
_perfect_paradox_mags = {magazines.TacticalMag}

wishlist.add(
    PerfectParadox,
    'Special rolls for melee damage increase',
    _perfect_paradox_barrels,
    _perfect_paradox_mags,
    {traits.FieldPrep},
    {traits.OneTwoPunch},
    )

wishlist.add(
    PerfectParadox,
    'Rolls for shotgun DPS',
    _perfect_paradox_barrels,
    _perfect_paradox_mags,
    {traits.ThreatDetector, traits.FieldPrep},
    {traits.TrenchBarrel},
    )

wishlist.add(
    MartyrsRetribution,
    'Special Clip combo',
    {barrels.VolatileLaunch},
    {magazines.HighVelocityRounds},
    {traits.HealClip},
    {traits.KillClip},
    )

wishlist.add(
    MartyrsRetribution,
    'Roll for grenade builds',
    {barrels.VolatileLaunch},
    {magazines.HighVelocityRounds},
    {traits.Demolitionist},
    {traits.AdrenalineJunkie},
    )

wishlist.add(
    MartyrsRetribution,
    'Good PvE rolls',
    {barrels.VolatileLaunch},
    {magazines.HighVelocityRounds},
    {traits.Demolitionist, traits.HealClip, traits.AutoLoadingHolster},
    {traits.DesperateMeasures, traits.Incandescent},
    )

wishlist.add(
    LineInTheSand,
    'DPS rolls',
    {barrels.ArrowheadBrake},
    {traits.Demolitionist, traits.ClownCartridge},
    {traits.BaitAndSwitch},
    )

# endregion

if __name__ == '__main__':
    wishlist.to_dim_wishlist_file('wishlist.txt')
