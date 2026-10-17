from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,collections,csv
R=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self,t):
  super().__init__();self.links=[];self.ids=[];self.titles=0;self.feed(t)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='title':self.titles+=1
  for k in ['href','src']:
   if a.get(k):self.links.append(a[k])
errors=[];pages={p:Page(p.read_text()) for p in R.rglob('*.html')}
for p,v in pages.items():
 if v.titles!=1:errors.append(f'{p}: title count {v.titles}')
 dup=[x for x,n in collections.Counter(v.ids).items() if n>1]
 if dup:errors.append(f'{p}: duplicate IDs {dup}')
 for link in v.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  if u.path.startswith('/the-sir-files/'):
   u=u._replace(path=u.path[len('/the-sir-files/'):]);target=(R/unquote(u.path)).resolve()
  else:target=(p.parent/unquote(u.path)).resolve() if u.path else p
  if target.is_dir():target=target/'index.html'
  if not target.is_file():errors.append(f'{p.relative_to(R)} missing {link}');continue
  if u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:errors.append(f'{p.relative_to(R)} missing fragment {link}')
d=json.loads((R/'assets/research-data.json').read_text());ids=[s['id'] for s in d['sources']]
assert len(ids)==len(set(ids))
assert len(d['jurisdictions'])==36
for j in d['jurisdictions']:
 for source in j['sources']:
  if source not in ids:errors.append(f'Unknown source {source}')
for c in d['claims']:
 if c['source_id'] not in ids:errors.append(f'Unknown claim source {c}')
g=d['goa'];assert g['draft']+g['accepted']-g['form_deletions']-g['eligibility_deletions']==g['final']
assert sum(g['non_returns'].values())==g['pre']-g['draft']
assert sum(g['logical_flags'].values())==58923
assert g['pre']-g['final']==127468
assert len(list(csv.DictReader((R/'assets/claims.csv').open())))==len(d['claims'])
st=d['revision_stages']
groups=[set(st[k]) for k in ['ssr_scheduled','ssr_deferred','sir_not_started_as_stated_in_order']]
assert [len(g) for g in groups]==[17,16,3]
assert set.union(*groups)=={j['slug'] for j in d['jurisdictions']}
assert not (groups[0]&groups[1] or groups[0]&groups[2] or groups[1]&groups[2])
a=d['maharashtra_applications']
assert a['form_6']+a['form_7']+a['form_8']==a['total']==1138055
assert a['outcomes_observed'] is False
assert len({c['id'] for c in d['claims']})==len(d['claims'])
for j in d['jurisdictions']:
 assert j['revision_stage_source'] in ids
u=d['uttarakhand']
assert len(u['districts'])==13
for row in u['districts']:
 assert row['draft']+row['accepted_claims']-row['admitted_objections']==row['final']
for field in ['draft','accepted_claims','admitted_objections','final']:
 assert sum(row[field] for row in u['districts'])==u[field]
assert u['pre']-u['final']==801813
assert len(d['jurisdiction_audit'])==36
assert all(not x['local_individual_legality_audit_completed'] for x in d['jurisdiction_audit'])
assert len(d['gap_register'])==14
assert next(x for x in d['sources'] if x['id']=='RPA-1950')['audit_disposition']=='qualified'
assert next(x for x in d['sources'] if x['id']=='DELHI-SCHEDULE-CANDIDATE')['type']=='Source pending verification'
for j in d['jurisdictions']:
 text=(R/'state-files'/j['slug']/'index.html').read_text()
 if j['slug']!='tripura':assert j['deck'].replace('&','&amp;').replace('"','&quot;') in text
 else:assert '21 October to 20 November' in text
 assert 'No independent' not in text or 'audit' in text
for c in d['claims']:
 assert 'id="'+c['id']+'"' in (R/'claims/index.html').read_text()
for g in d['gap_register']:
 assert 'id="'+g['id']+'"' in (R/'investigations/index.html').read_text()
assert '7,158,949' in (R/'state-files/uttarakhand/index.html').read_text()
# Correction history remains in the dataset; public pages show the corrected SIR facts.
assert len(d['editorial_corrections'])==7
assert any('21 October–20 November' in c['correction'] for c in d['editorial_corrections'])
print(json.dumps({'html_pages':len(pages),'jurisdictions':36,'sources':len(ids),'claims':len(d['claims']),'internal_link_and_fragment_errors':errors,'goa_arithmetic':'pass'},indent=2))
raise SystemExit(bool(errors))
