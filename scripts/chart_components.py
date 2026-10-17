"""Accessible, zero-based charts generated only from the SIR dataset."""
from pathlib import Path
import json,html
D=json.loads((Path(__file__).resolve().parents[1]/'assets/research-data.json').read_text());E=html.escape

def bars(rows,diverging=False):
 maximum=max(abs(value) for _,value in rows) or 1
 out='<div class="chart-bars'+(' diverging' if diverging else '')+'" role="list">'
 for label,value in rows:
  width=abs(value)/maximum*(50 if diverging else 100);left=50-width if value<0 else 50
  style=f'width:{width:.4f}%;'+(f'left:{left:.4f}%;' if diverging else '')
  number=f'{value:+,}' if diverging else f'{value:,}'
  out+=f'<div class="chart-row" role="listitem"><div class="chart-label"><span>{E(label)}</span><strong>{number}</strong></div><div class="chart-track" aria-hidden="true"><i class="chart-bar {"negative" if value<0 else "positive"}" style="{style}"></i></div></div>'
 return out+'</div>'
def controls(id,labels):
 return '<div class="chart-controls" role="group" aria-label="Chart view">'+''.join(f'<button data-chart-target="{id}-{key}" aria-controls="{id}-{key}" aria-pressed="{"true" if n==0 else "false"}">{E(label)}</button>' for n,(key,label) in enumerate(labels))+'</div>'
def panel(id,key,body,initial=False):return f'<div id="{id}-{key}" class="chart-panel"'+('' if initial else ' hidden')+'>'+body+'</div>'
def goa(base=''):
 g=D['goa'];stock=[('Before SIR',g['pre']),('Draft roll',g['draft']),('Final roll',g['final'])];movement=[('Accepted additions',g['accepted']),('Form-based removals',-g['form_deletions']),('Eligibility determinations',-g['eligibility_deletions'])]
 return '<figure class="sir-chart" data-chart><figcaption><span class="eyebrow">GOA / FEBRUARY 2026</span><h3>How the roll changed</h3></figcaption>'+controls('goa',[('size','Roll sizes'),('change','Draft-to-final changes')])+panel('goa','size',bars(stock)+'<p class="chart-note">Three roll sizes, on the same scale starting at zero. These are entries, not a count of wrongful exclusions.</p>',True)+panel('goa','change',bars(movement,True)+f'<p class="chart-note">Net change from draft to final: {g["final"]-g["draft"]:+,} entries. The central line is zero. Different removal categories are shown separately.</p>')+f'<p class="chart-source">Source: <a href="{base}evidence/#GOA-FINAL">Goa CEO final-publication report</a>.</p></figure>'
def uttarakhand(base=''):
 rows=D['uttarakhand']['districts'];final=[(r['district'],r['final']) for r in rows];change=[(r['district'],r['final']-r['draft']) for r in rows]
 table='<details class="chart-table"><summary>View the district figures</summary><div class="table-wrap"><table><thead><tr><th>District</th><th>Draft</th><th>Final</th><th>Change</th></tr></thead><tbody>'+''.join(f'<tr><td>{E(r["district"])}</td><td>{r["draft"]:,}</td><td>{r["final"]:,}</td><td>{r["final"]-r["draft"]:+,}</td></tr>' for r in rows)+'</tbody></table></div></details>'
 return '<figure class="sir-chart" data-chart><figcaption><span class="eyebrow">UTTARAKHAND / OCTOBER 2026</span><h3>The final roll, district by district</h3></figcaption>'+controls('uk',[('final','Final roll'),('change','Change since draft')])+panel('uk','final',bars(final)+'<p class="chart-note">All bars start at zero. District sizes differ, so these counts are not rates of exclusion.</p>',True)+panel('uk','change',bars(change,True)+'<p class="chart-note">Final minus draft. The central line is zero. These net changes do not establish wrongful removals or restorations.</p>')+table+f'<p class="chart-source">Source: <a href="{base}evidence/#UK-FINAL-OCT03">Uttarakhand final report and district annexure</a>.</p></figure>'
def ssr(base=''):
 s=D['revision_stages'];names={j['slug']:j['name'] for j in D['jurisdictions']};groups=[('scheduled','SSR scheduled',s['ssr_scheduled']),('deferred','SSR deferred',s['ssr_deferred']),('not-started','SIR not started',s['sir_not_started_as_stated_in_order'])]
 stack='<div class="scope-stack" aria-hidden="true">'+''.join(f'<span class="scope-{key}" style="width:{len(values)/36*100:.4f}%">{len(values)}</span>' for key,_,values in groups)+'</div>'
 panels=''.join(panel('ssr',key,'<h4>'+E(label)+'</h4><ul class="scope-list">'+''.join('<li>'+E(names[id])+'</li>' for id in values)+'</ul>',i==0) for i,(key,label,values) in enumerate(groups))
 return '<figure class="sir-chart" data-chart><figcaption><span class="eyebrow">ECI ORDER / 15 OCTOBER 2026</span><h3>Which revision stage applies?</h3></figcaption>'+stack+controls('ssr',[(key,label+' · '+str(len(values))) for key,label,values in groups])+panels+'<p class="chart-note">The 36 states and Union Territories fall into three disjoint groups in this order. This shows its administrative scope, not successful completion or individual outcomes.</p>'+f'<p class="chart-source">Source: <a href="{base}evidence/#ECI-SSR-OCT15">15 October SSR order</a>.</p></figure>'
