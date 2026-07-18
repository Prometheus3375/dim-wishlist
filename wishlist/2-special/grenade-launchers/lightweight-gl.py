from wishlist import *

# Quick Launch is used because -5 points of Blast Radius from Hard Launch
# are removed by any Masterwork on T5 weapon.
default_barrels = [launcher_barrel.QuickLaunch, AnyPerk]
default_magazine = [magazine.SpikeGrenades, AnyPerk]

blinding_trash_roll = Roll(
    'Danger Zone does not buff radius of Disorienting Grenades',
    [magazine.DisorientingGrenades],
    [trait.DangerZone],
    is_trash=True,
    )


class PardonOurDust(RollDefinition):
    """
    Kinetic Breechloaded Grenade Launcher, Lightweight Frame, Anti-Overload, Craftable
    Source: Eternity
    https://www.light.gg/db/items/3849810018
    https://destiny.report/w/3849810018
    """
    item = Item('Pardon Our Dust', hash=3849810018)
    rolls = [
        Roll(
            'Debuff support',
            default_barrels,
            [magazine.DisorientingGrenades],
            [trait.AutoLoadingHolster],
            ),
        blinding_trash_roll,
        ]


class ProdigalReturn(RollDefinition):
    """
    Arc Breechloaded Grenade Launcher, Lightweight Frame, Anti-Overload, Craftable
    Source: Exotic mission "//NODE.OVRD.AVALON//"
    https://www.light.gg/db/items/268260373
    https://destiny.report/w/268260373
    """
    item = Item('Prodigal Return', hash=268260373)
    roll = Roll(
        'Ad clear',
        default_barrels,
        default_magazine,
        [trait.FieldPrep],
        [trait.Voltshot],
        )


class SalvagersSalvo(RollDefinition):
    """
    Arc Breechloaded Grenade Launcher, Lightweight Frame, Anti-Overload
    Source: Pinnacle Ops
    https://www.light.gg/db/items/1692109318
    https://destiny.report/w/1692109318
    """
    items = [
        Item("Salvager's Salvo", hash=1692109318),
        Item("Salvager's Salvo", hash=2461640837),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_magazine,
            [trait.AmbitiousAssassin],
            [trait.ChainReaction],
            [trait.TrickleCharge],
            [trait.GearShift],
            [trait.Voltshot],
            [trait.ReapersTithe],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_magazine,
            [trait.ChainReaction, trait.AmbitiousAssassin],
            [trait.Voltshot],
            ),
        Roll(
            'Damage dealing',
            default_barrels,
            default_magazine,
            [trait.TrickleCharge],
            [trait.GearShift, trait.ReapersTithe],
            ),
        ]


class EmptyVessel(RollDefinition):
    """
    Solar Breechloaded Grenade Launcher, Lightweight Frame, Anti-Overload
    Source: Commander Zavala
    https://www.light.gg/db/items/198068259
    https://destiny.report/w/198068259
    """
    item = Item('Empty Vessel', hash=198068259)
    rolls = [
        Roll(
            'Debuff support',
            default_barrels,
            [magazine.DisorientingGrenades],
            [trait.AutoLoadingHolster],
            ),
        blinding_trash_roll,
        ]


class LingeringDread(RollDefinition):
    """
    Stasis Breechloaded Grenade Launcher, Lightweight Frame, Anti-Overload
    Source: Dungeon "Duality"
    https://www.light.gg/db/items/1745368385
    https://destiny.report/w/1745368385
    """
    item = Item('Lingering Dread', hash=1745368385)
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_magazine,
            [trait.AutoLoadingHolster],
            [trait.AmbitiousAssassin],
            [trait.Discord],
            [trait.Bipod],
            [trait.ChillClip],
            [trait.ChainReaction],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_magazine,
            [trait.AmbitiousAssassin, trait.Discord],
            [trait.Bipod, trait.ChainReaction],
            ),
        Roll(
            'Debuff support',
            default_barrels,
            [magazine.DisorientingGrenades],
            [trait.AutoLoadingHolster],
            [trait.ChillClip]
            ),
        ]
