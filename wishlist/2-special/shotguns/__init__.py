__all__ = 'pvp_barrels', 'pvp_mags', 'pve_barrels', 'pve_mags'

from wishlist import AnyPerk, barrel, magazine

pvp_barrels = [barrel.BarrelShroud, barrel.CorkscrewRifling, barrel.Smallbore]
pvp_mags = [magazine.AccurizedRounds, magazine.LightMag]

pve_barrels = [barrel.BarrelShroud, AnyPerk]
pve_mags = [magazine.TacticalMag, AnyPerk]
