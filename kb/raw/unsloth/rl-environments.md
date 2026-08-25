---
source_url: https://unsloth.ai/blog/rl-environments
slug: rl-environments
title: "Reinforcement Learning environments and how to build them"
captured_date: 2026-08-25
status: raw_capture
provenance: unsloth_blog_first_party
---

# Reinforcement Learning environments and how to build them

-                             Reinforcement Learning environments and how to build them   {"@context":"https://schema.org","@type":"WebSite","name":"Unsloth - Train and Run Models Locally","url":"https://unsloth.ai"}
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
# What are RL environments and how to build them

## Mar 13, 2026

## Mar 13, 2026
Authors:  Daniel, Michael, and from NVIDIA: Shashank Verma, Sylendran Arunagiri, Chris Wing, Brian Yu   [Reinforcement learning (RL)](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide) has shaped AI for decades, from early control systems to game-playing agents and, more recently, large language models that learn through interaction. At its core, RL works by teaching a model to learn, respond, and receive feedback, improving the model over the course of time.

However, as AI becomes [agentic](https://www.nvidia.com/en-us/glossary/ai-agents/), capable of multi-step reasoning, tool use, and decision-making, we are entering the ["Era of Experience"](https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf), where progress is driven by systems that learn from their own experience rather than just static data. RL must evolve from optimizing single responses to shaping behaviors across entire trajectories. In this context, learning happens through interaction with "environments" that define permissible actions, state changes, and the definition of success.

An RL workflow unifies a policy model, a training algorithm, and an environment, along with a method to verify agent responses. This interaction loop enables agents to plan, adapt, and recover from failure.

This blog explores how RL is evolving for agentic AI, why environments are central to this shift, and how open tools like [Unsloth](https://unsloth.ai/), [NVIDIA NeMo RL](https://github.com/NVIDIA-NeMo/RL), [NVIDIA NeMo Gym](https://github.com/NVIDIA-NeMo/Gym), and [NVIDIA NeMo Data Designer](https://github.com/NVIDIA-NeMo/DataDesigner) help developers build these RL workflows efficiently.

## Comparing SFT and RL

Before building an environment, it is critical to understand when RL is the right tool.

Supervised Fine-Tuning (SFT) fits best when you can provide clear target behaviors through demonstrations, or instruction-response pairs. It is great for teaching format and style. However, SFT has limitations.

Imitation over adaptivity.  When the dataset is small, models learn to mimic the answer rather than learn the process to get there.

-  Brittleness.  SFT models often struggle when scenarios fall outside their training distribution, so the dataset needs to be diverse and large.

Reinforcement Learning (RL) becomes the better choice as complexity grows. Instead of telling the model "say exactly this," you provide a goal and a way to verify it. This allows the model to explore reasoning paths, making it resilient to edge cases. This tends to work well for tasks like math, code, and tool calling, among other things that have a clear path to answer verification.

In practice, SFT and RL are not mutually exclusive, and a hybrid strategy is often employed.

-  SFT for warm-starting RL.  Use a high-quality set of demonstrations to teach the chat template, tool-calling format, and general readability. This helps RL avoid wasting time trying to learn the format of your dataset.

-  RL for scaling.  Transition to RL to allow the model to explore and self-correct. This "post-training" refinement is where reasoning and robustness are truly forged.

For example, the [NVIDIA Nemotron 3](https://research.nvidia.com/labs/nemotron/Nemotron-3/) family of models utilizes SFT as a substantial first stage to ground the model before moving into RL refinement. The ultimate choice depends on your compute budget, data availability, and the level of generalization your agent requires. The industry is generally shifting toward allocating more compute during RL stages, especially as RL environments become more sophisticated and accessible.

## From Algorithms to Environments and the Rise of RLVR

Traditionally, RL methods like [PPO (Proximal Policy Optimization)](https://arxiv.org/abs/1707.06347v2) were the standard. However, their resource intensiveness, which requires multiple complex and compute-intensive models like the reward and critic models, has driven a shift toward more scalable algorithms.

Modern workflows are increasingly adopting more efficient methods like DPO and GRPO to handle different aspects of model improvement.

Direct Preference Optimization (DPO)  sidesteps the RL loop entirely, treating alignment as a classification problem on static preference data.

-  Reward type.  Pairwise. It relies on labeled preferences ("Response A > Response B").

-  Efficiency.  Computationally light and stable, making it ideal for alignment tasks such as safety, tone, and style.

However, DPO lacks explicit reward optimization or exploration. It learns from fixed preference pairs, which prevents it from discovering new strategies or optimizing long-horizon outcomes. Furthermore, because the DPO algorithm models relative output preference rather than trajectory reward, it is less effective for agentic workflows that require multi-step reasoning and tool use.

To address these limitations in agentic domains, developers are turning to algorithms that leverage verifiable rewards.

One such algorithm is  [Group Relative Policy Optimization (GRPO)](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide#from-rlhf-ppo-to-grpo-and-rlvr) , which is an optimized version of PPO. In this setup, heavy critic models are replaced by generating groups of outputs and scoring them against a deterministic verifier.

-  Reward type.  Typically binary (`0` or `1`), but it also supports continuous values (`-∞` to `+∞`). While it thrives when an environment can programmatically say "Yes" or "No," for example by checking whether a unit test passes, it also supports complex rewards where scores may exceed `1` to provide more granular feedback.

-  Efficiency.  Eliminating the value model and the reward model from PPO significantly reduces memory overhead and is a key factor in scaling reasoning capabilities.

This broader shift toward verifiable correctness is distinct from any single algorithm. While verification can drive improvements even in supervised settings, such as rejection sampling, it is central to the paradigm of  Reinforcement Learning from Verifiable Rewards (RLVR) . By replacing subjective scoring with explicit checks, such as whether the agent produced the correct answer or called the right tools, RLVR moves the center of gravity from the optimizer to the environment. Algorithms like GRPO simply provide an efficient mechanism to optimize against these environmental signals.

In RLVR, the environment becomes the contract between learning and behavior.

Let’s now define more concretely what we mean by an environment.

## What Is an Environment?

The environment is everything outside the absolute control of the agent. An environment is defined by the task the agent must accomplish, the actions the agent can take, and the state of the world the agent observes and acts upon. The environment also determines how the agent’s performance is evaluated, including what constitutes success and how reward is assigned.

Before we move further, it’s important to formally introduce key terminology.

Rollout.  The process of executing a policy in an environment to generate experience. It emphasizes the act of collecting data by stepping through the environment, taking actions, and recording what happens.

Trajectory.  The resulting sequence of states, actions, and rewards produced by a rollout. It emphasizes the data itself, or the ordered record of what happened. In practice, most codebases and papers treat the terms as synonymous, since a rollout produces exactly one trajectory, and when people say "trajectory," they usually imply it came from rolling out a policy.

## Challenges of Building and Scaling Environments

-  Decoupling environments from training.  Many RL workflows tightly couple environment logic with the training pipeline, making it difficult to integrate complex agent loops, iterate on environment design, and run controlled ablations.

-  Representing agentic trajectories consistently.  The community widely uses Chat Completions today, but it was designed for stateless, single-turn interactions. Yet agentic rollouts include interleaved reasoning, tool calls, and text across multiple turns. Without a schema that natively represents this, you will need to custom-parse and serialize model outputs for every environment.

-  Resource management.  Environments often depend on external resources such as sandboxed execution, databases, APIs, and more. Each rollout needs isolated instances, and those instances must be reliably initialized and cleaned up.

-  Scalability.  Training may require thousands of parallel rollouts. Environment instances must scale accordingly, with distribution, load balancing, and fault tolerance.

## NVIDIA NeMo Gym

[NeMo Gym](https://github.com/NVIDIA-NeMo/Gym) is an open-source library for building and scaling RL environments, battle-tested through the development of the Nemotron 3 model family.

NeMo Gym is designed to address these challenges by providing a clean decoupling of rollout collection from training, standardizing trajectories using the OpenAI Responses API, and providing infrastructure to manage resource lifecycles that scale to thousands of parallel environments.

In NeMo Gym, tasks define what the agent must accomplish. Resources provide the external state the agent interacts with, for example tools, databases, sandboxed execution, as well as the verification logic that scores performance. The Model Interface handles generation, producing the model’s actions at each turn, such as text, tool calls, or code. The Agent orchestrates each rollout by calling the model to generate actions, updating the environment state via resource servers, and collecting the final reward.

Figure 1:  The architecture of NeMo Gym, which works alongside an RL training framework, illustrating the decoupling of environment rollout orchestration from model training and generation.

NVIDIA NeMo Gym integrates with RL training libraries such as NeMo RL, Unsloth, Hugging Face TRL, and others that implement training algorithms (for example, GRPO) to update the model. NeMo Gym collects rollout trajectories and rewards from the environment and passes them to the training framework, which manages policy updates and serves the updated model for the next round of rollouts.

## RLVR User Journey: From Benchmarking to Training

Before writing a single line of code, it is essential to understand the two-phase journey of an RLVR practitioner.

Figure 2:  In the RLVR workflow, environment preparation precedes and shapes model training.

## Phase 1: Environment Preparation

-  Benchmarking:  Evaluate your base model to identify specific capability gaps (for example, it fails at multi-step math or hallucinates tool arguments).

-  Defining capabilities:  Map these failures to target capabilities.

-  Environment development:  Either adapt an existing environment or build a new one.

-  Task generation:  Curate data to create diverse task sets that exercise the environment. This often involves Synthetic Data Generation (SDG).

-  Reward profiling:  "Sanity check" the environment by running rollouts across different models (including large frontier models) to ensure that environment output aligns the targeted capability with actual capabilities.

## Phase 2: Model Training

-  Optimization:  Train the model using an algorithm like GRPO, which uses the environment’s verifiable signals to update weights.

-  Validation:  Verify that performance on the specific environment improves and, more importantly, that this translates to improvements on broader downstream benchmarks.

The key insight is that environment preparation is how you define what "better" means. The training phase simply optimizes for the signal you’ve built.

For the purposes of this blog post, we will assume that you have a good understanding of the capability or benchmark you want to see the model improve on. The following section covers, specifically, concepts around Phase 1.3 above, that is, building an environment.

## Building an RL Environment for Model Training

NeMo Gym, an open-source library within the [NVIDIA NeMo](https://github.com/NVIDIA-NeMo/) framework, defines and orchestrates RL environments and generates scalable, verifiable rollout data, while Unsloth consumes these rollouts for efficient RL training.

Within the NeMo Gym ecosystem, building an environment relies on three foundational pillars, culminating in model training executed via an integrated RL framework.

## 1. Task Preparation

Agents need to be exposed to a diverse set of scenarios in order to specialize and improve on a given task. For instance, in the [Workplace Assistant environment](https://docs.nvidia.com/nemo/gym/latest/training-tutorials/nemo-rl-grpo/about-workplace-assistant.html), task data consists of natural language business requests that require the agent to autonomously navigate simulated databases and tools over multiple steps. A simple single-step example of a user query and expected response would be:

User query:

"Send an email to [ [email protected] ](/cdn-cgi/l/email-protection#c6aca9aea8e8b5abafb2ae86a7b2aaa7b5e8a5a9ab) with the subject 'Team Meeting' and body 'Let's meet tomorrow at 2pm to discuss the project.'"

Expected tool call:

`email_send_email(
recipient="[[email protected]](/cdn-cgi/l/email-protection)",
subject="Team Meeting",
body="Let's meet tomorrow at 2pm to discuss the project."
)
`
When short on task-specific data, developers can turn to synthetic data generation (SDG) using tools such as [NeMo Data Designer](https://github.com/NVIDIA-NeMo/DataDesigner) to programmatically create task queries, and potentially corresponding ground truths. To train effectively, you need thousands of diverse prompts that exercise the environment’s tools. For example, if you are building a coding environment, you might use an LLM to generate 5,000 unique Python word problems, while a deterministic script generates the unit tests (the ground truth) used to verify the answers.

Understanding the task is the first step in designing the environment itself.

## 2. Environment Design

Referring back to the left half of Figure 1, the environment design consists of three primary components:

-  The Agent Server:  The central component of environment design is the agent itself. The agent orchestrates all interaction logic, such as calling the model and using tools. It acts as the scaffolding that ties everything together, managing the conversation loop (send to model, execute tool calls, repeat).

-  The Resources Server:  This component hosts the tools, maintains session state, and computes the reward.

-  The Model Interface:  This provides a standardized interface to communicate with the generation backend.

## 2.1 Agent Server

Take a look at an example Agent Server pseudocode below. It sends the conversation to the model, gets back a response, and, if the model makes any tool calls, it routes the tool calls to the resources server and feeds the results back to the model. This repeats until the model replies with a plain text message (no tool calls), hits the token limit, or exceeds `max_steps`.

`# Agent Server pseudocode (based on SimpleAgent)

async def run(task_data):
# 1. Initialize episode
resource_server.seed_session(task_data)

# 2. Run the agent loop
response = self.responses(task_data.prompt, task_data.tools)

# 3. Grade the result
reward = resource_server.verify(response, task_data.ground_truth)
return response, reward

async def responses(prompt, tools):
conversation = prompt
step = 0

while step < max_steps:
model_output = model_server.responses(conversation, tools)
conversation.append(model_output)

if model_output is text:
break  # model is done, no more tool calls

for tool_call in model_output.function_calls:
result = resource_server.post(
f"/{tool_call.name}",
tool_call.arguments,
)
conversation.append(result)

step += 1

return conversation
`
Importantly, you can use an [existing agent in NeMo Gym](https://github.com/NVIDIA-NeMo/Gym/tree/main/responses_api_agents/simple_agent), bring your own, or create a completely new one. As such, it’s possible this loop looks very different depending on your setup. The [MiniSWEAgent](https://github.com/NVIDIA-NeMo/Gym/tree/main/responses_api_agents/mini_swe_agent), for example, delegates the run logic to an external harness running in Docker containers and then converts the output back into the NeMo Gym format.

Existing agents may also come with predefined tools, allowing you to leverage them directly. You can then seamlessly use the resources server to supplement the agent with any additional external tools it may need.

## 2.2 The Resources Server

The Resources Server is the "world" the agent interacts with. In NeMo Gym, this is implemented as a lightweight FastAPI application. It exposes tools as HTTP endpoints (for example, `POST /search_database`) that the model can call via standard OpenAI-compatible tool schemas, as well as reward calculation logic.

Crucially, these servers handle session management. Because an agentic rollout involves multiple steps, the environment must "remember" what happened in previous steps. NeMo Gym uses a `session_id` to maintain isolated state for every parallel rollout.

`# Conceptual Resources Server Structure

class MyResourceServer(SimpleResourcesServer):
async def seed_session(self, session_id, initial_data):
# Initialize the "sandbox" for this specific rollout
self.state[session_id] = initialize_environment(initial_data)

async def my_custom_tool(self, session_id, tool_args):
# Model calls this during the rollout
result = execute_action(self.state[session_id], tool_args)
return result
`

## 2.3 Verification Logic

The verifier is one of the most critical parts of environment design. It is often a deterministic function that evaluates the final state of a rollout and returns a reward signal.

Two common ways to design these rewards are:

-  Trajectory matching:  Comparing the agent’s specific tool calls and arguments against a "golden path." This is easier to implement but can be brittle if there are multiple correct ways to solve a problem.

-  State matching:  Checking the final outcome (for example, if the end state of the database matches the ground truth) regardless of how the agent got there. This is more robust and is the approach used for complex environments like the [Workplace Assistant](https://docs.nvidia.com/nemo/gym/latest/training-tutorials/nemo-rl-grpo/about-workplace-assistant.html).

Other major ways to design verification logic include sandboxed execution (running generated code or artifacts against unit tests), using an LLM-as-a-judge (for semantic or open-ended evaluation), and training reward models (to capture human preferences), among others.

`# Conceptual Verification Logic

async def verify(self, session_id, agent_response, ground_truth):
# 1. Extract what the agent actually did
actual_outcome = self.state[session_id].get_final_state()

# 2. Compare against the "Golden" result
if actual_outcome == ground_truth:
return reward(1.0)  # Success!

return reward(0.0)  # Failure
`
Some best practices for designing verification logic include:

-  Prefer binary rewards:  While it might seem intuitive to award partial credit for intermediate steps, strict binary signals (success/failure) typically yield the most stable and effective optimization targets for algorithms like GRPO.

-  Profile your reward signals:  Before committing to a large-scale training run, evaluate your environment against multiple models of varying capabilities (for example, a small base model versus a large frontier model). If the frontier model cannot consistently outscore the base model, your verifier logic or task definitions likely require recalibration.

## 3. Model Training

With environments in place, agent training proceeds by generating rollouts through repeated interaction between the policy model(s) and the environment. NeMo Gym orchestrates this process by running environments at scale, managing session state, and producing structured rollout trajectories annotated with rewards from the verification logic.

These rollouts are then consumed by an RL training framework such as Unsloth, NeMo RL, or HuggingFace TRL, which applies an optimization algorithm (for example, GRPO or PPO-style methods) to update model weights. Check out tutorials for [GRPO runs with NeMo RL and NeMo Gym](https://docs.nvidia.com/nemo/gym/latest/training-tutorials/nemo-rl-grpo/index.html) and [RL training with Unsloth and the NeMo Gym Sudoku environment](https://unsloth.ai/docs/models/tutorials/nemotron-3#reinforcement-learning--nemo-gym).

The training framework remains decoupled from environment implementation, allowing teams to swap optimizers, scaling strategies, or hardware backends without modifying environment logic.

Training follows an iterative loop: generate rollouts, verify outcomes, update the policy, and re-evaluate performance. This separation of rollout generation and optimization enables scalable, flexible RL workflows across different domains and infrastructure.

Deep dive:  For a step-by-step technical walkthrough, including code examples for stateful and multi-step environments, refer to the [supplemental developer guide for building environments](https://docs.nvidia.com/nemo/gym/latest/environment-tutorials/index.html).

## Environment-Driven RL, and the Open Ecosystem

Environment-driven RL workflows are increasingly shaping how agentic systems are trained across research and industry. By separating environment definition, rollout generation, and optimization, teams can iterate faster and scale reinforcement learning without tightly coupling reward logic to a single training framework.

This pattern has already been applied in real-world systems. For example, the [NVIDIA Nemotron 3](https://research.nvidia.com/labs/nemotron/Nemotron-3/) model family was predominantly refined using structured RL across interactive environments, where verification logic prioritized correct trajectories and tool usage over single-step responses. The same environment abstractions used in that work are now available as open libraries and integrate with multiple RL training frameworks.

RL environments are also being developed for applied domains. For example, Edison Scientific integrated NeMo Gym with their [Aviary gym](https://github.com/NVIDIA-NeMo/Gym/tree/main/resources_servers/aviary) to train scientific agents that explore hypotheses, run simulations, and receive deterministic feedback from domain-specific environments. See also NVIDIA’s post on [how to train scientific agents with reinforcement learning](https://developer.nvidia.com/blog/how-to-train-scientific-agents-with-reinforcement-learning/).

Today, interactive environments built with NeMo Gym generate verifiable rollout data that can be consumed by libraries such as Unsloth, HuggingFace TRL, NeMo RL, and other PyTorch-native stacks. This interoperability allows practitioners to choose optimizers, memory strategies, and hardware backends independently of environment design, supporting scalable agentic AI from research through production.

## Conclusion & Resources

In the era of agentic AI, the environment defines the contract for intelligence.
Here’s how you can get started today:

- [Unsloth + NeMo Gym](https://unsloth.ai/docs/models/tutorials/nemotron-3#reinforcement-learning--nemo-gym): RL notebooks for Sudoku and multi-environment training with Unsloth and NeMo Gym.

- [NeMo Gym environment tutorials](https://docs.nvidia.com/nemo/gym/latest/environment-tutorials/index.html) and [training tutorials](https://docs.nvidia.com/nemo/gym/latest/training-tutorials/index.html) help you build custom RL environments and use them with your preferred RL training framework.

- [NeMo Gym GitHub](https://github.com/NVIDIA-NeMo/Gym): The core library for building and orchestrating verifiable RL environments.

💕 Thank you!   A huge thank you to NVIDIA for authoring this educational blog along with us. Also thank you for reading and using Unsloth - we appreciate it. 🙏

As always, be sure to join our [Reddit page](https://www.reddit.com/r/unsloth/) and [Discord](https://discord.gg/unsloth) server for help or just to show your support! You can also follow us on [Twitter](https://twitter.com/unslothai) and our newsletter on: [Substack](https://unslothai.substack.com/).   Thank you for reading!    Daniel & Michael Han  🦥
March 12, 2026
##  Learn how to RL now!
[Get started for free](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide)           img[src*="cdn.simpleicons.org/reddit/"]{width:16px!important;height:16px!important;max-width:16px!important;max-height:16px!important;display:inline-block!important;flex:0 0 16px!important;object-fit:contain!important}  #unsloth-shared-footer{--u-green:#14b789!important;--u-green-soft:#dff8ef!important;--u-green-pale:#effbf7!important;--u-green-wash:#f6fcf9!important;--u-ink:#111411!important;--u-muted:#66706a!important;--u-paper:#f8faf8!important;--u-white:#ffffff!important;--u-soft:#f0f4f1!important;width:100%!important;color:var(--u-ink)!important;background:var(--u-paper)!important;font-family:Hellix,Inter,Arial,sans-serif!important;font-size:16px!important;font-weight:400!important;line-height:1.55!important;-webkit-font-smoothing:antialiased!important;text-rendering:optimizeLegibility!important}#unsloth-shared-footer,#unsloth-shared-footer *,#unsloth-shared-footer *::before,#unsloth-shared-footer *::after{box-sizing:border-box!important}#unsloth-shared-footer *{animation:none!important;text-transform:none!important}#unsloth-shared-footer .u-shell{width:min(1216px,calc(100% - 64px))!important;max-width:1216px!important;margin-inline:auto!important;padding-inline:0!important}#unsloth-shared-footer .u-logo{display:inline-flex!important;align-items:center!important;gap:10px!important;flex:0 0 auto!important;color:var(--u-ink)!important;font-size:20px!important;font-weight:600!important;letter-spacing:-.035em!important}#unsloth-shared-footer .u-logo img{width:36px!important;height:36px!important;object-fit:contain!important}#unsloth-shared-footer .u-nav-links a:hover,#unsloth-shared-footer .u-footer a:hover,#unsloth-shared-footer .u-principle a:hover,#unsloth-shared-footer .u-news-more:hover{opacity:.55!important}#unsloth-shared-footer .u-footer{padding:92px 0 38px!important;color:var(--u-ink)!important;background:#fff!important;border:0!important}#unsloth-shared-footer .u-footer-grid{display:grid!important;grid-template-columns:1.18fr 2fr!important;align-items:start!important;gap:110px!important}#unsloth-shared-footer .u-footer-intro p{margin-top:28px!important;color:var(--u-muted)!important;font-size:14px!important}#unsloth-shared-footer .u-footer-links{display:grid!important;grid-template-columns:repeat(3,minmax(0,1fr))!important;gap:54px!important}#unsloth-shared-footer .u-footer-links h3{margin-bottom:24px!important;font-size:14px!important;font-weight:600!important;letter-spacing:-.02em!important}#unsloth-shared-footer .u-footer-links a{display:block!important;width:fit-content!important;margin-top:14px!important;color:var(--u-muted)!important;font-size:14px!important}#unsloth-shared-footer .u-footer-bottom{display:flex!important;align-items:center!important;justify-content:space-between!important;gap:24px!important;margin-top:94px!important;padding-top:0!important;border:0!important;color:#858e88!important;font-size:13px!important}@media (max-width:1100px){#unsloth-shared-footer .u-shell{width:min(100% - 44px,1216px)!important}}@media (max-width:991px){#unsloth-shared-footer .u-shell{width:min(100% - 36px,760px)!important}#unsloth-shared-footer .u-footer-grid{grid-template-columns:1fr!important;gap:64px!important}}@media (max-width:767px){#unsloth-shared-footer .u-shell{width:calc(100% - 28px)!important}#unsloth-shared-footer .u-logo{font-size:18px!important}#unsloth-shared-footer .u-logo img{width:34px!important;height:34px!important}#unsloth-shared-footer .u-footer{padding-top:72px!important}#unsloth-shared-footer .u-footer-links{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:44px 28px!important}#unsloth-shared-footer .u-footer-bottom{align-items:flex-start!important;flex-direction:column!important;margin-top:70px!important}}@media (max-width:479px){#unsloth-shared-footer .u-footer-links{grid-template-columns:1fr 1fr!important}}@media (prefers-reduced-motion:reduce){#unsloth-shared-footer *,#unsloth-shared-footer *::before,#unsloth-shared-footer *::after{scroll-behavior:auto!important;animation:none!important;transition:none!important}}#unsloth-shared-footer .u-footer-links img{width:18px!important;height:18px!important}#unsloth-shared-footer{--u-ink:#171717!important;--u-muted:#646864!important;--u-paper:#fafaf8!important;--u-soft:#f1f2f0!important;color:var(--u-ink)!important;background:var(--u-paper)!important}#unsloth-shared-footer .u-performance>.u-shell{padding:96px!important;overflow:hidden!important;border:0!important;border-radius:42px!important;color:#fff!important;background:#1b1b19!important;box-shadow:0 30px 88px rgba(0,0,0,.14)!important}#unsloth-shared-footer .u-footer{padding:98px 0 40px!important}@media(max-width:991px){#unsloth-shared-footer .u-performance>.u-shell{padding:68px!important}}@media(max-width:767px){#unsloth-shared-footer .u-performance>.u-shell{padding:50px 26px!important;border-radius:30px!important}}#unsloth-shared-footer .u-footer{padding:112px 0 44px!important;color:#171717!important;background:#fff!important}#unsloth-shared-footer .u-footer-grid{display:grid!important;grid-template-columns:minmax(240px,1.35fr) repeat(3,minmax(0,1fr))!important;align-items:start!important;gap:clamp(48px,5vw,84px)!important}#unsloth-shared-footer .u-footer-grid>div{min-width:0!important}#unsloth-shared-footer .u-footer .u-logo,#unsloth-shared-footer .u-footer .u-logo span{color:#171717!important}#unsloth-shared-footer .u-footer-intro p{margin-top:30px!important;color:#646864!important;font-size:15px!important}#unsloth-shared-footer .u-footer-intro p a{color:inherit!important}#unsloth-shared-footer .u-footer-grid>div>h3{display:block!important;margin:0 0 28px!important;color:#171717!important;font-size:15px!important;font-weight:600!important;line-height:1.2!important;letter-spacing:-.02em!important}#unsloth-shared-footer .u-footer-grid>div>.u-footer-links{width:100%!important;height:auto!important;display:grid!important;grid-template-columns:1fr!important;gap:16px!important;padding:0!important}#unsloth-shared-footer .u-footer-grid>div>.u-footer-links a{width:fit-content!important;display:inline-flex!important;align-items:center!important;gap:10px!important;margin:0!important;color:#646864!important;font-size:15px!important;line-height:1.5!important}#unsloth-shared-footer .u-footer-grid>div>.u-footer-links a img{display:block!important}#unsloth-shared-footer .u-footer-bottom{margin-top:92px!important;padding-top:0!important;color:#858a86!important}#unsloth-shared-footer .u-footer-bottom a{color:inherit!important}@media(max-width:767px){#unsloth-shared-footer .u-footer{padding:78px 0 34px!important}#unsloth-shared-footer .u-footer-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:48px 30px!important}#unsloth-shared-footer .u-footer-intro{grid-column:1/-1!important}#unsloth-shared-footer .u-footer-grid>div>h3{margin-bottom:22px!important}#unsloth-shared-footer .u-footer-grid>div>.u-footer-links{gap:14px!important}#unsloth-shared-footer .u-footer-bottom{margin-top:68px!important}}@media(max-width:479px){#unsloth-shared-footer .u-footer-grid{gap:42px 22px!important}#unsloth-shared-footer .u-footer-bottom{align-items:flex-start!important;flex-direction:column!important}}#unsloth-shared-footer a{text-decoration:none!important}  .w-box:has(> .w-html-embed #unsloth-shared-footer > footer.u-footer)> .w-box{display:none!important}      [  unsloth ](/)
[ [email protected] ](/cdn-cgi/l/email-protection#1b686e6b6b74696f5b6e756877746f73357a72)

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
window.__remixContext = {"basename":"/","future":{"v3_fetcherPersist":false,"v3_relativeSplatPath":false,"v3_throwAbortReason":false,"v3_routeConfig":false,"v3_singleFetch":false,"v3_lazyRouteDiscovery":false,"unstable_optimizeDeps":false},"isSpaMode":false,"state":{"loaderData":{"root":null,"routes/[blog].[rl-environments]._index":{"host":"unsloth.ai","url":"https://unsloth.ai/blog/rl-environments","system":{"params":{},"search":{},"origin":"https://unsloth.ai","pathname":"/blog/rl-environments"},"resources":{},"pageMeta":{"title":"Reinforcement Learning environments and how to build them","description":"Learn what Reinforcement Learning (RL) environments are and how to build them with Unsloth and NVIDIA.","excludePageFromSearch":false,"socialImageAssetName":"rl_thumbb_l-rBjhBi0-KmQGJmPbzLn.png","custom":[]}}},"actionData":null,"errors":null}};  import "/assets/manifest-64340927.js";
import * as route0 from "/assets/root-Bi8uDDMw.js";
import * as route1 from "/assets/_blog_._rl-environments_._index-BBj4MDWU.js";

window.__remixRouteModules = {"root":route0,"routes/[blog].[rl-environments]._index":route1};

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
