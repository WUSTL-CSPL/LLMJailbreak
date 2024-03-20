var _____WB$wombat$assign$function_____ = function(name) {return (self._wb_wombat && self._wb_wombat.local_init && self._wb_wombat.local_init(name)) || self[name]; };
if (!self.__WB_pmw) { self.__WB_pmw = function(obj) { this.__WB_source = obj; return this; } }
{
  let window = _____WB$wombat$assign$function_____("window");
  let self = _____WB$wombat$assign$function_____("self");
  let document = _____WB$wombat$assign$function_____("document");
  let location = _____WB$wombat$assign$function_____("location");
  let top = _____WB$wombat$assign$function_____("top");
  let parent = _____WB$wombat$assign$function_____("parent");
  let frames = _____WB$wombat$assign$function_____("frames");
  let opener = _____WB$wombat$assign$function_____("opener");

import{e as _,d as f,s as w,a as v}from"./usePageTransition.b4e70269.js";import{_ as x,o,c as i,b as m,F as y,x as H,C as T,l as p,w as C,f as L,m as k,a as $,u as z}from"./entry.55cac59a.js";import{u as E}from"./useAsyncNavigationData.6e72d51b.js";import{u as M}from"./usePageLoading.a044c130.js";const N={data(){return{isMounted:!1,windowHeight:0}},setup(){return{pageTheme:_()}},computed:{classes(){return[]},themeClass(){return`theme-${this.pageTheme??"light-gray"}`},lineCount(){return this.isMounted?Math.ceil(this.windowHeight/24):36}},mounted(){this.isMounted=!0,this.windowHeight=window.innerHeight,window.addEventListener("resize",this.updateHeight)},beforeDestroy(){this.isMounted=!1,window.removeEventListener("resize",this.updateHeight)},methods:{updateHeight(){this.windowHeight=window.innerHeight}}},A={class:"flex items-center h-full"},S={class:"w-full mt-spacing-7 pb-spacing-7","aria-hidden":"true"};function b(a,s,r,n,u,e){return o(),i("div",{class:p([e.themeClass,"fixed inset-0 z-[999] shutter-transition"])},[m("div",A,[m("div",S,[(o(!0),i(y,null,H(e.lineCount,t=>(o(),i("div",{key:t,class:"shutter-row overflow-hidden",style:T(`--shutter-delay: ${(e.lineCount-t)*7.5}ms`)},null,4))),128))])])],2)}const B=x(N,[["render",b]]),q={__name:"app",async setup(a){var d,h;let s,r;const n=f(),{data:u,error:e}=([s,r]=C(()=>E()),s=await s,r(),s);!e.value&&w((d=u.value)==null?void 0:d.navigation),!e.value&&v((h=u.value)==null?void 0:h.social);const t=L(),c=M();return t.hook("page:start",()=>{c.value=!0,document.documentElement.classList.remove("scroll-smooth")}),t.hook("page:finish",()=>{const l=n.value=="simple"?150:600;c.value=!1,setTimeout(()=>{n.value="simple"},l+100)}),t.hook("page:transition:finish",()=>{window.scrollTo(0,0),document.documentElement.classList.add("scroll-smooth")}),(l,P)=>{const g=B;return o(),i("div",{class:p(`${z(n)}-transition`)},[k(l.$slots,"default"),$(g)],2)}}};export{q as default};


}
/*
     FILE ARCHIVED ON 12:00:22 Jun 28, 2023 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 19:20:03 Mar 18, 2024.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  exclusion.robots: 0.078
  exclusion.robots.policy: 0.067
  cdx.remote: 0.097
  esindex: 0.009
  LoadShardBlock: 149.314 (6)
  PetaboxLoader3.datanode: 72.362 (7)
  PetaboxLoader3.resolve: 73.688 (2)
  load_resource: 63.121
*/