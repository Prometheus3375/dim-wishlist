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

# region Relativism
wishlist.add(
    Relativism,
    'Combination Blow builds',
    {unique.SpiritOf.Assassin, unique.SpiritOf.Caliban},
    {unique.SpiritOf.Liar},
    )

wishlist.add(
    Relativism,
    'Other melee builds; '
    'Synthoceps increase damage of Combination Blow very little',
    {unique.SpiritOf.Assassin, unique.SpiritOf.Caliban},
    {unique.SpiritOf.Synthoceps},
    )

wishlist.add(
    Relativism,
    'Duskfield build',
    {unique.SpiritOf.Renewal},
    {unique.SpiritOf.Cyrtarachne},
    )

# wishlist.add(
#     Relativism,
#     'Woven Mail builds',
#     {unique.SpiritOf.InmostLight, unique.SpiritOf.Foetracer},
#     {unique.SpiritOf.Cyrtarachne},
#     )

# wishlist.add(
#     Relativism,
#     'Dodge builds',
#     {unique.SpiritOf.Dragon},
#     {unique.SpiritOf.Coyote, unique.SpiritOf.Wormhusk},
#     )

wishlist.add(
    Relativism,
    'Super build',
    {unique.SpiritOf.Galanor},
    {unique.SpiritOf.StarEater},
    )

wishlist.add(
    Relativism,
    'Super and weapon damage',
    {unique.SpiritOf.Foetracer},
    {unique.SpiritOf.StarEater},
    )

# wishlist.add(
#     Relativism,
#     'Gyrfalcon builds',
#     {unique.SpiritOf.Dragon, unique.SpiritOf.Foetracer},
#     {unique.SpiritOf.Gyrfalcon},
#     )

wishlist.add(
    Relativism,
    'PvP build',
    {unique.SpiritOf.Ophidian},
    {unique.SpiritOf.Wormhusk},
    )
# endregion


# region Stoicism
wishlist.add(
    Stoicism,
    'Melee builds',
    {unique.SpiritOf.Assassin, unique.SpiritOf.InmostLight, unique.SpiritOf.Severance},
    {unique.SpiritOf.Synthoceps, unique.SpiritOf.Contact},
    )

wishlist.add(
    Stoicism,
    'Barricade builds',
    {unique.SpiritOf.Hoarfrost},
    {unique.SpiritOf.AlphaLupi, unique.SpiritOf.Horn},
    )

# todo Check if Verity buffs damage from Unbreakable
wishlist.add(
    Stoicism,
    'Unbreakable build',
    {unique.SpiritOf.Bear},
    {unique.SpiritOf.Armamentarium},
    )

wishlist.add(
    Stoicism,
    "Drengr's Lash build",
    {unique.SpiritOf.Abeyant},
    {unique.SpiritOf.Horn},
    )

wishlist.add(
    Stoicism,
    'Super and weapon damage',
    {unique.SpiritOf.EternalWarrior},
    {unique.SpiritOf.StarEater},
    )

wishlist.add(
    Stoicism,
    'PvP build',
    {unique.SpiritOf.Ophidian},
    {unique.SpiritOf.AlphaLupi},
    )
# endregion


# region Solipsism
wishlist.add(
    Solipsism,
    'Melee builds',
    {unique.SpiritOf.Assassin, unique.SpiritOf.InmostLight, unique.SpiritOf.Necrotic},
    {unique.SpiritOf.Synthoceps, unique.SpiritOf.Claw},
    )

# wishlist.add(
#     Solipsism,
#     'Grenade build',
#     {unique.SpiritOf.Osmiomancy},
#     {unique.SpiritOf.Verity},
#     )

wishlist.add(
    Solipsism,
    'Empowered Rift combo',
    {unique.SpiritOf.Filaments},
    {unique.SpiritOf.Starfire},
    )

# wishlist.add(
#     Solipsism,
#     'Other Rift builds',
#     {unique.SpiritOf.InmostLight, unique.SpiritOf.Stag},
#     {unique.SpiritOf.Vesper},
#     )

wishlist.add(
    Solipsism,
    'Super builds',
    {unique.SpiritOf.Apotheosis},
    {unique.SpiritOf.Harmony, unique.SpiritOf.StarEater},
    )

wishlist.add(
    Solipsism,
    'Song of Flame grenade build',
    {unique.SpiritOf.Apotheosis},
    {unique.SpiritOf.Verity},
    )

wishlist.add(
    Solipsism,
    'PvP build',
    {unique.SpiritOf.Ophidian},
    {unique.SpiritOf.Harmony},
    )
# endregion

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
