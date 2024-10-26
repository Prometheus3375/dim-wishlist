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


_note_spirit_of_the_star_eater = """
Roll with Star-Eater
Feast of Light stacks are preserved when swapping from
one class item w/ Spirit of Star-Eater to another
"""


class Relativism(RD):
    item = Item(name='Relativism', hash=2809120022)
    rolls = [
        roll(
            _note_spirit_of_the_star_eater,
            [unique.SpiritOf.InmostLight, unique.SpiritOf.Renewal, unique.SpiritOf.Caliban,
             unique.SpiritOf.Foetracer, unique.SpiritOf.Galanor],
            [unique.SpiritOf.StarEater],
            ),
        roll(
            """
            Roll for melee builds.
            Melee builds should be paired with Stylish Executioner aspect
            as it increases melee damage dealt from invisibility.
            It also provides invisibility, making Spirit of the Assassin redundant.
            Note: Spirit of Synthoceps has reduced damage increase for Combination Blow
            """,
            [unique.SpiritOf.Caliban, unique.SpiritOf.Renewal],
            [unique.SpiritOf.Liar, unique.SpiritOf.Synthoceps],
            ),
        roll(
            'Roll with Cyrtarachne',
            [unique.SpiritOf.InmostLight, unique.SpiritOf.Renewal, unique.SpiritOf.Foetracer],
            [unique.SpiritOf.Cyrtarachne],
            ),
        roll(
            'Roll with Gyrfalcon',
            [unique.SpiritOf.InmostLight],
            [unique.SpiritOf.Gyrfalcon],
            ),
        roll(
            'Roll for PvP',
            [unique.SpiritOf.Ophidian],
            [unique.SpiritOf.Wormhusk],
            ),
        ]


class Stoicism(RD):
    item = Item(name='Stoicism', hash=266021826)
    rolls = [
        roll(
            _note_spirit_of_the_star_eater,
            [unique.SpiritOf.InmostLight, unique.SpiritOf.Bear, unique.SpiritOf.EternalWarrior],
            [unique.SpiritOf.StarEater],
            ),
        roll(
            'Roll for grenade builds',
            [unique.SpiritOf.InmostLight],
            [unique.SpiritOf.Verity, unique.SpiritOf.Armamentarium],
            ),
        roll(
            'Roll for melee builds',
            [unique.SpiritOf.InmostLight, unique.SpiritOf.Severance],
            [unique.SpiritOf.Synthoceps, unique.SpiritOf.Contact],
            ),
        roll(
            'Roll for class ability builds',
            [unique.SpiritOf.Hoarfrost],
            [unique.SpiritOf.Horn],
            ),
        roll(
            'Roll for Unbreakable aspect',
            [unique.SpiritOf.Bear],
            [unique.SpiritOf.Armamentarium],
            ),
        roll(
            "Roll for Drengr's Lash aspect",
            [unique.SpiritOf.Abeyant],
            [unique.SpiritOf.Horn],
            ),
        roll(
            'Roll for PvP',
            [unique.SpiritOf.Ophidian],
            [unique.SpiritOf.AlphaLupi],
            ),
        ]


class Solipsism(RD):
    item = Item(name='Solipsism', hash=2273643087)
    rolls = [
        roll(
            _note_spirit_of_the_star_eater,
            [unique.SpiritOf.InmostLight, unique.SpiritOf.Apotheosis, unique.SpiritOf.Necrotic],
            [unique.SpiritOf.StarEater],
            ),
        roll(
            'Roll for grenade builds',
            [unique.SpiritOf.InmostLight, unique.SpiritOf.Apotheosis, unique.SpiritOf.Osmiomancy],
            [unique.SpiritOf.Verity],
            ),
        roll(
            'Roll for melee builds',
            [unique.SpiritOf.InmostLight, unique.SpiritOf.Necrotic],
            [unique.SpiritOf.Synthoceps, unique.SpiritOf.Claw],
            ),
        roll(
            'Roll for Empowered Rift',
            [unique.SpiritOf.Filaments, unique.SpiritOf.Osmiomancy],
            [unique.SpiritOf.Starfire],
            ),
        # roll(
        #     'Other Rift builds',
        #     [unique.SpiritOf.InmostLight, unique.SpiritOf.Stag],
        #     [unique.SpiritOf.Vesper],
        #     ),
        roll(
            'Roll for PvP',
            [unique.SpiritOf.Ophidian],
            [unique.SpiritOf.Harmony],
            ),
        ]
