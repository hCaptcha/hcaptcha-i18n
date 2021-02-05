"""
Compares translation_key.json to a specific language file to see
if either values are missing or superfluous keys are included.

Args: file_to_check.json
"""
import json
import sys

def NestedDictValues(d):
  for v in d.values():
    if isinstance(v, dict):
      yield from NestedDictValues(v)
    else:
      yield v

def NestedDictKeys(d):
  for k in d.keys():
    if isinstance(k, dict):
      yield from NestedDictKeys(k)
    else:
      yield k

with open('src/translation_key.json', encoding='utf-8') as fh:
    data = json.load(fh)

to_check = sys.argv[1]

with open(to_check, encoding='utf-8') as fh:
    data2 = json.load(fh)

wanted = set(list(NestedDictValues(data)))
found = set(list(NestedDictKeys(data2)))

diff = wanted.difference(found)

if diff:
    print(f"{to_check}: wanted {len(wanted)} found {len(found)}")
    print(diff)
    sys.exit(1)

