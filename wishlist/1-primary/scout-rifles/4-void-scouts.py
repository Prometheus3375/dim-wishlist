from wishlist import *


class AishasEmbrace(RollDefinition):
    """
    Void Scout Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Saint-14
    https://www.light.gg/db/items/3709368142
    https://destiny.report/w/3709368142
    """
    item = Item("Aisha's Embrace", hash=3709368142)
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.RapidHit, trait.Demoralize],
            [trait.DestabilizingRounds],
            ),
        Roll(
            'Withering Gaze',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.RapidHit, trait.Demoralize],
            [trait.WitheringGaze],
            ),
        ]


class BryasLove(RollDefinition):
    """
    Void Scout Rifle, Precision Frame, Anti-Barrier, Craftable
    Source: Xûr
    https://www.light.gg/db/items/2779821308
    https://destiny.report/w/2779821308
    """
    item = Item("Brya's Love", hash=2779821308)


class DoomOfChelchis(RollDefinition):
    """
    Void Scout Rifle, Precision Frame, Anti-Barrier, Craftable
    Source: King's Fall
    https://www.light.gg/db/items/1937552980
    https://destiny.report/w/1937552980
    """
    items = [
        Item('Doom of Chelchis', hash=1937552980),
        Item('Doom of Chelchis (Harrowed)', hash=1184692845),
        ]


class PointedInquiry(RollDefinition):
    """
    Void Scout Rifle, High-Impact Frame, Anti-Unstoppable, Craftable
    Source: Savathûn's Throne World
    https://www.light.gg/db/items/297296830
    https://destiny.report/w/297296830
    """
    item = Item('Pointed Inquiry', hash=297296830)


class Vouchsafe(RollDefinition):
    """
    Void Scout Rifle, Lightweight Frame, Anti-Overload
    Source: The Dreaming City
    https://www.light.gg/db/items/3218302023
    https://destiny.report/w/3218302023
    """
    item = Item('Vouchsafe', hash=3218302023)
