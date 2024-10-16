from database import *


class Scintillation(RD):
    items = [
        Item(name='Scintillation', hash=2591257541),
        Item(name='Scintillation (Adept)', hash=1492522228),
        ]
    rolls = [
        roll(
            'Roll for damage dealing',
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.EnhancedBattery, batteries.AcceleratedCoils, AnyPerk],
            [traits.RewindRounds, traits.EnviousAssassin],
            [traits.BaitAndSwitch, traits.Surrounded],
            [origin.VeistStinger],
            ),
        roll(
            'ALH and BnS are good combo',
            [barrels.ArrowheadBrake, AnyPerk],
            [batteries.EnhancedBattery, batteries.AcceleratedCoils, AnyPerk],
            [traits.AutoLoadingHolster],
            [traits.BaitAndSwitch],
            [origin.VeistStinger],
            ),
        roll(
            'Rewind Rounds with Veist Stinger usually allows to fire all reserves. '
            'Unfortunately, any mag stat increase above 20 reduces reserves; '
            'Enhanced Battery is +20, Ionized Battery is +40',
            [batteries.IonizedBattery],
            is_trash=True,
            ),
        ]
