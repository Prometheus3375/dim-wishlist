from database import *


class ArcaneEmbrace(RD):
    """
    Arc Shotgun, Heavy Burst
    https://www.light.gg/db/items/3649985571
    """
    item = Item(name='Arcane Embrace', hash=3649985571)
    roll = Roll(
        'Roll for damage dealing',
        [barrels.ArrowheadBrake, AnyPerk],
        [magazines.TacticalMag, magazines.AlloyMagazine, magazines.FlaredMagwell],
        [traits.FourthTimesTheCharm],
        [traits.PrecisionInstrument, traits.Surrounded],
        )
