from database import *


class ArcaneEmbrace(RollDefinition):
    """
    Arc Shotgun, Heavy Burst
    https://www.light.gg/db/items/3649985571
    """
    item = Item(name='Arcane Embrace', hash=3649985571)
    roll = Roll(
        'Damage dealing',
        [barrels.ArrowheadBrake, AnyPerk],
        [magazines.TacticalMag, magazines.AlloyMagazine, magazines.FlaredMagwell],
        [traits.FourthTimesTheCharm],
        [traits.PrecisionInstrument, traits.Surrounded],
        )
