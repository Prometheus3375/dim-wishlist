from classes import Wishlist
from database import *

wishlist = Wishlist(
    title='Wishlist made by Prometheus3375',
    description='Rolls on weapons and armor Prometheus3375 would like to have',
    )

# region Omolon

wishlist.add(
    'YarovitMG4 rolls',
    YarovitMG4,
    {RewindRounds, Strategist, EnlightenedAction},
    {Surrounded, DesperateMeasures},
    notes='Good PvE roll',
    )

# endregion

# region Veist

wishlist.add(
    'Spectrum-4FR DPS rolls',
    Suspectum4FR,
    {ArrowheadBrake},
    {EnlightenedAction, EnviousAssassin},
    {PrecisionInstrument},
    notes='Roll for DPS',
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
    notes='Regular good PvE roll',
    )

wishlist.add(
    'Patron of Lost Causes class ability rolls',
    PatronOfLostCauses,
    {Strategist},
    {ExplosivePayload, KineticTremors},
    notes='An interesting roll to get class ability energy from afar',
    )

wishlist.add(
    'Patron of Lost Causes classic rolls',
    PatronOfLostCauses,
    {RapidHit},
    {ExplosivePayload, KineticTremors},
    notes='A classic PvE roll for a scout rifle',
    )

wishlist.add(
    'Perfect Paradox melee rolls',
    PerfectParadox,
    {Smallbore, CorkscrewRifling, BarrelShroud},
    {TacticalMag},
    {FieldPrep},
    {OneTwoPunch},
    notes='Special roll for melee damage increase',
    )

wishlist.add(
    'Perfect Paradox DPS rolls',
    PerfectParadox,
    {Smallbore, CorkscrewRifling, BarrelShroud},
    {TacticalMag},
    {ThreatDetector, FieldPrep},
    {TrenchBarrel},
    notes='Roll for shotgun DPS',
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
    notes='Good PvE roll',
    )

wishlist.add(
    'Line in the Sand DPS rolls',
    LineInTheSand,
    {ArrowheadBrake},
    {Demolitionist, ClownCartridge},
    {BaitAndSwitch},
    notes='DPS roll'
    )

# endregion

if __name__ == '__main__':
    wishlist.to_dim_wishlist_file('wishlist.txt')
