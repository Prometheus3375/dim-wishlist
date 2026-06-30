from wishlist import *


class DoomedPetitioner(RollDefinition):
    """
    Void Linear Fusion Rifle, Adaptive Burst, Anti-Barrier, Craftable
    Source: Starcrossed
    https://www.light.gg/db/items/1501688142
    https://destiny.report/w/1501688142
    """
    item = Item('Doomed Petitioner', hash=1501688142)


class EyesUnveiled(RollDefinition):
    """
    Void Linear Fusion Rifle, Precision Frame, Anti-Barrier
    Source: Pit of Heresy
    https://www.light.gg/db/items/4147428506
    https://destiny.report/w/4147428506
    """
    item = Item('Eyes Unveiled', hash=4147428506)


class MistralLift(RollDefinition):
    """
    Void Linear Fusion Rifle, Adaptive Burst, Anti-Barrier
    Source: The Dawning
    https://www.light.gg/db/items/766122634
    https://destiny.report/w/766122634
    """
    items = [
        Item('Mistral Lift', hash=766122634),
        Item('Mistral Lift', hash=270610849),
        ]
    roll = Roll(
        'Damage dealing',
        [barrel.ArrowheadBrake, AnyPerk],
        [battery.AcceleratedCoils, AnyPerk],
        [trait.EnviousArsenal, trait.WitheringGaze],
        [trait.BaitAndSwitch],
        [origin.VeistStinger],
        )


class Taipan4fr(RollDefinition):
    """
    Void Linear Fusion Rifle, Precision Frame, Anti-Barrier, Craftable
    Source: Quest "Foundry Resonance"
    https://www.light.gg/db/items/1911060537
    https://destiny.report/w/1911060537
    """
    item = Item('Taipan-4fr', hash=1911060537)
