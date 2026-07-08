__all__ = 'default_barrels', 'default_mags',

from database import barrel
from wishlist import AnyPerk, magazine

default_barrels = [barrel.Smallbore, AnyPerk]
default_mags = [magazine.TacticalMag, AnyPerk]
