from database import *


class Adamantite(RD):
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
            [barrels.FullBore, barrels.HammerForgedRifling, barrels.Smallbore,
             barrels.CorkscrewRifling, AnyPerk],
            [magazines.FlaredMagwell, magazines.AlloyMagazine, magazines.TacticalMag, AnyPerk],
            [traits.Reciprocity],
            [traits.Hatchling, traits.AttritionOrbs],
            ),
        ]


class Psychopomp(RD):
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
            [barrels.QuickLaunch, AnyPerk],
            [magazines.HighVelocityRounds],
            [traits.AmbitiousAssassin],
            [traits.Unrelenting],
            ),
        Roll(
            'Damage rotations combo',
            [barrels.Countermass, AnyPerk],
            [magazines.HighVelocityRounds],
            [traits.EnviousArsenal],
            [traits.FullCourt, traits.Frenzy],
            ),
        Roll(
            'Melee regen',
            [barrels.QuickLaunch, AnyPerk],
            [magazines.HighVelocityRounds],
            [traits.Pugilist],
            [traits.RollingStorm],
            ),
        ]


class EyesUnveiled(RD):
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


class WatchfulEye(RD):
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
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.AppendedMag, AnyPerk],
            [traits.Overflow],
            [traits.KillingTally, traits.JoltingFeedback],
            ),
        Roll(
            'Arc combo',
            [barrels.ArrowheadBrake, AnyPerk],
            [magazines.FlaredMagwell, AnyPerk],
            [traits.EddyCurrent],
            [traits.JoltingFeedback],
            ),
        ]


class AbyssalEdge(RD):
    """
    Strand Sword, Wave Sword Frame
    https://www.light.gg/db/items/547165496
    """
    items = [
        Item(name='Psychopomp', hash=547165496),
        Item(name='Psychopomp (Adept)', hash=2712683313),
        # With Runneth Over
        Item(name='Psychopomp', hash=4221591387),
        Item(name='Psychopomp (Adept)', hash=3054597646),
        ]
    roll = Roll(
        'Damage dealing',
        [blades.JaggedEdge],
        [guards.SwordmastersGuard, AnyPerk],
        [traits.RelentlessStrikes],
        [traits.Surrounded],
        )


class RefusalOfTheCall(RD):
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
            [hafts.LowImpedanceWindings, AnyPerk],
            [magazines.AlloyMagazine, magazines.LightMag, AnyPerk],
            [traits.ReplenishingAegis],
            [traits.UnstoppableForce, traits.VorpalWeapon],
            ),
        Roll(
            'Shield energy from melee',
            [hafts.LowImpedanceWindings, AnyPerk],
            [magazines.AlloyMagazine, magazines.LightMag, AnyPerk],
            [traits.ReplenishingAegis],
            [traits.MeleeMomentum],
            ),
        Roll(
            'Melee damage',
            [hafts.LowImpedanceWindings, AnyPerk],
            [magazines.AlloyMagazine, magazines.LightMag, AnyPerk],
            [traits.ReplenishingAegis],
            [traits.CloseToMelee],
            ),
        ]


class MirrorImago(RD):
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


class Anamnesis(RD):
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
            [strings.PolymerString, AnyPerk],
            [arrows.FiberglassArrowShaft, AnyPerk],
            [traits.RepulsorBrace],
            [traits.DestabilizingRounds, traits.Demoralize],
            )
        ]


class Afterlight(RD):
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


class Division(RD):
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
        [barrels.FlutedBarrel, AnyPerk],
        [magazines.FlaredMagwell, AnyPerk],
        [traits.EddyCurrent],
        [traits.Voltshot, traits.Surrounded],
        )


class FalsePromises(RD):
    """
    Stasis Auto Rifle, High-Impact Frame
    https://www.light.gg/db/items/1390080550
    """
    item = Item(name='False Promises', hash=1390080550)


class WhisperingSlab(RD):
    """
    Kinetic Combat Bow, Lightweight Frame
    https://www.light.gg/db/items/690341468
    """
    item = Item(name='Whispering Slab', hash=690341468)
    rolls = [
        Roll(
            'PvE',
            [strings.PolymerString, AnyPerk],
            [arrows.FiberglassArrowShaft, AnyPerk],
            [traits.ArchersTempo],
            [traits.VorpalWeapon],
            ),
        ]


class ColdDenial(RD):
    """
    Kinetic Pulse Rifle, High-Impact Frame
    https://www.light.gg/db/items/558794124
    """
    item = Item(name='Cold Denial', hash=558794124)
    rolls = [
        Roll(
            'PvP',
            [barrels.ArrowheadBrake, barrels.ExtendedBarrel],
            [magazines.RicochetRounds, AnyPerk],
            [traits.ZenMoment],
            [traits.Headseeker],
            ),
        Roll(
            'Desperado',
            [barrels.ArrowheadBrake, barrels.ExtendedBarrel],
            [magazines.RicochetRounds, AnyPerk],
            [traits.TunnelVision],
            [traits.Desperado],
            ),
        ]


class HollowWords(RD):
    """
    Arc Fusion Rifle, Precision Frame
    https://www.light.gg/db/items/342027677
    """
    item = Item(name='Hollow Words', hash=342027677)


class TemptationsHook(RD):
    """
    Arc Sword, Caster Frame
    https://www.light.gg/db/items/1587953057
    """
    item = Item(name="Temptation's Hook", hash=1587953057)
    rolls = [
        Roll(
            'PvP, ad clear',
            [blades.JaggedEdge],
            [guards.SwordmastersGuard, AnyPerk],
            [traits.TirelessBlade],
            [traits.ChainReaction],
            ),
        Roll(
            'Damage dealing',
            [blades.JaggedEdge],
            [guards.SwordmastersGuard, AnyPerk],
            [traits.RelentlessStrikes],
            [traits.WhirlwindBlade],
            ),
        Roll(
            'Attrition Orbs',
            [blades.JaggedEdge],
            [guards.SwordmastersGuard, AnyPerk],
            [traits.AttritionOrbs],
            [traits.WhirlwindBlade],
            ),
        ]
