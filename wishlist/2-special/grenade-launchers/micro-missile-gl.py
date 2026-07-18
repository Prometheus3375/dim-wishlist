from wishlist import *

# Quick Launch is used because -5 points of Blast Radius from Hard Launch
# are removed by any Masterwork on T5 weapon.
default_barrels = [launcher_barrel.QuickLaunch, AnyPerk]
default_magazine = [magazine.SpikeGrenades, AnyPerk]


class TheMountaintop(RollDefinition):
    """
    Kinetic Breechloaded Grenade Launcher, Micro-Missile Frame, Anti-Unstoppable
    Source: Onslaught
    https://www.light.gg/db/items/3736001861
    https://destiny.report/w/3736001861
    """
    item = Item('The Mountaintop', hash=3736001861)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_magazine,
            [trait.AutoLoadingHolster],
            [trait.Overflow],
            [trait.BewilderingBurst],
            [trait.Recombination],
            [trait.AllStar],
            [trait.AncillaryOrdinance],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_magazine,
            [trait.BewilderingBurst],
            [trait.AncillaryOrdinance],
            ),
        Roll(
            'Damage rotations',
            default_barrels,
            default_magazine,
            [trait.AutoLoadingHolster],
            [trait.AllStar, trait.Recombination],
            ),
        ]


class Theodolite(RollDefinition):
    """
    Arc Breechloaded Grenade Launcher, Micro-Missile Frame, Anti-Unstoppable
    Source: Commander Zavala; Tenet of Bravery
    https://www.light.gg/db/items/4146673635
    https://destiny.report/w/4146673635
    """
    item = Item('Theodolite', hash=4146673635)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_magazine,
            [trait.EddyCurrent],
            [trait.Reconstruction],
            [trait.Voltshot],
            [trait.ReapersTithe],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_magazine,
            [trait.EddyCurrent],
            [trait.Voltshot],
            ),
        Roll(
            'Damage rotations',
            default_barrels,
            default_magazine,
            [trait.Reconstruction],
            [trait.ReapersTithe],
            ),
        ]


class GizmoWeft(RollDefinition):
    """
    Strand Breechloaded Grenade Launcher, Micro-Missile Frame, Anti-Unstoppable
    Source: Events during season "Lawless"
    https://www.light.gg/db/items/4069880346
    https://destiny.report/w/4069880346
    """
    items = [
        Item('Gizmo Weft', hash=4069880346),
        Item('Gizmo Weft', hash=1572604081),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_magazine,
            [trait.AirTrigger],
            [trait.EnviousArsenal],
            [trait.AggregateCharge],
            [trait.Bipod],
            ),
        Roll(
            'Movement',
            default_barrels,
            default_magazine,
            [trait.AirTrigger],
            [trait.Bipod],
            ),
        Roll(
            'Damage rotations',
            default_barrels,
            default_magazine,
            [trait.EnviousArsenal],
            [trait.AggregateCharge],
            ),
        ]
