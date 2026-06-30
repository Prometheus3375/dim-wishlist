from wishlist import *


class Adamantite(RollDefinition):
    """
    Strand Auto Rifle, Support Frame, Anti-Overload
    Source: Pit of Heresy
    https://www.light.gg/db/items/621450049
    https://destiny.report/w/621450049
    """
    item = Item('Adamantite', hash=621450049)


class AuricDisabler(RollDefinition):
    """
    Strand Auto Rifle, Precision Frame, Anti-Barrier
    Source: Saint-14
    https://www.light.gg/db/items/702001725
    https://destiny.report/w/702001725
    """
    item = Item('Auric Disabler', hash=702001725)
    roll = Roll(
        'PvE',
        [barrel.ArrowheadBrake, AnyPerk],
        [magazine.FlaredMagwell, AnyPerk],
        [trait.Hatchling],
        [trait.Tear, trait.SwordLogic, trait.DesperateMeasures],
        )


class LethalAbundance(RollDefinition):
    """
    Strand Auto Rifle, High-Impact Frame, Anti-Unstoppable
    Source: Iron Banner
    https://www.light.gg/db/items/1884897339
    https://destiny.report/w/1884897339
    """
    item = Item('Lethal Abundance', hash=1884897339)


class Perpetualis(RollDefinition):
    """
    Strand Auto Rifle, Adaptive Frame, Anti-Barrier, Craftable
    Source: Season of Defiance
    https://www.light.gg/db/items/392008588
    https://destiny.report/w/392008588
    """
    item = Item('Perpetualis', hash=392008588)


class RufussFury(RollDefinition):
    """
    Strand Auto Rifle, Rapid-Fire Frame, Anti-Overload, Craftable
    Source: "Root of Nightmares" Raid
    https://www.light.gg/db/items/484515708
    https://destiny.report/w/484515708
    """
    items = [
        Item("Rufus's Fury", hash=484515708),
        Item("Rufus's Fury (Adept)", hash=342514437),
        ]


class TheForwardPath(RollDefinition):
    """
    Strand Auto Rifle, Adaptive Frame, Anti-Barrier
    Source: Iron Banner
    https://www.light.gg/db/items/1884897338
    https://destiny.report/w/1884897338
    """
    item = Item('The Forward Path', hash=1884897338)
