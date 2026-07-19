from wishlist import *

default_barrels = [launcher_barrel.VolatileLaunch, AnyPerk]
default_magazine = [magazine.HighVelocityRounds]


class Forbearance(RollDefinition):
    """
    Arc Breechloaded Grenade Launcher, Wave Frame, Anti-Unstoppable, Craftable
    Source: Raid "Vow of the Disciple"
    https://www.light.gg/db/items/613334176
    https://destiny.report/w/613334176
    """
    items = [
        Item('Forbearance', hash=613334176),
        Item('Forbearance (Adept)', hash=4038592169),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_magazine,
            [trait.Unrelenting],
            [trait.AmbitiousAssassin],
            [trait.Demolitionist],
            [trait.Rampage],
            [trait.ChainReaction],
            [trait.GearShift],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_magazine,
            [trait.AmbitiousAssassin, trait.Unrelenting],
            [trait.ChainReaction, trait.GearShift, trait.Rampage],
            ),
        ]


class ForbearanceOnslaught(RollDefinition):
    """
    Arc Breechloaded Grenade Launcher, Wave Frame, Anti-Unstoppable
    Source: Onslaught
    https://www.light.gg/db/items/3736001860
    https://destiny.report/w/3736001860
    """
    item = Item('Forbearance', hash=3736001860)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_magazine,
            [trait.Redirection],
            [trait.AirTrigger],
            [trait.Demolitionist],
            [trait.ChainReaction],
            [trait.Voltshot],
            [trait.OneForAll],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_magazine,
            [trait.Redirection, trait.AirTrigger],
            [trait.Voltshot, trait.ChainReaction, trait.OneForAll],
            ),
        ]


class ExplosivePersonality(RollDefinition):
    """
    Solar Breechloaded Grenade Launcher, Wave Frame, Anti-Unstoppable, Craftable
    Source: Exotic mission "Vox Obscura"
    https://www.light.gg/db/items/4096943616
    https://destiny.report/w/4096943616
    """
    item = Item('Explosive Personality', hash=4096943616)
    roll = Roll(
        'Ad clear',
        default_barrels,
        default_magazine,
        [trait.AutoLoadingHolster],
        [trait.OneForAll],
        )


class RomanticDeath(RollDefinition):
    """
    Void Breechloaded Grenade Launcher, Wave Frame, Anti-Unstoppable
    Source: Events during season "Reclamation"
    https://www.light.gg/db/items/4169082039
    https://destiny.report/w/4169082039
    """
    items = [
        Item('Romantic Death', hash=4169082039),
        Item('Romantic Death', hash=2979965244),
        Item('Romantic Death', hash=2979965245),
        Item('Romantic Death', hash=2979965246),
        Item('Romantic Death', hash=2979965247),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_magazine,
            default_barrels,
            [trait.RepulsorBrace],
            [trait.FeedingFrenzy],
            [trait.DestabilizingRounds],
            [trait.OneForAll],
            [trait.ChainReaction],
            ),
        Roll(
            'Ad clear',
            default_magazine,
            default_barrels,
            [trait.FeedingFrenzy],
            [trait.ChainReaction, trait.DestabilizingRounds, trait.OneForAll],
            ),
        Roll(
            'Void combo',
            default_magazine,
            default_barrels,
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds],
            ),
        ]


class NewPacificEpitaph(RollDefinition):
    """
    Stasis Breechloaded Grenade Launcher, Wave Frame, Anti-Unstoppable
    Source: Dungeon "Ghosts of the Deep"
    https://www.light.gg/db/items/2988180391
    https://destiny.report/w/2988180391
    """
    item = Item('New Pacific Epitaph', hash=2988180391)
    is_chosen = True
    rolls = [
        Roll(
            'Super roll',
            default_magazine,
            default_barrels,
            [trait.ChainReaction],
            [trait.Rimestealer],
            [trait.AirTrigger],
            [trait.CrystallineCorpsebloom],
            [trait.Redirection],
            [trait.ReapersTithe],  # todo Check if it works properly, replace with Kill Clip if not.
            ),
        Roll(
            'Ad clear',
            default_magazine,
            default_barrels,
            [trait.ChainReaction],
            [trait.CrystallineCorpsebloom, trait.Redirection, trait.ReapersTithe],
            ),
        Roll(
            'Stasis combo',
            default_magazine,
            default_barrels,
            [trait.Rimestealer],
            [trait.CrystallineCorpsebloom],
            ),
        ]


class Permafrost(RollDefinition):
    """
    Stasis Breechloaded Grenade Launcher, Wave Frame, Anti-Unstoppable
    Source: The Dawning
    https://www.light.gg/db/items/2922964484
    https://destiny.report/w/2922964484
    """
    items = [
        Item('Permafrost', hash=2922964484),
        Item('Permafrost', hash=2316331767),
        ]
    rolls = [
        Roll(
            'Super roll',
            default_magazine,
            default_barrels,
            [trait.Rimestealer],
            [trait.Demolitionist],
            [trait.ImpromptuAmmunition],
            [trait.CrystallineCorpsebloom],
            [trait.ReapersTithe],
            # todo Check if Reapers Tithe works properly, replace with One For All if not.
            [trait.AdrenalineJunkie],
            ),
        Roll(
            'Ad clear',
            default_magazine,
            default_barrels,
            [trait.ImpromptuAmmunition],
            [trait.CrystallineCorpsebloom, trait.ReapersTithe],
            ),
        Roll(
            'Stasis combo',
            default_magazine,
            default_barrels,
            [trait.Rimestealer],
            [trait.CrystallineCorpsebloom],
            ),
        Roll(
            'Grenade combo',
            default_magazine,
            default_barrels,
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
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
    rolls = [
        Roll(
            'Super roll',
            default_barrels,
            default_magazine,
            [trait.Slice],
            [trait.Slideways],
            [trait.ChainReaction],
            [trait.Hatchling],
            [trait.Deconstruct],
            ),
        Roll(
            'Ad clear',
            default_barrels,
            default_magazine,
            [trait.Slideways],
            [trait.ChainReaction, trait.Hatchling],
            ),
        Roll(
            'Strand combo',
            default_barrels,
            default_magazine,
            [trait.Slice],
            [trait.Hatchling],
            ),
        ]
