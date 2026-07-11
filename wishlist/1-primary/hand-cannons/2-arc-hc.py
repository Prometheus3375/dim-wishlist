from wishlist import *
from . import *


class NationOfBeasts(RollDefinition):
    """
    Arc Hand Cannon, Adaptive Frame, Anti-Barrier, Craftable
    Source: Raid "Last Wish"
    https://www.light.gg/db/items/70083888
    https://destiny.report/w/70083888
    """
    item = Item('Nation of Beasts', hash=70083888)
    is_chosen = True
    roll = Roll(
        'Arc combo',
        default_barrels,
        default_mags,
        [trait.GearShift],
        [trait.JoltingFeedback],
        )


class Posterity(RollDefinition):
    """
    Arc Hand Cannon, Precision Frame, Anti-Barrier, Craftable
    Source: Raid "Deep Stone Crypt"
    https://www.light.gg/db/items/3281285075
    https://destiny.report/w/3281285075
    """
    item = Item('Posterity', hash=3281285075)
    roll = Roll(
        'Ad clear',
        default_barrels,
        default_mags,
        [trait.SuperchargedMagazine],
        [trait.Redirection, trait.OneForAll],
        )


class SightlineSurvey(RollDefinition):
    """
    Arc Hand Cannon, Precision Frame, Anti-Barrier, Craftable
    Source: Exotic mission "Encore"
    https://www.light.gg/db/items/2350330520
    https://destiny.report/w/2350330520
    """
    item = Item('Sightline Survey', hash=2350330520)


class SolemnLie(RollDefinition):
    """
    Arc Hand Cannon, Lightweight Frame, Anti-Overload
    Source: Competitive Crucible
    https://www.light.gg/db/items/1041028435
    https://destiny.report/w/1041028435
    """
    item = Item('Solemn Lie', hash=1041028435)


class ThePalindrome(RollDefinition):
    """
    Arc Hand Cannon, Adaptive Frame, Anti-Barrier
    Source: Pinnacle Ops
    https://www.light.gg/db/items/739029152
    https://destiny.report/w/739029152
    """
    items = [
        Item('The Palindrome', hash=739029152),
        Item('The Palindrome', hash=3303271523),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.ExplosivePayload],
            [trait.SuperchargedMagazine],
            [trait.MasterOfArms],
            [trait.Voltshot],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.SuperchargedMagazine],
            [trait.MasterOfArms],
            ),
        ]


class TrueProphecy(RollDefinition):
    """
    Arc Hand Cannon, Aggressive Frame, Anti-Unstoppable
    Source: Nessus, Unstable Centaur
    https://www.light.gg/db/items/960948343
    https://destiny.report/w/960948343
    """
    item = Item('True Prophecy', hash=960948343)


class WakingVigil(RollDefinition):
    """
    Arc Hand Cannon, Lightweight Frame, Anti-Overload
    Source: The Dreaming City
    https://www.light.gg/db/items/1727550459
    https://destiny.report/w/1727550459
    """
    item = Item('Waking Vigil', hash=1727550459)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            [magazine.AlloyMagazine, AnyPerk],
            [trait.Outlaw],
            [trait.Voltshot],
            [trait.GearShift],
            [trait.Meganeura],
            ),
        Roll(
            'Reload combo',
            default_barrels,
            [magazine.AlloyMagazine, AnyPerk],
            [trait.Outlaw],
            [trait.Voltshot, trait.GearShift],
            ),
        ]


class YesterdaysQuestion(RollDefinition):
    """
    Arc Hand Cannon, Heavy Burst, Anti-Unstoppable
    Source: Saint-14
    https://www.light.gg/db/items/1803480512
    https://destiny.report/w/1803480512
    """
    item = Item("Yesterday's Question", hash=1803480512)
    rolls = [
        Roll(
            'Super roll',
            [barrel.ChamberedCompensator, AnyPerk],
            [magazine.AlloyMagazine, AnyPerk],
            [trait.AirTrigger],
            [trait.FourthTimesTheCharm],
            [trait.Voltshot],
            [trait.VorpalWeapon],
            ),
        Roll(
            'Reload combo',
            [barrel.ChamberedCompensator, AnyPerk],
            [magazine.AlloyMagazine, AnyPerk],
            [trait.AirTrigger],
            [trait.Voltshot],
            ),
        Roll(
            'Miniboss damage dealing',
            [barrel.ChamberedCompensator, AnyPerk],
            [magazine.AlloyMagazine, AnyPerk],
            [trait.FourthTimesTheCharm],
            [trait.VorpalWeapon],
            ),
        ]
