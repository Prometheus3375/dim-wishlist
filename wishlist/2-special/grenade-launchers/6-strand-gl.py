from wishlist import *


class GizmoWeft(RollDefinition):
    """
    Strand Breechloaded Grenade Launcher, Micro-Missile Frame, Anti-Unstoppable
    Source: Lawless Events
    https://www.light.gg/db/items/4069880346
    https://destiny.report/w/4069880346
    """
    items = [
        Item('Gizmo Weft', hash=4069880346),
        Item('Gizmo Weft', hash=1572604081),
        ]
    rolls = [
        Roll(
            'Movement',
            [launcher_barrel.HardLaunch, AnyPerk],
            [magazine.SpikeGrenades, AnyPerk],
            [trait.AirTrigger],
            [trait.Bipod],
            ),
        Roll(
            'Damage dealing',
            [launcher_barrel.HardLaunch, AnyPerk],
            [magazine.SpikeGrenades, AnyPerk],
            [trait.EnviousArsenal],
            [trait.AggregateCharge, trait.BaitAndSwitch, trait.ElementalHoning],
            ),
        ]


class TuskOfTheBoar(RollDefinition):
    """
    Strand Breechloaded Grenade Launcher, Wave Frame, Anti-Unstoppable
    Source: Unspecified
    https://www.light.gg/db/items/491956886
    https://destiny.report/w/491956886
    """
    item = Item('Tusk of the Boar', hash=491956886)
