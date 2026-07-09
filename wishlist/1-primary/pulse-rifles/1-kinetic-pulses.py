from wishlist import *
from . import *


class AutumnWind(RollDefinition):
    """
    Kinetic Pulse Rifle, Rapid-Fire Frame, Anti-Overload
    Source: Crucible
    https://www.light.gg/db/items/2150012407
    https://destiny.report/w/2150012407
    """
    items = [
        Item('Autumn Wind', hash=2150012407),
        Item('Autumn Wind', hash=2459087496),
        ]


class BattleScar(RollDefinition):
    """
    Kinetic Pulse Rifle, Lightweight Frame, Anti-Overload
    Source: European Dead Zone
    https://www.light.gg/db/items/1525080480
    https://destiny.report/w/1525080480
    """
    item = Item('Battle Scar', hash=1525080480)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.ShootToLoot],
            [trait.Overflow],
            [trait.AttritionOrbs],
            [trait.KineticTremors],
            [trait.AllStar],
            ),
        Roll(
            'Hit combo',
            default_barrels,
            default_mags,
            [trait.AttritionOrbs],
            [trait.KineticTremors],
            ),
        Roll(
            'Shoot to Loot',
            default_barrels,
            default_mags,
            [trait.ShootToLoot],
            [trait.KineticTremors, trait.AllStar],
            ),
        ]


class BlastFurnace(RollDefinition):
    """
    Kinetic Pulse Rifle, Aggressive Burst, Anti-Unstoppable
    Source: Arena Ops
    https://www.light.gg/db/items/52683113
    https://destiny.report/w/52683113
    """
    items = [
        Item('Blast Furnace', hash=52683113),
        Item('Blast Furnace', hash=2631356658),
        ]
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.BewilderingBurst],
            [trait.AncillaryOrdinance],
            [trait.KineticTremors],
            [trait.Firefly],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.KineticTremors],
            [trait.Firefly, trait.ChaosReshaped],
            ),
        ]


class Bygones(RollDefinition):
    """
    Kinetic Pulse Rifle, Adaptive Frame, Anti-Barrier
    Source: Gambit
    https://www.light.gg/db/items/767170345
    https://destiny.report/w/767170345
    """
    item = Item('Bygones', hash=767170345)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.AttritionOrbs],
            [trait.ShootToLoot],
            [trait.StoppingPower],
            [trait.KineticTremors],
            [trait.Firefly],
            [trait.AllStar],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.KineticTremors],
            [trait.Firefly, trait.ChaosReshaped],
            ),
        Roll(
            'Shoot to Loot',
            default_barrels,
            default_mags,
            [trait.ShootToLoot],
            [trait.KineticTremors, trait.AllStar],
            ),
        ]


class ChatteringBone(RollDefinition):
    """
    Kinetic Pulse Rifle, Lightweight Frame, Anti-Overload, Craftable
    Source: Raid "Last Wish"
    https://www.light.gg/db/items/501329015
    https://destiny.report/w/501329015
    """
    item = Item('Chattering Bone', hash=501329015)
    roll = Roll(
        'Ad clear',
        default_barrels,
        default_mags,
        [trait.StoppingPower],
        [trait.KineticTremors],
        )


class ChatteringBonePantheon(RollDefinition):
    """
    Kinetic Pulse Rifle, Lightweight Frame, Anti-Overload
    Source: Pantheon
    https://www.light.gg/db/items/830651379
    https://destiny.report/w/830651379
    """
    items = [
        Item('Chattering Bone', hash=830651379),
        Item('Chattering Bone', hash=4157371152),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.BewilderingBurst],
            [trait.AttritionOrbs],
            [trait.CollectiveDemolition],
            [trait.KineticTremors],
            [trait.AncillaryOrdinance],
            [trait.ChaosReshaped],
            ),
        Roll(
            'Hit combo',
            default_barrels,
            default_mags,
            [trait.AttritionOrbs],
            [trait.KineticTremors],
            ),
        ]


class ColdDenial(RollDefinition):
    """
    Kinetic Pulse Rifle, High-Impact Frame, Anti-Unstoppable
    Source: Banshee-44
    https://www.light.gg/db/items/324584913
    https://destiny.report/w/324584913
    """
    item = Item('Cold Denial', hash=324584913)


class PieceOfMind(RollDefinition):
    """
    Kinetic Pulse Rifle, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: Exotic mission "Vox Obscura"
    https://www.light.gg/db/items/2097055732
    https://destiny.report/w/2097055732
    """
    item = Item('Piece of Mind', hash=2097055732)


class SacredProvenance(RollDefinition):
    """
    Kinetic Pulse Rifle, Aggressive Burst, Anti-Unstoppable, Craftable
    Source: Raid "Garden of Salvation"
    https://www.light.gg/db/items/2241507890
    https://destiny.report/w/2241507890
    """
    item = Item('Sacred Provenance', hash=2241507890)
    roll = Roll(
        'Ad clear',
        default_barrels,
        default_mags,
        [trait.StoppingPower],
        [trait.KineticTremors],
        )


class SmiteOfMerain(RollDefinition):
    """
    Kinetic Pulse Rifle, Adaptive Frame, Anti-Barrier, Craftable
    Source: Raid "King's Fall"
    https://www.light.gg/db/items/2221264583
    https://destiny.report/w/2221264583
    """
    items = [
        Item('Smite of Merain', hash=2221264583),
        Item('Smite of Merain (Harrowed)', hash=3407395594),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.Demolitionist],
            [trait.AncillaryOrdinance],
            [trait.BewilderingBurst],
            [trait.AdrenalineJunkie],
            [trait.Firefly],
            [trait.AllStar],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.BewilderingBurst],
            [trait.Firefly],
            ),
        Roll(
            'Grenade combo',
            default_barrels,
            default_mags,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        ]


class TheMessenger(RollDefinition):
    """
    Kinetic Pulse Rifle, High-Impact Frame, Anti-Unstoppable
    Source: Trials of Osiris
    https://www.light.gg/db/items/4277548087
    https://destiny.report/w/4277548087
    """
    item = Item('The Messenger', hash=4277548087)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_mags,
            [trait.BewilderingBurst],
            [trait.Firefly],
            [trait.StoppingPower],
            [trait.KineticTremors],
            [trait.AncillaryOrdinance],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_mags,
            [trait.Firefly, trait.StoppingPower],
            [trait.KineticTremors],
            ),
        ]
