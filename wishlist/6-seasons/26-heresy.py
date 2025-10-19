from wishlist import *


class Adamantite(RollDefinition):
    """
    Strand Auto Rifle, Support Frame
    https://www.light.gg/db/items/3229982889
    """
    items = [
        Item(name='Adamantite', hash=3229982889),
        Item(name='Adamantite (Adept)', hash=3485029080),
        # With Runneth Over
        Item(name='Adamantite', hash=2987244302),
        Item(name='Adamantite (Adept)', hash=601574723),
        ]
    rolls = [
        Roll(
            'Self-healing. Attrition Orbs procs from healing allies',
            [barrel.FullBore, barrel.HammerForgedRifling, barrel.Smallbore,
             barrel.CorkscrewRifling, AnyPerk],
            [magazine.FlaredMagwell, magazine.AlloyMagazine, magazine.TacticalMag, AnyPerk],
            [trait.Reciprocity],
            [trait.Hatchling, trait.AttritionOrbs],
            ),
        ]


class Psychopomp(RollDefinition):
    """
    Arc Breechloaded Grenade Launcher, Area Denial Frame
    https://www.light.gg/db/items/4028298892
    """
    items = [
        Item(name='Psychopomp', hash=4028298892),
        Item(name='Psychopomp (Adept)', hash=2553380021),
        # With Runneth Over
        Item(name='Psychopomp', hash=3840794631),
        Item(name='Psychopomp (Adept)', hash=704410186),
        ]
    rolls = [
        Roll(
            'PvE',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.AmbitiousAssassin],
            [trait.Unrelenting],
            ),
        Roll(
            'Damage rotations combo',
            [launcher_barrel.Countermass, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.EnviousArsenal],
            [trait.ElementalHoning, trait.FullCourt],
            ),
        Roll(
            'Melee regen',
            [launcher_barrel.QuickLaunch, AnyPerk],
            [magazine.HighVelocityRounds],
            [trait.Pugilist],
            [trait.RollingStorm],
            ),
        ]


class EyesUnveiled(RollDefinition):
    """
    Void Linear Fusion Rifle, Precision Frame
    https://www.light.gg/db/items/727781522
    """
    items = [
        Item(name='Eyes Unveiled', hash=727781522),
        Item(name='Eyes Unveiled (Adept)', hash=282549639),
        # With Runneth Over
        Item(name='Eyes Unveiled', hash=615373993),
        Item(name='Eyes Unveiled (Adept)', hash=4173311704),
        ]


class WatchfulEye(RollDefinition):
    """
    Arc Machine Gun, Aggressive Frame
    https://www.light.gg/db/items/1757177186
    """
    items = [
        Item(name='Watchful Eye', hash=1757177186),
        Item(name='Watchful Eye (Adept)', hash=737409399),
        # With Runneth Over
        Item(name='Watchful Eye', hash=768610585),
        Item(name='Watchful Eye (Adept)', hash=2856225832),
        ]
    rolls = [
        Roll(
            'Ad clear',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.AppendedMag, AnyPerk],
            [trait.Overflow],
            [trait.KillingTally, trait.JoltingFeedback],
            ),
        Roll(
            'Arc combo',
            [barrel.ArrowheadBrake, AnyPerk],
            [magazine.FlaredMagwell, AnyPerk],
            [trait.EddyCurrent],
            [trait.JoltingFeedback],
            ),
        ]


class AbyssalEdge(RollDefinition):
    """
    Strand Sword, Wave Sword Frame
    https://www.light.gg/db/items/547165496
    """
    items = [
        Item(name='Abyssal Edge', hash=547165496),
        Item(name='Abyssal Edge (Adept)', hash=2712683313),
        # With Runneth Over
        Item(name='Abyssal Edge', hash=4221591387),
        Item(name='Abyssal Edge (Adept)', hash=3054597646),
        ]
    rolls = [
        Roll(
            'Damage dealing',
            [blade.JaggedEdge],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.RelentlessStrikes],
            [trait.Surrounded],
            ),
        Roll(
            'Damage blocking',
            [blade.JaggedEdge, AnyPerk],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.FlashCounter],
            [trait.Redirection, trait.Hatchling],
            ),
        ]


class RefusalOfTheCall(RollDefinition):
    """
    Strand Adaptive Glaive
    https://www.light.gg/db/items/3269398063
    """
    items = [
        Item(name='Refusal of the Call', hash=3269398063),
        Item(name='Refusal of the Call (Adept)', hash=25228802),
        # With Runneth Over
        Item(name='Refusal of the Call', hash=2671849376),
        Item(name='Refusal of the Call (Adept)', hash=2755584425),
        ]
    rolls = [
        Roll(
            'Damage blocking',
            [haft.LowImpedanceWindings, AnyPerk],
            [magazine.AlloyMagazine, magazine.LightMag, AnyPerk],
            [trait.ReplenishingAegis],
            [trait.UnstoppableForce, trait.VorpalWeapon],
            ),
        Roll(
            'Shield energy from melee',
            [haft.LowImpedanceWindings, AnyPerk],
            [magazine.AlloyMagazine, magazine.LightMag, AnyPerk],
            [trait.ReplenishingAegis],
            [trait.MeleeMomentum],
            ),
        Roll(
            'Melee damage',
            [haft.LowImpedanceWindings, AnyPerk],
            [magazine.AlloyMagazine, magazine.LightMag, AnyPerk],
            [trait.ReplenishingAegis],
            [trait.CloseToMelee],
            ),
        ]


class MirrorImago(RollDefinition):
    """
    Strand Submachine Gun, Adaptive Frame
    https://www.light.gg/db/items/3234363830
    """
    items = [
        Item(name='Mirror Imago', hash=3234363830),
        Item(name='Mirror Imago (Adept)', hash=302039451),
        # With Runneth Over
        Item(name='Mirror Imago', hash=3877448149),
        Item(name='Mirror Imago (Adept)', hash=4116546788),
        ]


class Anamnesis(RollDefinition):
    """
    Void Combat Bow, Lightweight Frame
    https://www.light.gg/db/items/2291392465
    """
    items = [
        Item(name='Anamnesis', hash=2291392465),
        Item(name='Anamnesis (Adept)', hash=1536325168),
        # With Runneth Over
        Item(name='Anamnesis', hash=3417731926),
        Item(name='Anamnesis (Adept)', hash=3949253499),
        ]
    rolls = [
        Roll(
            'Void combo',
            [bowstring.PolymerString, AnyPerk],
            [arrow.FiberglassArrowShaft, AnyPerk],
            [trait.RepulsorBrace],
            [trait.DestabilizingRounds, trait.Demoralize],
            )
        ]


class Afterlight(RollDefinition):
    """
    Vois Fusion Rifle, Adaptive Frame
    https://www.light.gg/db/items/3228630258
    """
    items = [
        Item(name='Afterlight', hash=3228630258),
        Item(name='Afterlight (Adept)', hash=3953163559),
        # With Runneth Over
        Item(name='Afterlight', hash=1834313033),
        Item(name='Afterlight (Adept)', hash=861521336),
        ]


class Division(RollDefinition):
    """
    Arc Sidearm, Heavy Burst
    https://www.light.gg/db/items/2903168058
    """
    items = [
        Item(name='Division', hash=2903168058),
        Item(name='Division (Adept)', hash=3734001727),
        # With Runneth Over
        Item(name='Division', hash=2992463569),
        Item(name='Division (Adept)', hash=2501377328),
        ]
    roll = Roll(
        'PvE',
        [barrel.FlutedBarrel, AnyPerk],
        [magazine.FlaredMagwell, AnyPerk],
        [trait.EddyCurrent],
        [trait.Voltshot, trait.Surrounded],
        )


class FalsePromises(RollDefinition):
    """
    Stasis Auto Rifle, High-Impact Frame
    https://www.light.gg/db/items/1390080550
    """
    item = Item(name='False Promises', hash=1390080550)


class WhisperingSlab(RollDefinition):
    """
    Kinetic Combat Bow, Lightweight Frame
    https://www.light.gg/db/items/690341468
    """
    item = Item(name='Whispering Slab', hash=690341468)
    rolls = [
        Roll(
            'PvE',
            [bowstring.PolymerString, AnyPerk],
            [arrow.FiberglassArrowShaft, AnyPerk],
            [trait.ArchersTempo],
            [trait.VorpalWeapon],
            ),
        ]


class ColdDenial(RollDefinition):
    """
    Kinetic Pulse Rifle, High-Impact Frame
    https://www.light.gg/db/items/558794124
    """
    item = Item(name='Cold Denial', hash=558794124)
    rolls = [
        Roll(
            'PvP',
            [barrel.ArrowheadBrake, barrel.ExtendedBarrel],
            [magazine.RicochetRounds, AnyPerk],
            [trait.ZenMoment],
            [trait.Headseeker],
            ),
        Roll(
            'Desperado',
            [barrel.ArrowheadBrake, barrel.ExtendedBarrel],
            [magazine.RicochetRounds, AnyPerk],
            [trait.TunnelVision],
            [trait.Desperado],
            ),
        ]


class HollowWords(RollDefinition):
    """
    Arc Fusion Rifle, Precision Frame
    https://www.light.gg/db/items/342027677
    """
    item = Item(name='Hollow Words', hash=342027677)


class TemptationsHook(RollDefinition):
    """
    Arc Sword, Caster Frame
    https://www.light.gg/db/items/1587953057
    """
    item = Item(name="Temptation's Hook", hash=1587953057)
    rolls = [
        Roll(
            'PvP, ad clear',
            [blade.JaggedEdge],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.TirelessBlade],
            [trait.ChainReaction],
            ),
        Roll(
            'Damage dealing',
            [blade.JaggedEdge],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.RelentlessStrikes],
            [trait.WhirlwindBlade],
            ),
        Roll(
            'Attrition Orbs',
            [blade.JaggedEdge],
            [guard.SwordmastersGuard, AnyPerk],
            [trait.AttritionOrbs],
            [trait.WhirlwindBlade],
            ),
        ]
