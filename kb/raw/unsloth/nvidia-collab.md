---
source_url: https://unsloth.ai/blog/nvidia-collab
slug: nvidia-collab
title: "How to Make LLM Training Faster with Unsloth and NVIDIA"
captured_date: 2026-08-25
status: raw_capture
provenance: unsloth_blog_first_party
---

# How to Make LLM Training Faster with Unsloth and NVIDIA

-                             How to Make LLM Training Faster with Unsloth and NVIDIA   {"@context":"https://schema.org","@type":"WebSite","name":"Unsloth - Train and Run Models Locally","url":"https://unsloth.ai"}
!function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.crossOrigin="anonymous",p.async=!0,p.src=s.api_host.replace(".i.posthog.com","-assets.i.posthog.com")+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="init capture register register_once register_for_session unregister unregister_for_session getFeatureFlag getFeatureFlagPayload isFeatureEnabled reloadFeatureFlags updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures on onFeatureFlags onSessionId getSurveys getActiveMatchingSurveys renderSurvey canRenderSurvey getNextSurveyStep identify setPersonProperties group resetGroups setPersonPropertiesForFlags resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags reset get_distinct_id getGroups get_session_id get_session_replay_url alias set_config startSessionRecording stopSessionRecording sessionRecordingStarted captureException loadToolbar get_property getSessionProperty createPersonProfile opt_in_capturing opt_out_capturing has_opted_in_capturing has_opted_out_capturing clear_opt_in_out_capturing debug".split(" "),n=0;n

:root{color-scheme:light}
html[data-unsloth-theme="dark"]{color-scheme:dark;background:#080909!important}
html[data-unsloth-theme="dark"] body{color:#f2f5f3!important;background:#080909!important}
.u-theme-toggle{width:40px!important;height:40px!important;min-width:40px!important;min-height:40px!important;display:inline-grid!important;place-items:center!important;flex:0 0 40px!important;padding:0!important;border:0!important;border-radius:999px!important;color:#303633!important;background:#edf0ee!important;box-shadow:none!important;cursor:pointer!important}
.u-theme-toggle:hover{color:#101311!important;background:#e3e7e4!important;opacity:1!important}
.u-theme-toggle:focus-visible{outline:2px solid #35d6a4!important;outline-offset:3px!important}
.u-theme-toggle svg{width:18px!important;height:18px!important;display:block!important;fill:none!important;stroke:currentColor!important;stroke-width:1.8!important;stroke-linecap:round!important;stroke-linejoin:round!important}
.u-theme-icon-sun{display:none!important}
html[data-unsloth-theme="dark"] .u-theme-icon-sun{display:block!important}
html[data-unsloth-theme="dark"] .u-theme-icon-moon{display:none!important}
.u-theme-toggle-floating{position:fixed!important;top:18px!important;right:18px!important;z-index:9999!important}
html[data-unsloth-theme="dark"] body *,
html[data-unsloth-theme="dark"] body *::before,
html[data-unsloth-theme="dark"] body *::after{border-color:transparent!important;box-shadow:none!important}
html[data-unsloth-theme="dark"] body .u-theme-auto-surface-1{background-color:#111313!important;background-image:none!important}
html[data-unsloth-theme="dark"] body .u-theme-auto-surface-2{background-color:#171a19!important;background-image:none!important}
html[data-unsloth-theme="dark"] body .u-theme-auto-surface-accent{background-color:#13231d!important;background-image:none!important}
html[data-unsloth-theme="dark"] body .u-theme-auto-text{color:#f2f5f3!important}
html[data-unsloth-theme="dark"] body .u-theme-auto-muted{color:#a4ada8!important}
html[data-unsloth-theme="dark"] body .u-theme-auto-accent-text{color:#78e6c4!important}
html[data-unsloth-theme="dark"] body .u-theme-auto-control{color:#eef2f0!important;background-color:#202422!important;border:0!important;box-shadow:none!important}
html[data-unsloth-theme="dark"] body .u-theme-auto-control:hover{color:#fff!important;background-color:#292e2b!important}
html[data-unsloth-theme="dark"] body .u-nav{background:transparent!important;background-image:none!important;box-shadow:none!important}
html[data-unsloth-theme="dark"] body .u-nav-row{color:#f2f5f3!important;background:#2b302d!important;border:0!important;box-shadow:none!important}
html[data-unsloth-theme="dark"] body .u-logo,
html[data-unsloth-theme="dark"] body .u-logo span,
html[data-unsloth-theme="dark"] body .u-nav-links a,
html[data-unsloth-theme="dark"] body .u-social-link{color:#e8edea!important}
html[data-unsloth-theme="dark"] body .u-theme-toggle{color:#e7ece9!important;background:#232725!important}
html[data-unsloth-theme="dark"] body .u-theme-toggle:hover{color:#fff!important;background:#2c312e!important}
html[data-unsloth-theme="dark"] body .u-social-link:hover{color:#35d6a4!important;background:#182b24!important}
html[data-unsloth-theme="dark"] body .u-nav-download{color:#07110d!important;background:#35d6a4!important}
html[data-unsloth-theme="dark"] body .u-nav-download:hover{color:#07110d!important;background:#62e1bb!important}
html[data-unsloth-theme="dark"] body .u-mobile-nav>summary{color:#eef2f0!important;background:#242826!important;border:0!important;box-shadow:none!important}
html[data-unsloth-theme="dark"] body .u-mobile-nav-panel{color:#f2f5f3!important;background:#171a19!important;border:0!important;box-shadow:none!important}
html[data-unsloth-theme="dark"] body .u-mobile-nav-panel a{color:#eef2f0!important}
html[data-unsloth-theme="dark"] body .u-mobile-nav-panel a:hover{background:#202622!important}
html[data-unsloth-theme="dark"] body .u-footer,
html[data-unsloth-theme="dark"] body #unsloth-shared-footer,
html[data-unsloth-theme="dark"] body .unsloth-global-chrome{color:#f2f5f3!important;background:#0e0f0f!important;border:0!important;box-shadow:none!important}
html[data-unsloth-theme="dark"] body .u-footer .u-logo,
html[data-unsloth-theme="dark"] body .u-footer .u-logo span,
html[data-unsloth-theme="dark"] body .u-footer-grid>div>h3{color:#f2f5f3!important}
html[data-unsloth-theme="dark"] body .u-footer-intro p,
html[data-unsloth-theme="dark"] body .u-footer-links a{color:#a4ada8!important}
html[data-unsloth-theme="dark"] body .u-footer-bottom,
html[data-unsloth-theme="dark"] body .u-footer-bottom a{color:#828b86!important}
html[data-unsloth-theme="dark"] body table,
html[data-unsloth-theme="dark"] body thead,
html[data-unsloth-theme="dark"] body tbody,
html[data-unsloth-theme="dark"] body tr{background:#111313!important}
html[data-unsloth-theme="dark"] body th,
html[data-unsloth-theme="dark"] body td{color:#e7ece9!important;background:#171a19!important;border:0!important}
html[data-unsloth-theme="dark"] body input,
html[data-unsloth-theme="dark"] body textarea,
html[data-unsloth-theme="dark"] body select{color:#f2f5f3!important;background:#1b1f1d!important;border:0!important;box-shadow:none!important}
html[data-unsloth-theme="dark"] body input::placeholder,
html[data-unsloth-theme="dark"] body textarea::placeholder{color:#7f8984!important}
html[data-unsloth-theme="dark"] body code,
html[data-unsloth-theme="dark"] body pre{color:#d8efe7!important;background:#151817!important;border:0!important;box-shadow:none!important}
html[data-unsloth-theme="dark"] body ::selection{color:#07110d!important;background:#54ddb4!important}
@media(max-width:991px){.u-theme-toggle:not(.u-theme-toggle-floating){margin-left:auto!important;margin-right:4px!important}}
@media(max-width:479px){.u-theme-toggle{width:38px!important;height:38px!important;min-width:38px!important;min-height:38px!important;flex-basis:38px!important}}
@media(print){.u-theme-toggle{display:none!important}}

(function(){
if(window.__unslothGlobalTheme2026&&window.__unslothGlobalTheme2026.version==='footer-switch-v3'){window.__unslothGlobalTheme2026.refresh();return}
var storageKey='unsloth-theme';
var modeKey='unsloth-theme-mode';
var root=document.documentElement;
var media=window.matchMedia('(prefers-color-scheme: dark)');
var control=null;
var scanQueued=false;
function storedMode(){
try{
var mode=window.localStorage.getItem(modeKey);
if(mode==='dark'||mode==='light'||mode==='system')return mode;
var legacy=window.localStorage.getItem(storageKey);
return legacy==='dark'||legacy==='light'?legacy:'system';
}catch(error){return 'system'}
}
function themeForMode(mode){return mode==='system'?(media.matches?'dark':'light'):mode}
function persistMode(mode){
try{
window.localStorage.setItem(modeKey,mode);
if(mode==='system')window.localStorage.removeItem(storageKey);
else window.localStorage.setItem(storageKey,mode);
}catch(error){}
}
function rgb(value){
var match=String(value||'').match(/rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)(?:\s*[,/]\s*([\d.]+))?\s*\)/i);
return match?{r:+match[1],g:+match[2],b:+match[3],a:match[4]===undefined?1:+match[4]}:null;
}
function luminance(color){
function channel(value){value/=255;return value .05){
var bgLum=luminance(background);
var bgSat=saturation(background);
if(bgLum>.9)element.classList.add('u-theme-auto-surface-1');
else if(bgLum>.68)element.classList.add(bgSat>.12?'u-theme-auto-surface-accent':'u-theme-auto-surface-2');
}
var color=rgb(style.color);
if(color&&color.a>.05){
var textLum=luminance(color);
var textSat=saturation(color);
if(textLum .34?'u-theme-auto-accent-text':'u-theme-auto-muted');
}
var interactive=/^(A|BUTTON|INPUT|TEXTAREA|SELECT|SUMMARY)$/.test(tag);
var hasBorder=['Top','Right','Bottom','Left'].some(function(side){
return parseFloat(style['border'+side+'Width'])>0&&style['border'+side+'Style']!=='none';
});
if(interactive&&hasBorder)element.classList.add('u-theme-auto-control');
});
}
function scheduleScan(){
if(scanQueued)return;
scanQueued=true;
(window.requestAnimationFrame||window.setTimeout)(classify);
}
function updateControl(mode,theme){
if(!control)return;
control.setAttribute('data-theme-mode',mode);
control.setAttribute('data-resolved-theme',theme);
control.querySelectorAll('.u-theme-option').forEach(function(option){
var active=option.getAttribute('data-theme-choice')===mode;
option.setAttribute('aria-checked',active?'true':'false');
option.setAttribute('aria-pressed',active?'true':'false');
});
}
function applyTheme(theme){
root.setAttribute('data-unsloth-theme',theme);
if(theme==='dark')scheduleScan();
}
function applyMode(mode){
if(mode!=='dark'&&mode!=='light'&&mode!=='system')mode='system';
var theme=themeForMode(mode);
root.setAttribute('data-unsloth-theme-mode',mode);
applyTheme(theme);
updateControl(mode,theme);
}
function ensureControl(){
if(!document.body)return false;
var footer=document.querySelector('footer,.u-footer,[role="contentinfo"]');
var logo=footer&&(footer.querySelector('.u-footer-intro .u-logo')||footer.querySelector('.u-logo')||footer.querySelector('a[href="/"]'));
var host=logo&&logo.parentElement;
document.querySelectorAll('.u-theme-toggle').forEach(function(oldToggle){oldToggle.remove()});
control=document.querySelector('.u-theme-switch');
if(!host)return false;
if(!control){
control=document.createElement('div');
control.className='u-theme-switch u-theme-switch-footer';
control.setAttribute('role','radiogroup');
control.setAttribute('aria-label','Theme preference');
control.innerHTML="
";
}
if(control.getAttribute('data-unsloth-global-switch')!=='true'){
if(control.parentElement){
var cleanControl=control.cloneNode(true);
control.parentElement.replaceChild(cleanControl,control);
control=cleanControl;
}
control.removeAttribute('data-unsloth-local-switch');
control.setAttribute('data-unsloth-global-switch','true');
control.querySelectorAll('.u-theme-option').forEach(function(option){
option.onclick=function(){
var mode=option.getAttribute('data-theme-choice');
persistMode(mode);
applyMode(mode);
};
});
}
control.classList.add('u-theme-switch-footer');
if(control.parentElement!==host||control.previousElementSibling!==logo)host.insertBefore(control,logo.nextSibling);
updateControl(storedMode(),themeForMode(storedMode()));
return true;
}
function refresh(){
applyMode(storedMode());
ensureControl();
scheduleScan();
}
function systemChange(){if(storedMode()==='system')applyMode('system')}
var observer=new MutationObserver(function(){ensureControl();scheduleScan()});
observer.observe(root,{childList:true,subtree:true});
if(media.addEventListener)media.addEventListener('change',systemChange);
else if(media.addListener)media.addListener(systemChange);
var controller={version:'footer-switch-v3',refresh:refresh};
window.__unslothGlobalTheme2026=controller;
window.__unslothThemeController2026=controller;
applyMode(storedMode());
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',refresh,{once:true});
else refresh();
})();

.u-theme-toggle{position:relative!important}
.u-theme-toggle .u-theme-icon-moon,
.u-theme-toggle .u-theme-icon-sun{position:absolute!important;top:50%!important;left:50%!important;width:18px!important;height:18px!important;margin:0!important;transform:translate(-50%,-50%)!important}
html[data-unsloth-theme="light"] body .u-theme-toggle .u-theme-icon-moon{display:block!important}
html[data-unsloth-theme="light"] body .u-theme-toggle .u-theme-icon-sun{display:none!important}
html[data-unsloth-theme="dark"] body .u-theme-toggle .u-theme-icon-moon{display:none!important}
html[data-unsloth-theme="dark"] body .u-theme-toggle .u-theme-icon-sun{display:block!important}

html body img{border-radius:16px!important}
html body main img,
html body article img,
html body .u-news-thumb img,
html body .u-app-shot>img,
html body img.u-product-shot,
html body .u-feature .u-visual-field>img,
html body .u-hero-visual img{border-radius:20px!important}
html body .u-news-thumb,
html body .u-app-shot,
html body .u-product-shot{overflow:hidden!important}
html body .u-logo img,
html body .u-social-link img,
html body .u-footer-links img,
html body .u-download-icon img,
html body .u-current-os-icon img,
html body .unsloth-download-option-icon img{border-radius:0!important}
@media(max-width:479px){
html body img{border-radius:14px!important}
html body main img,
html body article img,
html body .u-app-shot>img,
html body img.u-product-shot,
html body .u-feature .u-visual-field>img,
html body .u-hero-visual img{border-radius:18px!important}
html body .u-logo img,
html body .u-social-link img,
html body .u-footer-links img,
html body .u-download-icon img,
html body .u-current-os-icon img,
html body .unsloth-download-option-icon img{border-radius:0!important}
}

footer .u-footer-intro,.u-footer .u-footer-intro,[role="contentinfo"] .u-footer-intro{display:flex!important;flex-direction:column!important;align-items:flex-start!important;gap:24px!important}
footer .u-logo,.u-footer .u-logo,[role="contentinfo"] .u-logo{gap:14px!important}
footer .u-logo img,.u-footer .u-logo img,[role="contentinfo"] .u-logo img,footer a[href="/"] img[alt*="unsloth" i]{width:48px!important;height:48px!important;max-width:none!important}
footer .u-logo span,.u-footer .u-logo span,[role="contentinfo"] .u-logo span{font-size:32px!important;line-height:1!important}
footer .u-theme-toggle-footer,.u-footer .u-theme-toggle-footer,[role="contentinfo"] .u-theme-toggle-footer{margin:0!important;align-self:flex-start!important}
@media(max-width:479px){
footer .u-logo img,.u-footer .u-logo img,[role="contentinfo"] .u-logo img,footer a[href="/"] img[alt*="unsloth" i]{width:44px!important;height:44px!important}
footer .u-logo span,.u-footer .u-logo span,[role="contentinfo"] .u-logo span{font-size:29px!important}
}

.u-current-os-direct[aria-label="Download for Linux"] .u-current-os-icon,
#unsloth-os-download-cta[aria-label="Download for Linux"] .unsloth-download-icon{
width:38px!important;height:38px!important;min-width:38px!important;flex:0 0 38px!important;display:inline-grid!important;place-items:center!important
}
.u-current-os-direct[aria-label="Download for Linux"] .u-current-os-icon img,
#unsloth-os-download-cta[aria-label="Download for Linux"] .unsloth-download-icon img{
display:block!important;width:34px!important;height:34px!important;max-width:none!important;object-fit:contain!important;filter:brightness(0) invert(1)!important
}
html[data-unsloth-theme="dark"] .u-current-os-direct[aria-label="Download for Linux"] .u-current-os-icon img,
html[data-unsloth-theme="dark"] #unsloth-os-download-cta[aria-label="Download for Linux"] .unsloth-download-icon img{
filter:brightness(0)!important
}
@media(prefers-color-scheme:dark){
html:not([data-unsloth-theme]) .u-current-os-direct[aria-label="Download for Linux"] .u-current-os-icon img,
html:not([data-unsloth-theme]) #unsloth-os-download-cta[aria-label="Download for Linux"] .unsloth-download-icon img{filter:brightness(0)!important}
}
@media(max-width:479px){
.u-current-os-direct[aria-label="Download for Linux"] .u-current-os-icon,
#unsloth-os-download-cta[aria-label="Download for Linux"] .unsloth-download-icon{width:34px!important;height:34px!important;min-width:34px!important;flex-basis:34px!important}
.u-current-os-direct[aria-label="Download for Linux"] .u-current-os-icon img,
#unsloth-os-download-cta[aria-label="Download for Linux"] .unsloth-download-icon img{width:30px!important;height:30px!important}
}

.u-theme-switch{display:inline-grid!important;grid-template-columns:repeat(3,36px)!important;gap:6px!important;align-items:center!important;width:auto!important;height:44px!important;padding:4px!important;border:0!important;border-radius:999px!important;background:#e4e8e5!important;box-shadow:none!important;color:#3b423e!important}
.u-theme-option{width:36px!important;height:36px!important;display:flex!important;align-items:center!important;justify-content:center!important;position:relative!important;line-height:0!important;padding:0!important;border:0!important;border-radius:999px!important;background:transparent!important;box-shadow:none!important;color:inherit!important;cursor:pointer!important}
.u-theme-option:hover{background:#d9dedb!important;color:#111412!important}
.u-theme-option[aria-checked="true"]{background:#fff!important;color:#101311!important}
.u-theme-option:focus-visible{outline:2px solid #35d6a4!important;outline-offset:2px!important}
.u-theme-option svg{width:17px!important;height:17px!important;display:block!important;position:absolute!important;top:50%!important;left:50%!important;transform:translate(-50%,-50%)!important;margin:0!important;fill:none!important;stroke:currentColor!important;stroke-width:1.8!important;stroke-linecap:round!important;stroke-linejoin:round!important}
html[data-unsloth-theme="dark"] body .u-theme-switch{background:#0e1010!important;color:#9ca5a0!important}
html[data-unsloth-theme="dark"] body .u-theme-option:hover{background:#1b1f1d!important;color:#fff!important}
html[data-unsloth-theme="dark"] body .u-theme-option[aria-checked="true"]{background:#252a27!important;color:#fff!important}
footer .u-theme-switch-footer,.u-footer .u-theme-switch-footer,[role="contentinfo"] .u-theme-switch-footer{margin:0!important;align-self:flex-start!important}
@media(max-width:479px){
.u-theme-switch{grid-template-columns:repeat(3,34px)!important;gap:5px!important;height:42px!important}
.u-theme-option{width:34px!important;height:34px!important}
.u-theme-option svg{width:17px!important;height:17px!important}
}
@media(print){.u-theme-switch{display:none!important}}

html[data-unsloth-theme="dark"] body .platform .linux-logo-crop img,
html[data-unsloth-theme="dark"] body [role="tab"] .linux-logo-crop img{filter:brightness(0) invert(1)!important}

html[data-unsloth-theme="dark"] body .u-nav,
html[data-unsloth-theme="dark"] body header.u-theme-auto-surface-1{background-color:transparent!important;background-image:none!important}
html[data-unsloth-theme="dark"] body .u-nav-row{background-color:#2b302d!important;background-image:none!important}
html[data-unsloth-theme="dark"] body header .u-social-link img,
html[data-unsloth-theme="dark"] body .u-nav-row .u-social-link img{filter:brightness(2.25)!important}

html[data-unsloth-theme="dark"] body .u-download-panel .u-download-option[href*="Ubuntu"] .u-download-icon{position:relative!important;overflow:visible!important;display:grid!important;place-items:center!important}
html[data-unsloth-theme="dark"] body .u-download-panel .u-download-option[href*="Ubuntu"] .u-download-icon>img{position:absolute!important;top:50%!important;left:50%!important;translate:-50% -50%!important;scale:1.04!important;transform-origin:center!important;filter:brightness(0) saturate(100%) invert(66%) sepia(6%) saturate(300%) hue-rotate(100deg) brightness(90%) contrast(90%)!important}

(function(){
var mode='system';
try{
var saved=window.localStorage.getItem('unsloth-theme-mode');
var legacy=window.localStorage.getItem('unsloth-theme');
if(saved==='dark'||saved==='light'||saved==='system')mode=saved;
else if(legacy==='dark'||legacy==='light')mode=legacy;
}catch(error){}
var dark=window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches;
var theme=mode==='system'?(dark?'dark':'light'):mode;
document.documentElement.setAttribute('data-unsloth-theme-mode',mode);
document.documentElement.setAttribute('data-unsloth-theme',theme);
})();

:root{color-scheme:light}
html[data-unsloth-theme="light"]{color-scheme:light}
html[data-unsloth-theme="dark"]{
color-scheme:dark;
--u-dark-canvas:#181818;
--u-dark-surface-1:#1f1f1f;
--u-dark-surface-2:#292929;
--u-dark-surface-3:#2c2c2c;
--u-dark-surface-4:#3a3a3a;
--u-dark-accent-surface:#2c2c2c;
--u-dark-text:#f5f5f5;
--u-dark-muted:#b4b4b4;
--u-dark-subtle:#8e8e8e;
--u-dark-accent:#6ce0b8;
--u-dark-accent-strong:#43d3a3;
background:#181818!important;
}
html[data-unsloth-theme="dark"] body{
color:var(--u-dark-text)!important;
background:var(--u-dark-canvas)!important;
}
html[data-unsloth-theme="dark"] body *,
html[data-unsloth-theme="dark"] body *::before,
html[data-unsloth-theme="dark"] body *::after{
border-color:transparent!important;
box-shadow:none!important;
text-shadow:none!important;
}
html[data-unsloth-theme="dark"] body .u-theme-auto-surface-1{
--u-dark-auto-background:var(--u-dark-surface-1);
--u-dark-auto-background-image:none;
background-color:var(--u-dark-surface-1)!important;
background-image:none!important;
}
html[data-unsloth-theme="dark"] body .u-theme-auto-surface-2{
--u-dark-auto-background:var(--u-dark-surface-2);
--u-dark-auto-background-image:none;
background-color:var(--u-dark-surface-2)!important;
background-image:none!important;
}
html[data-unsloth-theme="dark"] body .u-theme-auto-surface-accent{
--u-dark-auto-background:var(--u-dark-accent-surface);
--u-dark-auto-background-image:none;
background-color:var(--u-dark-accent-surface)!important;
background-image:none!important;
}
html[data-unsloth-theme="dark"] body .u-theme-auto-text{--u-dark-auto-color:var(--u-dark-text);color:var(--u-dark-text)!important}
html[data-unsloth-theme="dark"] body .u-theme-auto-muted{--u-dark-auto-color:var(--u-dark-muted);color:var(--u-dark-muted)!important}
html[data-unsloth-theme="dark"] body .u-theme-auto-accent-text{--u-dark-auto-color:var(--u-dark-accent);color:var(--u-dark-accent)!important}
html[data-unsloth-theme="dark"] body .u-theme-auto-control{
--u-dark-auto-background:var(--u-dark-surface-3);
--u-dark-auto-color:var(--u-dark-text);
color:var(--u-dark-text)!important;
background-color:var(--u-dark-surface-3)!important;
border:0!important;
box-shadow:none!important;
}
html[data-unsloth-theme="dark"] body .u-theme-auto-control:hover{
color:#fff!important;
background-color:var(--u-dark-surface-4)!important;
}
html[data-unsloth-theme="dark"]:not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity){
background-color:#181818!important;
}
html[data-unsloth-theme="dark"]:not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity) body{
color:#f5f5f5!important;
background-color:#181818!important;
}
html[data-unsloth-theme="dark"]:not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity) body *,
html[data-unsloth-theme="dark"]:not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity) body *::before,
html[data-unsloth-theme="dark"]:not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity) body *::after{
border-color:transparent!important;
box-shadow:none!important;
text-shadow:none!important;
}
html[data-unsloth-theme="dark"]:not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity) body :is(.u-theme-auto-surface-1,.u-theme-auto-surface-2,.u-theme-auto-surface-accent,.u-theme-auto-text,.u-theme-auto-muted,.u-theme-auto-accent-text,.u-theme-auto-control){
color:var(--u-dark-auto-color)!important;
background-color:var(--u-dark-auto-background)!important;
background-image:var(--u-dark-auto-background-image)!important;
}
html[data-unsloth-theme="dark"] body .u-nav{
background:transparent!important;
background-image:none!important;
box-shadow:none!important;
}
html[data-unsloth-theme="dark"] body .u-nav-row{
--u-dark-auto-background:var(--u-dark-surface-3);
color:var(--u-dark-text)!important;
background:var(--u-dark-surface-3)!important;
border:0!important;
box-shadow:none!important;
}
html[data-unsloth-theme="dark"] body .u-logo,
html[data-unsloth-theme="dark"] body .u-logo span,
html[data-unsloth-theme="dark"] body .u-nav-links a,
html[data-unsloth-theme="dark"] body .u-social-link{color:#e8e8e8!important}
html[data-unsloth-theme="dark"] body .u-social-link:hover{
color:var(--u-dark-accent)!important;
background:var(--u-dark-accent-surface)!important;
}
html[data-unsloth-theme="dark"] body .u-nav-download{
color:#181818!important;
background:var(--u-dark-accent-strong)!important;
}
html[data-unsloth-theme="dark"] body .u-nav-download:hover{
color:#181818!important;
background:#70e6bd!important;
}
html[data-unsloth-theme="dark"] body .u-mobile-nav>summary{
--u-dark-auto-background:var(--u-dark-surface-3);
--u-dark-auto-color:#f7f7f7;
color:#f7f7f7!important;
background:var(--u-dark-surface-3)!important;
border:0!important;
box-shadow:none!important;
}
html[data-unsloth-theme="dark"] body .u-mobile-nav-panel{
--u-dark-auto-background:var(--u-dark-surface-3);
color:var(--u-dark-text)!important;
background:var(--u-dark-surface-3)!important;
border:0!important;
box-shadow:none!important;
}
html[data-unsloth-theme="dark"] body .u-mobile-nav-panel a{color:#e8e8e8!important}
html[data-unsloth-theme="dark"] body .u-mobile-nav-panel a:hover{background:var(--u-dark-surface-3)!important}
html[data-unsloth-theme="dark"] body .u-footer,
html[data-unsloth-theme="dark"] body #unsloth-shared-footer,
html[data-unsloth-theme="dark"] body .unsloth-global-chrome{
color:var(--u-dark-text)!important;
background:var(--u-dark-surface-1)!important;
border:0!important;
box-shadow:none!important;
}
html[data-unsloth-theme="dark"] body .u-footer .u-logo,
html[data-unsloth-theme="dark"] body .u-footer .u-logo span,
html[data-unsloth-theme="dark"] body .u-footer-grid>div>h3{color:var(--u-dark-text)!important}
html[data-unsloth-theme="dark"] body .u-footer-intro p,
html[data-unsloth-theme="dark"] body .u-footer-links a{color:var(--u-dark-muted)!important}
html[data-unsloth-theme="dark"] body .u-footer-links a:hover{color:var(--u-dark-text)!important}
html[data-unsloth-theme="dark"] body .u-footer-bottom,
html[data-unsloth-theme="dark"] body .u-footer-bottom a{color:var(--u-dark-subtle)!important}
html[data-unsloth-theme="dark"] body table,
html[data-unsloth-theme="dark"] body thead,
html[data-unsloth-theme="dark"] body tbody,
html[data-unsloth-theme="dark"] body tr{background:var(--u-dark-surface-1)!important}
html[data-unsloth-theme="dark"] body th,
html[data-unsloth-theme="dark"] body td{
color:#e8e8e8!important;
background:var(--u-dark-surface-2)!important;
border:0!important;
}
html[data-unsloth-theme="dark"] body input,
html[data-unsloth-theme="dark"] body textarea,
html[data-unsloth-theme="dark"] body select{
color:var(--u-dark-text)!important;
background:var(--u-dark-surface-3)!important;
border:0!important;
box-shadow:none!important;
}
html[data-unsloth-theme="dark"] body input::placeholder,
html[data-unsloth-theme="dark"] body textarea::placeholder{color:var(--u-dark-subtle)!important}
html[data-unsloth-theme="dark"] body code,
html[data-unsloth-theme="dark"] body pre{
color:#dedede!important;
background:var(--u-dark-surface-2)!important;
border:0!important;
box-shadow:none!important;
}
html[data-unsloth-theme="dark"] body ::selection{color:#181818!important;background:#63ddb4!important}

.u-theme-switch{
display:inline-grid!important;
grid-template-columns:repeat(3,36px)!important;
gap:5px!important;
align-items:center!important;
width:auto!important;
height:44px!important;
padding:4px!important;
border:0!important;
border-radius:999px!important;
color:#3a3a3a!important;
background:#e8e8e8!important;
box-shadow:none!important;
}
.u-theme-option{
position:relative!important;
display:flex!important;
align-items:center!important;
justify-content:center!important;
width:36px!important;
height:36px!important;
padding:0!important;
border:0!important;
border-radius:999px!important;
color:inherit!important;
background:transparent!important;
box-shadow:none!important;
line-height:0!important;
cursor:pointer!important;
}
.u-theme-option:hover{color:#1f1f1f!important;background:#d9d9d9!important}
.u-theme-option[aria-checked="true"]{color:#1f1f1f!important;background:#fff!important}
.u-theme-option:focus-visible{outline:2px solid #35d6a4!important;outline-offset:2px!important}
.u-theme-option svg{
position:absolute!important;
top:50%!important;
left:50%!important;
width:17px!important;
height:17px!important;
margin:0!important;
transform:translate(-50%,-50%)!important;
fill:none!important;
stroke:currentColor!important;
stroke-width:1.8!important;
stroke-linecap:round!important;
stroke-linejoin:round!important;
}
html[data-unsloth-theme="dark"] body .u-theme-switch{
color:#a3a3a3!important;
background:var(--u-dark-surface-2)!important;
}
html[data-unsloth-theme="dark"] body .u-theme-option:hover{
color:#fff!important;
background:var(--u-dark-surface-3)!important;
}
html[data-unsloth-theme="dark"] body .u-theme-option[aria-checked="true"]{
color:#fff!important;
background:var(--u-dark-surface-4)!important;
}
.u-theme-switch-floating{
position:fixed!important;
top:18px!important;
right:18px!important;
z-index:9999!important;
}
footer .u-footer-intro,.u-footer .u-footer-intro,[role="contentinfo"] .u-footer-intro{
display:flex!important;
flex-direction:column!important;
align-items:flex-start!important;
gap:24px!important;
}
footer .u-logo,.u-footer .u-logo,[role="contentinfo"] .u-logo{gap:14px!important}
footer .u-logo img,.u-footer .u-logo img,[role="contentinfo"] .u-logo img,footer a[href="/"] img[alt*="unsloth" i]{
width:48px!important;
height:48px!important;
max-width:none!important;
}
footer .u-logo span,.u-footer .u-logo span,[role="contentinfo"] .u-logo span{font-size:32px!important;line-height:1!important}
footer .u-theme-switch-footer,.u-footer .u-theme-switch-footer,[role="contentinfo"] .u-theme-switch-footer{
margin:0!important;
align-self:flex-start!important;
}

html body img{border-radius:16px!important}
html body main img,
html body article img,
html body .u-news-thumb img,
html body .u-app-shot>img,
html body img.u-product-shot,
html body .u-feature .u-visual-field>img,
html body .u-hero-visual img{border-radius:20px!important}
html body .u-news-thumb,
html body .u-app-shot,
html body .u-product-shot{overflow:hidden!important}
html body .u-logo img,
html body .u-social-link img,
html body .u-footer-links img,
html body .u-download-icon img,
html body .u-current-os-icon img,
html body .unsloth-download-option-icon img{border-radius:0!important}

.u-current-os-direct[aria-label="Download for Linux"] .u-current-os-icon,
#unsloth-os-download-cta[aria-label="Download for Linux"] .unsloth-download-icon{
width:38px!important;
height:38px!important;
min-width:38px!important;
flex:0 0 38px!important;
display:inline-grid!important;
place-items:center!important;
}
.u-current-os-direct[aria-label="Download for Linux"] .u-current-os-icon img,
#unsloth-os-download-cta[aria-label="Download for Linux"] .unsloth-download-icon img{
display:block!important;
width:34px!important;
height:34px!important;
max-width:none!important;
object-fit:contain!important;
filter:brightness(0) invert(1)!important;
}
html[data-unsloth-theme="dark"] .u-current-os-direct[aria-label="Download for Linux"] .u-current-os-icon img,
html[data-unsloth-theme="dark"] #unsloth-os-download-cta[aria-label="Download for Linux"] .unsloth-download-icon img{filter:brightness(0)!important}
html[data-unsloth-theme="dark"] body .platform .linux-logo-crop img,
html[data-unsloth-theme="dark"] body [role="tab"] .linux-logo-crop img{filter:brightness(0) invert(1)!important}
html[data-unsloth-theme="dark"] body .u-nav,
html[data-unsloth-theme="dark"] body header.u-theme-auto-surface-1{
background-color:transparent!important;
background-image:none!important;
}
html[data-unsloth-theme="dark"] body header .u-social-link img,
html[data-unsloth-theme="dark"] body .u-nav-row .u-social-link img{filter:brightness(2.25)!important}
html[data-unsloth-theme="dark"] body .u-download-panel .u-download-option[href*="Ubuntu"] .u-download-icon{
position:relative!important;
overflow:visible!important;
display:grid!important;
place-items:center!important;
}
html[data-unsloth-theme="dark"] body .u-download-panel .u-download-option[href*="Ubuntu"] .u-download-icon>img{
position:absolute!important;
top:50%!important;
left:50%!important;
translate:-50% -50%!important;
scale:1.04!important;
transform-origin:center!important;
filter:brightness(0) saturate(100%) invert(66%) sepia(6%) saturate(300%) hue-rotate(100deg) brightness(90%) contrast(90%)!important;
}

@media(min-width:768px) and (max-width:991px){
html:not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity) body .u-nav-row{
width:calc(100% - 48px)!important;
max-width:1080px!important;
min-height:56px!important;
height:56px!important;
margin-left:auto!important;
margin-right:auto!important;
padding:7px 9px 7px 14px!important;
align-items:center!important;
gap:8px!important;
}
html:not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity) body :is(.u-mobile-nav,.u-mobile-nav>summary){
width:42px!important;
height:42px!important;
min-width:42px!important;
min-height:42px!important;
flex:0 0 42px!important;
margin:0!important;
}
}

@media(max-width:991px){
html:not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity) body .u-mobile-nav{
position:relative!important;
display:block!important;
}
html:not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity) body .u-mobile-nav>summary{
display:grid!important;
place-items:center!important;
padding:0!important;
border:0!important;
border-radius:999px!important;
color:#292929!important;
background:transparent!important;
box-shadow:none!important;
font-size:0!important;
line-height:0!important;
list-style:none!important;
cursor:pointer!important;
}
html[data-unsloth-theme="dark"]:not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity) body .u-mobile-nav>summary{
--u-dark-auto-background:var(--u-dark-surface-3)!important;
--u-dark-auto-color:#f7f7f7!important;
color:#f7f7f7!important;
background:transparent!important;
}
html:not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity) body .u-mobile-nav>summary::before{
content:""!important;
display:block!important;
width:21px!important;
height:15px!important;
margin:0!important;
border:0!important;
background:
linear-gradient(currentColor,currentColor) 0 0/100% 2px no-repeat,
linear-gradient(currentColor,currentColor) 0 50%/100% 2px no-repeat,
linear-gradient(currentColor,currentColor) 0 100%/100% 2px no-repeat!important;
box-shadow:none!important;
transform:none!important;
}
html:not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity) body .u-mobile-nav>summary::after{
content:none!important;
display:none!important;
}
html[data-unsloth-theme="dark"]:not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity) body .u-mobile-nav-panel{
--u-dark-auto-background:var(--u-dark-surface-3)!important;
color:var(--u-dark-text)!important;
background:var(--u-dark-surface-3)!important;
border:0!important;
box-shadow:none!important;
}
}

@media(prefers-color-scheme:dark){
html:not([data-unsloth-theme]) .u-current-os-direct[aria-label="Download for Linux"] .u-current-os-icon img,
html:not([data-unsloth-theme]) #unsloth-os-download-cta[aria-label="Download for Linux"] .unsloth-download-icon img{filter:brightness(0)!important}
}
@media(max-width:479px){
.u-theme-switch{grid-template-columns:repeat(3,34px)!important;gap:4px!important;height:42px!important}
.u-theme-option{width:34px!important;height:34px!important}
footer .u-logo img,.u-footer .u-logo img,[role="contentinfo"] .u-logo img,footer a[href="/"] img[alt*="unsloth" i]{width:44px!important;height:44px!important}
footer .u-logo span,.u-footer .u-logo span,[role="contentinfo"] .u-logo span{font-size:29px!important}
html body img{border-radius:14px!important}
html body main img,
html body article img,
html body .u-app-shot>img,
html body img.u-product-shot,
html body .u-feature .u-visual-field>img,
html body .u-hero-visual img{border-radius:18px!important}
html body .u-logo img,
html body .u-social-link img,
html body .u-footer-links img,
html body .u-download-icon img,
html body .u-current-os-icon img,
html body .unsloth-download-option-icon img{border-radius:0!important}
.u-current-os-direct[aria-label="Download for Linux"] .u-current-os-icon,
#unsloth-os-download-cta[aria-label="Download for Linux"] .unsloth-download-icon{
width:34px!important;
height:34px!important;
min-width:34px!important;
flex-basis:34px!important;
}
.u-current-os-direct[aria-label="Download for Linux"] .u-current-os-icon img,
#unsloth-os-download-cta[aria-label="Download for Linux"] .unsloth-download-icon img{width:30px!important;height:30px!important}
}
@media(print){.u-theme-switch{display:none!important}}

(function(){
var version='clean-system-switch-v7';
if(window.__unslothGlobalTheme2026&&window.__unslothGlobalTheme2026.version===version){
window.__unslothGlobalTheme2026.refresh();
return;
}
var storageKey='unsloth-theme';
var modeKey='unsloth-theme-mode';
var root=document.documentElement;
var media=window.matchMedia('(prefers-color-scheme: dark)');
var control=null;
var observer=null;
var scanQueued=false;
var autoClasses=['u-theme-auto-surface-1','u-theme-auto-surface-2','u-theme-auto-surface-accent','u-theme-auto-text','u-theme-auto-muted','u-theme-auto-accent-text','u-theme-auto-control'];

function storedMode(){
try{
var mode=window.localStorage.getItem(modeKey);
if(mode==='dark'||mode==='light'||mode==='system')return mode;
var legacy=window.localStorage.getItem(storageKey);
return legacy==='dark'||legacy==='light'?legacy:'system';
}catch(error){return 'system'}
}
function themeForMode(mode){return mode==='system'?(media.matches?'dark':'light'):mode}
function persistMode(mode){
try{
window.localStorage.setItem(modeKey,mode);
if(mode==='system')window.localStorage.removeItem(storageKey);
else window.localStorage.setItem(storageKey,mode);
}catch(error){}
}
function rgb(value){
var match=String(value||'').match(/rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)(?:\s*[,/]\s*([\d.]+))?\s*\)/i);
return match?{r:+match[1],g:+match[2],b:+match[3],a:match[4]===undefined?1:+match[4]}:null;
}
function luminance(color){
function channel(value){value/=255;return value .05&&style.backgroundImage==='none'){
var bgLum=luminance(background);
var bgSat=saturation(background);
if(bgLum>.9)element.classList.add('u-theme-auto-surface-1');
else if(bgLum>.62)element.classList.add(bgSat>.12?'u-theme-auto-surface-accent':'u-theme-auto-surface-2');
}
if(color&&color.a>.05){
var textLum=luminance(color);
var textSat=saturation(color);
if(textLum .3?'u-theme-auto-accent-text':'u-theme-auto-muted');
}
var interactive=/^(A|BUTTON|INPUT|TEXTAREA|SELECT|SUMMARY)$/.test(tag);
var hasBorder=['Top','Right','Bottom','Left'].some(function(side){
return parseFloat(style['border'+side+'Width'])>0&&style['border'+side+'Style']!=='none';
});
if(interactive&&(hasBorder||(background&&background.a>.05&&luminance(background)>.62&&saturation(background)                      ';
}
function ensureControl(){
if(!document.body)return false;
document.querySelectorAll('.u-theme-toggle').forEach(function(oldToggle){oldToggle.remove()});
var footer=document.querySelector('footer,.u-footer,[role="contentinfo"]');
var logo=footer&&(footer.querySelector('.u-footer-intro .u-logo')||footer.querySelector('.u-logo')||footer.querySelector('a[href="/"]'));
var host=(logo&&logo.parentElement)||footer||document.body;
control=document.querySelector('.u-theme-switch');
if(!control){
control=document.createElement('div');
control.className='u-theme-switch';
control.setAttribute('role','radiogroup');
control.setAttribute('aria-label','Theme preference');
control.innerHTML=controlMarkup();
}
if(control.getAttribute('data-unsloth-theme-control')!==version){
if(control.parentElement){
var cleanControl=control.cloneNode(true);
control.parentElement.replaceChild(cleanControl,control);
control=cleanControl;
}
control.setAttribute('data-unsloth-theme-control',version);
control.querySelectorAll('.u-theme-option').forEach(function(option){
option.addEventListener('click',function(){
var mode=option.getAttribute('data-theme-choice');
persistMode(mode);
applyMode(mode);
});
});
}
control.classList.toggle('u-theme-switch-footer',!!footer);
control.classList.toggle('u-theme-switch-floating',!footer);
if(footer&&logo){
if(control.parentElement!==host||control.previousElementSibling!==logo)host.insertBefore(control,logo.nextSibling);
}else if(control.parentElement!==host){host.appendChild(control)}
var mode=storedMode();
updateControl(mode,themeForMode(mode));
return true;
}
function refresh(){
applyMode(storedMode());
ensureControl();
scheduleScan();
}
function systemChange(){if(storedMode()==='system')applyMode('system')}
observer=new MutationObserver(function(){ensureControl();scheduleScan()});
observer.observe(root,{childList:true,subtree:true});
if(media.addEventListener)media.addEventListener('change',systemChange);
else if(media.addListener)media.addListener(systemChange);
var controller={
version:version,
refresh:refresh,
setMode:function(mode){persistMode(mode);applyMode(mode)},
getMode:storedMode
};
window.__unslothGlobalTheme2026=controller;
window.__unslothThemeController2026=controller;
applyMode(storedMode());
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',refresh,{once:true});
else refresh();
})();

(function(){
var BASE='#2c2c2c',ACTIVE='#3a3a3a',PANEL='#292929';
function paint(el,bg,border,shadow){if(!el)return;el.style.setProperty('background-color',bg,'important');el.style.setProperty('border',border||'0','important');el.style.setProperty('box-shadow',shadow||'none','important')}
function hover(el,base,active,selected){if(!el)return;el.__unslothBase=base;el.__unslothActive=active;el.__unslothSelected=selected;if(el.dataset.unslothContrastBound)return;el.dataset.unslothContrastBound='1';el.addEventListener('mouseenter',function(){this.style.setProperty('background-color',this.__unslothActive,'important')});el.addEventListener('mouseleave',function(){this.style.setProperty('background-color',this.__unslothSelected&&this.matches('[aria-selected=\"true\"],[aria-current=\"page\"]')?this.__unslothActive:this.__unslothBase,'important')})}
function apply(){
document.querySelectorAll('summary[aria-label=\"Choose another platform\"],.u-mobile-hero-download').forEach(function(el){paint(el,BASE,'0','0 1px 2px rgba(0,0,0,.24)');hover(el,BASE,ACTIVE,false)});
document.querySelectorAll('.u-download-panel').forEach(function(el){if(document.documentElement.getAttribute('data-unsloth-theme')==='light'){el.style.removeProperty('background-color');el.style.removeProperty('border');el.style.removeProperty('box-shadow')}else{paint(el,PANEL,'1px solid '+ACTIVE,'0 18px 44px rgba(0,0,0,.38)')}});
document.querySelectorAll('.u-cta').forEach(function(el){paint(el,PANEL,'0','0 16px 48px rgba(0,0,0,.22)')});
document.querySelectorAll('.download-main .platform').forEach(function(el){var selected=el.matches('[aria-selected=\"true\"],[aria-current=\"page\"]');paint(el,selected?ACTIVE:BASE,'0','none');hover(el,BASE,ACTIVE,true)});
document.querySelectorAll('.download-main .linux-download-options>a').forEach(function(el){paint(el,BASE,'0','none');hover(el,BASE,ACTIVE,false)});
}
function schedule(){if(window.__unslothContrastFrame)return;window.__unslothContrastFrame=requestAnimationFrame(function(){window.__unslothContrastFrame=0;apply()})}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',apply);else apply();
if(!window.__unslothContrastObserver){window.__unslothContrastObserver=new MutationObserver(schedule);window.__unslothContrastObserver.observe(document.documentElement,{subtree:true,childList:true,attributes:true,attributeFilter:['aria-selected','aria-current','open']})}
})();

(function(){
function clearBackground(el){
if(!el)return;
el.style.setProperty('background-color','transparent','important');
el.style.setProperty('background-image','none','important');
}
function apply(){
document.querySelectorAll('.u-cta h2,.u-download-panel .u-download-option,.u-news-item > .u-news-thumb,.u-news-item > .u-theme-auto-accent-text,.u-news-item .u-news-meta,.u-news-item h3').forEach(clearBackground);
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',apply);else apply();
if(!window.__unslothNestedSurfaceObserver){
window.__unslothNestedSurfaceObserver=new MutationObserver(function(){requestAnimationFrame(apply)});
window.__unslothNestedSurfaceObserver.observe(document.documentElement,{subtree:true,childList:true});
}
})();

@media (min-width:480px) and (max-width:991px){
html body .u-nav-row .u-mobile-nav>summary[aria-label="Open navigation"]{display:grid!important;place-items:center!important;place-content:center!important;align-self:center!important;justify-self:center!important;line-height:0!important;text-align:center!important;margin:auto!important}
html body .u-nav-row .u-mobile-nav>summary[aria-label="Open navigation"]::before{margin:auto!important;align-self:center!important;justify-self:center!important;position:static!important;inset:auto!important;transform:none!important}
}
html[data-unsloth-theme="dark"] body .u-nav-row .u-mobile-nav-socials .u-social-link img{filter:brightness(0) invert(1)!important;opacity:.82!important}
html[data-unsloth-theme="dark"] body .u-nav-row .u-mobile-nav-socials .u-social-link:hover img,
html[data-unsloth-theme="dark"] body .u-nav-row .u-mobile-nav-socials .u-social-link:focus-visible img{opacity:1!important}
#unsloth-shared-header{--u-green:#14b789!important;--u-green-soft:#dff8ef!important;--u-green-pale:#effbf7!important;--u-green-wash:#f6fcf9!important;--u-ink:#111411!important;--u-muted:#66706a!important;--u-paper:#f8faf8!important;--u-white:#ffffff!important;--u-soft:#f0f4f1!important;width:100%!important;color:var(--u-ink)!important;background:var(--u-paper)!important;font-family:Hellix,Inter,Arial,sans-serif!important;font-size:16px!important;font-weight:400!important;line-height:1.55!important;-webkit-font-smoothing:antialiased!important;text-rendering:optimizeLegibility!important}#unsloth-shared-header,#unsloth-shared-header *,#unsloth-shared-header *::before,#unsloth-shared-header *::after{box-sizing:border-box!important}#unsloth-shared-header *{animation:none!important;text-transform:none!important}#unsloth-shared-header .u-shell{width:min(1216px,calc(100% - 64px))!important;max-width:1216px!important;margin-inline:auto!important;padding-inline:0!important}#unsloth-shared-header .u-nav{position:sticky!important;inset:0 0 auto!important;z-index:100!important;height:92px!important;padding-top:18px!important;pointer-events:none!important;background:linear-gradient(180deg,rgba(248,250,248,.94),rgba(248,250,248,0))!important;border:0!important;box-shadow:none!important}#unsloth-shared-header .u-nav-row{width:min(1040px,100%)!important;min-height:60px!important;display:flex!important;align-items:center!important;justify-content:space-between!important;gap:28px!important;margin-inline:auto!important;padding:8px 10px 8px 18px!important;pointer-events:auto!important;border:0!important;border-radius:999px!important;background:rgba(255,255,255,.92)!important;box-shadow:0 16px 40px rgba(17,20,17,.07)!important;-webkit-backdrop-filter:blur(18px) saturate(120%)!important;backdrop-filter:blur(18px) saturate(120%)!important}#unsloth-shared-header .u-logo{display:inline-flex!important;align-items:center!important;gap:10px!important;flex:0 0 auto!important;color:var(--u-ink)!important;font-size:clamp(19px,2.4vw,24px)!important;font-weight:600!important;letter-spacing:-.035em!important}#unsloth-shared-header .u-logo img{width:36px!important;height:36px!important;object-fit:contain!important}#unsloth-shared-header .u-nav-links,#unsloth-shared-header .u-nav-socials{display:flex!important;align-items:center!important}#unsloth-shared-header .u-nav-links{gap:30px!important;margin-left:auto!important}#unsloth-shared-header .u-nav-links a{color:#343a36!important;font-size:14px!important;font-weight:500!important;letter-spacing:-.012em!important}#unsloth-shared-header .u-nav-links a:hover,#unsloth-shared-header .u-footer a:hover,#unsloth-shared-header .u-principle a:hover,#unsloth-shared-header .u-news-more:hover{opacity:.55!important}#unsloth-shared-header .u-nav-socials{gap:4px!important}#unsloth-shared-header .u-social-link{width:31px!important;height:31px!important;display:inline-grid!important;place-items:center!important;border:0!important;border-radius:50%!important;color:#3c443f!important;background:transparent!important;box-shadow:none!important;font-size:11px!important;font-weight:600!important}#unsloth-shared-header .u-social-link:hover{color:var(--u-ink)!important;background:var(--u-green-soft)!important}#unsloth-shared-header .u-mobile-nav{display:none!important}#unsloth-shared-header .u-btn,#unsloth-shared-header .u-newsletter-form button,#unsloth-shared-header .u-download summary,#unsloth-shared-header .u-nav-download{min-height:52px!important;display:inline-flex!important;align-items:center!important;justify-content:center!important;gap:9px!important;padding:15px 24px!important;border:0!important;border-radius:999px!important;box-shadow:none!important;cursor:pointer!important;font-size:14px!important;font-weight:600!important;line-height:1!important;letter-spacing:-.012em!important;text-align:center!important}#unsloth-shared-header .u-btn-primary,#unsloth-shared-header .u-newsletter-form button,#unsloth-shared-header .u-nav-download{color:#fff!important;background:#14b789!important}#unsloth-shared-header .u-btn-primary:hover,#unsloth-shared-header .u-newsletter-form button:hover,#unsloth-shared-header .u-nav-download:hover{background:#63cba9!important}#unsloth-shared-header .u-nav-download{min-height:40px!important;padding:10px 18px!important}@media (max-width:1100px){#unsloth-shared-header .u-shell{width:min(100% - 44px,1216px)!important}#unsloth-shared-header .u-nav-row{width:min(960px,100%)!important}#unsloth-shared-header .u-nav-links{gap:22px!important}#unsloth-shared-header .u-nav-socials{display:none!important}}@media (max-width:991px){#unsloth-shared-header .u-shell{width:min(100% - 36px,760px)!important}#unsloth-shared-header .u-nav{height:82px!important;padding-top:14px!important}#unsloth-shared-header .u-nav-row{min-height:56px!important;padding:7px 9px 7px 14px!important}#unsloth-shared-header .u-nav-links,#unsloth-shared-header .u-nav-socials,#unsloth-shared-header .u-nav-download{display:none!important}#unsloth-shared-header .u-mobile-nav{position:relative!important;display:block!important;margin-left:auto!important}#unsloth-shared-header .u-mobile-nav>summary{width:42px!important;height:42px!important;display:grid!important;place-items:center!important;padding:0!important;border:0!important;border-radius:50%!important;color:var(--u-ink)!important;background:var(--u-soft)!important;list-style:none!important}#unsloth-shared-header .u-mobile-nav>summary::-webkit-details-marker{display:none!important}#unsloth-shared-header .u-mobile-nav-panel{position:absolute!important;top:calc(100% + 12px)!important;right:0!important;width:min(340px,calc(100vw - 36px))!important;display:grid!important;padding:16px!important;border:0!important;border-radius:24px!important;background:#fff!important;box-shadow:0 24px 70px rgba(17,20,17,.16)!important}#unsloth-shared-header .u-mobile-nav-panel a{display:flex!important;align-items:center!important;min-height:48px!important;padding:0 15px!important;border:0!important;border-radius:14px!important;font-size:15px!important;font-weight:500!important}#unsloth-shared-header .u-mobile-nav-panel a:hover{background:var(--u-green-pale)!important}}@media (max-width:767px){#unsloth-shared-header .u-shell{width:calc(100% - 28px)!important}#unsloth-shared-header .u-logo{font-size:19px!important}#unsloth-shared-header .u-logo img{width:34px!important;height:34px!important}}@media (prefers-reduced-motion:reduce){#unsloth-shared-header *,#unsloth-shared-header *::before,#unsloth-shared-header *::after{scroll-behavior:auto!important;animation:none!important;transition:none!important}}@media (max-width:991px){#unsloth-shared-header .u-mobile-nav-panel{left:auto!important;right:0!important}}#unsloth-shared-header .u-social-link{width:24px!important;height:24px!important;display:grid!important;place-items:center!important}#unsloth-shared-header .u-social-link img{width:17px!important;height:17px!important}#unsloth-shared-header .u-nav-socials{gap:6px!important;transform:translateX(-10px)!important}#unsloth-shared-header .u-nav-socials a:nth-child(1) img{width:16px!important;height:16px!important;transform:none!important}#unsloth-shared-header .u-nav-socials a:nth-child(2) img{width:14px!important;height:14px!important}@media(max-width:991px){#unsloth-shared-header .u-nav-row{gap:8px!important}#unsloth-shared-header .u-nav-download{min-height:40px!important;display:inline-flex!important;margin-left:auto!important;padding:0 16px!important;font-size:13px!important}#unsloth-shared-header .u-mobile-nav{margin-left:0!important}}@media(max-width:479px){#unsloth-shared-header .u-nav-download{min-height:38px!important;padding:0 13px!important;font-size:12px!important}#unsloth-shared-header .u-logo{font-size:17px!important}}#unsloth-shared-header{--u-ink:#171717!important;--u-muted:#646864!important;--u-paper:#fafaf8!important;--u-soft:#f1f2f0!important;color:var(--u-ink)!important;background:var(--u-paper)!important}#unsloth-shared-header .u-nav{height:96px!important;padding-top:20px!important;background:linear-gradient(180deg,rgba(250,250,248,.96),rgba(250,250,248,0))!important}#unsloth-shared-header .u-nav-row{width:min(1080px,100%)!important;background:rgba(255,255,255,.94)!important;box-shadow:0 14px 42px rgba(0,0,0,.055)!important;backdrop-filter:blur(20px) saturate(115%)!important}#unsloth-shared-header .u-nav-download{color:#fff!important;background:#14b789!important;min-height:40px!important;padding:10px 18px!important}#unsloth-shared-header .u-nav-download:hover{color:#fff!important;background:#4fcaa7!important;opacity:1!important}#unsloth-shared-header .u-performance>.u-shell{padding:96px!important;overflow:hidden!important;border:0!important;border-radius:42px!important;color:#fff!important;background:#1b1b19!important;box-shadow:0 30px 88px rgba(0,0,0,.14)!important}@media(max-width:991px){#unsloth-shared-header .u-performance>.u-shell{padding:68px!important}}@media(max-width:767px){#unsloth-shared-header .u-nav{height:82px!important;padding-top:12px!important}#unsloth-shared-header .u-nav-row{min-height:56px!important;padding:7px 8px 7px 14px!important}#unsloth-shared-header .u-performance>.u-shell{padding:50px 26px!important;border-radius:30px!important}}#unsloth-shared-header .u-footer .u-logo,#unsloth-shared-header .u-footer .u-logo span{color:#171717!important}#unsloth-shared-header a{text-decoration:none!important}#unsloth-shared-footer a{text-decoration:none!important}.w-box:has(> .w-html-embed #unsloth-shared-footer > footer.u-footer)> :not(.w-html-embed){display:none!important}  .w-box:has(> .w-html-embed #unsloth-shared-header > header.u-nav)> .w-box{display:none!important}

[  unsloth ](/)
[Models](https://unsloth.ai/docs/models/tutorials)[Blog](/blog)[Unsloth Desktop✨](https://unsloth.ai/docs/desktop)[Docs](https://unsloth.ai/docs)
[Download](https://unsloth.ai/download)

[ ](https://discord.com/invite/unsloth)
[ ](https://x.com/unslothai)
[ ](https://github.com/unslothai/unsloth)
[ ](https://www.reddit.com/r/unsloth/)

☰
[Models](https://unsloth.ai/docs/models/tutorials)[Blog](/blog)[Unsloth Desktop](https://unsloth.ai/docs/desktop)[Documentation](https://unsloth.ai/docs)
[ ](https://discord.com/invite/unsloth)[ ](https://x.com/unslothai)[ ](https://github.com/unslothai/unsloth)[ ](https://www.reddit.com/r/unsloth/) [     Download ](https://unsloth.ai/download)

@media(max-width:991px){#unsloth-shared-header .u-nav{margin-inline:16px!important}}@media(max-width:767px){#unsloth-shared-header .u-nav{margin-inline:8px!important}}@media(max-width:479px){#unsloth-shared-header .u-nav{padding-top:8px!important}}  @media(max-width:479px){#unsloth-shared-header .u-nav-row{min-height:48px!important;padding:6px 6px 6px 12px!important;gap:6px!important}#unsloth-shared-header .u-logo{gap:5px!important}#unsloth-shared-header .u-logo img{width:30px!important;height:30px!important}#unsloth-shared-header .u-nav-download{min-height:36px!important;height:36px!important;padding:0 14px!important;font-size:11px!important;gap:6px!important}#unsloth-shared-header .u-mobile-nav>summary{width:36px!important;height:36px!important;font-size:0!important}}  #unsloth-shared-header .u-news-thumb{box-shadow:none!important}#unsloth-shared-header .u-download-icon,.unsloth-download-option-icon{position:relative!important;overflow:hidden!important;background:transparent!important;box-shadow:none!important}#unsloth-shared-header .u-current-os-icon>img,#unsloth-shared-header .u-download-icon>img,.unsloth-download-option-icon>img{position:absolute!important;top:50%!important;left:50%!important;width:168%!important;height:168%!important;max-width:none!important;transform:translate(-50%,-50%)!important}#unsloth-shared-header .u-hero .u-download>summary>span.u-current-os-menu:last-child{width:38px!important;margin-left:-2px!important;transform:translateX(-6px)!important}#unsloth-shared-header .u-hero .u-current-os-menu svg{width:20px!important;height:20px!important;max-width:none!important;flex:0 0 20px!important}#unsloth-shared-header .u-feature-links .u-btn.u-btn-secondary{background:#fff!important;box-shadow:0 7px 15px rgba(17,20,17,.10)!important}@media(min-width:768px){#unsloth-shared-header .u-hero .u-download>summary .u-current-os-icon svg{width:20px!important;height:20px!important;flex:0 0 20px!important}}@media(max-width:767px){#unsloth-shared-header .u-hero-actions{width:min(100%,430px)!important;display:grid!important;grid-template-columns:minmax(0,1fr) auto!important;align-items:center!important;gap:10px!important}#unsloth-shared-header .u-hero .u-download{width:100%!important;min-width:0!important}#unsloth-shared-header .u-hero .u-download>summary{width:100%!important;min-width:0!important;min-height:56px!important;padding:0 13px!important;gap:8px!important;font-size:16px!important}#unsloth-shared-header .u-current-os-icon{width:21px!important;height:21px!important;flex:0 0 21px!important}#unsloth-shared-header .u-current-os-label{white-space:nowrap!important}#unsloth-shared-header .u-hero .u-download>summary>span.u-current-os-menu:last-child{display:none!important}#unsloth-shared-header .u-btn-secondary{min-height:56px!important;padding:0 18px!important;white-space:nowrap!important;font-size:16px!important}#unsloth-shared-header .u-mobile-nav-extras{display:grid!important;gap:12px!important;margin-top:24px!important}#unsloth-shared-header .u-mobile-nav-panel .u-mobile-nav-socials{display:flex!important;align-items:center!important;justify-content:center!important;gap:14px!important;padding:0 20px!important}#unsloth-shared-header .u-mobile-nav-panel .u-mobile-nav-socials>a.u-social-link{width:30px!important;min-height:30px!important;display:grid!important;place-items:center!important;padding:0!important}#unsloth-shared-header .u-mobile-nav-panel .u-mobile-nav-socials>a:nth-child(2) img{width:15px!important;height:15px!important}#unsloth-shared-header .u-mobile-nav-panel .u-mobile-nav-extras>a.u-mobile-nav-download{width:calc(100% - 40px)!important;min-height:44px!important;justify-self:center!important;justify-content:center!important;gap:8px!important;padding:0 14px!important;border-radius:999px!important;color:#fff!important;background:#14b789!important;box-shadow:0 6px 12px rgba(17,20,17,.12)!important;font-size:15px!important}#unsloth-shared-header .u-mobile-nav-panel .u-mobile-nav-download>svg{width:16px!important;height:16px!important;flex:0 0 16px!important}}#unsloth-shared-header .u-footer-grid .u-footer-links a[href*="x.com"] img{width:15px!important;height:15px!important;flex:0 0 15px!important}#unsloth-shared-header .u-feature:nth-child(even) .u-feature-links .u-btn.u-btn-primary:hover{color:#fff!important}#unsloth-shared-header .u-nav .u-logo{gap:6px!important;font-size:clamp(19px,2.4vw,24px)!important;letter-spacing:0!important}#unsloth-shared-header .u-section.u-updates{padding-bottom:48px!important}
@media(min-width:768px) and (max-width:991px){html body #unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-nav{width:calc(100% - 32px)!important;margin-left:16px!important;margin-right:16px!important}}@media(max-width:767px){html body #unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-nav{width:calc(100% - 16px)!important;margin-left:8px!important;margin-right:8px!important}}
@media(max-width:479px){html body #unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-nav{padding-top:8px!important}html body #unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-nav-row{height:48px!important;min-height:48px!important;padding:6px 6px 6px 12px!important;gap:6px!important}html body #unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-nav .u-logo{font-size:17px!important;gap:5px!important}html body #unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-nav .u-logo>img{width:30px!important;height:30px!important;flex:0 0 30px!important}html body #unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-nav .u-nav-download{height:36px!important;min-height:36px!important;padding:0 14px!important;font-size:11px!important;gap:6px!important}html body #unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-mobile-nav,html body #unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-mobile-nav>summary{width:36px!important;height:36px!important;min-height:36px!important}html body #unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-btn,html body #unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-hero .u-download>summary{height:48px!important;min-height:48px!important;padding:0 18px!important;font-size:14px!important}html body #unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-mobile-nav-panel .u-mobile-nav-download{height:40px!important;min-height:40px!important;padding:0 12px!important;gap:7px!important}html body #unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-mobile-nav-panel .u-mobile-nav-download span{font-size:13px!important}html body #unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-mobile-nav-panel .u-mobile-nav-download>svg{width:15px!important;height:15px!important;flex:0 0 15px!important}}
@media(max-width:991px){
#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-mobile-nav-extras{display:grid!important;gap:12px!important;margin-top:24px!important}
#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-mobile-nav-panel .u-mobile-nav-socials{display:flex!important;align-items:center!important;justify-content:center!important;gap:14px!important;padding:0 20px!important}
#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-mobile-nav-panel .u-mobile-nav-socials>a.u-social-link{width:30px!important;height:30px!important;min-height:30px!important;display:grid!important;place-items:center!important;padding:0!important}
#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-mobile-nav-panel .u-mobile-nav-socials>a.u-social-link img{width:18px!important;height:18px!important;object-fit:contain!important}
#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-mobile-nav-panel .u-mobile-nav-socials>a:nth-child(2) img{width:14px!important;height:14px!important}
#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-mobile-nav-panel .u-mobile-nav-extras>a.u-mobile-nav-download{width:calc(100% - 40px)!important;min-height:44px!important;display:flex!important;align-items:center!important;justify-self:center!important;justify-content:center!important;gap:8px!important;padding:0 14px!important;border-radius:999px!important;color:#fff!important;background:#14b789!important;box-shadow:0 6px 12px rgba(17,20,17,.12)!important;font-size:0!important;line-height:0!important}
#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-mobile-nav-download span{font-size:14px!important;line-height:1.2!important}
#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-mobile-nav>summary{width:42px!important;height:42px!important;display:grid!important;place-items:center!important;padding:0!important;font-size:0!important;line-height:0!important;list-style:none!important}
#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-mobile-nav>summary::before{content:""!important;display:block!important;width:15px!important;height:11px!important;background:linear-gradient(#171717,#171717) top/15px 1.5px no-repeat,linear-gradient(#171717,#171717) center/15px 1.5px no-repeat,linear-gradient(#171717,#171717) bottom/15px 1.5px no-repeat!important;transform:translateY(-.5px)!important}
}
@media(max-width:479px){html body #unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-mobile-nav>summary[aria-label="Open navigation"]{display:grid!important;place-items:center!important;align-content:center!important;justify-content:center!important;padding:0!important;font-size:0!important;line-height:0!important}html body #unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-mobile-nav>summary[aria-label="Open navigation"]::before{content:""!important;display:block!important;position:static!important;width:15px!important;height:10px!important;margin:0!important;padding:0!important;justify-self:center!important;align-self:center!important;background-image:linear-gradient(#171b17,#171b17),linear-gradient(#171b17,#171b17),linear-gradient(#171b17,#171b17)!important;background-size:15px 1.5px,15px 1.5px,15px 1.5px!important;background-position:50% 0,50% 50%,50% 100%!important;background-repeat:no-repeat!important;transform:none!important}html body #unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header#unsloth-shared-header .u-mobile-nav>summary[aria-label="Open navigation"]::after{display:none!important;content:none!important}}

@media (max-width: 767px) {
#unsloth-shared-header .u-mobile-nav > summary[aria-label="Open navigation"]::before {
transform: scale(0.86) !important;
transform-origin: center !important;
}
}

#unsloth-shared-header {
background: transparent !important;
isolation: isolate !important;
z-index: 2147483647 !important;
}
.w-box:has(> .w-html-embed > #unsloth-shared-header) {
background: transparent !important;
overflow: visible !important;
z-index: 2147483647 !important;
}
#unsloth-shared-header .u-nav,
#unsloth-shared-header .u-mobile-nav,
#unsloth-shared-header .u-mobile-nav-panel {
z-index: 2147483647 !important;
}

html, body {
background: #ffffff !important;
}

html body #unsloth-shared-header#unsloth-shared-header {
background: transparent !important;
}
html body #unsloth-shared-header#unsloth-shared-header .u-nav {
background: transparent !important;
}

@media (max-width:991px){
#unsloth-shared-header .u-mobile-nav-panel,#unsloth-shared-header .u-mobile-nav-panel *{box-sizing:border-box!important}
#unsloth-shared-header .u-mobile-nav-panel nav>a,#unsloth-shared-header .u-mobile-nav-panel nav>a:link,#unsloth-shared-header .u-mobile-nav-panel nav>a:visited{color:#171717!important;background:transparent!important;text-decoration:none!important}
#unsloth-shared-header .u-mobile-nav-panel nav>a:hover,#unsloth-shared-header .u-mobile-nav-panel nav>a:focus-visible{color:#171717!important;background:#effbf7!important}
#unsloth-shared-header .u-mobile-nav-panel .u-mobile-nav-extras{display:grid!important;gap:12px!important;margin-top:10px!important}
#unsloth-shared-header .u-mobile-nav-panel .u-mobile-nav-socials{display:flex!important;align-items:center!important;justify-content:center!important;gap:10px!important}
#unsloth-shared-header .u-mobile-nav-panel .u-mobile-nav-socials>a.u-social-link{flex:0 0 36px!important;width:36px!important;height:36px!important;min-height:36px!important;max-height:36px!important;padding:0!important;border-radius:50%!important;color:#171717!important;background:transparent!important}
#unsloth-shared-header .u-mobile-nav-panel .u-mobile-nav-socials>a.u-social-link:hover{background:#effbf7!important}
#unsloth-shared-header .u-mobile-nav-panel .u-mobile-nav-socials img{display:block!important;width:18px!important;height:18px!important;max-width:18px!important;max-height:18px!important;object-fit:contain!important}
#unsloth-shared-header .u-mobile-nav-panel a.u-mobile-nav-download,#unsloth-shared-header .u-mobile-nav-panel a.u-mobile-nav-download:link,#unsloth-shared-header .u-mobile-nav-panel a.u-mobile-nav-download:visited{display:inline-flex!important;align-items:center!important;justify-content:center!important;width:100%!important;height:52px!important;min-height:52px!important;max-height:52px!important;padding:0 20px!important;gap:10px!important;border:0!important;border-radius:999px!important;color:#fff!important;background:#14b789!important;box-shadow:none!important;font-size:15px!important;font-weight:600!important;line-height:1!important;text-decoration:none!important}
#unsloth-shared-header .u-mobile-nav-panel a.u-mobile-nav-download:hover,#unsloth-shared-header .u-mobile-nav-panel a.u-mobile-nav-download:focus-visible{color:#fff!important;background:#4fcaa7!important}
#unsloth-shared-header .u-mobile-nav-panel a.u-mobile-nav-download>svg{display:block!important;flex:0 0 20px!important;width:20px!important;height:20px!important;min-width:20px!important;min-height:20px!important;max-width:20px!important;max-height:20px!important;margin:0!important;transform:none!important}
#unsloth-shared-header .u-mobile-nav-panel a.u-mobile-nav-download>span{display:inline!important;width:auto!important;height:auto!important;margin:0!important;color:#fff!important}
}
[Blog](/blog)
# How to Make LLM Training Faster with Unsloth and NVIDIA

## May 6, 2026

## May 6, 2026
Authors:  Daniel, Michael, Mathew and Datta, with help from NVIDIA   We collabed with NVIDIA to make LLM training ~25% faster and in this blog/guide we'll breakdown exactly how we did it. These optimizations have no loss in accuracy and are an extra addition on top of Unsloth’s already 2-5x faster speedup! The new algorithms are auto enabled on RTX laptops, data center GPUs and DGX Spark machines, so just update Unsloth to get the latest improvements. By working with NVIDIA, we show how:

Caching packed sequence metadata makes training 14.3% faster.

- Using double buffered async gradient checkpointing gives a 8% speedup.

- gpt-oss training is 15% faster by using argsort and bincount during MoE routing.

## 1. Caching Packed-Sequence Metadata

Suppose we have several short examples:

Instead of padding all of them to the same length and wasting compute on padding tokens, we concatenate them into one longer packed sequence:

The model still needs to know where each original sequence starts and ends. So, alongside the packed tokens, we carry sequence metadata such as:

- sequence lengths

- cumulative sequence offsets (`cu_seqlens`)

- the maximum sequence length

- attention structure derived from the three items above

This is the key point: for a fixed packed batch, that metadata is the same for every layer.

If we write the boundary information for a packed batch as:

B  = { lengths, cu_seqlens, max_seqlen, mask structure }

then every transformer layer in that forward pass consumes the same  B .

If the model has  L  layers, rebuilding or re-synchronizing on  B  once per layer is not new work. It is the same information being reconstructed again and again.

In other words, the useful work is:

build  B  once, use it  L  times.

The wasteful version is:

build  B  + build  B  + ⋯ + build  B      ( L  times)

The overhead here is not primarily extra FLOPs. Some of these paths can force device-to-host synchronization, effectively creating a GPU-CPU sync point. Once that happens inside a per-layer path, the overhead recurs at every layer.

That is what the packed-sequence caching change reduces. Instead of repeatedly reconstructing packed sequence info, SDPA packed masks, and xFormers block masks, it caches the reusable metadata and the attention-side structures derived from it, per device, for the current packed batch. Those cached structures are then reused across layers.

### Why this helps

Packed training already improves utilization by eliminating padding waste. But if the metadata path keeps forcing synchronization, some of that gain is lost to overhead that has nothing to do with the model's actual learning.

Caching helps because it removes repeated coordination work from the hot path. The forward pass benefits the most because that is where the same packed metadata is consumed repeatedly across many layers.

### Benchmarks

On `Qwen3-14B QLoRA SFT`:

- forward: `+43.3%`

- backward: `+5.8%`

- per batch: `+14.3%`

The forward pass sees the biggest benefit because repeated metadata and mask preparation show up most directly there. Backward also improves, but the effect is smaller. The time saved is similar, but the backward pass, especially with gradient checkpointing, takes longer, so the relative gains appear smaller.

Now that we know the measured gain, we can ask a simpler question: does that scale make sense?

### A quick sanity check

If we assume each layer is roughly similar, we can model the packed-attention path as:

T_uncached  ≈  L  · ( A  +  s )

where:

-  L  is the number of layers,

-  A  is the useful attention-side work per layer,

-  s  is the repeated metadata and mask-preparation overhead per layer.

With caching, that repeated overhead is paid once for the batch instead of once per layer:

T_cached    ≈  L  ·  A  +  s

So the saved time is approximately:

T_saved     ≈ ( L  − 1) ·  s

For the packed `SDPA` path, our microbenchmark on NVIDIA Blackwell GPUs showed that the low-level, host-visible metadata calls were real but small, at about `0.2 ms` each. The dominant repeated cost was the packed `SDPA` mask-construction path itself, which measured about `13.7 ms` for a synthetic packed batch with `2048` total packed tokens.

For the `SDPA` backend, a better mental model is:

small stream fence  +  mask rebuild   ≈   mask rebuild

That lets us do a cleaner consistency check. If one packed-mask rebuild costs `m` milliseconds, then under a uniform-layer model:

T_saved  ≈ ( L  − 1) ·  m

With  m  ≈ 13.7 ms, that predicts:

- `16` layers: `(16 - 1) x 13.7 ≈ 206 ms`

- `28` layers: `(28 - 1) x 13.7 ≈ 370 ms`

Smaller packed-sequence runs showed the same pattern:

- `Llama-3.2-1B`, `16` layers: about `199 ms` saved per step, which is about `11.5%` lower end-to-end step time

- `Qwen3-0.6B`, `28` layers: about `319 ms` saved per step, which is about `14.8%` lower end-to-end step time

Those percentages are relative to full training step time, so they still include work outside the packed-attention path, such as embeddings, the MLP, the LM head, the loss, and framework overhead. This estimate is intentionally only about the packed-attention side of the block, not the whole transformer layer. It is there only to check that the measured gains are in the right range for the packed `SDPA` path.

## 2. Hiding Latency With Double-Buffered Checkpoint Reloads

Activation checkpointing is a standard technique for training large models. The idea is to save memory by not keeping every intermediate activation alive through the backward pass. In exchange, we pay for some extra work during backward.

That trade-off is usually worth it, especially for larger models.

But it raises another systems question: if an activation has been offloaded, how does it get back to the GPU for backward?

In Unsloth's smart checkpointing path, activations can be staged in pinned CPU memory and copied back when needed. That saves VRAM, but it can introduce a bottleneck:

- Copy the activation from CPU to GPU.

- Wait for the copy to complete.

- Run backward compute on that activation.

- Start the next copy.

That is a serialization pattern. If one buffer is reused for both copy and compute, the copy stream and the compute stream keep taking turns.

Let  T_copy  be the activation reload time and  T_compute  be the backward compute time for the current layer.

With a single buffer, this part of the step is roughly limited by:

T_single  ≈  T_copy  +  T_compute

That is the serialized case. We pay for both almost entirely, one after the other.

A cleaner way to handle this is to use two buffers.

While the backward pass is running on buffer  A , the copy stream can preload the next activation into buffer  B . Then the roles swap. That creates pipeline overlap, though not perfect overlap.

Double buffering does not reduce the amount of math. It hides copy latency behind useful compute.

### Why this helps

This kind of optimization tends to get stronger once the model is large enough that backward compute is substantial, but not so dominant that all copy overhead disappears into noise. For larger models, higher hidden dimensions mean more data movement, so hiding that movement has a larger impact. Larger models also tend to have more layers, which creates more opportunities to hide copies behind computation.

That is why larger dense models are a good fit for this improvement. The GPU has enough real work going on that the copy can overlap with it, and the extra VRAM needed for the second buffer stays modest.

The implementation also keeps practical guardrails in place:

- use extra buffers only when enough VRAM is available

- fall back cleanly when the memory budget is tight

- keep correctness unchanged

### Benchmarks

On the larger dense-model runs, benchmarked with NVIDIA B200 Blackwell GPUs:

- `8B`: `0.3739 -> 0.4053 steps/s`, `+8.40%`

- `14B`: `0.2245 -> 0.2395 steps/s`, `+6.70%`

- `32B`: `0.1979 -> 0.2070 steps/s`, `+4.61%`

Memory overhead stayed modest:

- `+0.37 GB` at `8B`

- `+0.47 GB` at `14B`

- `+0.23 GB` at `32B`

In these runs, final losses were effectively unchanged.

The speedup is consistent across larger dense models, and the extra VRAM cost stays relatively small.

Once we know the measured gain, the natural follow-up is: does the scale make sense?

### A quick sanity check

If we assume there are  L  checkpointed layers and each layer is roughly similar:

- each reload takes time  c

- each backward compute chunk takes time  g

This also scales with batch size, sequence length, and other factors that affect data movement and computation. We omit those terms for brevity.

With one buffer:

T_single  ≈  L  · ( c  +  g )

With two buffers, the first layer still has to wait for its activation to arrive, and the last layer still has to finish computing. So a better approximation is:

T_double  ≈  c  + ( L  − 1) ·  max ( c ,  g ) +  g

So the saved time is approximately:

T_saved   ≈ ( L  − 1) ·  min ( c ,  g )

This is the useful reading of the result:

- the first copy is still exposed

- the last compute is still exposed

- but for the middle of the pipeline, copy and compute can overlap

If the overlap is good, the  per-layer  cost in the middle gets much closer to:

T_middle  ≈  max ( T_copy ,  T_compute )

From the measured larger-model results, the saved time per training step is roughly:

- `8B`: about `207 ms`

- `14B`: about `279 ms`

- `32B`: about `222 ms`

These host buffers are pinned allocations, so the relevant bandwidth is measured pinned-memory host-to-device bandwidth, not pageable-memory bandwidth. On our NVIDIA B200 Blackwell-based system, that bandwidth was about `55.7 GB/s`, with `64 GB/s` as a useful PCIe ceiling for comparison.

If we use the extra buffer size as a rough proxy for one activation reload, then each reload is naturally on the order of only a few milliseconds:

- `8B`, `0.37 GB`: about `6.6 ms` at `55.7 GB/s`, or `5.8 ms` at the `64 GB/s` ceiling

- `14B`, `0.47 GB`: about `8.4 ms` at `55.7 GB/s`, or `7.3 ms` at the `64 GB/s` ceiling

- `32B`, `0.23 GB`: about `4.1 ms` at `55.7 GB/s`, or `3.6 ms` at the `64 GB/s` ceiling

To explain the observed saved time per step, we would need to hide roughly a few dozen such reloads:

- `8B`: about `31` reloads at `55.7 GB/s`, or `36` at `64 GB/s`

- `14B`: about `33` reloads at `55.7 GB/s`, or `38` at `64 GB/s`

- `32B`: about `54` reloads at `55.7 GB/s`, or `62` at `64 GB/s`

Hiding one such reload across a few dozen checkpointed layers lands in the few-hundred-millisecond range of saved step time, which is exactly the scale we observed.

Again, that saved time is part of the full end-to-end training step. It is not supposed to explain embeddings, the LM head, the loss, optimizer work, or every other non-checkpointed part of the step. The point is only that the communication we can hide is large enough to plausibly account for the measured step-time gains.

## 3. A Smaller but Useful MoE Optimization

The third change is more specialized, but it shows the same pattern in MoE routing.

In the PyTorch-based GPT-OSS MoE path we examined, one expensive part of routing is figuring out which tokens go to which expert. A naive implementation can do something like:

`for expert_idx in range(num_experts):
token_idx, _ = torch.where(router_indices == expert_idx)
`
At first glance, this looks harmless. But `torch.where` is data-dependent here: the number of tokens routed to each expert changes from batch to batch. This can introduce CPU-GPU synchronization or related runtime overhead because output sizes depend on the routing pattern. If this happens once per expert, the number of dynamic queries scales with `num_experts`.

The better approach is to group everything once:

- Flatten all expert assignments.

- Stable-sort by expert ID.

- Use `bincount` once to get tokens per expert.

- Build offsets from those counts.

- Slice the grouped token list per expert.

Mathematically, the gain is not that we changed the routing logic. We changed how often we asked the runtime to answer a dynamic indexing question.

Instead of roughly:

dynamic-query overhead   ∝   num_experts

because we do one dynamic query per expert, we move much closer to:

dynamic-query overhead   ∝  1

plus cheap bookkeeping after that.

This is the same theme in a more specialized setting: group once, then reuse offsets instead of repeatedly asking for dynamic token lists.

### Benchmarks

Note that these optimizations apply to any MoE using the `native_torch` backend.

For this GPT-OSS-specific routing improvement:

- team validation showed roughly `10-15%` speedups on GPT-OSS configurations

- in the targeted routing path, we saw `+23%` forward and `+13%` backward

## What These Changes Have in Common

Even though these three optimizations live in different parts of the stack, they are solving the same problem.

The key optimization opportunities were in the glue code around the main kernels:

- rebuilding metadata that already exists

- synchronizing on information we could have cached

- letting copies and compute serialize instead of overlap

This is also why the improvements compose conceptually. As the main kernels get faster, overhead that used to be invisible starts becoming a meaningful fraction of the total step time.

There is a useful engineering lesson here. Once the math kernels are optimized, "faster" often means one of two things:

- do less unnecessary work

- make the unavoidable work happen in parallel

That is exactly what happened here.

## TL;DR

Optimization
Main bottleneck removed
Measured gain

Packed-sequence metadata caching  [(PR link)](https://github.com/unslothai/unsloth/pull/4243)
Repeated metadata reconstruction and synchronization across layers
Qwen3-14B QLoRA SFT: +43.3% forward, +5.8% backward, +14.3% per batch

Double-buffered checkpoint reload  [(PR link)](https://github.com/unslothai/unsloth-zoo/pull/534)
Copy and backward compute serialized on one buffer
+8.4% on 8B, +6.7% on 14B, +4.6% on 32B

GPT-OSS MoE routing with `bincount`  [(PR link)](https://github.com/unslothai/unsloth-zoo/pull/535)
Repeated synchronization from per-expert dynamic indexing
~10-15% in team validation, targeted-path +23% forward and +13% backward

💕 Thank you!   A huge thank you to NVIDIA for assisting us with open-source efforts to help the community and for helping us with this article. Also thank you for reading and using Unsloth - we appreciate it. 🙏

As always, be sure to join our [Reddit page](https://www.reddit.com/r/unsloth/) and [Discord](https://discord.gg/unsloth) server for help or just to show your support! You can also follow us on [Twitter](https://twitter.com/unslothai) and our newsletter on: [Substack](https://unslothai.substack.com/).   Thank you for reading!    Daniel & Michael Han  🦥
May 6, 2026
##  Train + Run LLMs with a UI
[Get started for free](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide)           img[src*="cdn.simpleicons.org/reddit/"]{width:16px!important;height:16px!important;max-width:16px!important;max-height:16px!important;display:inline-block!important;flex:0 0 16px!important;object-fit:contain!important}  #unsloth-shared-footer{--u-green:#14b789!important;--u-green-soft:#dff8ef!important;--u-green-pale:#effbf7!important;--u-green-wash:#f6fcf9!important;--u-ink:#111411!important;--u-muted:#66706a!important;--u-paper:#f8faf8!important;--u-white:#ffffff!important;--u-soft:#f0f4f1!important;width:100%!important;color:var(--u-ink)!important;background:var(--u-paper)!important;font-family:Hellix,Inter,Arial,sans-serif!important;font-size:16px!important;font-weight:400!important;line-height:1.55!important;-webkit-font-smoothing:antialiased!important;text-rendering:optimizeLegibility!important}#unsloth-shared-footer,#unsloth-shared-footer *,#unsloth-shared-footer *::before,#unsloth-shared-footer *::after{box-sizing:border-box!important}#unsloth-shared-footer *{animation:none!important;text-transform:none!important}#unsloth-shared-footer .u-shell{width:min(1216px,calc(100% - 64px))!important;max-width:1216px!important;margin-inline:auto!important;padding-inline:0!important}#unsloth-shared-footer .u-logo{display:inline-flex!important;align-items:center!important;gap:10px!important;flex:0 0 auto!important;color:var(--u-ink)!important;font-size:20px!important;font-weight:600!important;letter-spacing:-.035em!important}#unsloth-shared-footer .u-logo img{width:36px!important;height:36px!important;object-fit:contain!important}#unsloth-shared-footer .u-nav-links a:hover,#unsloth-shared-footer .u-footer a:hover,#unsloth-shared-footer .u-principle a:hover,#unsloth-shared-footer .u-news-more:hover{opacity:.55!important}#unsloth-shared-footer .u-footer{padding:92px 0 38px!important;color:var(--u-ink)!important;background:#fff!important;border:0!important}#unsloth-shared-footer .u-footer-grid{display:grid!important;grid-template-columns:1.18fr 2fr!important;align-items:start!important;gap:110px!important}#unsloth-shared-footer .u-footer-intro p{margin-top:28px!important;color:var(--u-muted)!important;font-size:14px!important}#unsloth-shared-footer .u-footer-links{display:grid!important;grid-template-columns:repeat(3,minmax(0,1fr))!important;gap:54px!important}#unsloth-shared-footer .u-footer-links h3{margin-bottom:24px!important;font-size:14px!important;font-weight:600!important;letter-spacing:-.02em!important}#unsloth-shared-footer .u-footer-links a{display:block!important;width:fit-content!important;margin-top:14px!important;color:var(--u-muted)!important;font-size:14px!important}#unsloth-shared-footer .u-footer-bottom{display:flex!important;align-items:center!important;justify-content:space-between!important;gap:24px!important;margin-top:94px!important;padding-top:0!important;border:0!important;color:#858e88!important;font-size:13px!important}@media (max-width:1100px){#unsloth-shared-footer .u-shell{width:min(100% - 44px,1216px)!important}}@media (max-width:991px){#unsloth-shared-footer .u-shell{width:min(100% - 36px,760px)!important}#unsloth-shared-footer .u-footer-grid{grid-template-columns:1fr!important;gap:64px!important}}@media (max-width:767px){#unsloth-shared-footer .u-shell{width:calc(100% - 28px)!important}#unsloth-shared-footer .u-logo{font-size:18px!important}#unsloth-shared-footer .u-logo img{width:34px!important;height:34px!important}#unsloth-shared-footer .u-footer{padding-top:72px!important}#unsloth-shared-footer .u-footer-links{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:44px 28px!important}#unsloth-shared-footer .u-footer-bottom{align-items:flex-start!important;flex-direction:column!important;margin-top:70px!important}}@media (max-width:479px){#unsloth-shared-footer .u-footer-links{grid-template-columns:1fr 1fr!important}}@media (prefers-reduced-motion:reduce){#unsloth-shared-footer *,#unsloth-shared-footer *::before,#unsloth-shared-footer *::after{scroll-behavior:auto!important;animation:none!important;transition:none!important}}#unsloth-shared-footer .u-footer-links img{width:18px!important;height:18px!important}#unsloth-shared-footer{--u-ink:#171717!important;--u-muted:#646864!important;--u-paper:#fafaf8!important;--u-soft:#f1f2f0!important;color:var(--u-ink)!important;background:var(--u-paper)!important}#unsloth-shared-footer .u-performance>.u-shell{padding:96px!important;overflow:hidden!important;border:0!important;border-radius:42px!important;color:#fff!important;background:#1b1b19!important;box-shadow:0 30px 88px rgba(0,0,0,.14)!important}#unsloth-shared-footer .u-footer{padding:98px 0 40px!important}@media(max-width:991px){#unsloth-shared-footer .u-performance>.u-shell{padding:68px!important}}@media(max-width:767px){#unsloth-shared-footer .u-performance>.u-shell{padding:50px 26px!important;border-radius:30px!important}}#unsloth-shared-footer .u-footer{padding:112px 0 44px!important;color:#171717!important;background:#fff!important}#unsloth-shared-footer .u-footer-grid{display:grid!important;grid-template-columns:minmax(240px,1.35fr) repeat(3,minmax(0,1fr))!important;align-items:start!important;gap:clamp(48px,5vw,84px)!important}#unsloth-shared-footer .u-footer-grid>div{min-width:0!important}#unsloth-shared-footer .u-footer .u-logo,#unsloth-shared-footer .u-footer .u-logo span{color:#171717!important}#unsloth-shared-footer .u-footer-intro p{margin-top:30px!important;color:#646864!important;font-size:15px!important}#unsloth-shared-footer .u-footer-intro p a{color:inherit!important}#unsloth-shared-footer .u-footer-grid>div>h3{display:block!important;margin:0 0 28px!important;color:#171717!important;font-size:15px!important;font-weight:600!important;line-height:1.2!important;letter-spacing:-.02em!important}#unsloth-shared-footer .u-footer-grid>div>.u-footer-links{width:100%!important;height:auto!important;display:grid!important;grid-template-columns:1fr!important;gap:16px!important;padding:0!important}#unsloth-shared-footer .u-footer-grid>div>.u-footer-links a{width:fit-content!important;display:inline-flex!important;align-items:center!important;gap:10px!important;margin:0!important;color:#646864!important;font-size:15px!important;line-height:1.5!important}#unsloth-shared-footer .u-footer-grid>div>.u-footer-links a img{display:block!important}#unsloth-shared-footer .u-footer-bottom{margin-top:92px!important;padding-top:0!important;color:#858a86!important}#unsloth-shared-footer .u-footer-bottom a{color:inherit!important}@media(max-width:767px){#unsloth-shared-footer .u-footer{padding:78px 0 34px!important}#unsloth-shared-footer .u-footer-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:48px 30px!important}#unsloth-shared-footer .u-footer-intro{grid-column:1/-1!important}#unsloth-shared-footer .u-footer-grid>div>h3{margin-bottom:22px!important}#unsloth-shared-footer .u-footer-grid>div>.u-footer-links{gap:14px!important}#unsloth-shared-footer .u-footer-bottom{margin-top:68px!important}}@media(max-width:479px){#unsloth-shared-footer .u-footer-grid{gap:42px 22px!important}#unsloth-shared-footer .u-footer-bottom{align-items:flex-start!important;flex-direction:column!important}}#unsloth-shared-footer a{text-decoration:none!important}  .w-box:has(> .w-html-embed #unsloth-shared-footer > footer.u-footer)> .w-box{display:none!important}      [  unsloth ](/)
[ [email protected] ](/cdn-cgi/l/email-protection#9feceaefeff0edebdfeaf1ecf3f0ebf7b1fef6)

### Product
[Unsloth Desktop](https://unsloth.ai/docs/desktop)[Models](https://unsloth.ai/docs/models/tutorials)[Documentation](https://unsloth.ai/docs)[Download](https://github.com/unslothai/unsloth/releases/tag/v0.1.801-beta)
### Company
[About](/about)[Blog](/blog)[Newsletter](/newsletter)[Support](https://www.reddit.com/r/unsloth/)
### Community
[ GitHub](https://github.com/unslothai/unsloth)[ Discord](https://discord.com/invite/unsloth)[   LinkedIn](https://www.linkedin.com/company/unsloth)[ X / Twitter](https://x.com/unslothai)[ Reddit](https://www.reddit.com/r/unsloth/)     © 2026 Unsloth. All rights reserved.      #unsloth-shared-footer .u-footer-intro>p:has(a[href="mailto:support@unsloth.ai"]){display:none!important}    (()=>{const root=document.querySelector("#unsloth-shared-footer");root?.querySelectorAll('.u-footer-intro a[href="mailto:support@unsloth.ai"]').forEach(link=>{const paragraph=link.closest("p");if(paragraph&¶graph.parentElement?.classList.contains("u-footer-intro"))paragraph.remove();else link.remove()})})()       [

Join Our Discord ](https://discord.com/invite/unsloth)
(function(){
var mode='system';
try{
var saved=window.localStorage.getItem('unsloth-theme-mode');
var legacy=window.localStorage.getItem('unsloth-theme');
if(saved==='dark'||saved==='light'||saved==='system')mode=saved;
else if(legacy==='dark'||legacy==='light')mode=legacy;
}catch(error){}
var dark=window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches;
var theme=mode==='system'?(dark?'dark':'light'):mode;
document.documentElement.setAttribute('data-unsloth-theme-mode',mode);
document.documentElement.setAttribute('data-unsloth-theme',theme);
})();

:root{color-scheme:light}
html[data-unsloth-theme="light"]{color-scheme:light}
html[data-unsloth-theme="dark"]{
color-scheme:dark;
--u-dark-canvas:#181818;
--u-dark-surface-1:#1f1f1f;
--u-dark-surface-2:#292929;
--u-dark-surface-3:#2c2c2c;
--u-dark-surface-4:#3a3a3a;
--u-dark-accent-surface:#2c2c2c;
--u-dark-text:#f5f5f5;
--u-dark-muted:#b4b4b4;
--u-dark-subtle:#8e8e8e;
--u-dark-accent:#6ce0b8;
--u-dark-accent-strong:#43d3a3;
background:#181818!important;
}
html[data-unsloth-theme="dark"] body{
color:var(--u-dark-text)!important;
background:var(--u-dark-canvas)!important;
}
html[data-unsloth-theme="dark"] body *,
html[data-unsloth-theme="dark"] body *::before,
html[data-unsloth-theme="dark"] body *::after{
border-color:transparent!important;
box-shadow:none!important;
text-shadow:none!important;
}
html[data-unsloth-theme="dark"] body .u-theme-auto-surface-1{
--u-dark-auto-background:var(--u-dark-surface-1);
--u-dark-auto-background-image:none;
background-color:var(--u-dark-surface-1)!important;
background-image:none!important;
}
html[data-unsloth-theme="dark"] body .u-theme-auto-surface-2{
--u-dark-auto-background:var(--u-dark-surface-2);
--u-dark-auto-background-image:none;
background-color:var(--u-dark-surface-2)!important;
background-image:none!important;
}
html[data-unsloth-theme="dark"] body .u-theme-auto-surface-accent{
--u-dark-auto-background:var(--u-dark-accent-surface);
--u-dark-auto-background-image:none;
background-color:var(--u-dark-accent-surface)!important;
background-image:none!important;
}
html[data-unsloth-theme="dark"] body .u-theme-auto-text{--u-dark-auto-color:var(--u-dark-text);color:var(--u-dark-text)!important}
html[data-unsloth-theme="dark"] body .u-theme-auto-muted{--u-dark-auto-color:var(--u-dark-muted);color:var(--u-dark-muted)!important}
html[data-unsloth-theme="dark"] body .u-theme-auto-accent-text{--u-dark-auto-color:var(--u-dark-accent);color:var(--u-dark-accent)!important}
html[data-unsloth-theme="dark"] body .u-theme-auto-control{
--u-dark-auto-background:var(--u-dark-surface-3);
--u-dark-auto-color:var(--u-dark-text);
color:var(--u-dark-text)!important;
background-color:var(--u-dark-surface-3)!important;
border:0!important;
box-shadow:none!important;
}
html[data-unsloth-theme="dark"] body .u-theme-auto-control:hover{
color:#fff!important;
background-color:var(--u-dark-surface-4)!important;
}
html[data-unsloth-theme="dark"]:not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity){
background-color:#181818!important;
}
html[data-unsloth-theme="dark"]:not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity) body{
color:#f5f5f5!important;
background-color:#181818!important;
}
html[data-unsloth-theme="dark"]:not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity) body *,
html[data-unsloth-theme="dark"]:not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity) body *::before,
html[data-unsloth-theme="dark"]:not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity) body *::after{
border-color:transparent!important;
box-shadow:none!important;
text-shadow:none!important;
}
html[data-unsloth-theme="dark"]:not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity):not(#unsloth-theme-specificity) body :is(.u-theme-auto-surface-1,.u-theme-auto-surface-2,.u-theme-auto-surface-accent,.u-theme-auto-text,.u-theme-auto-muted,.u-theme-auto-accent-text,.u-theme-auto-control){
color:var(--u-dark-auto-color)!important;
background-color:var(--u-dark-auto-background)!important;
background-image:var(--u-dark-auto-background-image)!important;
}
html[data-unsloth-theme="dark"] body .u-nav{
background:transparent!important;
background-image:none!important;
box-shadow:none!important;
}
html[data-unsloth-theme="dark"] body .u-nav-row{
--u-dark-auto-background:var(--u-dark-surface-3);
color:var(--u-dark-text)!important;
background:var(--u-dark-surface-3)!important;
border:0!important;
box-shadow:none!important;
}
html[data-unsloth-theme="dark"] body .u-logo,
html[data-unsloth-theme="dark"] body .u-logo span,
html[data-unsloth-theme="dark"] body .u-nav-links a,
html[data-unsloth-theme="dark"] body .u-social-link{color:#e8e8e8!important}
html[data-unsloth-theme="dark"] body .u-social-link:hover{
color:var(--u-dark-accent)!important;
background:var(--u-dark-accent-surface)!important;
}
html[data-unsloth-theme="dark"] body .u-nav-download{
color:#181818!important;
background:var(--u-dark-accent-strong)!important;
}
html[data-unsloth-theme="dark"] body .u-nav-download:hover{
color:#181818!important;
background:#70e6bd!important;
}
html[data-unsloth-theme="dark"] body .u-mobile-nav>summary{
--u-dark-auto-background:var(--u-dark-surface-3);
--u-dark-auto-color:#f7f7f7;
color:#f7f7f7!important;
background:var(--u-dark-surface-3)!important;
border:0!important;
box-shadow:none!important;
}
html[data-unsloth-theme="dark"] body .u-mobile-nav-panel{
--u-dark-auto-background:var(--u-dark-surface-3);
color:var(--u-dark-text)!important;
background:var(--u-dark-surface-3)!important;
border:0!important;
box-shadow:none!important;
}
html[data-unsloth-theme="dark"] body .u-mobile-nav-panel a{color:#e8e8e8!important}
html[data-unsloth-theme="dark"] body .u-mobile-nav-panel a:hover{background:var(--u-dark-surface-3)!important}
html[data-unsloth-theme="dark"] body .u-footer,
html[data-unsloth-theme="dark"] body #unsloth-shared-footer,
html[data-unsloth-theme="dark"] body .unsloth-global-chrome{
color:var(--u-dark-text)!important;
background:var(--u-dark-surface-1)!important;
border:0!important;
box-shadow:none!important;
}
html[data-unsloth-theme="dark"] body .u-footer .u-logo,
html[data-unsloth-theme="dark"] body .u-footer .u-logo span,
html[data-unsloth-theme="dark"] body .u-footer-grid>div>h3{color:var(--u-dark-text)!important}
html[data-unsloth-theme="dark"] body .u-footer-intro p,
html[data-unsloth-theme="dark"] body .u-footer-links a{color:var(--u-dark-muted)!important}
html[data-unsloth-theme="dark"] body .u-footer-links a:hover{color:var(--u-dark-text)!important}
html[data-unsloth-theme="dark"] body .u-footer-bottom,
html[data-unsloth-theme="dark"] body .u-footer-bottom a{color:var(--u-dark-subtle)!important}
html[data-unsloth-theme="dark"] body table,
html[data-unsloth-theme="dark"] body thead,
html[data-unsloth-theme="dark"] body tbody,
html[data-unsloth-theme="dark"] body tr{background:var(--u-dark-surface-1)!important}
html[data-unsloth-theme="dark"] body th,
html[data-unsloth-theme="dark"] body td{
color:#e8e8e8!important;
background:var(--u-dark-surface-2)!important;
border:0!important;
}
html[data-unsloth-theme="dark"] body input,
html[data-unsloth-theme="dark"] body textarea,
html[data-unsloth-theme="dark"] body select{
color:var(--u-dark-text)!important;
background:var(--u-dark-surface-3)!important;
border:0!important;
box-shadow:none!important;
}
html[data-unsloth-theme="dark"] body input::placeholder,
html[data-unsloth-theme="dark"] body textarea::placeholder{color:var(--u-dark-subtle)!important}
html[data-unsloth-theme="dark"] body code,
html[data-unsloth-theme="dark"] body pre{
color:#dedede!important;
background:var(--u-dark-surface-2)!important;
border:0!important;
box-shadow:none!important;
}
html[data-unsloth-theme="dark"] body ::selection{color:#181818!important;background:#63ddb4!important}

.u-theme-switch{
display:inline-grid!important;
grid-template-columns:repeat(3,36px)!important;
gap:5px!important;
align-items:center!important;
width:auto!important;
height:44px!important;
padding:4px!important;
border:0!important;
border-radius:999px!important;
color:#3a3a3a!important;
background:#e8e8e8!important;
box-shadow:none!important;
}
.u-theme-option{
position:relative!important;
display:flex!important;
align-items:center!important;
justify-content:center!important;
width:36px!important;
height:36px!important;
padding:0!important;
border:0!important;
border-radius:999px!important;
color:inherit!important;
background:transparent!important;
box-shadow:none!important;
line-height:0!important;
cursor:pointer!important;
}
.u-theme-option:hover{color:#1f1f1f!important;background:#d9d9d9!important}
.u-theme-option[aria-checked="true"]{color:#1f1f1f!important;background:#fff!important}
.u-theme-option:focus-visible{outline:2px solid #35d6a4!important;outline-offset:2px!important}
.u-theme-option svg{
position:absolute!important;
top:50%!important;
left:50%!important;
width:17px!important;
height:17px!important;
margin:0!important;
transform:translate(-50%,-50%)!important;
fill:none!important;
stroke:currentColor!important;
stroke-width:1.8!important;
stroke-linecap:round!important;
stroke-linejoin:round!important;
}
html[data-unsloth-theme="dark"] body .u-theme-switch{
color:#a3a3a3!important;
background:var(--u-dark-surface-2)!important;
}
html[data-unsloth-theme="dark"] body .u-theme-option:hover{
color:#fff!important;
background:var(--u-dark-surface-3)!important;
}
html[data-unsloth-theme="dark"] body .u-theme-option[aria-checked="true"]{
color:#fff!important;
background:var(--u-dark-surface-4)!important;
}
.u-theme-switch-floating{
position:fixed!important;
top:18px!important;
right:18px!important;
z-index:9999!important;
}
footer .u-footer-intro,.u-footer .u-footer-intro,[role="contentinfo"] .u-footer-intro{
display:flex!important;
flex-direction:column!important;
align-items:flex-start!important;
gap:24px!important;
}
footer .u-logo,.u-footer .u-logo,[role="contentinfo"] .u-logo{gap:14px!important}
footer .u-logo img,.u-footer .u-logo img,[role="contentinfo"] .u-logo img,footer a[href="/"] img[alt*="unsloth" i]{
width:48px!important;
height:48px!important;
max-width:none!important;
}
footer .u-logo span,.u-footer .u-logo span,[role="contentinfo"] .u-logo span{font-size:32px!important;line-height:1!important}
footer .u-theme-switch-footer,.u-footer .u-theme-switch-footer,[role="contentinfo"] .u-theme-switch-footer{
margin:0!important;
align-self:flex-start!important;
}

html body img{border-radius:16px!important}
html body main img,
html body article img,
html body .u-news-thumb img,
html body .u-app-shot>img,
html body img.u-product-shot,
html body .u-feature .u-visual-field>img,
html body .u-hero-visual img{border-radius:20px!important}
html body .u-news-thumb,
html body .u-app-shot,
html body .u-product-shot{overflow:hidden!important}
html body .u-logo img,
html body .u-social-link img,
html body .u-footer-links img,
html body .u-download-icon img,
html body .u-current-os-icon img,
html body .unsloth-download-option-icon img{border-radius:0!important}

.u-current-os-direct[aria-label="Download for Linux"] .u-current-os-icon,
#unsloth-os-download-cta[aria-label="Download for Linux"] .unsloth-download-icon{
width:38px!important;
height:38px!important;
min-width:38px!important;
flex:0 0 38px!important;
display:inline-grid!important;
place-items:center!important;
}
.u-current-os-direct[aria-label="Download for Linux"] .u-current-os-icon img,
#unsloth-os-download-cta[aria-label="Download for Linux"] .unsloth-download-icon img{
display:block!important;
width:34px!important;
height:34px!important;
max-width:none!important;
object-fit:contain!important;
filter:brightness(0) invert(1)!important;
}
html[data-unsloth-theme="dark"] .u-current-os-direct[aria-label="Download for Linux"] .u-current-os-icon img,
html[data-unsloth-theme="dark"] #unsloth-os-download-cta[aria-label="Download for Linux"] .unsloth-download-icon img{filter:brightness(0)!important}
html[data-unsloth-theme="dark"] body .platform .linux-logo-crop img,
html[data-unsloth-theme="dark"] body [role="tab"] .linux-logo-crop img{filter:brightness(0) invert(1)!important}
html[data-unsloth-theme="dark"] body .u-nav,
html[data-unsloth-theme="dark"] body header.u-theme-auto-surface-1{
background-color:transparent!important;
background-image:none!important;
}
html[data-unsloth-theme="dark"] body header .u-social-link img,
html[data-unsloth-theme="dark"] body .u-nav-row .u-social-link img{filter:brightness(2.25)!important}
html[data-unsloth-theme="dark"] body .u-download-panel .u-download-option[href*="Ubuntu"] .u-download-icon{
position:relative!important;
overflow:visible!important;
display:grid!important;
place-items:center!important;
}
html[data-unsloth-theme="dark"] body .u-download-panel .u-download-option[href*="Ubuntu"] .u-download-icon>img{
position:absolute!important;
top:50%!important;
left:50%!important;
translate:-50% -50%!important;
scale:1.04!important;
transform-origin:center!important;
filter:brightness(0) saturate(100%) invert(66%) sepia(6%) saturate(300%) hue-rotate(100deg) brightness(90%) contrast(90%)!important;
}

@media(min-width:768px) and (max-width:991px){
html:not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity) body .u-nav-row{
width:calc(100% - 48px)!important;
max-width:1080px!important;
min-height:56px!important;
height:56px!important;
margin-left:auto!important;
margin-right:auto!important;
padding:7px 9px 7px 14px!important;
align-items:center!important;
gap:8px!important;
}
html:not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity) body :is(.u-mobile-nav,.u-mobile-nav>summary){
width:42px!important;
height:42px!important;
min-width:42px!important;
min-height:42px!important;
flex:0 0 42px!important;
margin:0!important;
}
}

@media(max-width:991px){
html:not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity) body .u-mobile-nav{
position:relative!important;
display:block!important;
}
html:not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity) body .u-mobile-nav>summary{
display:grid!important;
place-items:center!important;
padding:0!important;
border:0!important;
border-radius:999px!important;
color:#292929!important;
background:transparent!important;
box-shadow:none!important;
font-size:0!important;
line-height:0!important;
list-style:none!important;
cursor:pointer!important;
}
html[data-unsloth-theme="dark"]:not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity) body .u-mobile-nav>summary{
--u-dark-auto-background:var(--u-dark-surface-3)!important;
--u-dark-auto-color:#f7f7f7!important;
color:#f7f7f7!important;
background:transparent!important;
}
html:not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity) body .u-mobile-nav>summary::before{
content:""!important;
display:block!important;
width:21px!important;
height:15px!important;
margin:0!important;
border:0!important;
background:
linear-gradient(currentColor,currentColor) 0 0/100% 2px no-repeat,
linear-gradient(currentColor,currentColor) 0 50%/100% 2px no-repeat,
linear-gradient(currentColor,currentColor) 0 100%/100% 2px no-repeat!important;
box-shadow:none!important;
transform:none!important;
}
html:not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity) body .u-mobile-nav>summary::after{
content:none!important;
display:none!important;
}
html[data-unsloth-theme="dark"]:not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity):not(#unsloth-responsive-specificity) body .u-mobile-nav-panel{
--u-dark-auto-background:var(--u-dark-surface-3)!important;
color:var(--u-dark-text)!important;
background:var(--u-dark-surface-3)!important;
border:0!important;
box-shadow:none!important;
}
}

@media(prefers-color-scheme:dark){
html:not([data-unsloth-theme]) .u-current-os-direct[aria-label="Download for Linux"] .u-current-os-icon img,
html:not([data-unsloth-theme]) #unsloth-os-download-cta[aria-label="Download for Linux"] .unsloth-download-icon img{filter:brightness(0)!important}
}
@media(max-width:479px){
.u-theme-switch{grid-template-columns:repeat(3,34px)!important;gap:4px!important;height:42px!important}
.u-theme-option{width:34px!important;height:34px!important}
footer .u-logo img,.u-footer .u-logo img,[role="contentinfo"] .u-logo img,footer a[href="/"] img[alt*="unsloth" i]{width:44px!important;height:44px!important}
footer .u-logo span,.u-footer .u-logo span,[role="contentinfo"] .u-logo span{font-size:29px!important}
html body img{border-radius:14px!important}
html body main img,
html body article img,
html body .u-app-shot>img,
html body img.u-product-shot,
html body .u-feature .u-visual-field>img,
html body .u-hero-visual img{border-radius:18px!important}
html body .u-logo img,
html body .u-social-link img,
html body .u-footer-links img,
html body .u-download-icon img,
html body .u-current-os-icon img,
html body .unsloth-download-option-icon img{border-radius:0!important}
.u-current-os-direct[aria-label="Download for Linux"] .u-current-os-icon,
#unsloth-os-download-cta[aria-label="Download for Linux"] .unsloth-download-icon{
width:34px!important;
height:34px!important;
min-width:34px!important;
flex-basis:34px!important;
}
.u-current-os-direct[aria-label="Download for Linux"] .u-current-os-icon img,
#unsloth-os-download-cta[aria-label="Download for Linux"] .unsloth-download-icon img{width:30px!important;height:30px!important}
}
@media(print){.u-theme-switch{display:none!important}}

(function(){
var version='clean-system-switch-v7';
if(window.__unslothGlobalTheme2026&&window.__unslothGlobalTheme2026.version===version){
window.__unslothGlobalTheme2026.refresh();
return;
}
var storageKey='unsloth-theme';
var modeKey='unsloth-theme-mode';
var root=document.documentElement;
var media=window.matchMedia('(prefers-color-scheme: dark)');
var control=null;
var observer=null;
var scanQueued=false;
var autoClasses=['u-theme-auto-surface-1','u-theme-auto-surface-2','u-theme-auto-surface-accent','u-theme-auto-text','u-theme-auto-muted','u-theme-auto-accent-text','u-theme-auto-control'];

function storedMode(){
try{
var mode=window.localStorage.getItem(modeKey);
if(mode==='dark'||mode==='light'||mode==='system')return mode;
var legacy=window.localStorage.getItem(storageKey);
return legacy==='dark'||legacy==='light'?legacy:'system';
}catch(error){return 'system'}
}
function themeForMode(mode){return mode==='system'?(media.matches?'dark':'light'):mode}
function persistMode(mode){
try{
window.localStorage.setItem(modeKey,mode);
if(mode==='system')window.localStorage.removeItem(storageKey);
else window.localStorage.setItem(storageKey,mode);
}catch(error){}
}
function rgb(value){
var match=String(value||'').match(/rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)(?:\s*[,/]\s*([\d.]+))?\s*\)/i);
return match?{r:+match[1],g:+match[2],b:+match[3],a:match[4]===undefined?1:+match[4]}:null;
}
function luminance(color){
function channel(value){value/=255;return value .05&&style.backgroundImage==='none'){
var bgLum=luminance(background);
var bgSat=saturation(background);
if(bgLum>.9)element.classList.add('u-theme-auto-surface-1');
else if(bgLum>.62)element.classList.add(bgSat>.12?'u-theme-auto-surface-accent':'u-theme-auto-surface-2');
}
if(color&&color.a>.05){
var textLum=luminance(color);
var textSat=saturation(color);
if(textLum .3?'u-theme-auto-accent-text':'u-theme-auto-muted');
}
var interactive=/^(A|BUTTON|INPUT|TEXTAREA|SELECT|SUMMARY)$/.test(tag);
var hasBorder=['Top','Right','Bottom','Left'].some(function(side){
return parseFloat(style['border'+side+'Width'])>0&&style['border'+side+'Style']!=='none';
});
if(interactive&&(hasBorder||(background&&background.a>.05&&luminance(background)>.62&&saturation(background)                      ';
}
function ensureControl(){
if(!document.body)return false;
document.querySelectorAll('.u-theme-toggle').forEach(function(oldToggle){oldToggle.remove()});
var footer=document.querySelector('footer,.u-footer,[role="contentinfo"]');
var logo=footer&&(footer.querySelector('.u-footer-intro .u-logo')||footer.querySelector('.u-logo')||footer.querySelector('a[href="/"]'));
var host=(logo&&logo.parentElement)||footer||document.body;
control=document.querySelector('.u-theme-switch');
if(!control){
control=document.createElement('div');
control.className='u-theme-switch';
control.setAttribute('role','radiogroup');
control.setAttribute('aria-label','Theme preference');
control.innerHTML=controlMarkup();
}
if(control.getAttribute('data-unsloth-theme-control')!==version){
if(control.parentElement){
var cleanControl=control.cloneNode(true);
control.parentElement.replaceChild(cleanControl,control);
control=cleanControl;
}
control.setAttribute('data-unsloth-theme-control',version);
control.querySelectorAll('.u-theme-option').forEach(function(option){
option.addEventListener('click',function(){
var mode=option.getAttribute('data-theme-choice');
persistMode(mode);
applyMode(mode);
});
});
}
control.classList.toggle('u-theme-switch-footer',!!footer);
control.classList.toggle('u-theme-switch-floating',!footer);
if(footer&&logo){
if(control.parentElement!==host||control.previousElementSibling!==logo)host.insertBefore(control,logo.nextSibling);
}else if(control.parentElement!==host){host.appendChild(control)}
var mode=storedMode();
updateControl(mode,themeForMode(mode));
return true;
}
function refresh(){
applyMode(storedMode());
ensureControl();
scheduleScan();
}
function systemChange(){if(storedMode()==='system')applyMode('system')}
observer=new MutationObserver(function(){ensureControl();scheduleScan()});
observer.observe(root,{childList:true,subtree:true});
if(media.addEventListener)media.addEventListener('change',systemChange);
else if(media.addListener)media.addListener(systemChange);
var controller={
version:version,
refresh:refresh,
setMode:function(mode){persistMode(mode);applyMode(mode)},
getMode:storedMode
};
window.__unslothGlobalTheme2026=controller;
window.__unslothThemeController2026=controller;
applyMode(storedMode());
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',refresh,{once:true});
else refresh();
})();

(function(){
var BASE='#2c2c2c',ACTIVE='#3a3a3a',PANEL='#292929';
function paint(el,bg,border,shadow){if(!el)return;el.style.setProperty('background-color',bg,'important');el.style.setProperty('border',border||'0','important');el.style.setProperty('box-shadow',shadow||'none','important')}
function hover(el,base,active,selected){if(!el)return;el.__unslothBase=base;el.__unslothActive=active;el.__unslothSelected=selected;if(el.dataset.unslothContrastBound)return;el.dataset.unslothContrastBound='1';el.addEventListener('mouseenter',function(){this.style.setProperty('background-color',this.__unslothActive,'important')});el.addEventListener('mouseleave',function(){this.style.setProperty('background-color',this.__unslothSelected&&this.matches('[aria-selected=\"true\"],[aria-current=\"page\"]')?this.__unslothActive:this.__unslothBase,'important')})}
function apply(){
document.querySelectorAll('summary[aria-label=\"Choose another platform\"],.u-mobile-hero-download').forEach(function(el){paint(el,BASE,'0','0 1px 2px rgba(0,0,0,.24)');hover(el,BASE,ACTIVE,false)});
document.querySelectorAll('.u-download-panel').forEach(function(el){paint(el,PANEL,'1px solid '+ACTIVE,'0 18px 44px rgba(0,0,0,.38)')});
document.querySelectorAll('.u-cta').forEach(function(el){paint(el,PANEL,'0','0 16px 48px rgba(0,0,0,.22)')});
document.querySelectorAll('.download-main .platform').forEach(function(el){var selected=el.matches('[aria-selected=\"true\"],[aria-current=\"page\"]');paint(el,selected?ACTIVE:BASE,'0','none');hover(el,BASE,ACTIVE,true)});
document.querySelectorAll('.download-main .linux-download-options>a').forEach(function(el){paint(el,BASE,'0','none');hover(el,BASE,ACTIVE,false)});
}
function schedule(){if(window.__unslothContrastFrame)return;window.__unslothContrastFrame=requestAnimationFrame(function(){window.__unslothContrastFrame=0;apply()})}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',apply);else apply();
if(!window.__unslothContrastObserver){window.__unslothContrastObserver=new MutationObserver(schedule);window.__unslothContrastObserver.observe(document.documentElement,{subtree:true,childList:true,attributes:true,attributeFilter:['aria-selected','aria-current','open']})}
})();

(function(){
function clearBackground(el){
if(!el)return;
el.style.setProperty('background-color','transparent','important');
el.style.setProperty('background-image','none','important');
}
function apply(){
document.querySelectorAll('.u-cta h2,.u-download-panel .u-download-option,.u-news-item > .u-news-thumb,.u-news-item > .u-theme-auto-accent-text,.u-news-item .u-news-meta,.u-news-item h3').forEach(clearBackground);
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',apply);else apply();
if(!window.__unslothNestedSurfaceObserver){
window.__unslothNestedSurfaceObserver=new MutationObserver(function(){requestAnimationFrame(apply)});
window.__unslothNestedSurfaceObserver.observe(document.documentElement,{subtree:true,childList:true});
}
})();

@media(min-width:480px) and (max-width:991px){html body .u-nav-row .u-mobile-nav>summary[aria-label="Open navigation"]{display:grid!important;place-items:center!important;place-content:center!important;align-self:center!important;justify-self:center!important;line-height:0!important;text-align:center!important;margin:auto!important}html body .u-nav-row .u-mobile-nav>summary[aria-label="Open navigation"]::before{margin:auto!important;align-self:center!important;justify-self:center!important;position:static!important;inset:auto!important;transform:none!important}}html[data-unsloth-theme="dark"] body .u-nav-row .u-mobile-nav-socials .u-social-link img{filter:brightness(0) invert(1)!important;opacity:.82!important}
window.__remixContext = {"basename":"/","future":{"v3_fetcherPersist":false,"v3_relativeSplatPath":false,"v3_throwAbortReason":false,"v3_routeConfig":false,"v3_singleFetch":false,"v3_lazyRouteDiscovery":false,"unstable_optimizeDeps":false},"isSpaMode":false,"state":{"loaderData":{"root":null,"routes/[blog].[nvidia-collab]._index":{"host":"unsloth.ai","url":"https://unsloth.ai/blog/nvidia-collab","system":{"params":{},"search":{},"origin":"https://unsloth.ai","pathname":"/blog/nvidia-collab"},"resources":{},"pageMeta":{"title":"How to Make LLM Training Faster with Unsloth and NVIDIA","description":"Learn how NVIDIA helped Unsloth to make fine-tuning AI models 20% faster with explanations and diagrams.","excludePageFromSearch":false,"socialImageAssetName":"how_to_make_llm_faster_U2z2dRaYlhanzK1QvFDPI.png","custom":[]}}},"actionData":null,"errors":null}};  import "/assets/manifest-64340927.js";
import * as route0 from "/assets/root-Bi8uDDMw.js";
import * as route1 from "/assets/_blog_._nvidia-collab_._index-DqV6mlXz.js";

window.__remixRouteModules = {"root":route0,"routes/[blog].[nvidia-collab]._index":route1};

import("/assets/entry.client-0UdrQI2f.js");  ((h, l) => {
if (!window.history.state || !window.history.state.key) {
let u = Math.random().toString(32).slice(2);
window.history.replaceState({ key: u }, "");
}
try {
let m = JSON.parse(sessionStorage.getItem(h) || "{}")[l || window.history.state.key];
typeof m == "number" && window.scrollTo(0, m);
} catch (u) {
console.error(u), sessionStorage.removeItem(h);
}
})("positions", null)
