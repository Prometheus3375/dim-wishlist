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
    {RewindRounds, Strategist, EnlightenedAction},
    {Surrounded, DesperateMeasures},
    notes='Good PvE rolls',
    )

# endregion

# region Veist

wishlist.add(
    'Spectrum-4FR DPS rolls',
    Suspectum4FR,
    {ArrowheadBrake},
    {EnlightenedAction, EnviousAssassin},
    {PrecisionInstrument},
    notes='Rolls for DPS',
    )

wishlist.add(
    'Spectrum-4FR bad combo',
    Suspectum4FR,
    {EnviousAssassin},
    {FourthTimesTheCharm},
    notes='FTTC does not regenerate ammo if mag is overflowed',
    trash=True,
    )

# endregion

# region The Pale Heart

wishlist.add(
    'Ergo Sum Wolfpack Rounds',
    ErgoSum,
    {ES_WolfpackRounds},
    {EnduringBlade, HungryEdge, TemperedEdge},
    {ES_LightweightFrame},
    notes='Roll to activate Wolfpack Rounds on swords. '
          'Lightweight Frame has fast heavy attack which consumes only 3 ammo',
    )

wishlist.add(
    'Ergo Sum Gathering Light',
    ErgoSum,
    {ES_GatheringLight},
    {EnduringBlade, HungryEdge, TemperedEdge},
    {ES_WaveSwordFrame},
    notes='Good roll to get ability energy from sword kills',
    )

# endregion

# region Echoes

wishlist.add(
    'Breachlight grenade roll',
    Breachlight,
    {Demolitionist},
    {AdrenalineJunkie},
    notes='Roll for grenade builds',
    )

wishlist.add(
    'Breachlight melee roll',
    Breachlight,
    {Pugilist},
    {Swashbuckler},
    notes='Roll for melee builds and synergy with the origin trait',
    )

wishlist.add(
    'Breachlight Strand roll',
    Breachlight,
    {Slice},
    {Hatchling},
    notes='Roll for Strand builds',
    )

wishlist.add(
    'Breachlight rolls',
    Breachlight,
    {ThreatDetector, Demolitionist},
    {DesperateMeasures, Hatchling},
    notes='Good PvE rolls',
    )

wishlist.add(
    'Patron of Lost Causes class ability rolls',
    PatronOfLostCauses,
    {Strategist},
    {ExplosivePayload, KineticTremors},
    notes='Rolls to get class ability energy from afar',
    )

wishlist.add(
    'Patron of Lost Causes classic rolls',
    PatronOfLostCauses,
    {RapidHit},
    {ExplosivePayload, KineticTremors},
    notes='Classic PvE rolls for a scout rifle',
    )

wishlist.add(
    'Perfect Paradox melee rolls',
    PerfectParadox,
    {Smallbore, CorkscrewRifling, BarrelShroud},
    {TacticalMag},
    {FieldPrep},
    {OneTwoPunch},
    notes='Special rolls for melee damage increase',
    )

wishlist.add(
    'Perfect Paradox DPS rolls',
    PerfectParadox,
    {Smallbore, CorkscrewRifling, BarrelShroud},
    {TacticalMag},
    {ThreatDetector, FieldPrep},
    {TrenchBarrel},
    notes='Rolls for shotgun DPS',
    )

wishlist.add(
    "Martyr's Retribution Clip roll",
    MartyrsRetribution,
    {VolatileLaunch},
    {HighVelocityRounds},
    {HealClip},
    {KillClip},
    notes='Special Clip combo',
    )

wishlist.add(
    "Martyr's Retribution grenade roll",
    MartyrsRetribution,
    {VolatileLaunch},
    {HighVelocityRounds},
    {Demolitionist},
    {AdrenalineJunkie},
    notes='Roll for grenade builds',
    )

wishlist.add(
    "Martyr's Retribution regular rolls",
    MartyrsRetribution,
    {VolatileLaunch},
    {HighVelocityRounds},
    {Demolitionist, HealClip, AutoLoadingHolster},
    {DesperateMeasures, Incandescent},
    notes='Good PvE rolls',
    )

wishlist.add(
    'Line in the Sand DPS rolls',
    LineInTheSand,
    {ArrowheadBrake},
    {Demolitionist, ClownCartridge},
    {BaitAndSwitch},
    notes='DPS rolls'
    )

# endregion

if __name__ == '__main__':
    wishlist.to_dim_wishlist_file('wishlist.txt')
