from database import *


class ArcaneEmbrace(RD):
    item = Item(name='Arcane Embrace', hash=3649985571)
    roll = roll(
        'Roll for damage dealing',
        [barrels.ArrowheadBrake, AnyPerk],
        [magazines.TacticalMag, magazines.AlloyMagazine, magazines.FlaredMagwell],
        [traits.FourthTimesTheCharm],
        [traits.PrecisionInstrument, traits.Surrounded],
        )
