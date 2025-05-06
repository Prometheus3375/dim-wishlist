import os
from importlib import import_module

from classes import RollDefinition, Wishlist

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

if __name__ == '__main__':
    wishlist.to_dim_wishlist_file('wishlist.txt')
