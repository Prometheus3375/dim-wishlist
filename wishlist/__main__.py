import os
from importlib import import_module

from classes import RollDefinition, Wishlist

__all__ = 'define_wishlist',


def define_wishlist() -> Wishlist:
    this_dir = os.path.dirname(__file__)
    this_package = os.path.basename(this_dir)
    for dirpath, dirnames, filenames in os.walk(this_dir):
        module_path = os.path.relpath(dirpath, this_dir).replace(os.sep, '.')
        for file in filenames:
            if file.endswith('.py') and not file.startswith('_'):
                import_module(f'{this_package}.{module_path}.{file[:-3]}')

    wishlist = Wishlist(
        title='Wishlist made by Prometheus3375',
        description='Rolls on weapons and armor Prometheus3375 would like to have',
        )

    for cls in RollDefinition.__subclasses__():
        for item in cls.items:
            wishlist.add_many(item, *cls.rolls)

    return wishlist


if __name__ == '__main__':
    define_wishlist().to_dim_wishlist_file('wishlist.txt')
