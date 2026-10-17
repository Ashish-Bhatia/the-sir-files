// Browser-local logic checks. This does not inspect rendered layout.
const vm=require('node:vm'),fs=require('node:fs'),assert=require('node:assert/strict');
class Element{
 constructor(){this.dataset={};this.value='';this.events={};this.innerHTML='';this.textContent='';this.classes=new Set();this.classList={add:x=>this.classes.add(x),remove:x=>this.classes.delete(x),contains:x=>this.classes.has(x),toggle:(x,on)=>{on?this.classes.add(x):this.classes.delete(x)}}}
 addEventListener(k,f){(this.events[k]??=[]).push(f)}fire(k,e={}){for(const f of this.events[k]||[])f(e)}focus(){document.activeElement=this}querySelectorAll(){return []}
}
const ids={};for(const id of ['search-modal','site-search','search-results','state-filter','state-count','state-empty','evidence-filter','evidence-type','evidence-count','questions-filter'])ids[id]=new Element();ids['evidence-type'].value='all';
const states=['goa','bihar','assam'].map(name=>{const el=new Element();el.dataset.state=name;return el});
const sources=[['goa report','Official'],['delhi order','Court']].map(([text,type])=>{const el=new Element();el.dataset={evidence:text,type};return el});
const claims=['goa arithmetic','form 6 declaration'].map(text=>{const el=new Element();el.dataset.question=text;return el});
const openButton=new Element(),closeButton=new Element(),all={'[data-search-open]':[openButton],'[data-search-close]':[closeButton],'[data-state]':states,'[data-evidence]':sources,'[data-question]':claims},keys={};
const document={body:{dataset:{base:'../'}},activeElement:new Element(),getElementById:id=>ids[id]||null,querySelectorAll:s=>all[s]||[],addEventListener:(k,f)=>keys[k]=f};const window={SIR_INDEX:[{title:'Goa',description:'Final roll',kind:'State report',url:'state-files/goa/index.html'}]};
vm.runInNewContext(fs.readFileSync('assets/site.js','utf8'),{document,window});
assert.equal(ids['state-count'].textContent,'3 states and UTs');ids['state-filter'].value='Goa';ids['state-filter'].fire('input');assert.equal(ids['state-count'].textContent,'1 state or UT');ids['state-filter'].value='nothing';ids['state-filter'].fire('input');assert(!ids['state-empty'].classList.contains('hidden'));
assert.equal(ids['evidence-count'].textContent,'2 entries');ids['evidence-type'].value='Court';ids['evidence-type'].fire('change');assert.equal(ids['evidence-count'].textContent,'1 entry');ids['evidence-filter'].value='goa';ids['evidence-filter'].fire('input');assert.equal(ids['evidence-count'].textContent,'0 entries');
ids['questions-filter'].value='form 6';ids['questions-filter'].fire('input');assert(claims[0].classList.contains('hidden'));assert(!claims[1].classList.contains('hidden'));
openButton.fire('click');assert(ids['search-modal'].classList.contains('open'));assert(ids['search-results'].innerHTML.includes('../state-files/goa/index.html'));ids['site-search'].value='nothing';ids['site-search'].fire('input');assert(ids['search-results'].innerHTML.includes('No matching article'));keys.keydown({key:'Escape'});assert(!ids['search-modal'].classList.contains('open'));openButton.fire('click');closeButton.fire('click');assert(!ids['search-modal'].classList.contains('open'));
console.log('Search, close/escape, state filtering, source filtering and statement filtering: pass.');
