#!/usr/bin/env python3
"""Check Creator Terms DB structure and ensure HTML's embedded entries match database.json."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = json.loads((root / 'database.json').read_text(encoding='utf-8'))
html = (root / 'index.html').read_text(encoding='utf-8')
entries = data.get('entries')
if not isinstance(entries, list):
    raise SystemExit('ERROR: database.json entries must be an array')
if data.get('count') != len(entries):
    raise SystemExit(f"ERROR: count={data.get('count')} but entries={len(entries)}")
names = [entry.get('name') for entry in entries]
if any(not name for name in names):
    raise SystemExit('ERROR: every entry must have a name')
if len(names) != len(set(names)):
    raise SystemExit('ERROR: duplicate entry names found')
match = re.search(r'const entries = (\[.*?\]);', html, flags=re.S)
if not match:
    raise SystemExit('ERROR: could not find embedded const entries in index.html')
embedded = json.loads(match.group(1))
if embedded != entries:
    raise SystemExit('ERROR: embedded HTML entries differ from database.json')
print(f'OK: {len(entries)} entries; names unique; HTML and JSON synchronized.')
