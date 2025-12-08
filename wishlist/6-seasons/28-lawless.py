from wishlist import *


class KingOrfeo(RollDefinition):
    """
    Arc Combat Bow, Precision Frame
    https://www.light.gg/db/items/3481382332
    """
    items = [
        Item('King Orfeo', hash=3481382332),
        Item('King Orfeo', hash=784540300),
        Item('King Orfeo', hash=784540301),
        Item('King Orfeo', hash=784540302),
        Item('King Orfeo', hash=784540303),
        ]
    rolls = [
        Roll(
            'Ad clear',
            [bowstring.ElasticString, AnyPerk],
            [arrow.CompactArrowShaft, AnyPerk],
            [trait.ArchersTempo],
            [trait.Dragonfly, trait.Meganeura, trait.JoltingFeedback],
            ),
        Roll(
            'Ad clear',
            [bowstring.ElasticString, AnyPerk],
            [arrow.CompactArrowShaft, AnyPerk],
            [trait.ExplosiveHead],
            [trait.JoltingFeedback],
            ),
        ]


# Special


class ActionItem(RollDefinition):
    """
    Stasis Trace Rifle, Adaptive Frame
    https://www.light.gg/db/items/527989828
    """
    items = [
        Item('Action Item', hash=527989828),
        Item('Action Item', hash=437854388),
        Item('Action Item', hash=437854389),
        Item('Action Item', hash=437854390),
        Item('Action Item', hash=437854391),
        ]
    rolls = [
        Roll(
            'Stasis combo',
            [barrel.Smallbore, AnyPerk],
            [battery.LightBattery, AnyPerk],
            [trait.Rimestealer],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Ad clear',
            [barrel.Smallbore, AnyPerk],
            [battery.LightBattery, AnyPerk],
            [trait.Demolitionist],
            [trait.CrystallineCorpsebloom, trait.DetonatorBeam],
            ),
        Roll(
            'Deconstruct',
            [barrel.Smallbore, AnyPerk],
            [battery.LightBattery, AnyPerk],
            [trait.Deconstruct],
            [trait.CrystallineCorpsebloom, trait.DetonatorBeam],
            ),
        ]


class GizmoWeft(RollDefinition):
    """
    Strand Breechloaded Grenade Launcher, Micro-Missile Frame
    https://www.light.gg/db/items/4069880346
    """
    items = [
        Item('Gizmo Weft', hash=4069880346),
        Item('Gizmo Weft', hash=1572604081),
        ]
    rolls = [
        Roll(
            'Damage dealing',
            [launcher_barrel.HardLaunch, AnyPerk],
            [magazine.SpikeGrenades, AnyPerk],
            [trait.EnviousArsenal],
            [trait.AggregateCharge, trait.BaitAndSwitch, trait.ElementalHoning],
            ),
        ]


class TheHeron(RollDefinition):
    """
    Void Aggressive Glaive
    https://www.light.gg/db/items/2246386812
    """
    items = [
        Item('The Heron', hash=2246386812),
        Item('The Heron', hash=617566156),
        Item('The Heron', hash=617566157),
        Item('The Heron', hash=617566158),
        Item('The Heron', hash=617566159),
        ]
    rolls = [
        # todo: probably add Proximity Power roll
        Roll(
            'Damage blocking',
            [haft.LowImpedanceWindings, AnyPerk],
            [magazine.AlloyMagazine, AnyPerk],
            [trait.ReplenishingAegis],
            [trait.Redirection, trait.AncillaryOrdinance, trait.DestabilizingRounds],
            ),
        ]


# Heavy


class Micromort(RollDefinition):
    """
    Arc Rocket Launcher, Precision Frame
    https://www.light.gg/db/items/474671201
    """
    items = [
        Item('Micromort', hash=474671201),
        Item('Micromort', hash=602331464),
        Item('Micromort', hash=602331465),
        Item('Micromort', hash=602331466),
        Item('Micromort', hash=602331467),
        ]
    rolls = [
        Roll(
            'Damage dealing',
            [launcher_barrel.QuickLaunch],
            [magazine.ImpactCasing],
            [trait.ExplosivePayload, trait.EnviousArsenal],
            [trait.BaitAndSwitch],
            ),
        ]
