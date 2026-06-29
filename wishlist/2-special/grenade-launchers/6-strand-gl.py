from wishlist import *


class FestivalFlight(RollDefinition):
    """
    Strand Breechloaded Grenade Launcher, Area Denial Frame, Anti-Overload
    Source: Solstice
    https://www.light.gg/db/items/4019651319
    https://destiny.report/w/4019651319
    """
    items = [
        Item('Festival Flight', hash=4019651319),
        Item('Festival Flight', hash=3977654524),
        ]
    rolls = [
        # todo: add a roll with Blast Distributor next Solstice
        Roll(
            'Ad clear',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.AmbitiousAssassin, trait.Demolitionist, trait.Slice],
            [trait.OneForAll, trait.Hatchling],
            ),
        Roll(
            'Damage rotations',
            [launcher_barrel.Countermass, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.EnviousArsenal],
            [trait.ElementalHoning],
            ),
        ]


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
    Source: Lord Saladin
    https://www.light.gg/db/items/491956886
    https://destiny.report/w/491956886
    """
    item = Item('Tusk of the Boar', hash=491956886)
