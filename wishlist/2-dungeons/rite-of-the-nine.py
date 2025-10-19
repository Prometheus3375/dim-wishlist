from wishlist import *


class Judgement(RollDefinition):
    """
    Stasis Hand Cannon, Adaptive Frame
    https://www.light.gg/db/items/2226572694
    """
    items = [
        Item(name='Judgment', hash=2226572694),
        Item(name='Judgment (Adept)', hash=1987644603),
        Item(name='Judgment', hash=1773934241),
        Item(name='Judgment (Adept)', hash=3329218848),
        ]
    rolls = [
        Roll(
            'PvE classic',
            [sight.SteadyhandHCS, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.RapidHit],
            [trait.TimedPayload],
            ),
        Roll(
            'Stasis Combo',
            [sight.SteadyhandHCS, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.Headstone],
            [trait.Rimestealer],
            ),
        ]


class Relentless(RollDefinition):
    """
    Strand Pulse Rifle, High-Impact Frame
    https://www.light.gg/db/items/3733988413
    """
    items = [
        Item(name='Relentless', hash=3733988413),
        Item(name='Relentless (Adept)', hash=1827058652),
        Item(name='Relentless', hash=3681280908),
        Item(name='Relentless (Adept)', hash=1066598837),
        ]
    rolls = [
        Roll(
            'PvE',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Firefly, trait.Tear],
            [trait.Hatchling],
            ),
        ]


class Prosecutor(RollDefinition):
    """
    Arc Auto Rifle, Precision Frame
    https://www.light.gg/db/items/880829467
    """
    items = [
        Item(name='Prosecutor', hash=880829467),
        Item(name='Prosecutor (Adept)', hash=4025177550),
        Item(name='Prosecutor', hash=2129814338),
        Item(name='Prosecutor (Adept)', hash=749483159),
        ]


class SuddenDeath(RollDefinition):
    """
    Void Shotgun, Aggressive Frame
    https://www.light.gg/db/items/1976481399
    """
    items = [
        Item(name='A Sudden Death', hash=1976481399),
        Item(name='A Sudden Death (Adept)', hash=1626437786),
        Item(name='A Sudden Death', hash=1904170910),
        Item(name='A Sudden Death (Adept)', hash=2764074355),
        ]


class LiminalVigil(RollDefinition):
    """
    Stasis Sidearm, Heavy Burst
    https://www.light.gg/db/items/2575844666
    """
    items = [
        Item(name='Liminal Vigil', hash=2575844666),
        Item(name='Liminal Vigil (Adept)', hash=1905934655),
        Item(name='Liminal Vigil', hash=1460079227),
        Item(name='Liminal Vigil (Adept)', hash=3421639790),
        ]
    rolls = [
        Roll(
            'Stasis combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.Headstone],
            [trait.Rimestealer],
            ),
        ]


class LongArm(RollDefinition):
    """
    Arc Scout Rifle, Aggressive Frame
    https://www.light.gg/db/items/4249949938
    """
    items = [
        Item(name='Long Arm', hash=4249949938),
        Item(name='Long Arm (Adept)', hash=4239378215),
        Item(name='Long Arm', hash=14929251),
        Item(name='Long Arm (Adept)', hash=3692140710),
        ]
    rolls = [
        Roll(
            'PvE',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.DualLoader, trait.HipFireGrip],
            [trait.Redirection, trait.ExplosivePayload],
            ),
        ]


class Wilderflight(RollDefinition):
    """
    Void Breechloaded Grenade Launcher, Double Fire
    https://www.light.gg/db/items/1206729100
    """
    items = [
        Item(name='Wilderflight', hash=1206729100),
        Item(name='Wilderflight (Adept)', hash=559523765),
        Item(name='Wilderflight', hash=2982006965),
        Item(name='Wilderflight (Adept)', hash=2477408004),
        ]
    rolls = [
        Roll(
            'Damage rotations',
            [launcher_barrel.HardLaunch, AnyPerk],
            [magazine.SpikeGrenades, AnyPerk],
            [trait.EnviousArsenal],
            [trait.BaitAndSwitch],
            ),
        ]


class TerminusHorizon(RollDefinition):
    """
    Arc Machine Gun, High-Impact Frame
    https://www.light.gg/db/items/3984556130
    """
    items = [
        Item(name='Terminus Horizon', hash=3984556130),
        Item(name='Terminus Horizon (Adept)', hash=2210806903),
        Item(name='Terminus Horizon', hash=2730671571),
        Item(name='Terminus Horizon (Adept)', hash=4267192886),
        ]
    rolls = [
        Roll(
            'PvE',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.AppendedMag, AnyPerk],
            [trait.Reconstruction],
            [trait.KillingTally, trait.JoltingFeedback],
            ),
        ]


class NoSurvivors(RollDefinition):
    """
    Solar Submachine Gun, Aggressive Frame
    https://www.light.gg/db/items/4228149269
    """
    items = [
        Item(name='No Survivors', hash=4228149269),
        Item(name='No Survivors (Adept)', hash=189194532),
        Item(name='No Survivors', hash=4193602194),
        Item(name='No Survivors (Adept)', hash=1157220231),
        ]
    rolls = [
        Roll(
            'PvE',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.HealClip],
            [trait.Incandescent, trait.MasterOfArms],
            ),
        ]


class NewPacificEpitaph(RollDefinition):
    """
    Stasis Breechloaded Grenade Launcher, Wave Frame
    https://www.light.gg/db/items/2059741649
    """
    items = [
        Item(name='New Pacific Epitaph', hash=2059741649),
        Item(name='New Pacific Epitaph (Adept)', hash=233402416),
        Item(name='New Pacific Epitaph', hash=492673102),
        Item(name='New Pacific Epitaph (Adept)', hash=3185151619),
        ]
    rolls = [
        Roll(
            'Ad clear',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.Unrelenting],
            [trait.ChainReaction, trait.KillClip, trait.Redirection],
            ),
        Roll(
            'Grenade combo',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.Demolitionist],
            [trait.AdrenalineJunkie],
            ),
        Roll(
            'Reload combo',
            [launcher_barrel.VolatileLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.RecycledEnergy],
            [trait.KillClip],
            ),
        ]


class GreasyLuck(RollDefinition):
    """
    Solar Rapid-Fire Glaive
    https://www.light.gg/db/items/2934305134
    """
    items = [
        Item(name='Greasy Luck', hash=2934305134),
        Item(name='Greasy Luck (Adept)', hash=3210739171),
        Item(name='Greasy Luck', hash=1685406703),
        Item(name='Greasy Luck (Adept)', hash=1050582210),
        ]
    rolls = [
        Roll(
            'PvE',
            [haft.AuxiliaryReserves, haft.LowImpedanceWindings, AnyPerk],
            [magazine.AlloyMagazine, magazine.LightMag, AnyPerk],
            [trait.ReplenishingAegis, trait.Reconstruction],
            [trait.Redirection, trait.Incandescent],
            ),
        Roll(
            'Melee damage',
            [haft.AuxiliaryReserves, haft.LowImpedanceWindings, AnyPerk],
            [magazine.AlloyMagazine, magazine.LightMag, AnyPerk],
            [trait.ReplenishingAegis, trait.Reconstruction],
            [trait.CloseToMelee],
            ),
        ]


class ColdComfort(RollDefinition):
    """
    Stasis Rocket Launcher, Aggressive Frame
    https://www.light.gg/db/items/291447487
    """
    items = [
        Item(name='Cold Comfort', hash=291447487),
        Item(name='Cold Comfort (Adept)', hash=1817605554),
        Item(name='Cold Comfort', hash=2760833884),
        Item(name='Cold Comfort (Adept)', hash=2126543269),
        ]
    rolls = [
        Roll(
            "Damage dealing; prefer Heretic's Fervor for roll with Explosive Light",
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.ImpactCasing, AnyPerk],
            [trait.EnviousArsenal, trait.Reconstruction],
            [trait.BaitAndSwitch, trait.ElementalHoning],
            ),
        ]
