"""Verify the case reading paths and the publication's single-palette contract."""
from pathlib import Path
import json,re,hashlib,subprocess
R=Path(__file__).resolve().parents[1];M=json.loads((R/'assets/case-studies.json').read_text());D=json.loads((R/'assets/research-data.json').read_text())
assert len(M['cases'])==8 and len(M['groups'])==4
assert len({x['id'] for x in M['cases']})==8
assert {c['id'] for c in M['cases']}=={j['slug'] for j in D['jurisdictions'] if j['depth']!='Reference file'}
source_ids={s['id'] for s in D['sources']};groups={g['id'] for g in M['groups']};owners={}
for c in M['cases']:
 assert c['group'] in groups and set(c['sources'])<=source_ids
 overview=(R/'case-studies'/c['id']/'index.html').read_text()
 for section in ['question','story','established','limit','unresolved','chapters','source-records']:
  assert 'id="'+section+'"' in overview,(c['id'],section)
 for n,chapter in enumerate(c['sequence']):
  assert chapter['path'] not in owners,'A chapter must have an unambiguous primary path'
  owners[chapter['path']]=c['id']
  text=(R/chapter['path']/'index.html').read_text()
  assert text.count('class="case-context"')==1
  assert text.count('class="chapter-continue"')==1
  assert f'CHAPTER {n+1} OF {len(c["sequence"])}' in text
  assert f'case-studies/{c["id"]}/' in text
  if n+1<len(c['sequence']):assert c['sequence'][n+1]['path'] in text
for p in R.rglob('*.html'):
 text=p.read_text();assert 'data-theme="light"' in text,p
 assert 'assets/theme.js' not in text,p
 assert not re.search(r'<button[^>]*\bdata-theme\b',text),p
 if 'data-base=' not in text:continue
 for asset in ['site.css','site.js','search-data.js']:
  digest=hashlib.sha256((R/'assets'/asset).read_bytes()).hexdigest()[:12]
  assert f'assets/{asset}?v={digest}' in text,(p,asset)
css=(R/'assets/site.css').read_text();assert 'prefers-color-scheme' not in css and '[data-theme=dark]' not in css
assert not (R/'assets/theme.js').exists()
print(f'Case structure: 4 groups, 8 cases, {len(owners)} connected chapters. Single light palette and asset versions: pass.')
