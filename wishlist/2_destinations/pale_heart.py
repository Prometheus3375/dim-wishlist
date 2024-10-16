from database import *


class ErgoSum(RD):
    item = ErgoSum = Item(name='Ergo Sum', hash=1681583613)
    _blades = [blades.EnduringBlade, AnyPerk]
    _dmg_note = (
        'Roll for damage dealing. Blade and guard is not that important. '
        'Prefer Enduring Blade for more ammo. '
        'In any damage situation you should be transcendent '
        'which maximizes Charge Rate anyway. '
        'Aegis thoughts: https://youtu.be/bGTXGydS8uM'
    )
    rolls = [
        roll(
            _dmg_note,
            [unique.ErgoSum.ThePerfectFifth],
            [unique.ErgoSum.CasterFrame],
            _blades,
            ),
        roll(
            _dmg_note,
            [unique.ErgoSum.UnplannedReprieve],
            [unique.ErgoSum.LightweightFrame],
            _blades,
            ),
        roll(
            'Roll to activate Wolfpack Rounds on swords. '
            'Lightweight Frame has fast heavy attack which consumes only 3 ammo',
            [unique.ErgoSum.WolfpackRounds],
            [unique.ErgoSum.LightweightFrame],
            _blades,
            [guards.SwordmastersGuard, AnyPerk],
            ),
        roll(
            'Roll for ad clear',
            [unique.ErgoSum.ArcConductor],
            [
                unique.ErgoSum.LightweightFrame,
                unique.ErgoSum.WaveSwordFrame,
                unique.ErgoSum.CasterFrame,
                ],
            _blades,
            [guards.SwordmastersGuard, AnyPerk],
            ),
        # roll(
        #     'Good roll to get ability energy from sword kills',
        #     [unique.ErgoSum.GatheringLight],
        #     [unique.ErgoSum.WaveSwordFrame],
        #     _ergo_sum_blades,
        #     ),
        roll(
            'Stormbringer requires 3 kills to activate and barely makes a difference in ad clear',
            [unique.ErgoSum.Stormbringer],
            is_trash=True,
            ),
        ]


class Relativism(RD):
    item = Item(name='Relativism', hash=2809120022)
    rolls = [
        roll(
            'Combination Blow builds',
            [unique.SpiritOf.Assassin, unique.SpiritOf.Caliban],
            [unique.SpiritOf.Liar],
            ),
        roll(
            'Other melee builds; '
            'Synthoceps increase damage of Combination Blow very little',
            [unique.SpiritOf.Assassin, unique.SpiritOf.Caliban],
            [unique.SpiritOf.Synthoceps],
            ),
        roll(
            'Duskfield builds',
            [unique.SpiritOf.Renewal],
            [unique.SpiritOf.Cyrtarachne, unique.SpiritOf.StarEater],
            ),
        # roll(
        #     'Woven Mail builds',
        #     [unique.SpiritOf.InmostLight, unique.SpiritOf.Foetracer],
        #     [unique.SpiritOf.Cyrtarachne],
        #     ),
        # roll(
        #     'Dodge builds',
        #     [unique.SpiritOf.Dragon],
        #     [unique.SpiritOf.Coyote, unique.SpiritOf.Wormhusk],
        #     ),
        roll(
            'Super build',
            [unique.SpiritOf.Galanor],
            [unique.SpiritOf.StarEater],
            ),
        roll(
            'Super and weapon damage',
            [unique.SpiritOf.Foetracer],
            [unique.SpiritOf.StarEater],
            ),
        roll(
            'Ad clear and super damage',
            [unique.SpiritOf.Caliban],
            [unique.SpiritOf.StarEater],
            ),
        roll(
            'Gyrfalcon build',
            [unique.SpiritOf.InmostLight],
            [unique.SpiritOf.Gyrfalcon],
            ),
        roll(
            'PvP build',
            [unique.SpiritOf.Ophidian],
            [unique.SpiritOf.Wormhusk],
            ),
        ]


class Stoicism(RD):
    item = Item(name='Stoicism', hash=266021826)
    rolls = [
        roll(
            'Melee builds',
            [unique.SpiritOf.InmostLight, unique.SpiritOf.Assassin, unique.SpiritOf.Severance],
            [unique.SpiritOf.Synthoceps],
            ),
        roll(
            'Severance and Contact combo',
            [unique.SpiritOf.Severance],
            [unique.SpiritOf.Contact],
            ),
        roll(
            'Barricade combo',
            [unique.SpiritOf.Hoarfrost],
            [unique.SpiritOf.Horn],
            ),
        roll(
            'Unbreakable build',
            [unique.SpiritOf.Bear],
            [unique.SpiritOf.Armamentarium],
            ),
        roll(
            "Drengr's Lash build",
            [unique.SpiritOf.Abeyant],
            [unique.SpiritOf.Horn],
            ),
        roll(
            'Super and weapon damage',
            [unique.SpiritOf.EternalWarrior],
            [unique.SpiritOf.StarEater],
            ),
        roll(
            'PvP build',
            [unique.SpiritOf.Ophidian],
            [unique.SpiritOf.AlphaLupi],
            ),
        ]


class Solipsism(RD):
    item = Item(name='Solipsism', hash=2273643087)
    rolls = [
        roll(
            'Melee builds',
            [unique.SpiritOf.Necrotic, unique.SpiritOf.InmostLight, unique.SpiritOf.Assassin],
            [unique.SpiritOf.Synthoceps, unique.SpiritOf.Claw],
            ),
        # roll(
        #     'Grenade build',
        #     [unique.SpiritOf.Osmiomancy],
        #     [unique.SpiritOf.Verity],
        #     ),
        roll(
            'Empowered Rift combo',
            [unique.SpiritOf.Filaments],
            [unique.SpiritOf.Starfire],
            ),
        # roll(
        #     'Other Rift builds',
        #     [unique.SpiritOf.InmostLight, unique.SpiritOf.Stag],
        #     [unique.SpiritOf.Vesper],
        #     ),
        roll(
            'Super builds',
            [unique.SpiritOf.Apotheosis],
            [unique.SpiritOf.StarEater, unique.SpiritOf.Harmony],
            ),
        roll(
            'Song of Flame grenade build',
            [unique.SpiritOf.Apotheosis],
            [unique.SpiritOf.Verity],
            ),
        roll(
            'PvP build',
            [unique.SpiritOf.Ophidian],
            [unique.SpiritOf.Harmony],
            ),
        ]
