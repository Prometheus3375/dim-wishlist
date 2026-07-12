import json

from wishlist import RollDefinition
from wishlist.__main__ import define_wishlist

_ = define_wishlist()
found_sources = set()
hash2weapon = {}
for cls in RollDefinition.__subclasses__():
    docs = cls.__doc__.strip().splitlines()
    if len(docs) < 4:
        print(f'Class {cls.__module__}.{cls.__qualname__} has old description.')
        continue

    source_line = docs[1].strip()[7:]
    sources = [s.strip() for s in source_line.split(';')]
    found_sources.update(sources)
    for item in cls.items:
        hash2weapon[item.hash] = dict(name=item.name, sources=sources)

with open('source-mapping.json', 'w') as f:
    json.dump(
        dict(sources=sorted(found_sources), weapons=hash2weapon),
        f,
        ensure_ascii=False,
        indent=2,
        sort_keys=True,
        )
    f.write('\n')
