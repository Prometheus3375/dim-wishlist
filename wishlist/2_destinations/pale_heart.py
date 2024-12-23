from database import *


class ErgoSum(RD):
    """
    Exotic Sword on Special Ammo
    https://www.light.gg/db/items/1681583613
    """
    item = ErgoSum = Item(name='Ergo Sum', hash=1681583613)
    _blades = [blades.EnduringBlade, AnyPerk]
    _dmg_note = """
        Damage dealing. Blade and guard is not that important.
        Prefer Enduring Blade for more ammo.
        In any damage situation you should be transcendent
        which maximizes Charge Rate anyway.
        Aegis thoughts: https://youtu.be/bGTXGydS8uM
        """

    rolls = [
        Roll(
            _dmg_note,
            [unique.ErgoSum.ThePerfectFifth],
            [unique.ErgoSum.CasterFrame],
            _blades,
            ),
        Roll(
            _dmg_note,
            [unique.ErgoSum.UnplannedReprieve],
            [unique.ErgoSum.LightweightFrame],
            _blades,
            ),
        Roll(
            """
            Lightweight Frame has fast heavy attack which consumes only 3 ammo,
            good for Wolfpack Rounds
            """,
            [unique.ErgoSum.WolfpackRounds],
            [unique.ErgoSum.LightweightFrame],
            _blades,
            [guards.SwordmastersGuard, AnyPerk],
            ),
        Roll(
            'Ad clear',
            [unique.ErgoSum.ArcConductor],
            [
                unique.ErgoSum.WaveSwordFrame,
                unique.ErgoSum.LightweightFrame,
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
        Roll(
            'Stormbringer requires 3 kills to activate and barely makes a difference in ad clear',
            [unique.ErgoSum.Stormbringer],
            is_trash=True,
            ),
        ]


_note_spirit_of_the_star_eater = """
    Star-Eater.
    Feast of Light stacks are preserved when swapping from
    one class item w/ Spirit of Star-Eater to another
    """


class Relativism(RD):
    """
    Hunter Exotic Class Item
    https://www.light.gg/db/items/2809120022
    """
    item = Item(name='Relativism', hash=2809120022)
    rolls = [
        Roll(
            _note_spirit_of_the_star_eater,
            [unique.SpiritOf.InmostLight, unique.SpiritOf.Renewal, unique.SpiritOf.Caliban,
             unique.SpiritOf.Foetracer, unique.SpiritOf.Galanor],
            [unique.SpiritOf.StarEater],
            ),
        Roll(
            """
            Melee builds.
            Should be paired with Stylish Executioner aspect
            as it increases melee damage dealt from invisibility.
            It also provides invisibility, making Spirit of the Assassin redundant.
            Note: Spirit of Synthoceps has reduced damage increase for Combination Blow
            """,
            [unique.SpiritOf.Caliban, unique.SpiritOf.Renewal],
            [unique.SpiritOf.Liar, unique.SpiritOf.Synthoceps],
            ),
        Roll(
            'Class ability builds',
            [unique.SpiritOf.InmostLight],
            [unique.SpiritOf.Coyote],
            ),
        Roll(
            'Cyrtarachne',
            [unique.SpiritOf.InmostLight, unique.SpiritOf.Renewal, unique.SpiritOf.Foetracer],
            [unique.SpiritOf.Cyrtarachne],
            ),
        Roll(
            'Gyrfalcon',
            [unique.SpiritOf.InmostLight],
            [unique.SpiritOf.Gyrfalcon],
            ),
        Roll(
            'PvP',
            [unique.SpiritOf.Ophidian],
            [unique.SpiritOf.Wormhusk],
            ),
        ]


class Stoicism(RD):
    """
    Titan Exotic Class Item
    https://www.light.gg/db/items/266021826
    """
    item = Item(name='Stoicism', hash=266021826)
    rolls = [
        Roll(
            _note_spirit_of_the_star_eater,
            [unique.SpiritOf.InmostLight, unique.SpiritOf.Bear, unique.SpiritOf.EternalWarrior],
            [unique.SpiritOf.StarEater],
            ),
        Roll(
            'Grenade builds',
            [unique.SpiritOf.InmostLight],
            [unique.SpiritOf.Verity, unique.SpiritOf.Armamentarium],
            ),
        Roll(
            'Melee builds',
            [unique.SpiritOf.InmostLight, unique.SpiritOf.Severance],
            [unique.SpiritOf.Synthoceps, unique.SpiritOf.Contact],
            ),
        Roll(
            'Class ability builds',
            [unique.SpiritOf.Hoarfrost],
            [unique.SpiritOf.Horn],
            ),
        Roll(
            'Unbreakable aspect',
            [unique.SpiritOf.Bear],
            [unique.SpiritOf.Armamentarium],
            ),
        Roll(
            "Drengr's Lash aspect",
            [unique.SpiritOf.Abeyant],
            [unique.SpiritOf.Horn],
            ),
        Roll(
            'PvP',
            [unique.SpiritOf.Ophidian],
            [unique.SpiritOf.AlphaLupi],
            ),
        ]


class Solipsism(RD):
    """
    Warlock Exotic Class Item
    https://www.light.gg/db/items/2273643087
    """
    item = Item(name='Solipsism', hash=2273643087)
    rolls = [
        Roll(
            _note_spirit_of_the_star_eater,
            [unique.SpiritOf.InmostLight, unique.SpiritOf.Apotheosis, unique.SpiritOf.Necrotic],
            [unique.SpiritOf.StarEater],
            ),
        Roll(
            'Grenade builds',
            [unique.SpiritOf.InmostLight, unique.SpiritOf.Apotheosis, unique.SpiritOf.Osmiomancy],
            [unique.SpiritOf.Verity],
            ),
        Roll(
            'Melee builds',
            [unique.SpiritOf.InmostLight, unique.SpiritOf.Necrotic],
            [unique.SpiritOf.Synthoceps, unique.SpiritOf.Claw],
            ),
        Roll(
            'Empowered Rift builds',
            [unique.SpiritOf.Filaments, unique.SpiritOf.Osmiomancy],
            [unique.SpiritOf.Starfire],
            ),
        # roll(
        #     'Other Rift builds',
        #     [unique.SpiritOf.InmostLight, unique.SpiritOf.Stag],
        #     [unique.SpiritOf.Vesper],
        #     ),
        Roll(
            'PvP',
            [unique.SpiritOf.Ophidian],
            [unique.SpiritOf.Harmony],
            ),
        ]
