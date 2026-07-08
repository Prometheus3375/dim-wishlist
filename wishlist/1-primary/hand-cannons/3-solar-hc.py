from wishlist import *
from . import *


class Agape(RollDefinition):
    """
    Solar Hand Cannon, Heavy Burst, Anti-Unstoppable
    Source: Kepler
    https://www.light.gg/db/items/4124362340
    https://destiny.report/w/4124362340
    """
    item = Item('Agape', hash=4124362340)
    rolls = [
        Roll(
            'Super roll',
            [barrel.ChamberedCompensator, AnyPerk],
            [magazine.AppendedMag, AnyPerk],
            [trait.HealClip],
            [trait.RewindRounds],
            [trait.Incandescent],
            [trait.PrecisionInstrument],
            [trait.Firefly],
            ),
        Roll(
            'Solar combo',
            [barrel.ChamberedCompensator, AnyPerk],
            [magazine.AlloyMagazine, AnyPerk],
            [trait.HealClip],
            [trait.Incandescent],
            ),
        Roll(
            'Miniboss damage dealing',
            [barrel.ChamberedCompensator, AnyPerk],
            [magazine.AppendedMag, AnyPerk],
            [trait.RewindRounds],
            [trait.PrecisionInstrument],
            ),
        ]


class EpochalIntegration(RollDefinition):
    """
    Solar Hand Cannon, Adaptive Frame, Anti-Barrier
    Source: Terminal Overload
    https://www.light.gg/db/items/3851394887
    https://destiny.report/w/3851394887
    """
    item = Item('Epochal Integration', hash=3851394887)
    rolls = [
        Roll(
            'Super roll',
            [barrel.ChamberedCompensator, AnyPerk],
            default_mags,
            [trait.HealClip],
            [trait.ExplosivePayload],
            [trait.Incandescent],
            [trait.Meganeura],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Solar combo',
            [barrel.ChamberedCompensator, AnyPerk],
            default_mags,
            [trait.HealClip],
            [trait.Incandescent],
            ),
        ]


class FiniteImpactor(RollDefinition):
    """
    Solar Hand Cannon, Adaptive Frame, Anti-Barrier
    Source: Iron Banner
    https://www.light.gg/db/items/1917334929
    https://destiny.report/w/1917334929
    """
    item = Item('Finite Impactor', hash=1917334929)


class FrontiersCry(RollDefinition):
    """
    Solar Hand Cannon, Precision Frame, Anti-Barrier
    Source: Lord Saladin
    https://www.light.gg/db/items/3203303472
    https://destiny.report/w/3203303472
    """
    item = Item("Frontier's Cry", hash=3203303472)


class IgneousHammer(RollDefinition):
    """
    Solar Hand Cannon, Aggressive Frame, Anti-Unstoppable
    Source: Trials of Osiris
    https://www.light.gg/db/items/2776092652
    https://destiny.report/w/2776092652
    """
    item = Item('Igneous Hammer', hash=2776092652)


class LunasHowl(RollDefinition):
    """
    Solar Hand Cannon, Precision Frame, Anti-Barrier
    Source: Onslaught
    https://www.light.gg/db/items/2033531688
    https://destiny.report/w/2033531688
    """
    item = Item("Luna's Howl", hash=2033531688)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            [magazine.AlloyMagazine, AnyPerk],
            [trait.HealClip],
            [trait.Firefly],
            [trait.ChaosReshaped],
            [trait.Incandescent],
            ),
        Roll(
            'Solar combo',
            default_barrels,
            [magazine.AlloyMagazine, AnyPerk],
            [trait.HealClip],
            [trait.Incandescent],
            ),
        ]


class Trust(RollDefinition):
    """
    Solar Hand Cannon, Precision Frame, Anti-Barrier
    Source: Gambit
    https://www.light.gg/db/items/810474118
    https://destiny.report/w/810474118
    """
    item = Item('Trust', hash=810474118)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Firefly],
            [trait.ExplosivePayload],
            [trait.Incandescent],
            ),
        Roll(
            'Solar combo',
            default_barrels,
            default_mags,
            [trait.Firefly],
            [trait.Incandescent],
            ),
        ]


class ZaoulisBane(RollDefinition):
    """
    Solar Hand Cannon, Adaptive Frame, Anti-Barrier, Craftable
    Source: King's Fall
    https://www.light.gg/db/items/431721920
    https://destiny.report/w/431721920
    """
    items = [
        Item("Zaouli's Bane", hash=431721920),
        Item("Zaouli's Bane (Harrowed)", hash=291092617),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            [barrel.ChamberedCompensator, AnyPerk],
            default_mags,
            [trait.ExplosivePayload],
            [trait.Redirection],
            [trait.Incandescent],
            [trait.Meganeura],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Ad clear',
            [barrel.ChamberedCompensator, AnyPerk],
            default_mags,
            [trait.Redirection, trait.ExplosivePayload],
            [trait.Incandescent, trait.ChaosReshaped],
            ),
        Roll(
            'Ad clear',
            [barrel.ChamberedCompensator, AnyPerk],
            default_mags,
            [trait.Redirection],
            [trait.Meganeura],
            ),
        ]


class ZaoulisBanePantheon(RollDefinition):
    """
    Solar Hand Cannon, Adaptive Frame, Anti-Barrier
    Source: Pantheon
    https://www.light.gg/db/items/3647341740
    https://destiny.report/w/3647341740
    """
    items = [
        Item("Zaouli's Bane", hash=3647341740),
        Item("Zaouli's Bane", hash=3066945855),
        ]
    rolls = [
        Roll(
            'Super roll',
            [barrel.ChamberedCompensator, AnyPerk],
            default_mags,
            [trait.ExplosivePayload],
            [trait.Firefly],
            [trait.Incandescent],
            [trait.Meganeura],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Ad clear',
            [barrel.ChamberedCompensator, AnyPerk],
            default_mags,
            [trait.Firefly, trait.ExplosivePayload],
            [trait.Incandescent, trait.ChaosReshaped],
            ),
        Roll(
            'Ad clear',
            [barrel.ChamberedCompensator, AnyPerk],
            default_mags,
            [trait.Firefly],
            [trait.Meganeura],
            ),
        ]
