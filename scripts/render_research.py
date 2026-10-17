"""Render data-backed research sections. Run after editing research-data.json."""
from pathlib import Path
import json,html,re,datetime,csv
R=Path(__file__).resolve().parents[1];D=json.loads((R/'assets/research-data.json').read_text());B={s['id']:s for s in D['sources']};E=html.escape

def replace_main(path,main,title=None,description=None):
 t=path.read_text();a=t.index('<main ');b=t.index('</main>',a)+len('</main>');t=t[:a]+main+t[b:]
 if title:t=re.sub(r'<title>.*?</title>',f'<title>{E(title)} | The SIR Files</title>',t)
 if description:t=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{E(description,quote=True)}">',t)
 path.write_text(t)
def new_page(slug,title,deck,body):
 p=R/slug/'index.html';p.parent.mkdir(exist_ok=True)
 if not p.exists():p.write_text((R/'research/index.html').read_text())
 replace_main(p,f'<main id="main" class="container"><div class="article-top"><span class="eyebrow">FULL RESEARCH AUDIT / 17 OCT 2026</span><h1 class="h1">{title}</h1><p class="lede">{deck}</p></div><article class="prose research-prose">{body}</article></main>',title,deck)
def cite(id,base='../',label=None):return f'<a class="citation" href="{base}evidence/#{id}">{E(label or id)}</a>'
def source_item(s,base='../'):
 u=s.get('preferred_url',s['url']);return f'<a class="source-item" href="{E(u,quote=True)}" target="_blank" rel="noopener noreferrer"><span class="source-id">{E(s["id"])}</span><div><h3>{E(s["title"])}</h3><p>{E(s["note"])}</p><small>{E(s["review_status"])}</small></div><span class="open">Source ↗</span></a>'
def table(headers,rows):return '<div class="table-wrap"><table><thead><tr>'+''.join('<th>'+E(v)+'</th>' for v in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+str(v)+'</td>' for v in row)+'</tr>' for row in rows)+'</tbody></table></div>'
# Regenerate all 36 state articles from the authoritative dataset.
for j in D['jurisdictions']:
 base='../../';sid=j['slug'];body='<div class="article-top"><span class="eyebrow">STATE FILE / '+E(j['depth'].upper())+'</span><h1 class="h1">'+E(j['name'])+'</h1><p class="lede">'+E(j['deck'])+'</p></div>'
 body+='<div class="briefing-strip">'+''.join('<div class="briefing"><span>'+E(label)+'</span><strong>'+E(value)+'</strong></div>' for value,label in j['facts'])+'</div>' if j['facts'] else ''
 body+='<div class="article-columns"><article class="prose"><p>'+E(j['lead'])+'</p><h2 id="scope">What is established here</h2><p>'+E(j['revision_stage'])+' in the 15 October order. '+cite('ECI-SSR-OCT15',base)+'</p><p>Historical reference: '+E(j['baseline'])+'. '+cite('ECI-2026-05',base)+'</p>'
 if j['draft']:body+=table(['Original May target','Date'],[['Draft',E(j['draft'])],['Final',E(j['final'])]])+'<p class="small">Historical targets. This table is not a current timetable.</p>'
 if sid=='maharashtra':body+='<p>The signed extension is inspected. Actual Gazette publication remains open. <a href="../../maharashtra-primary-records/">Read the primary-record follow-up.</a></p>'
 if sid=='tripura':body+='<p>Later reported targets do not replace authentication of the signed instrument. '+cite('TRIPURA-REVISED-AIR',base)+'</p>'
 for n,(heading,text) in enumerate(j['story'],1):body+=f'<h2 id="section{n}">{E(heading)}</h2><p>{E(text)}</p>'
 if sid=='uttarakhand':
  u=D['uttarakhand'];body+='<h2 id="reconciliation">District reconciliation</h2><p>The official annexure reports admitted claims and objections. They are not a person-level count of wrongful exclusions or restorations. '+cite('UK-FINAL-OCT03',base)+'</p>'
  body+=table(['District','Draft','Claims admitted','Objections admitted','Final'],[[E(v['district'])]+[f'{v[k]:,}' for k in ['draft','accepted_claims','admitted_objections','final']] for v in u['districts']])
  body+='<p>Every row reconciles as draft + claims − objections = final. State totals: 7,133,785 + 129,872 − 104,708 = 7,158,949. <a href="../../assets/uttarakhand-districts.csv" download>Download district CSV.</a></p><p>The pre-SIR to final decrease is a net stock change. It is not a count of unlawful removals. The report’s addition categories also include transfer-related forms.</p>'
 if sid=='goa':
  g=D['goa'];body+='<h2 id="reconciliation">Draft-to-final reconciliation</h2>'+table(['Movement','Entries'],[['Draft',f'{g["draft"]:,}'],['Accepted additions',f'+{g["accepted"]:,}'],['Form-based removals',f'−{g["form_deletions"]:,}'],['Eligibility determinations',f'−{g["eligibility_deletions"]:,}'],['Final',f'{g["final"]:,}']])+'<p>Accounting checks do not independently establish correct eligibility decisions. '+cite('GOA-FINAL',base)+'</p>'
 body+='<h2 id="gaps">Evidence still needed</h2><ul>'+''.join('<li>'+E(q)+'</li>' for q in j['questions'])+'</ul><div class="insight">This publication has completed no independent person-level legality audit in this jurisdiction. A developed article or reference file is not a completed forensic investigation.</div><h2 id="sources">Sources and qualifications</h2>'+''.join(source_item(B[x],base) for x in dict.fromkeys(j['sources']))+'</article><aside class="sticky-aside"><h4>REVIEW STATUS</h4><small>Reviewed 17 October 2026<br>'+E(j['depth'])+'<br>Original schedule and later observations are separate.</small><a href="#scope">Established scope</a><a href="#gaps">Remaining gaps</a><a href="#sources">Sources</a><a href="../../audit/">Full audit and coverage matrix</a></aside></div>'
 replace_main(R/'state-files'/sid/'index.html','<main id="main" class="container">'+body+'</main>',j['name']+' file',j['deck'])
# Source ledger, searchable over current qualifications.
body='<div class="article-top"><span class="eyebrow">EVIDENCE / SOURCE AUDIT</span><h1 class="h1">Inspect the record.</h1><p class="lede">Source records include aliases, mirrors and one unverified retrieval lead. Counts are not counts of independent corroborating documents.</p></div><div class="filterbar"><input id="evidence-filter" aria-label="Search sources" placeholder="Search source or qualification"><select id="evidence-type" aria-label="Source type"><option value="all">All source types</option>'+''.join('<option>'+E(x)+'</option>' for x in sorted({s['type'] for s in D['sources']}))+'</select><span id="evidence-count">'+str(len(D['sources']))+' records</span></div><div class="source-list">'
for s in D['sources']:
 item=source_item(s);item=item.replace('<a class="source-item"',f'<a id="{s["id"]}" data-evidence="{E(str(s).lower(),quote=True)}" data-type="{E(s["type"])}" class="source-item"',1);body+=item
body+='</div><div class="insight">An official statement establishes the institution’s position. An order establishes its directions. Neither alone proves implementation. Portal access does not verify an individual case. Historical compilations require amendment checks.</div>'
replace_main(R/'evidence/index.html','<main id="main" class="container">'+body+'</main>')
body='<div class="article-top"><span class="eyebrow">CLAIMS / FULL AUDIT</span><h1 class="h1">The claims register.</h1><p class="lede">Each claim has a source, a limit and the next evidence needed.</p></div><article class="prose research-prose"><div class="filterbar"><input id="questions-filter" placeholder="Search claims" aria-label="Search claims"></div><p><a href="../assets/claims.csv" download>Download claims CSV</a></p>'
for c in D['claims']:body+=f'<section id="{c["id"]}" class="claim-record" data-question="{E(str(c).lower(),quote=True)}"><span class="eyebrow">{c["id"]} / {E(c["status"])}</span><h2>{E(c["claim"])}</h2><p>{cite(c["source_id"])} · {E(c["locator"])}</p><p><strong>Limit:</strong> {E(c["limitation"])}</p><p><strong>Next evidence:</strong> {E(c["next_evidence"])}</p></section>'
replace_main(R/'claims/index.html','<main id="main" class="container">'+body+'</article></main>')
# Dated, actionable gap list.
body='<div class="article-top"><span class="eyebrow">GAP REGISTER / 17 OCT 2026</span><h1 class="h1">What remains to be proved.</h1><p class="lede">A source gap and an outcome gap are different. This register records both.</p></div><article class="prose research-prose">'
for g in D['gap_register']:body+=f'<section id="{g["id"]}"><span class="eyebrow">{g["id"]} / {E(g["status"])}</span><h2>{E(g["topic"])}</h2><p>{E(g["progress"])}</p><p><strong>Required:</strong> {E(g["needed"])}</p></section>'
body+='<p>No records requests, court filings or institutional communications have been sent by this publication.</p></article>'
replace_main(R/'investigations/index.html','<main id="main" class="container">'+body+'</main>')
# Audit result and state-level coverage matrix.
body='<div class="insight">This is an editorial, documentary and numerical audit of the full published corpus. It is not a completed investigation of every voter case. No national wrongful-exclusion total is established.</div><h2>Corrections and improvements</h2>'
for v in D['audit_findings']:body+='<h3>'+v['id']+' · '+E(v['finding'])+'</h3><p>'+E(v['action'])+'. '+(cite(v['source_id']) if v['source_id'] else '')+'</p>'
body+='<h2>Primary-source gaps filled</h2><ul><li>West Bengal January and February orders now inspected with case and paragraph locators.</li><li>Uttarakhand operational and final-publication sources located; 13 district equations and state totals reconciled.</li><li>Standard Form 6 declaration inspected. The online SIR version remains a separate missing record.</li><li>Citizenship Act and Form 7 guidance refreshed; statutory-version limitations recorded.</li></ul><h2>36-jurisdiction coverage matrix</h2><p>All jurisdictions are checked against the national scope records. Local person-level legality remains unaudited. “Aggregate reconciliation” means arithmetic over official counts, not validation of every exclusion.</p>'
rows=[]
for j in sorted(D['jurisdictions'],key=lambda x:x['name']):
 aggregate='Exact official reconciliation' if j['slug'] in ['goa','uttarakhand'] else 'Rounded official totals only' if j['slug']=='bihar' else 'Not established in archive'
 rows.append([f'<a href="../state-files/{j["slug"]}/">{E(j["name"])}</a>',E(j['depth']),E(j['revision_stage']),aggregate,'Not completed'])
body+=table(['Jurisdiction','Article depth','SSR order scope','Aggregate evidence','Individual legality audit'],rows)
body+='<h2>Closure criteria</h2><p>A gap closes only when its decisive evidence is obtained and examined. An indexed URL, a press statement, an accepted application or a proposed audit cannot replace the underlying record needed for the particular conclusion.</p><p>There are '+str(len(D['sources']))+' source records and '+str(len(D['claims']))+' tracked claims. Mirrors and repeated references are disclosed. <a href="../investigations/">Read the complete gap register.</a></p><h2>Verification limits</h2><p>No internal ECINet access, original Commission approval files, completed independent ECINet audit report or authenticated October Form 6 order has been obtained. Current consolidated statutory text and the actual Maharashtra Gazette issue remain open. Browser layout inspection has not been completed in this environment.</p>'
new_page('audit','Full research audit.','Corrections, evidence upgrades and a jurisdiction-by-jurisdiction account of what is still missing.',body)
body='<h2>The standard PDF provides a concrete starting point</h2><p>Declaration (iii) in the official standard Form 6 asserts first-time inclusion and absence from another constituency’s roll. '+cite('FORM6-STANDARD','../','Official form, page 2')+'</p><p>The legal question raised by previously registered applicants cannot be answered by relabelling every applicant “new”. Nor does the standard PDF establish what every online SIR screen required on a particular date.</p><h2>Keep four artefacts distinct</h2>'+table(['Artefact','What it would establish','Current status'],[['Standard Form 6','Published baseline wording','Inspected'],['SIR additional declaration','Extra assertions and supporting information','May annexure and September position available; exact October challenged version pending'],['Portal implementation','Mandatory fields and actual submission behaviour','Dated captures and version history pending'],['Court record','Issue decided and operative relief','May judgment inspected; signed October record pending']])+'<h2>Do not infer the result of the legal challenge</h2><p>October reporting describes no adjudication on the revised form. The source remains reporting of courtroom remarks. It is not a signed order invalidating the form or approving its precise later implementation. '+cite('LB-FORM6-OCT12')+'</p><h2>What a reproducible comparison needs</h2><p>Preserve the PDF and online version identifier, effective date, instruction authorising each field, conditions for submission, and treatment of someone previously enrolled. Compare the exact declaration text, rather than summaries of its purpose. Do not ask an applicant to make a statement that conflicts with their known registration history; the research task is to locate the applicable lawful instruction and case record.</p><h2>Legal sources need version control too</h2><p>The linked Act compilation lacks later amendments. Its upload path does not establish currency. A current consolidation and commencement chain are still required before relying on changed provisions. The page now labels that limitation rather than presenting the text as fully current. '+cite('RPA-1950')+'</p><p>Section 23(3), as reproduced in the linked text, covers amendments, transpositions and deletions under Section 22 as well as inclusion directions during the defined election-period freeze. A general statement about continuous enrolment must be read with that restriction and the operative election dates.</p><p><a href="../investigations/#G03">Form-version gap</a> · <a href="../investigations/#G09">Statutory-version gap</a></p>'
new_page('form-6','Form 6: compare the exact version.','The standard declaration is now inspected. The online version, authorising instructions and signed October court record remain separate evidence questions.',body)
# Synchronise the chronology while retaining the existing surrounding history article.
month={m:i for i,m in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],1)}
def key(row):
 date=row[0];years=re.findall(r'\d{4}',date);year=int(years[-1]) if years else 0;mon=next((v for k,v in month.items() if k in date),1);day=int(re.match(r'(\d{1,2})\s',date).group(1)) if re.match(r'(\d{1,2})\s',date) else 1;return year,mon,day
D['chronology'].sort(key=key)
p=R/'history/index.html';t=p.read_text();start=t.find('<h2 id="timeline"')
if start<0:
 match=re.search(r'<h2[^>]*>The primary-source chronology</h2>',t);start=match.start() if match else -1
if start>=0:
 end=t.find('<div class="insight',start)
 if end<0:end=t.find('</article>',start)
 timeline='<h2 id="timeline">Chronology and review trail</h2>'+''.join('<section class="timeline-item"><span class="eyebrow">'+E(date)+'</span><h3>'+E(title)+'</h3><p>'+E(text)+'</p></section>' for date,title,text in D['chronology'])
 t=t[:start]+timeline+t[end:];p.write_text(t)
# Refresh correction log from data, avoiding stale copies.
p=R/'methodology/index.html';t=p.read_text();start=t.find('<h2 id="corrections"')
if start>=0:
 end=t.find('<h2',start+4)
 if end<0:end=t.find('</article>',start)
 block='<h2 id="corrections">Corrections, in public</h2>'+''.join('<p><strong>'+E(x.get('id','Source update'))+' · '+x['date']+'</strong> '+E(x['correction'])+'</p>' for x in D['editorial_corrections'])
 t=t[:start]+block+t[end:];p.write_text(t)
# Updated legal qualification and links into the audit.
p=R/'legal/index.html';t=p.read_text();t=t if 'Version warning: the linked Act compilation' in t else t.replace('<main id="main" class="container">','<main id="main" class="container"><div class="insight">Version warning: the linked Act compilation is historical and omits later amendments. Current consolidation remains open. <a href="../form-6/">Read the form and source-version audit.</a></div>',1)
t=t.replace('Section 23(3) also prevents inclusion directions within a defined election-period freeze, beginning after the last nomination date.','Section 23(3) also bars the specified Section 22 amendments, transpositions and deletions, and Section 23 inclusion directions, after the last nomination date and before completion of the relevant election.');p.write_text(t)
# Audit navigation and dated front-page update.
for p in R.rglob('*.html'):
 if p.name=='404.html':continue
 t=p.read_text();base=re.search('data-base="([^"]*)"',t).group(1)
 if '>Full Audit <' not in t:t=t.replace('</nav><div class="rail-caption">',f'<a class="rail-link" href="{base}audit/">Full Audit <span>↗</span></a></nav><div class="rail-caption">',1)
 p.write_text(t)
p=R/'research/index.html';t=p.read_text();t=t if 'FULL AUDIT / EDITION 1.2' in t else t.replace('<main id="main" class="container">','<main id="main" class="container"><section class="review-strip"><span class="eyebrow">FULL AUDIT / EDITION 1.2</span><h2>Review the corrections and remaining gaps.</h2><p><a href="../audit/">Full audit and coverage matrix →</a> · <a href="../form-6/">Exact Form 6 version analysis →</a></p></section>',1);p.write_text(t)
p=R/'index.html';t=p.read_text().replace('Maharashtra’s signed extension located. Track what happens next.','Full audit: corrected sources, stronger accounting, explicit gaps.').replace('New primary records, application counts and the transition from SIR to the next summary revision.','Uttarakhand district reconciliation, Form 6 wording and a 36-jurisdiction coverage audit.');p.write_text(t)
# Uniform current datasets, search index and sitemap.
(R/'assets/research-data.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
idx=[]
for p in sorted(R.rglob('*.html')):
 if p.name=='404.html':continue
 t=p.read_text();title=html.unescape(re.search('<title>(.*?)</title>',t).group(1)).replace(' | The SIR Files','');m=re.search('<meta name="description" content="([^"]*)',t);idx.append(dict(title=title,description=html.unescape(m.group(1)) if m else '',kind='State file' if 'state-files/' in str(p) else 'Research',url=p.relative_to(R).as_posix()))
(R/'assets/search-data.js').write_text('window.SIR_INDEX = '+json.dumps(idx,ensure_ascii=False)+';\n')
(R/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>https://ashish-bhatia.github.io/the-sir-files/'+x['url']+'</loc><lastmod>2026-10-17</lastmod></url>' for x in idx)+'</urlset>')
print('Rendered',len(idx),'research pages and all data-backed state, claim, source and gap sections')
