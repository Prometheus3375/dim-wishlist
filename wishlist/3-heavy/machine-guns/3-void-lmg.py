from wishlist import *
from . import *


class BaneOfSorrow(RollDefinition):
    """
    Void Machine Gun, High-Impact Frame, Anti-Unstoppable
    Source: Pantheon
    https://www.light.gg/db/items/3779290676
    https://destiny.report/w/3779290676
    """
    items = [
        Item('Bane of Sorrow', hash=3779290676),
        Item('Bane of Sorrow', hash=2601084711),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            appended_mag,
            [trait.DestabilizingRounds],
            [trait.Demoralize],
            [trait.FeedingFrenzy],
            [trait.MegaKillClip],
            [trait.Meganeura],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            appended_mag,
            [trait.DestabilizingRounds],
            [trait.Meganeura, trait.MegaKillClip],
            ),
        ]


class Commemoration(RollDefinition):
    """
    Void Machine Gun, Adaptive Frame, Anti-Barrier, Craftable
    Source: Raid "Deep Stone Crypt"
    https://www.light.gg/db/items/4230965989
    https://destiny.report/w/4230965989
    """
    item = Item('Commemoration', hash=4230965989)
    Roll(
        'Ad clear',
        default_barrels,
        flared_mag,
        [trait.Dragonfly],
        [trait.Redirection],
        )


class CorrectiveMeasure(RollDefinition):
    """
    Void Machine Gun, Aggressive Frame, Anti-Unstoppable, Craftable
    Source: Raid "Vault of Glass"
    https://www.light.gg/db/items/3654744298
    https://destiny.report/w/3654744298
    """
    items = [
        Item('Corrective Measure', hash=3654744298),
        Item('Corrective Measure (Timelost)', hash=2334480463),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            [barrel.FlutedBarrel, AnyPerk],
            flared_mag,
            [trait.Redirection],
            [trait.Demolitionist],
            [trait.DestabilizingRounds],
            [trait.AdrenalineJunkie],
            [trait.OneForAll],
            [trait.KillingTally],
            ),
        Roll(
            'Ad clear',
            [barrel.FlutedBarrel, AnyPerk],
            flared_mag,
            [trait.Redirection, trait.DestabilizingRounds],
            [trait.OneForAll, trait.KillingTally],
            ),
        Roll(
            'Grenade combo',
            [barrel.FlutedBarrel, AnyPerk],
            flared_mag,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        ]


class Hammerhead(RollDefinition):
    """
    Void Machine Gun, Adaptive Frame, Anti-Barrier
    Source: Arena Ops
    https://www.light.gg/db/items/1346714574
    https://destiny.report/w/1346714574
    """
    items = [
        Item('Hammerhead', hash=1346714574),
        Item('Hammerhead', hash=850999853),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            flared_mag,
            [trait.DestabilizingRounds],
            [trait.Rampage],
            [trait.ImpromptuAmmunition],
            [trait.MegaKillClip],
            [trait.Demoralize],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            flared_mag,
            [trait.ImpromptuAmmunition, trait.DestabilizingRounds, trait.Rampage],
            [trait.MegaKillClip],
            ),
        ]


class RetrofitEscapade(RollDefinition):
    """
    Void Machine Gun, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Exotic mission "Seraph's Shield"
    https://www.light.gg/db/items/3103325054
    https://destiny.report/w/3103325054
    """
    item = Item('Retrofit Escapade', hash=3103325054)
