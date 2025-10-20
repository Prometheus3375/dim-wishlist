import os
from argparse import ArgumentParser, Namespace, RawTextHelpFormatter
from collections import defaultdict
from enum import StrEnum
from operator import attrgetter
from os.path import dirname, join
from typing import assert_never

import manifest
from manifest.core import (
    AmmunitionType,
    Manifest,
    PERK_TUPLE_SORT_BY_COMPLETENESS,
    PerkTuple,
    Weapon,
    )


class ListOptions(StrEnum):
    """
    All available options for listing.
    """
    RELEASE_STRINGS = 'release-strings'


PROJECT_DIR = dirname(dirname(__file__))
RELEASE_STRING_ALL = 'all'
RELEASE_STRING_LATEST = 'latest'
PERK_DATABASE_DIRECTORY = join(PROJECT_DIR, 'database')
WEAPON_DEFINITIONS_FILE = join(PROJECT_DIR, 'new-weapons.py')
PERK_MAPPING_FILE = join(PROJECT_DIR, 'regular-to-enhanced.json')


def parse_cmd_arguments() -> Namespace:
    cmd_update = '--update-cache'
    cmd_list = 'list'
    cmd_list_release_strings = f'{cmd_list} {ListOptions.RELEASE_STRINGS.value}'

    help_args = '-h', '--help'
    help_kwargs = dict(
        action='help',
        help='If specified, the script shows this help message and exits.',
        )

    parser = ArgumentParser(
        prog=f'python -m {manifest.__name__}',
        description='A script for working with Destiny 2 data.',
        formatter_class=RawTextHelpFormatter,
        add_help=False,
        )

    parser.set_defaults(function=None)
    parser.add_argument(*help_args, **help_kwargs)

    parser.add_argument(
        '-u', cmd_update,
        action='store_true',
        help=f'Downloads the most recent version of the game data '
             f'and stores it in directory {Manifest.CACHE_DIR!r}.\n'
             f'This command is executed at the very start of the script.'
        )

    parser.add_argument(
        '--clear-cache',
        action='store_true',
        help=f'Removes all, but the most recent cached manifest '
             f'from directory {Manifest.CACHE_DIR!r}.\n'
             f'This command is executed at the very end of the script.'
        )

    subparsers = parser.add_subparsers(
        title='subcommands',
        description=f'All of the subcommands use the most recent manifest '
                    f'in directory {Manifest.CACHE_DIR!r}.\n'
                    f'If there is no cached manifest, '
                    f'then a command downloads one to that directory and uses it instead.\n'
                    f'To force usage of the most recent data, '
                    f'specify flag {cmd_update!r} when running subcommands.',
        help="Run a subcommand with '--help' to learn more.",
        )
    parser_list = subparsers.add_parser(
        cmd_list,
        description=f'Commands for listing stuff using Destiny 2 data.',
        help='Subcommand for listing commands.',
        formatter_class=RawTextHelpFormatter,
        add_help=False,
        )

    parser_list.set_defaults(function=list_commands)
    parser_list.add_argument(*help_args, **help_kwargs)
    parser_list.add_argument(
        'list_option',
        choices=tuple(ListOptions),
        help='Options for listing.'
        )

    parser_generate = subparsers.add_parser(
        'generate',
        description=f'Commands for generating stuff using Destiny 2 data.\n\n'
                    f'Some commands accept release strings.\n'
                    f'A release string is {RELEASE_STRING_ALL!r}, {RELEASE_STRING_LATEST!r} '
                    f'or ony other string listed by command {cmd_list_release_strings!r}.',
        help='Subcommand for generating commands.',
        formatter_class=RawTextHelpFormatter,
        add_help=False,
        )

    parser_generate.set_defaults(function=generate_commands)
    parser_generate.add_argument(*help_args, **help_kwargs)

    perk_database_default = 'releases.v800.annual'
    parser_generate.add_argument(
        '-p', '--perk-database',
        nargs='?',
        const=perk_database_default,
        default=None,
        metavar='RELEASE_STRING',
        help=f'Generates perk database in directory {PERK_DATABASE_DIRECTORY!r} '
             f'listing perks met in weapons since the specified release.\n'
             f'Default release string is {perk_database_default!r}.',
        )

    weapon_definitions_default = 'latest'
    parser_generate.add_argument(
        '-w', '--weapon-definitions',
        nargs='?',
        const=weapon_definitions_default,
        default=None,
        metavar='RELEASE_STRING',
        help=f'Generates weapon roll definitions in file {WEAPON_DEFINITIONS_FILE!r} '
             f'listing weapons since the specified release.\n'
             f'Default release string is {weapon_definitions_default!r}.',
        )

    parser_generate.add_argument(
        '-m', '--perk-mapping',
        action='store_true',
        help=f'Generates the mapping between regular and enhanced perks '
             f'and saves it to file {PERK_MAPPING_FILE!r}.',
        )

    return parser.parse_args()


def main() -> None:
    args = parse_cmd_arguments()
    if args.update_cache:
        print('Loading the most recent game data from the API...')
        manifest_ = Manifest.from_api()
        print('Game data is loaded.')
    else:
        manifest_ = Manifest.from_recent()

    if args.function is not None:
        args.function(manifest_, args)

    if args.clear_cache:
        versions = Manifest.list_cached_versions()
        if len(versions) <= 1:
            print('Nothing to clear.')
        else:
            print('Clearing cache...')
            Manifest.clear_cache_directory()
            print(
                f'Cache cleared successfully.\n'
                f'The most recent version is {max(versions)!r}.'
                )


def list_commands(manifest_: Manifest, args: Namespace, /) -> None:
    """
    Main function for listing commands.
    """
    match args.list_option:
        case ListOptions.RELEASE_STRINGS:
            print(*sorted(manifest_.release_strings), sep='\n')

        case unknown:
            assert_never(unknown)


def generate_commands(manifest_: Manifest, args: Namespace, /) -> None:
    """
    Main function for generating commands.
    """
    perk_db_release = check_release_string(
        manifest_,
        args.perk_database,
        '--perk-database',
        )
    weapons_release = check_release_string(
        manifest_,
        args.weapon_definitions,
        '--weapon-definitions',
        )
    do_generate_mapping = args.perk_mapping

    if perk_db_release is not None:
        generate_perk_database(manifest_, perk_db_release)

    if weapons_release is not None:
        generate_weapons_definitions(manifest_, weapons_release)

    if do_generate_mapping:
        generate_perk_mapping(manifest_)


def check_release_string(
        manifest_: Manifest,
        release_string: str | None,
        cmd_name: str,
        /,
        ) -> str | None:
    """
    Verifies the given release string and return a proper value.
    If the string is invalid, then closes the program.

    If ``None`` is passed, ``None`` is returned.
    """
    if release_string is None: return None

    if release_string == RELEASE_STRING_ALL:
        return ''

    if release_string == RELEASE_STRING_LATEST:
        # Latest must cover any part of the same release
        release_string = max(manifest_.release_strings)
        parts = release_string.split('.')
        assert len(parts) >= 2, 'any release string must have at least one dot'
        return f'{parts[0]}.{parts[1]}'

    releases = manifest_.release_strings
    if release_string in releases: return release_string

    print(
        f'Error: invalid release string {release_string!r} for command {cmd_name!r}.\n'
        f'Release string can be {RELEASE_STRING_ALL!r}, {RELEASE_STRING_LATEST!r} '
        f'or any of the following:\n{'\n'.join(releases)}'
        )
    exit()


def name_to_python_identifier(name: str, /) -> str:
    """
    Converts the given name of a weapon or a perk to a proper Python identifier.
    """
    parts = name.replace("'", '').replace('-', ' ').split()
    return ''.join(f'{part[0].upper()}{part[1:]}' for part in parts)


def perk_category_to_python_identifier(category: str, /) -> str:
    """
    Converts the given category of a perk to a proper Python identifier.
    """
    category = category.lower().replace(' ', '_')

    match category:
        case 'origin_trait':
            category = 'origin'

    return category


def generate_perk_database(manifest_: Manifest, release: str, /) -> None:
    """
    Generates perk database since the given release.
    """
    print(f'Generating perk database listing perks met in weapons since {release!r}...')

    from classes import Perk

    os.makedirs(PERK_DATABASE_DIRECTORY, exist_ok=True)

    name_to_perks = manifest_.get_legendary_weapon_perks(release)
    category_to_perks: dict[str, list[PerkTuple]] = defaultdict(list)
    for perk_set in name_to_perks.values():
        perk = min(perk_set, key=PERK_TUPLE_SORT_BY_COMPLETENESS)
        category = perk_category_to_python_identifier(perk.category)
        category_to_perks[category].append(perk)

    for category, perk_list in category_to_perks.items():
        filepath = join(PERK_DATABASE_DIRECTORY, f'{category}.py')
        with open(filepath, 'w') as f:
            f.write(f'from {Perk.__module__} import {Perk.__name__}\n\n')

            perk_list.sort()
            for perk in perk_list:
                variable = name_to_python_identifier(perk.name)
                if perk.enhanced > 0:
                    hashes = f'regular={perk.regular}, enhanced={perk.enhanced}'
                else:
                    hashes = f'regular={perk.regular}'

                f.write(f'{variable} = {Perk.__name__}({perk.name!r}, {hashes})\n')

            f.write(f'\ndel {Perk.__name__}\n')

    modules = [
        name[:-3]
        for name in os.listdir(PERK_DATABASE_DIRECTORY)
        if name.endswith('.py') and not name.startswith('_')
        ]
    filepath = join(PERK_DATABASE_DIRECTORY, '__init__.py')
    with open(filepath, 'w') as f:
        f.write('__all__ = (\n')
        for name in modules:
            f.write(f'    {name!r},\n')

        f.write('    )\n')

    print(f'Generating perk database is complete.')


_sort_key_for_weapon = attrgetter('source')


def _sort_key_for_weapon_list(li: list[Weapon], /) -> tuple:
    w = li[0]
    return w.source, w.ammo_type, w.name


def get_weapon_type(w: Weapon, /) -> str:
    """
    Return a proper name of the weapon type.
    """
    match w.weapon_type:
        case 'Grenade Launcher' if w.ammo_type is AmmunitionType.Special:
            return 'Breechloaded Grenade Launcher'

        case 'Grenade Launcher' if w.ammo_type is AmmunitionType.Heavy:
            return 'Drum Grenade Launcher'

        case 'Combat Bow' if w.ammo_type is AmmunitionType.Heavy:
            return 'Crossbow'

        case other:
            return other


WEAPON_DEFINITION_CODE = """

class {identifier}({base_class}):
    \"""
    {damage_type} {weapon_type}, {intrinsic}
    {source}
    https://www.light.gg/db/items/{hash}
    \"""
"""


def generate_weapons_definitions(manifest_: Manifest, release: str, /) -> None:
    """
    Generates weapon definitions since the given release.
    """
    print(f'Generating weapon definitions for weapons since {release!r}...')

    import wishlist
    from classes import Item, RollDefinition

    name2weapons: dict[str, list[Weapon]] = defaultdict(list)
    for weapon in manifest_.iterate_legendary_weapons_since_release(release):
        name2weapons[weapon.name].append(weapon)

    for li in name2weapons.values():
        # Place the weapon with source at start.
        li.sort(key=_sort_key_for_weapon, reverse=True)

    # Sort weapon lists by the source.
    weapon_lists = sorted(name2weapons.values(), key=_sort_key_for_weapon_list)
    with open(WEAPON_DEFINITIONS_FILE, 'w') as f:
        f.write(f'from {wishlist.__name__} import *\n')

        for li in weapon_lists:
            main_weapon = li[0]
            format_params = dict(
                identifier=name_to_python_identifier(main_weapon.name),
                base_class=RollDefinition.__name__,
                damage_type='-'.join(main_weapon.damage_types),
                weapon_type=get_weapon_type(main_weapon),
                intrinsic=', '.join(main_weapon.intrinsics),
                source=main_weapon.source,
                hash=main_weapon.hash,
                )
            f.write(WEAPON_DEFINITION_CODE.format_map(format_params))
            if len(li) == 1:
                f.write(
                    f'    item = {Item.__name__}'
                    f'({main_weapon.name!r}, hash={main_weapon.hash})\n'
                    )

            else:
                f.write(f'    items = [\n')
                for w in li:
                    f.write(f'        {Item.__name__}({w.name!r}, hash={w.hash}),\n')

                f.write('        ]\n')

    print(f'Generating weapon definitions is complete.')


def generate_perk_mapping(manifest_: Manifest, /) -> None:
    """
    Generates a mapping between regular and correspondent enhanced perks.
    """
    print('Generating the mapping between regular and enhanced perks...')

    import json

    with open(PERK_MAPPING_FILE, 'w') as f:
        mapping = {
            # Convert key to string, so it is sorted by json as string, not number
            str(perk.regular): perk.enhanced
            for tuple_set in manifest_.get_legendary_weapon_perks().values()
            for perk in tuple_set
            if perk.is_complete
            }

        data = dict(version=manifest_.version, mapping=mapping)
        json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write('\n')

    print(f'Generating the mapping is complete.')


if __name__ == '__main__':
    main()
