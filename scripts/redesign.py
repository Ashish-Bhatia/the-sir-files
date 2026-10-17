"""Apply the editorial shell, front page and content-addressed assets."""
from pathlib import Path
import re,json,html,hashlib
R=Path(__file__).resolve().parents[1];D=json.loads((R/'assets/research-data.json').read_text());E=html.escape
links=[('research/','Latest research'),('state-files/','State files'),('claims/','Check a claim'),('evidence/','Sources'),('history/','Background'),('investigations/','Open questions')]
topics={'bihar':'The Supreme Court ruling and the limits of what it decides.','goa':'Official totals reconcile. Individual decisions still need scrutiny.','west-bengal':'Court directions and the handling of unresolved cases.','maharashtra':'Applications, revised deadlines and the records still missing.','karnataka':'Bulk objections, Form 7 and the evidence needed to establish outcomes.','delhi':'The Form 6 order and the reported re-verification drive.','uttarakhand':'Thirteen district totals checked against the final report.','tripura':'The corrected deadline and the later reported timetable.'}
for p in R.rglob('*.html'):
 t=p.read_text();m=re.search(r'data-base="([^"]*)"',t)
 if not m:continue
 b=m[1];relative=p.relative_to(R).as_posix()
 t=re.sub(r'<script>\(function\(\)\{try\{var t=localStorage.*?</script>','',t)
 t=re.sub(r'<script src="[^"]*assets/theme.js[^"]*"></script>','',t)
 t=t.replace('<link rel="stylesheet"',f'<script src="{b}assets/theme.js"></script><link rel="stylesheet"',1)
 t=re.sub(r'<div class="reading-progress" aria-hidden="true"><span></span></div>','',t)
 nav=''.join(f'<a href="{b}{url}"'+(' aria-current="page"' if relative==url+'index.html' else '')+'>'+label+'</a>' for url,label in links)
 header=f'''<header class="mast"><a class="top-brand" href="{b}index.html"><span class="brand-name">THE SIR FILES<span class="brand-dot">.</span></span><span class="brand-caption">INDEPENDENT RESEARCH ON INDIA’S ELECTORAL ROLLS</span></a><div class="mast-right"><button class="theme-toggle" data-theme aria-label="Switch colour theme"><span data-theme-icon aria-hidden="true">◐</span><span data-theme-label>Theme</span></button><button data-search-open aria-label="Search the publication">⌕ <span>Search</span></button><button class="mobile-menu" data-menu aria-label="Open all sections" aria-expanded="false">☰ <span>Menu</span></button></div><nav class="top-nav" aria-label="Sections">{nav}</nav></header><div class="reading-progress" aria-hidden="true"><span></span></div>'''
 t=re.sub(r'<header class="mast">.*?</header>',lambda _:header,t,flags=re.S)
 t=t.replace('sources checked through 16 OCT','latest source review: 17 OCT').replace('FRONT PAGE','THE FRONT PAGE')
 if p==R/'index.html':
  states=''.join(f'<a class="state-card" data-state="{E(j["name"].lower(),quote=True)}" data-scope="{"reference" if j["depth"]=="Reference file" else "detailed"}" href="state-files/{j["slug"]}/"><span class="count">{"Reference file" if j["depth"]=="Reference file" else "Developed analysis"}</span><h3>{E(j["name"])}</h3><p>{E(topics.get(j["slug"],"Schedule and source references. Further local evidence needed."))}</p><span class="card-foot">Read the file <span>↗</span></span></a>' for j in sorted(D['jurisdictions'],key=lambda x:(x['depth']=='Reference file',x['name'])))
  claimset=[next(x for x in D['claims'] if x['id']==id) for id in ['DELHI-F6-01','DATA-01','NAT-01']]
  claims=''.join(f'<details class="claim-preview"><summary><span class="status">{E(c["status"])}</span><h3>{E(c["claim"])}</h3><span class="detail-prompt">Read the qualification <b>+</b></span></summary><div class="claim-answer"><p>{E(c["limitation"])}</p><a href="claims/#{c["id"]}">Source and next evidence →</a></div></details>' for c in claimset)
  g=D['goa'];ratio=lambda n:f'{n/g["pre"]*100:.2f}%'
  bars=''.join(f'<div class="roll-row"><span>{label}</span><strong>{value:,}</strong><div class="roll-track"><span style="width:{ratio(value)}"></span></div></div>' for label,value in [('Before SIR',g['pre']),('Draft roll',g['draft']),('Final roll',g['final'])])
  main=f'''<main id="main" class="container home"><div class="edition"><span>THE FRONT PAGE</span><time datetime="2026-10-17">17 October 2026</time><a href="methodology/">Our method &amp; corrections ↗</a></div>
<section class="front-page"><article class="lead-article"><span class="eyebrow">THE LATEST / DELHI / COURT ORDER</span><h1>Delhi’s Form 6 order:<br>what it decides.</h1><p class="lede">Two voters, a disputed declaration and a route through Form 6. We read the 14 October order to separate what the Court decided from what still needs an answer.</p><div class="story-meta"><span>DOCUMENT REVIEW</span><span>Order copy inspected · 4 pages</span></div><a class="button" href="delhi-form-6-order/">Read the analysis <span>→</span></a></article><aside class="edition-aside"><h2>In this edition</h2><a href="statutory-source-update/"><span class="eyebrow">LAW / SOURCE UPDATE</span><h3>A newer Act compilation. A clearer version boundary.</h3><p>The ECI’s July 2025 text includes the 2021 amendments. Later changes still need checking.</p><span class="more">Read the note →</span></a><a href="state-files/delhi/"><span class="eyebrow">DELHI / REPORTED DEVELOPMENT</span><h3>A re-verification drive. Outcomes still to follow.</h3><p>A new report describes the local exercise. The signed instruction and results remain open.</p><span class="more">Open the Delhi file →</span></a><div class="edition-note"><strong>A dated investigation.</strong><p>This edition follows {len(D['claims'])} claims and {len(D['sources'])} source records. It does not provide live monitoring.</p></div></aside></section>
<section class="quick-paths" aria-label="Start reading"><a href="history/"><span>NEW TO SIR?</span><strong>Start with the background →</strong></a><a href="#places"><span>LOOKING CLOSER TO HOME?</span><strong>Find your state →</strong></a><a href="evidence/"><span>WANT THE ORIGINAL RECORD?</span><strong>Read the sources →</strong></a></section>
<section class="section-block" id="places"><div class="section-head"><div><span class="eyebrow">THE STATE FILES</span><h2>A national process.<br>A different record in each state.</h2></div><p>Eight developed analyses. Twenty-eight reference files. Article depth is shown on every file.</p></div><div class="filterbar"><label>State or Union Territory<input id="state-filter" type="search" placeholder="Search a state…"></label><label>Coverage<select id="state-scope"><option value="detailed">Developed analyses</option><option value="all">All 36 jurisdictions</option><option value="reference">Reference files</option></select></label><span id="state-count" aria-live="polite">36 jurisdictions</span></div><div class="state-grid">{states}</div><p class="empty-state hidden" id="state-empty">No matching state. Try another name or choose all jurisdictions.</p></section>
<section class="section-block evidence-feature"><div><span class="eyebrow">READING THE NUMBERS / GOA</span><h2>The totals reconcile.<br>The decisions need their own audit.</h2><p>These are roll stocks at three stages. The decrease is not a measured count of wrongful exclusions.</p><a class="more" href="state-files/goa/">Read the Goa analysis →</a><details class="arithmetic"><summary>See the draft-to-final calculation <span>+</span></summary><p>{g['draft']:,} + {g['accepted']:,} − {g['form_deletions']:,} − {g['eligibility_deletions']:,} = {g['final']:,}</p><p>Additions and two removal categories reconcile the change. The signed report is linked in the <a href="evidence/#GOA-FINAL">source ledger</a>.</p></details></div><div class="roll-figure" role="group" aria-label="Goa electoral roll stocks">{bars}<p>Source: Goa CEO final-publication report.<br>Bar lengths use the same scale, starting at zero.</p></div></section>
<section class="section-block" id="claims"><div class="section-head"><div><span class="eyebrow">CHECK A CLAIM</span><h2>What does the record support?</h2></div><a class="more" href="claims/">All {len(D['claims'])} tracked claims →</a></div><div class="claim-previews">{claims}</div></section>
<section class="closing"><div><span class="eyebrow">RESEARCH IN THE OPEN</span><h2>The gaps stay visible.</h2><p>See the missing records, the corrections and what would change a conclusion.</p></div><div class="button-row"><a class="button outline" href="investigations/">Open questions →</a><a class="button outline" href="audit/">What we checked →</a></div></section></main>'''
  t=re.sub(r'<main id="main" class="container".*?</main>',lambda _:main,t,flags=re.S)
 else:
  # Rebuild rather than duplicate tools when the research renderer regenerates articles.
  t=re.sub(r'<div class="reading-tools">.*?</div>','',t,flags=re.S)
  # Strip the previous generated contents before recreating from current headings.
  t=re.sub(r'<details class="page-contents">.*?</details>','',t,flags=re.S)
  used=set(re.findall(r'\bid="([^"]+)"',t))
  def heading(m):
   attr,text=m.groups()
   if 'id=' in attr:return m[0]
   name='section-'+re.sub('[^a-z0-9]+','-',html.unescape(re.sub('<[^>]*>','',text)).lower()).strip('-')
   candidate=name;n=2
   while candidate in used:candidate=name+'-'+str(n);n+=1
   used.add(candidate);return '<h2'+attr+' id="'+candidate+'">'+text+'</h2>'
  t=re.sub(r'<h2([^>]*)>(.*?)</h2>',heading,t,flags=re.S)
  contents=[(id,html.unescape(re.sub('<[^>]*>','',label))) for id,label in re.findall(r'<h2[^>]*id="([^"]+)"[^>]*>(.*?)</h2>',t,re.S)]
  contents=contents[:18]
  toc='<details class="page-contents"><summary>On this page <span>⌄</span></summary><nav aria-label="Article contents">'+''.join(f'<a href="#{E(id)}">{E(label)}</a>' for id,label in contents)+'</nav></details>' if contents else ''
  tools=f'<div class="reading-tools"><a href="{b}index.html">← Front page</a><span class="reading-actions"><button data-save>＋ Save</button><button data-share>↗ Share</button></span></div>'
  t=t.replace('<main id="main" class="container">','<main id="main" class="container">'+tools+toc,1)
 # Content-addressed URLs prevent stale asset combinations after publishing.
 for asset in ['site.css','site.js','search-data.js','theme.js']:
  digest=hashlib.sha256((R/'assets'/asset).read_bytes()).hexdigest()[:12]
  t=re.sub(r'(assets/'+re.escape(asset)+r')(?:\?v=[a-zA-Z0-9-]+)?',lambda m:m[1]+'?v='+digest,t)
 p.write_text(t)
print('Applied editorial design to the publication')
