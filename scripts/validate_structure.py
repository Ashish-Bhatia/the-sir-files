from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import re,json,hashlib
R=Path(__file__).resolve().parents[1]
class Menu(HTMLParser):
 def __init__(self,text):super().__init__();self.in_menu=False;self.hrefs=[];self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='nav' and a.get('class')=='main-menu':self.in_menu=True
  if self.in_menu and tag=='a':self.hrefs.append(a['href'])
 def handle_endtag(self,tag):
  if tag=='nav':self.in_menu=False
active=redirects=0
for p in R.rglob('*.html'):
 text=p.read_text();assert 'data-theme="dark"' in text,p
 if 'data-redirect="true"' in text:
  redirects+=1;target=re.search(r'content="0;url=([^"]+)"',text)[1];path=(p.parent/urlsplit(target).path).resolve()
  if path.is_dir():path/= 'index.html'
  assert 'data-redirect="true"' not in path.read_text(),('Redirect chain',p)
  continue
 if p.name=='404.html':continue
 active+=1;base=re.search(r'data-base="([^"]*)"',text)[1]
 assert Menu(text).hrefs==[base+x for x in ['index.html','history/','state-files/','forms/','evidence/','methodology/']],p
 for forbidden in ['case-context','chapter-continue','case-card','case-studies/','data-search-open aria-label="Open all sections"','assets/theme.js']:
  assert forbidden not in text,(p,forbidden)
 for asset in ['site.css','site.js','search-data.js']:
  digest=hashlib.sha256((R/'assets'/asset).read_bytes()).hexdigest()[:12];assert f'assets/{asset}?v={digest}' in text,(p,asset)
home=(R/'index.html').read_text();ordered=['what-is-sir','before-2025','bihar-2025','expansion-2025','may-2026','july-september-2026','october-1-7','october-9','october-12-14','october-15-17','where-things-stand'];assert [home.index('id="'+x+'"') for x in ordered]==sorted(home.index('id="'+x+'"') for x in ordered)
assert not (R/'assets/theme.js').exists();assert 'prefers-color-scheme' not in (R/'assets/site.css').read_text()
assert 'GitHub publication review' not in (R/'history/index.html').read_text()
assert len(json.loads((R/'assets/research-data.json').read_text())['sources'])==44
print(f'Basic structure: {active} pages, six menu items, dark palette, chronological article, {redirects} one-hop legacy redirects: pass.')
