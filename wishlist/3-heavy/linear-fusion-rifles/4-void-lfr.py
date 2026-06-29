from wishlist import *


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
