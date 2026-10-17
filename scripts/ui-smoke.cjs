// Exercise browser-local behaviour in a small DOM harness. This is not layout QA.
const vm=require('node:vm'),fs=require('node:fs'),assert=require('node:assert/strict');
class Element{
 constructor(){this.dataset={};this.attrs={};this.events={};this.value='';this.style={};this.textContent='';this.innerHTML='';this.classes=new Set();this.classList={add:x=>this.classes.add(x),remove:x=>this.classes.delete(x),contains:x=>this.classes.has(x),toggle:(x,on)=>{on=on===undefined?!this.classes.has(x):on;on?this.classes.add(x):this.classes.delete(x);return on}}}
 addEventListener(k,f){(this.events[k]??=[]).push(f)}
 fire(k,e={}){return Promise.all((this.events[k]||[]).map(f=>f(e)))}
 setAttribute(k,v){this.attrs[k]=String(v)}getAttribute(k){return this.attrs[k]}
 focus(){document.activeElement=this}prepend(x){this.first=x}append(x){this.child=x}querySelector(){return this.first||null}querySelectorAll(){return []}getClientRects(){return [1]}
}
const selectors={};for(const k of ['.rail','.mobile-shade','[data-menu]','[data-theme]','.reading-progress span','#search-modal','#site-search','#search-results','#toast','#state-filter','#state-scope','#state-count','#state-empty','[data-save]'])selectors[k]=new Element();
selectors['#state-scope'].value='detailed';
const states=[['goa','detailed'],['bihar','detailed'],['assam','reference']].map(([state,scope])=>{const e=new Element();e.dataset={state,scope};return e});
const all={'[data-theme]':[selectors['[data-theme]']],'[data-menu]':[selectors['[data-menu]']],'[data-search-open]':[new Element()],'[data-search-close]':[new Element()],'[data-state]':states};
const document={body:{dataset:{base:'../'}},documentElement:{dataset:{},style:{},scrollHeight:2000},readyState:'complete',activeElement:new Element(),querySelector:s=>selectors[s]||null,querySelectorAll:s=>all[s]||[],getElementById:s=>selectors['#'+s]||null,createElement:()=>new Element(),addEventListener(){},title:'Goa | The SIR Files'};
let storage={};const context={document,location:{pathname:'/the-sir-files/state-files/goa/'},localStorage:{getItem:k=>storage[k]||null,setItem:(k,v)=>storage[k]=v},matchMedia:()=>({matches:true}),addEventListener(){},innerHeight:1000,scrollY:500,requestAnimationFrame:f=>f(),setTimeout:()=>1,clearTimeout(){},navigator:{}};context.window=context;context.SIR_INDEX=[{title:'Goa',description:'Final roll',kind:'State file',url:'state-files/goa/index.html'}];
vm.runInNewContext(fs.readFileSync('assets/theme.js','utf8'),context);
vm.runInNewContext(fs.readFileSync('assets/site.js','utf8'),context);
(async()=>{
 assert.equal(selectors['#state-count'].textContent,'2 jurisdictions');
 selectors['#state-filter'].value='assam';await selectors['#state-filter'].fire('input');assert.equal(selectors['#state-count'].textContent,'0 jurisdictions');assert(!selectors['#state-empty'].classList.contains('hidden'));
 selectors['#state-scope'].value='all';await selectors['#state-scope'].fire('change');assert.equal(selectors['#state-count'].textContent,'1 jurisdictions');
 await selectors['[data-theme]'].fire('click');assert.equal(document.documentElement.dataset.theme,'light');assert.equal(storage['sir-theme'],'light');
 await selectors['[data-theme]'].fire('click');assert.equal(storage['sir-theme'],'dark');
 await selectors['[data-menu]'].fire('click');assert(selectors['.rail'].classList.contains('mobile-open'));assert.equal(selectors['[data-menu]'].attrs['aria-expanded'],'true');
 await selectors['.rail'].first.fire('click');assert(!selectors['.rail'].classList.contains('mobile-open'));
 await all['[data-search-open]'][0].fire('click');assert(selectors['#search-modal'].classList.contains('open'));assert(selectors['#search-results'].innerHTML.includes('Goa'));
 selectors['#site-search'].value='nonsense';await selectors['#site-search'].fire('input');assert(selectors['#search-results'].innerHTML.includes('Nothing matched'));
 await all['[data-search-close]'][0].fire('click');assert(!selectors['#search-modal'].classList.contains('open'));
 await selectors['[data-save]'].fire('click');assert.equal(JSON.parse(storage['sir-saved'])[0].path,'state-files/goa/index.html');
 await selectors['[data-save]'].fire('click');assert.equal(JSON.parse(storage['sir-saved']).length,0);
 assert.equal(selectors['.reading-progress span'].style.width,'50%');
 console.log('UI smoke checks passed: theme, filters, empty state, menu, search, reading list, progress.');
})().catch(e=>{console.error(e);process.exitCode=1});
