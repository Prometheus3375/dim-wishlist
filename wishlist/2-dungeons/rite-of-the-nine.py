from wishlist import *


class Judgement(RollDefinition):
    """
    Stasis Hand Cannon, Adaptive Frame
    https://www.light.gg/db/items/2226572694
    """
    items = [
        Item('Judgment', hash=2226572694),
        Item('Judgment (Adept)', hash=1987644603),
        Item('Judgment', hash=1773934241),
        Item('Judgment (Adept)', hash=3329218848),
        ]
    rolls = [
        Roll(
            'PvE classic',
            [sight.SteadyHandHCS, AnyPerk],
            [magazine.TacticalMag, AnyPerk],
            [trait.RapidHit],
            [trait.TimedPayload],
            ),
        Roll(
            'Stasis Combo',
            [sight.SteadyHandHCS, AnyPerk],
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
        Item('Relentless', hash=3733988413),
        Item('Relentless (Adept)', hash=1827058652),
        Item('Relentless', hash=3681280908),
        Item('Relentless (Adept)', hash=1066598837),
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
        Item('Prosecutor', hash=880829467),
        Item('Prosecutor (Adept)', hash=4025177550),
        Item('Prosecutor', hash=2129814338),
        Item('Prosecutor (Adept)', hash=749483159),
        ]


class SuddenDeath(RollDefinition):
    """
    Void Shotgun, Aggressive Frame
    https://www.light.gg/db/items/1976481399
    """
    items = [
        Item('A Sudden Death', hash=1976481399),
        Item('A Sudden Death (Adept)', hash=1626437786),
        Item('A Sudden Death', hash=1904170910),
        Item('A Sudden Death (Adept)', hash=2764074355),
        ]


class LiminalVigil(RollDefinition):
    """
    Stasis Sidearm, Heavy Burst
    https://www.light.gg/db/items/2575844666
    """
    items = [
        Item('Liminal Vigil', hash=2575844666),
        Item('Liminal Vigil (Adept)', hash=1905934655),
        Item('Liminal Vigil', hash=1460079227),
        Item('Liminal Vigil (Adept)', hash=3421639790),
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
        Item('Long Arm', hash=4249949938),
        Item('Long Arm (Adept)', hash=4239378215),
        Item('Long Arm', hash=14929251),
        Item('Long Arm (Adept)', hash=3692140710),
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
        Item('Wilderflight', hash=1206729100),
        Item('Wilderflight (Adept)', hash=559523765),
        Item('Wilderflight', hash=2982006965),
        Item('Wilderflight (Adept)', hash=2477408004),
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
        Item('Terminus Horizon', hash=3984556130),
        Item('Terminus Horizon (Adept)', hash=2210806903),
        Item('Terminus Horizon', hash=2730671571),
        Item('Terminus Horizon (Adept)', hash=4267192886),
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
        Item('No Survivors', hash=4228149269),
        Item('No Survivors (Adept)', hash=189194532),
        Item('No Survivors', hash=4193602194),
        Item('No Survivors (Adept)', hash=1157220231),
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
        Item('New Pacific Epitaph', hash=2059741649),
        Item('New Pacific Epitaph (Adept)', hash=233402416),
        Item('New Pacific Epitaph', hash=492673102),
        Item('New Pacific Epitaph (Adept)', hash=3185151619),
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
        Item('Greasy Luck', hash=2934305134),
        Item('Greasy Luck (Adept)', hash=3210739171),
        Item('Greasy Luck', hash=1685406703),
        Item('Greasy Luck (Adept)', hash=1050582210),
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
        Item('Cold Comfort', hash=291447487),
        Item('Cold Comfort (Adept)', hash=1817605554),
        Item('Cold Comfort', hash=2760833884),
        Item('Cold Comfort (Adept)', hash=2126543269),
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
