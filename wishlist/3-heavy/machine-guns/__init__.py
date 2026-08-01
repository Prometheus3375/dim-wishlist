__all__ = 'default_barrels', 'appended_mag', 'flared_mag'

from wishlist import AnyPerk, barrel, magazine

default_barrels = [barrel.ArrowheadBrake, AnyPerk]
appended_mag = [magazine.AppendedMag, AnyPerk]
flared_mag = [magazine.FlaredMagwell, AnyPerk]
