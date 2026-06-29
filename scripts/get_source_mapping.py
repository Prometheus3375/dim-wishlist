import json

from wishlist import RollDefinition
from wishlist.__main__ import define_wishlist

_ = define_wishlist()
sources = set()
hash2weapon = {}
for cls in RollDefinition.__subclasses__():
    docs = cls.__doc__.strip().splitlines()
    if len(docs) != 4:
        print(f'Class {cls.__module__}.{cls.__qualname__} has old description.')
        continue

    source_line = docs[1].strip()[7:].strip()
    sources.add(source_line)
    for item in cls.items:
        hash2weapon[str(item.hash)] = dict(name=item.name, source=source_line)

with open('source-mapping.json', 'w') as f:
    json.dump(dict(sources=sorted(sources), weapons=hash2weapon), f, ensure_ascii=False, indent=2)
    f.write('\n')
