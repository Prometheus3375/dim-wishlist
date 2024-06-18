from classes import Wishlist, roll
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

wishlist.add_many(
    ErgoSum,
    roll(
        'Roll to activate Wolfpack Rounds on swords. '
        'Lightweight Frame has fast heavy attack which consumes only 3 ammo',
        {unique.ErgoSum.WolfpackRounds},
        _es_blades,
        {unique.ErgoSum.LightweightFrame},
        ),
    roll(
        'Good roll to get ability energy from sword kills',
        {unique.ErgoSum.GatheringLight},
        _es_blades,
        {unique.ErgoSum.WaveSwordFrame},
        ),
    )

wishlist.add_many(
    Relativism,
    roll(
        'Combination Blow builds',
        {unique.SpiritOf.Assassin, unique.SpiritOf.Caliban},
        {unique.SpiritOf.Liar},
        ),
    roll(
        'Other melee builds; '
        'Synthoceps increase damage of Combination Blow very little',
        {unique.SpiritOf.Assassin, unique.SpiritOf.Caliban},
        {unique.SpiritOf.Synthoceps},
        ),
    roll(
        'Duskfield build',
        {unique.SpiritOf.Renewal},
        {unique.SpiritOf.Cyrtarachne},
        ),
    # roll(
    #     'Woven Mail builds',
    #     {unique.SpiritOf.InmostLight, unique.SpiritOf.Foetracer},
    #     {unique.SpiritOf.Cyrtarachne},
    #     ),
    # roll(
    #     'Dodge builds',
    #     {unique.SpiritOf.Dragon},
    #     {unique.SpiritOf.Coyote, unique.SpiritOf.Wormhusk},
    #     ),
    roll(
        'Super build',
        {unique.SpiritOf.Galanor},
        {unique.SpiritOf.StarEater},
        ),
    roll(
        'Super and weapon damage',
        {unique.SpiritOf.Foetracer},
        {unique.SpiritOf.StarEater},
        ),
    # roll(
    #     'Gyrfalcon builds',
    #     {unique.SpiritOf.Dragon, unique.SpiritOf.Foetracer},
    #     {unique.SpiritOf.Gyrfalcon},
    #     ),
    roll(
        'PvP build',
        {unique.SpiritOf.Ophidian},
        {unique.SpiritOf.Wormhusk},
        ),
    )

wishlist.add_many(
    Stoicism,
    roll(
        'Melee builds',
        {unique.SpiritOf.Assassin, unique.SpiritOf.InmostLight, unique.SpiritOf.Severance},
        {unique.SpiritOf.Synthoceps, unique.SpiritOf.Contact},
        ),
    roll(
        'Barricade builds',
        {unique.SpiritOf.Hoarfrost},
        {unique.SpiritOf.AlphaLupi, unique.SpiritOf.Horn},
        ),
    roll(
        # todo Check if Verity buffs damage from Unbreakable
        'Unbreakable build',
        {unique.SpiritOf.Bear},
        {unique.SpiritOf.Armamentarium},
        ),
    roll(
        "Drengr's Lash build",
        {unique.SpiritOf.Abeyant},
        {unique.SpiritOf.Horn},
        ),
    roll(
        'Super and weapon damage',
        {unique.SpiritOf.EternalWarrior},
        {unique.SpiritOf.StarEater},
        ),
    roll(
        'PvP build',
        {unique.SpiritOf.Ophidian},
        {unique.SpiritOf.AlphaLupi},
        ),
    )

wishlist.add_many(
    Solipsism,
    roll(
        'Melee builds',
        {unique.SpiritOf.Assassin, unique.SpiritOf.InmostLight, unique.SpiritOf.Necrotic},
        {unique.SpiritOf.Synthoceps, unique.SpiritOf.Claw},
        ),
    # roll(
    #     'Grenade build',
    #     {unique.SpiritOf.Osmiomancy},
    #     {unique.SpiritOf.Verity},
    #     ),
    roll(
        'Empowered Rift combo',
        {unique.SpiritOf.Filaments},
        {unique.SpiritOf.Starfire},
        ),
    # roll(
    #     'Other Rift builds',
    #     {unique.SpiritOf.InmostLight, unique.SpiritOf.Stag},
    #     {unique.SpiritOf.Vesper},
    #     ),
    roll(
        'Super builds',
        {unique.SpiritOf.Apotheosis},
        {unique.SpiritOf.Harmony, unique.SpiritOf.StarEater},
        ),
    roll(
        'Song of Flame grenade build',
        {unique.SpiritOf.Apotheosis},
        {unique.SpiritOf.Verity},
        ),
    roll(
        'PvP build',
        {unique.SpiritOf.Ophidian},
        {unique.SpiritOf.Harmony},
        ),
    )

# endregion

# region Echoes

wishlist.add_many(
    Breachlight,
    roll(
        'Roll for grenade builds',
        {traits.Demolitionist},
        {traits.AdrenalineJunkie},
        ),
    roll(
        'Roll for melee builds and synergy with the origin trait',
        {traits.Pugilist},
        {traits.Swashbuckler},
        ),
    roll(
        'Roll for Strand builds',
        {traits.Slice},
        {traits.Hatchling},
        ),
    roll(
        'Good PvE rolls',
        {traits.ThreatDetector, traits.Demolitionist},
        {traits.DesperateMeasures, traits.Hatchling},
        ),
    )

wishlist.add_many(
    PatronOfLostCauses,
    roll(
        'Rolls to get class ability energy from afar',
        {traits.Strategist},
        {traits.ExplosivePayload, traits.KineticTremors},
        ),
    roll(
        'Classic PvE rolls for a scout rifle',
        {traits.RapidHit},
        {traits.ExplosivePayload, traits.KineticTremors},
        ),
    )

_perfect_paradox_barrels = {barrels.Smallbore, barrels.CorkscrewRifling, barrels.BarrelShroud}
_perfect_paradox_mags = {magazines.TacticalMag}

wishlist.add_many(
    PerfectParadox,
    roll(
        'Rolls for melee damage increase',
        _perfect_paradox_barrels,
        _perfect_paradox_mags,
        {traits.FieldPrep},
        {traits.OneTwoPunch},
        ),
    roll(
        'Rolls for shotgun DPS',
        _perfect_paradox_barrels,
        _perfect_paradox_mags,
        {traits.ThreatDetector, traits.FieldPrep},
        {traits.TrenchBarrel},
        )
    )

wishlist.add_many(
    MartyrsRetribution,
    roll(
        'Clip combo',
        {barrels.VolatileLaunch},
        {magazines.HighVelocityRounds},
        {traits.HealClip},
        {traits.KillClip},
        ),
    roll(
        'Roll for grenade builds',
        {barrels.VolatileLaunch},
        {magazines.HighVelocityRounds},
        {traits.Demolitionist},
        {traits.AdrenalineJunkie},
        ),
    roll(
        'Good PvE rolls',
        {barrels.VolatileLaunch},
        {magazines.HighVelocityRounds},
        {traits.Demolitionist, traits.HealClip, traits.AutoLoadingHolster},
        {traits.DesperateMeasures, traits.Incandescent},
        ),
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
