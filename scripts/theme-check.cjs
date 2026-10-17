// Test the independently loaded theme script under different browser settings.
const vm=require('node:vm'),fs=require('node:fs'),assert=require('node:assert/strict');
const code=fs.readFileSync('assets/theme.js','utf8');
for(const systemDark of [false,true])for(const stored of [null,'light','dark','invalid'])for(const blocked of [false,true]){
 const root={dataset:{},style:{}},label={},icon={},attrs={},listeners={};let value=stored,change;
 const button={querySelector:s=>s==='[data-theme-label]'?label:icon,setAttribute:(k,v)=>attrs[k]=v,addEventListener:(k,f)=>listeners[k]=f};
 const document={documentElement:root,readyState:'complete',querySelectorAll:()=>[button]};
 const media={matches:systemDark,addEventListener:(k,f)=>change=f};
 const context={document,window:{matchMedia:()=>media},localStorage:{getItem(){if(blocked)throw Error();return value},setItem(k,v){if(blocked)throw Error();value=v}}};
 vm.runInNewContext(code,context);
 const expected=!blocked&&['light','dark'].includes(stored)?stored:systemDark?'dark':'light';
 assert.equal(root.dataset.theme,expected);assert.equal(root.style.colorScheme,expected);
 listeners.click();const next=expected==='dark'?'light':'dark';assert.equal(root.dataset.theme,next);assert.equal(label.textContent,next==='dark'?'Light':'Dark');assert.equal(attrs['aria-pressed'],String(next==='dark'));
 if(!blocked)assert.equal(value,next);
 change({matches:!systemDark});assert.equal(root.dataset.theme,next,'Explicit selection must survive a system change');
 listeners.click();assert.equal(root.dataset.theme,expected);
}
console.log('Theme checks passed: 16 system/storage combinations, blocked storage, visible labels, repeated toggles and system changes.');
