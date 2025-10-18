from argparse import ArgumentParser, Namespace, RawTextHelpFormatter
from enum import StrEnum
from os.path import dirname, join
from typing import assert_never

import manifest
from manifest.core import Manifest


class ListOptions(StrEnum):
    """
    All available options for listing.
    """
    RELEASE_STRINGS = 'release-strings'


RELEASE_STRING_ALL = 'all'
RELEASE_STRING_LATEST = 'latest'
PERK_DATABASE_DIRECTORY = join(dirname(dirname(__file__)), 'database')
WEAPON_DEFINITIONS_FILE = 'new_weapons.py'
PERK_MAPPING_FILE = 'regular-to-enhanced.json'


def list_commands(args: Namespace, /) -> None:
    """
    Main function for listing commands.
    """
    manifest_ = Manifest.from_recent()
    match args.list_option:
        case ListOptions.RELEASE_STRINGS:
            print('Available release strings:')
            print(*sorted(manifest_.release_strings), sep='\n')

        case unknown:
            assert_never(unknown)


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
        return max(manifest_.release_strings)

    releases = manifest_.release_strings
    if release_string in releases: return release_string

    print(
        f'Error: invalid release string {release_string!r} for command {cmd_name!r}.\n'
        f'Release string can be {RELEASE_STRING_ALL!r}, {RELEASE_STRING_LATEST!r} '
        f'or any of the following:\n  {'\n  '.join(releases)}'
        )
    exit()


def generate_commands(args: Namespace) -> None:
    """
    Main function for generating commands.
    """
    manifest_ = Manifest.from_api()
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

    if perk_db_release:
        generate_perk_database(manifest_, perk_db_release)

    if weapons_release:
        generate_weapons_definitions(manifest_, weapons_release)

    if do_generate_mapping:
        generate_perk_mapping(manifest_)


def generate_perk_database(manifest_: Manifest, release: str, /) -> None:
    """
    Generates perk database since the given release.
    """
    name_to_perks = manifest_.get_legendary_weapon_perks(release)


def generate_weapons_definitions(manifest_: Manifest, release: str, /) -> None:
    """
    Generates weapon definitions since the given release.
    """


def generate_perk_mapping(manifest_: Manifest, /) -> None:
    """
    Generates a mapping between regular and correspondent enhanced perks.
    """


def parse_cmd_arguments() -> Namespace:
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
        '--clear-cache',
        action='store_true',
        help=f'Removes all, but the most recent cached manifest '
             f'from directory {Manifest.CACHE_DIR!r}.\n'
             f'This command is executed at the end of the script.'
        )

    subparsers = parser.add_subparsers()
    parser_list = subparsers.add_parser(
        cmd_list,
        description=f'Commands for listing some Destiny 2 data.\n\n'
                    f'All commands use the most recent manifest '
                    f'in directory {Manifest.CACHE_DIR!r}.\n'
                    f'If there is no cached manifest, '
                    f'then a command downloads one to that directory and uses it instead.',
        help='Listing commands.',
        formatter_class=RawTextHelpFormatter,
        add_help=False,
        )

    parser_list.set_defaults(function=list_commands)
    parser_list.add_argument(*help_args, **help_kwargs)
    parser_list.add_argument(
        'list-option',
        choices=tuple(ListOptions),
        help='Options for listing.'
        )

    parser_generate = subparsers.add_parser(
        'generate',
        description=f'Commands for generating.\n\n'
                    f'Some commands accept release strings.\n'
                    f'A release string is {RELEASE_STRING_ALL!r}, {RELEASE_STRING_LATEST!r} '
                    f'or ony other string listed by command {cmd_list_release_strings!r}.',
        help='Generating commands.',
        formatter_class=RawTextHelpFormatter,
        add_help=False,
        )

    parser_list.set_defaults(function=generate_commands)
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
        help=f'Generates a mapping between regular and enhanced perks '
             f'and saves it to file {PERK_MAPPING_FILE!r}.',
        )

    return parser.parse_args()


def main() -> None:
    args = parse_cmd_arguments()
    if args.function is not None:
        args.function(args)

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


if __name__ == '__main__':
    main()
