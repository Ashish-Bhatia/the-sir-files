"""Apply the editorial shell, front page and content-addressed assets."""
from pathlib import Path
import re,json,html,hashlib
R=Path(__file__).resolve().parents[1];D=json.loads((R/'assets/research-data.json').read_text());E=html.escape
M=json.loads((R/'assets/case-studies.json').read_text())
links=[('start-here/','Start here'),('case-studies/','Case studies'),('state-files/','State directory'),('evidence/','Evidence'),('methodology/','Our method')]
def case_collection(base=''):
 blocks=[]
 for n,g in enumerate(M['groups'],1):
  cards=''.join(f'<a class="case-card" href="{base}case-studies/{c["id"]}/"><span class="eyebrow">{E(c["place"])} / CASE STUDY</span><h3>{E(c["title"])}</h3><p>{E(c["question"])}</p><span class="case-card-foot">Follow the case <span>→</span></span></a>' for c in M['cases'] if c['group']==g['id'])
  blocks.append(f'<section class="case-group" id="{g["id"]}"><div class="case-group-head"><span class="group-number">0{n}</span><div><h2>{E(g["title"])}</h2><p>{E(g["intro"])}</p></div></div><div class="case-grid">{cards}</div></section>')
 return ''.join(blocks)

for p in R.rglob('*.html'):
 t=p.read_text();m=re.search(r'data-base="([^"]*)"',t)
 if not m:continue
 b=m[1];relative=p.relative_to(R).as_posix()
 t=re.sub(r'<script>\(function\(\)\{try\{var t=localStorage.*?</script>','',t)
 t=re.sub(r'<script src="[^"]*assets/theme.js[^"]*"></script>','',t)
 t=re.sub(r'<html[^>]*>', '<html lang="en" data-theme="light">',t,count=1)
 t=t.replace('content="dark light"','content="light"').replace('content="dark"','content="light"')
 t=re.sub(r'<div class="reading-progress" aria-hidden="true"><span></span></div>','',t)
 nav=''.join(f'<a href="{b}{url}"'+(' aria-current="page"' if relative==url+'index.html' else '')+'>'+label+'</a>' for url,label in links)
 header=f'''<header class="mast"><a class="top-brand" href="{b}index.html"><span class="brand-name">THE SIR FILES<span class="brand-dot">.</span></span><span class="brand-caption">INDEPENDENT RESEARCH ON INDIA’S ELECTORAL ROLLS</span></a><div class="mast-right"><button data-search-open aria-label="Search the publication">⌕ <span>Search</span></button><button class="mobile-menu" data-menu aria-label="Open all sections" aria-expanded="false">☰ <span>Menu</span></button></div><nav class="top-nav" aria-label="Sections">{nav}</nav></header><div class="reading-progress" aria-hidden="true"><span></span></div>'''
 t=re.sub(r'<header class="mast">.*?</header>',lambda _:header,t,flags=re.S)
 side=''.join(f'<a class="rail-link" href="{b}{url}">{label}<span>→</span></a>' for url,label in links)
 side+='<div class="rail-caption">Research tools</div>'+''.join(f'<a class="rail-link" href="{b}{url}">{label}<span>→</span></a>' for url,label in [('research/','Updates to the cases'),('claims/','Claims register'),('investigations/','Open questions'),('audit/','Coverage audit'),('history/','Background and chronology')])
 t=re.sub(r'<nav class="rail-nav".*?</nav>',lambda _:'<nav class="rail-nav" aria-label="All sections">'+side+'</nav>',t,flags=re.S)
 t=t.replace('sources checked through 16 OCT','latest source review: 17 OCT').replace('FRONT PAGE','THE FRONT PAGE')
 if p==R/'index.html':
  main=f'''<main id="main" class="container home"><div class="edition"><span>THE INVESTIGATION</span><time datetime="2026-10-17">Reviewed 17 October 2026</time><a href="research/">Updates to the cases →</a></div><section class="front-page"><article class="lead-article"><span class="eyebrow">EIGHT CASES / FOUR CONNECTED QUESTIONS</span><h1>Follow a case.<br>Understand the process.</h1><p class="lede">Special Intensive Revision prepares electoral rolls afresh. Its effects differ by state. These case studies follow the decisions, the figures and the gaps in the record.</p><div class="button-row"><a class="button" href="#case-groups">Choose your question <span>↓</span></a><a class="button outline" href="start-here/">New to SIR? Start here →</a></div></article><aside class="edition-aside case-intro"><span class="eyebrow">A PLACE TO BEGIN / DELHI</span><h2>How does a voter return to the roll?</h2><ol><li>Two applicants challenge the procedure.</li><li>A court order records a route through Form 6.</li><li>The eventual inclusion still needs evidence.</li></ol><a class="more" href="case-studies/delhi/">Follow the Delhi case from the start →</a><p class="small">Document-based case studies. Individual legality audits remain open.</p></aside></section><section class="question-directory" id="case-groups"><div class="section-head"><div><span class="eyebrow">CHOOSE A QUESTION</span><h2>The investigation, grouped.</h2></div><p>Start with an overview. Follow the story, then read its supporting chapters in order.</p></div><nav class="group-jumps" aria-label="Case study groups">{''.join(f'<a href="#{g["id"]}">{E(g["title"])} ↓</a>' for g in M['groups'])}</nav>{case_collection()}</section><section class="research-library"><div><span class="eyebrow">GO DEEPER</span><h2>The reference material stays connected.</h2><p>The directory covers all 36 jurisdictions. Eight have developed analysis; 28 remain reference files. Source qualifications and corrections stay visible.</p></div><nav aria-label="Research resources"><a href="state-files/">Browse the state directory →</a><a href="claims/">Check the 23 tracked claims →</a><a href="evidence/">Inspect the source record →</a><a href="investigations/">See the unresolved questions →</a></nav></section></main>'''
  t=re.sub(r'<main id="main" class="container".*?</main>',lambda _:main,t,flags=re.S)
 else:
  t=re.sub(r'<section class="case-context".*?</section>','',t,flags=re.S)
  t=re.sub(r'<nav class="chapter-continue".*?</nav>','',t,flags=re.S)
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
 # Every supporting article has its place in a numbered reading path.
 for c in M['cases']:
  match=next((i for i,x in enumerate(c['sequence']) if relative==x['path']+'index.html'),None)
  if match is None:continue
  steps=''.join(f'<a href="{b}{x["path"]}"'+(' aria-current="page"' if i==match else '')+f'><span>{i+1:02d}</span>{E(x["title"])}</a>' for i,x in enumerate(c['sequence']))
  context=f'<section class="case-context" aria-label="Your place in the case"><div><a href="{b}case-studies/{c["id"]}/">← {E(c["place"])} case study</a><span>CHAPTER {match+1} OF {len(c["sequence"])}</span></div><nav aria-label="Case chapters">{steps}</nav></section>'
  t=t.replace('<div class="article-top',context+'<div class="article-top',1)
  following=c['sequence'][match+1] if match+1<len(c['sequence']) else None
  end=f'<nav class="chapter-continue" aria-label="Continue this case"><a href="{b}case-studies/{c["id"]}/">← Return to the case overview</a>'+(f'<a href="{b}{following["path"]}">Next: {E(following["title"])} →</a>' if following else f'<a href="{b}case-studies/{c["id"]}/#unresolved">Review what remains unresolved →</a>')+'</nav>'
  t=t.replace('</main>',end+'</main>',1)
  break
 # Content-addressed URLs prevent stale asset combinations after publishing.
 for asset in ['site.css','site.js','search-data.js']:
  digest=hashlib.sha256((R/'assets'/asset).read_bytes()).hexdigest()[:12]
  t=re.sub(r'(assets/'+re.escape(asset)+r')(?:\?v=[a-zA-Z0-9-]+)?',lambda m:m[1]+'?v='+digest,t)
 p.write_text(t)
print('Applied editorial design to the publication')
