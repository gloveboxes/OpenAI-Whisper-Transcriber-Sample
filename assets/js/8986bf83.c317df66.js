/*! For license information please see 8986bf83.c317df66.js.LICENSE.txt */
(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[817],{4137:(e,t,n)=>{"use strict";n.d(t,{Zo:()=>p,kt:()=>f});var r=n(7294);function o(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function i(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function a(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?i(Object(n),!0).forEach((function(t){o(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):i(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,r,o=function(e,t){if(null==e)return{};var n,r,o={},i=Object.keys(e);for(r=0;r<i.length;r++)n=i[r],t.indexOf(n)>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(r=0;r<i.length;r++)n=i[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}var l=r.createContext({}),c=function(e){var t=r.useContext(l),n=t;return e&&(n="function"==typeof e?e(t):a(a({},t),e)),n},p=function(e){var t=c(e.components);return r.createElement(l.Provider,{value:t},e.children)},u="mdxType",h={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},d=r.forwardRef((function(e,t){var n=e.components,o=e.mdxType,i=e.originalType,l=e.parentName,p=s(e,["components","mdxType","originalType","parentName"]),u=c(n),d=o,f=u["".concat(l,".").concat(d)]||u[d]||h[d]||i;return n?r.createElement(f,a(a({ref:t},p),{},{components:n})):r.createElement(f,a({ref:t},p))}));function f(e,t){var n=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var i=n.length,a=new Array(i);a[0]=d;var s={};for(var l in t)hasOwnProperty.call(t,l)&&(s[l]=t[l]);s.originalType=e,s[u]="string"==typeof e?e:o,a[1]=s;for(var c=2;c<i;c++)a[c]=n[c];return r.createElement.apply(null,a)}return r.createElement.apply(null,n)}d.displayName="MDXCreateElement"},4752:(e,t,n)=>{"use strict";n.r(t),n.d(t,{assets:()=>F,contentTitle:()=>z,default:()=>q,frontMatter:()=>M,metadata:()=>D,toc:()=>H});var r,o=n(7462),i=n(7294),a=n(4137),s=(r=function(e,t){return r=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(e,t){e.__proto__=t}||function(e,t){for(var n in t)Object.prototype.hasOwnProperty.call(t,n)&&(e[n]=t[n])},r(e,t)},function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Class extends value "+String(t)+" is not a constructor or null");function n(){this.constructor=e}r(e,t),e.prototype=null===t?Object.create(t):(n.prototype=t.prototype,new n)}),l=function(e){function t(t){var n=e.call(this,t)||this;return n.name="AssertionError",n}return s(t,e),t}(Error);function c(e,t){if(!e)throw new l(t)}function p(e){var t=Object.entries(e).filter((function(e){var t=e[1];return null!=t})).map((function(e){var t=e[0],n=e[1];return"".concat(encodeURIComponent(t),"=").concat(encodeURIComponent(String(n)))}));return t.length>0?"?".concat(t.join("&")):""}var u=n(4184),h=n.n(u),d=function(){var e=function(t,n){return e=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(e,t){e.__proto__=t}||function(e,t){for(var n in t)Object.prototype.hasOwnProperty.call(t,n)&&(e[n]=t[n])},e(t,n)};return function(t,n){if("function"!=typeof n&&null!==n)throw new TypeError("Class extends value "+String(n)+" is not a constructor or null");function r(){this.constructor=t}e(t,n),t.prototype=null===n?Object.create(n):(r.prototype=n.prototype,new r)}}(),f=function(){return f=Object.assign||function(e){for(var t,n=1,r=arguments.length;n<r;n++)for(var o in t=arguments[n])Object.prototype.hasOwnProperty.call(t,o)&&(e[o]=t[o]);return e},f.apply(this,arguments)},m=function(e,t,n,r){return new(n||(n=Promise))((function(o,i){function a(e){try{l(r.next(e))}catch(t){i(t)}}function s(e){try{l(r.throw(e))}catch(t){i(t)}}function l(e){var t;e.done?o(e.value):(t=e.value,t instanceof n?t:new n((function(e){e(t)}))).then(a,s)}l((r=r.apply(e,t||[])).next())}))},w=function(e,t){var n,r,o,i,a={label:0,sent:function(){if(1&o[0])throw o[1];return o[1]},trys:[],ops:[]};return i={next:s(0),throw:s(1),return:s(2)},"function"==typeof Symbol&&(i[Symbol.iterator]=function(){return this}),i;function s(i){return function(s){return function(i){if(n)throw new TypeError("Generator is already executing.");for(;a;)try{if(n=1,r&&(o=2&i[0]?r.return:i[0]?r.throw||((o=r.return)&&o.call(r),0):r.next)&&!(o=o.call(r,i[1])).done)return o;switch(r=0,o&&(i=[2&i[0],o.value]),i[0]){case 0:case 1:o=i;break;case 4:return a.label++,{value:i[1],done:!1};case 5:a.label++,r=i[1],i=[0];continue;case 7:i=a.ops.pop(),a.trys.pop();continue;default:if(!(o=a.trys,(o=o.length>0&&o[o.length-1])||6!==i[0]&&2!==i[0])){a=0;continue}if(3===i[0]&&(!o||i[1]>o[0]&&i[1]<o[3])){a.label=i[1];break}if(6===i[0]&&a.label<o[1]){a.label=o[1],o=i;break}if(o&&a.label<o[2]){a.label=o[2],a.ops.push(i);break}o[2]&&a.ops.pop(),a.trys.pop();continue}i=t.call(e,a)}catch(s){i=[6,s],r=0}finally{n=o=0}if(5&i[0])throw i[1];return{value:i[0]?i[1]:void 0,done:!0}}([i,s])}}},g=function(e,t){var n={};for(var r in e)Object.prototype.hasOwnProperty.call(e,r)&&t.indexOf(r)<0&&(n[r]=e[r]);if(null!=e&&"function"==typeof Object.getOwnPropertySymbols){var o=0;for(r=Object.getOwnPropertySymbols(e);o<r.length;o++)t.indexOf(r[o])<0&&Object.prototype.propertyIsEnumerable.call(e,r[o])&&(n[r[o]]=e[r[o]])}return n};const b=function(e){function t(){var t=null!==e&&e.apply(this,arguments)||this;return t.openShareDialog=function(e){var n,r,o=t.props,i=o.onShareWindowClose,a=o.windowHeight,s=void 0===a?400:a,l=o.windowPosition,c=void 0===l?"windowCenter":l,p=o.windowWidth,u=void 0===p?550:p;!function(e,t,n){var r=t.height,o=t.width,i=g(t,["height","width"]),a=f({height:r,width:o,location:"no",toolbar:"no",status:"no",directories:"no",menubar:"no",scrollbars:"yes",resizable:"no",centerscreen:"yes",chrome:"yes"},i),s=window.open(e,"",Object.keys(a).map((function(e){return"".concat(e,"=").concat(a[e])})).join(", "));if(n)var l=window.setInterval((function(){try{(null===s||s.closed)&&(window.clearInterval(l),n(s))}catch(e){console.error(e)}}),1e3)}(e,f({height:s,width:u},"windowCenter"===c?(n=u,r=s,{left:window.outerWidth/2+(window.screenX||window.screenLeft||0)-n/2,top:window.outerHeight/2+(window.screenY||window.screenTop||0)-r/2}):function(e,t){return{top:(window.screen.height-t)/2,left:(window.screen.width-e)/2}}(u,s)),i)},t.handleClick=function(e){return m(t,void 0,void 0,(function(){var t,n,r,o,i,a,s,l,c,p;return w(this,(function(u){switch(u.label){case 0:return t=this.props,n=t.beforeOnClick,r=t.disabled,o=t.networkLink,i=t.onClick,a=t.url,s=t.openShareDialogOnClick,l=t.opts,c=o(a,l),r?[2]:(e.preventDefault(),n?(p=n(),!(h=p)||"object"!=typeof h&&"function"!=typeof h||"function"!=typeof h.then?[3,2]:[4,p]):[3,2]);case 1:u.sent(),u.label=2;case 2:return s&&this.openShareDialog(c),i&&i(e,c),[2]}var h}))}))},t}return d(t,e),t.prototype.render=function(){var e=this.props,t=(e.beforeOnClick,e.children),n=e.className,r=e.disabled,o=e.disabledStyle,a=e.forwardedRef,s=(e.networkLink,e.networkName),l=(e.onShareWindowClose,e.openShareDialogOnClick,e.opts,e.resetButtonStyle),c=e.style,p=(e.url,e.windowHeight,e.windowPosition,e.windowWidth,g(e,["beforeOnClick","children","className","disabled","disabledStyle","forwardedRef","networkLink","networkName","onShareWindowClose","openShareDialogOnClick","opts","resetButtonStyle","style","url","windowHeight","windowPosition","windowWidth"])),u=h()("react-share__ShareButton",{"react-share__ShareButton--disabled":!!r,disabled:!!r},n),d=f(f(l?{backgroundColor:"transparent",border:"none",padding:0,font:"inherit",color:"inherit",cursor:"pointer"}:{},c),r&&o);return i.createElement("button",f({},p,{"aria-label":p["aria-label"]||s,className:u,onClick:this.handleClick,ref:a,style:d}),t)},t.defaultProps={disabledStyle:{opacity:.6},openShareDialogOnClick:!0,resetButtonStyle:!0},t}(i.Component);var y=function(){return y=Object.assign||function(e){for(var t,n=1,r=arguments.length;n<r;n++)for(var o in t=arguments[n])Object.prototype.hasOwnProperty.call(t,o)&&(e[o]=t[o]);return e},y.apply(this,arguments)};const v=function(e,t,n,r){function o(o,a){var s=n(o),l=y({},o);return Object.keys(s).forEach((function(e){delete l[e]})),i.createElement(b,y({},r,l,{forwardedRef:a,networkName:e,networkLink:t,opts:n(o)}))}return o.displayName="ShareButton-".concat(e),(0,i.forwardRef)(o)};const O=v("twitter",(function(e,t){var n=t.title,r=t.via,o=t.hashtags,i=void 0===o?[]:o,a=t.related,s=void 0===a?[]:a;return c(e,"twitter.url"),c(Array.isArray(i),"twitter.hashtags is not an array"),c(Array.isArray(s),"twitter.related is not an array"),"https://twitter.com/share"+p({url:e,text:n,via:r,hashtags:i.length>0?i.join(","):void 0,related:s.length>0?s.join(","):void 0})}),(function(e){return{hashtags:e.hashtags,title:e.title,via:e.via,related:e.related}}),{windowWidth:550,windowHeight:400});var k=function(){return k=Object.assign||function(e){for(var t,n=1,r=arguments.length;n<r;n++)for(var o in t=arguments[n])Object.prototype.hasOwnProperty.call(t,o)&&(e[o]=t[o]);return e},k.apply(this,arguments)},C=function(e,t){var n={};for(var r in e)Object.prototype.hasOwnProperty.call(e,r)&&t.indexOf(r)<0&&(n[r]=e[r]);if(null!=e&&"function"==typeof Object.getOwnPropertySymbols){var o=0;for(r=Object.getOwnPropertySymbols(e);o<r.length;o++)t.indexOf(r[o])<0&&Object.prototype.propertyIsEnumerable.call(e,r[o])&&(n[r[o]]=e[r[o]])}return n};function S(e){var t=function(t){var n=t.bgStyle,r=t.borderRadius,o=t.iconFillColor,a=t.round,s=t.size,l=C(t,["bgStyle","borderRadius","iconFillColor","round","size"]);return i.createElement("svg",k({viewBox:"0 0 64 64",width:s,height:s},l),a?i.createElement("circle",{cx:"32",cy:"32",r:"31",fill:e.color,style:n}):i.createElement("rect",{width:"64",height:"64",rx:r,ry:r,fill:e.color,style:n}),i.createElement("path",{d:e.path,fill:o}))};return t.defaultProps={bgStyle:{},borderRadius:0,iconFillColor:"white",size:64},t}const j=S({color:"#00aced",networkName:"twitter",path:"M48,22.1c-1.2,0.5-2.4,0.9-3.8,1c1.4-0.8,2.4-2.1,2.9-3.6c-1.3,0.8-2.7,1.3-4.2,1.6 C41.7,19.8,40,19,38.2,19c-3.6,0-6.6,2.9-6.6,6.6c0,0.5,0.1,1,0.2,1.5c-5.5-0.3-10.3-2.9-13.5-6.9c-0.6,1-0.9,2.1-0.9,3.3 c0,2.3,1.2,4.3,2.9,5.5c-1.1,0-2.1-0.3-3-0.8c0,0,0,0.1,0,0.1c0,3.2,2.3,5.8,5.3,6.4c-0.6,0.1-1.1,0.2-1.7,0.2c-0.4,0-0.8,0-1.2-0.1 c0.8,2.6,3.3,4.5,6.1,4.6c-2.2,1.8-5.1,2.8-8.2,2.8c-0.5,0-1.1,0-1.6-0.1c2.9,1.9,6.4,2.9,10.1,2.9c12.1,0,18.7-10,18.7-18.7 c0-0.3,0-0.6,0-0.8C46,24.5,47.1,23.4,48,22.1z"});const A=v("weibo",(function(e,t){var n=t.title,r=t.image;return c(e,"weibo.url"),"http://service.weibo.com/share/share.php"+p({url:e,title:n,pic:r})}),(function(e){return{title:e.title,image:e.image}}),{windowWidth:660,windowHeight:550,windowPosition:"screenCenter"});const I=S({color:"#CD201F",networkName:"weibo",path:"M40.9756152,15.0217119 C40.5000732,15.0546301 39.9999314,15.1204666 39.5325878,15.2192213 C38.6634928,15.4085016 38.0977589,16.2643757 38.2863368,17.1284787 C38.4667163,18.0008129 39.3194143,18.5686519 40.1885094,18.3793715 C42.8613908,17.8115326 45.7720411,18.6427174 47.7316073,20.8153207 C49.6911735,22.996153 50.2077122,25.975254 49.3714112,28.5840234 C49.1008441,29.4316684 49.5763861,30.3533789 50.4208857,30.6249537 C51.2653852,30.8965286 52.1754769,30.4192153 52.4542425,29.5715703 C53.6349013,25.9011885 52.9133876,21.7699494 50.1585171,18.7085538 C48.0923641,16.4042776 45.2063093,15.1533848 42.3530505,15.0217119 C41.8775084,14.9970227 41.4511594,14.9887937 40.9756152,15.0217119 Z M27.9227762,19.8277737 C24.9957268,20.140498 20.863421,22.4365431 17.2312548,26.0822378 C13.2711279,30.0571148 11,34.2871065 11,37.9328012 C11,44.9032373 19.8713401,49.125 28.5786978,49.125 C39.9917329,49.125 47.600423,42.4261409 47.600423,37.1427636 C47.600423,33.9496952 44.9603397,32.1638816 42.549827,31.4149913 C41.9594976,31.2339421 41.5167516,31.1434164 41.8283133,30.3616079 C42.5006339,28.66632 42.6236176,27.1932286 41.8939054,26.1480742 C40.5328692,24.1894405 36.7203236,24.2881952 32.448635,26.0822378 C32.448635,26.0822378 31.1203949,26.6912261 31.4647526,25.6213825 C32.1206742,23.4981576 32.0304845,21.712342 31.0056075,20.6836478 C30.2840938,19.9512176 29.2510184,19.6878718 27.9227762,19.8277737 Z M42.0906819,20.6836478 C41.6233383,20.6589586 41.1723917,20.716566 40.7132466,20.8153207 C39.9671353,20.9716828 39.4997917,21.7781784 39.6637721,22.5270687 C39.8277525,23.275959 40.5574647,23.7450433 41.303576,23.5804521 C42.1972686,23.3911718 43.2057485,23.6380596 43.8616701,24.3704897 C44.5175916,25.1029198 44.6733735,26.0657797 44.3864073,26.9381118 C44.1486363,27.6705419 44.5093932,28.4770397 45.2391054,28.7156963 C45.9688176,28.9461239 46.780521,28.5922524 47.0100936,27.8598223 C47.584026,26.0740087 47.2396661,24.0248493 45.8950269,22.5270687 C44.886547,21.4078489 43.4845162,20.7494842 42.0906819,20.6836478 Z M29.496988,29.9665891 C35.3100922,30.1723275 39.9917329,33.0691319 40.3852858,37.0769272 C40.8362324,41.6607904 35.5970585,45.9319315 28.6442899,46.6232144 C21.6915214,47.3144973 15.6488446,44.154347 15.197898,39.5787128 C14.7469514,34.9948495 20.059916,30.7237084 27.004486,30.0324256 C27.8735831,29.950131 28.6688875,29.9336709 29.496988,29.9665891 Z M25.5614586,34.3776322 C23.183744,34.5916017 20.9372116,35.9577073 19.9205332,37.9328012 C18.5348994,40.6238672 19.9041362,43.6029661 23.0689567,44.582284 C26.340366,45.5945202 30.1857056,44.0638213 31.5303448,41.1587879 C32.8503864,38.3195909 31.1613894,35.3734082 27.9227762,34.5751416 C27.1438688,34.3776322 26.356763,34.3035667 25.5614586,34.3776322 Z M24.052839,38.7228388 C24.3316067,38.7310678 24.5857748,38.8215935 24.8399449,38.9203482 C25.8648218,39.3400561 26.1845841,40.4428158 25.5614586,41.4221338 C24.9219361,42.3932227 23.5690963,42.8623069 22.5442194,42.4096807 C21.5357395,41.9652856 21.2487754,40.8542948 21.8882979,39.9078951 C22.3638421,39.2001542 23.2247386,38.7146097 24.052839,38.7228388 Z"});const W=v("facebook",(function(e,t){var n=t.quote,r=t.hashtag;return c(e,"facebook.url"),"https://www.facebook.com/sharer/sharer.php"+p({u:e,quote:n,hashtag:r})}),(function(e){return{quote:e.quote,hashtag:e.hashtag}}),{windowWidth:550,windowHeight:400});const x=S({color:"#3b5998",networkName:"facebook",path:"M34.1,47V33.3h4.6l0.7-5.3h-5.3v-3.4c0-1.5,0.4-2.6,2.6-2.6l2.8,0v-4.8c-0.5-0.1-2.2-0.2-4.1-0.2 c-4.1,0-6.9,2.5-6.9,7V28H24v5.3h4.6V47H34.1z"});const P=v("email",(function(e,t){var n=t.subject,r=t.body,o=t.separator;return"mailto:"+p({subject:n,body:r?r+o+e:e})}),(function(e){return{subject:e.subject,body:e.body,separator:e.separator||" "}}),{openShareDialogOnClick:!1,onClick:function(e,t){window.location.href=t}});const E=S({color:"#7f7f7f",networkName:"email",path:"M17,22v20h30V22H17z M41.1,25L32,32.1L22.9,25H41.1z M20,39V26.6l12,9.3l12-9.3V39H20z"});const N=v("linkedin",(function(e,t){var n=t.title,r=t.summary,o=t.source;return c(e,"linkedin.url"),"https://linkedin.com/shareArticle"+p({url:e,mini:"true",title:n,summary:r,source:o})}),(function(e){return{title:e.title,summary:e.summary,source:e.source}}),{windowWidth:750,windowHeight:600});const T=S({color:"#007fb1",networkName:"linkedin",path:"M20.4,44h5.4V26.6h-5.4V44z M23.1,18c-1.7,0-3.1,1.4-3.1,3.1c0,1.7,1.4,3.1,3.1,3.1 c1.7,0,3.1-1.4,3.1-3.1C26.2,19.4,24.8,18,23.1,18z M39.5,26.2c-2.6,0-4.4,1.4-5.1,2.8h-0.1v-2.4h-5.2V44h5.4v-8.6 c0-2.3,0.4-4.5,3.2-4.5c2.8,0,2.8,2.6,2.8,4.6V44H46v-9.5C46,29.8,45,26.2,39.5,26.2z"});function _(e){let{page_url:t,image_url:n,title:r,hashtags:o,hashtag:a,description:s}=e;return i.createElement("div",null,i.createElement(O,{url:t,title:s,hashtags:[o]},i.createElement(j,{size:32,round:!0})),"\xa0",i.createElement(A,{url:t,image:n},i.createElement(I,{size:32,round:!0})),"\xa0",i.createElement(W,{url:t,quote:r,hashtag:a},i.createElement(x,{size:32,round:!0})),"\xa0",i.createElement(N,{title:r,url:t},i.createElement(T,{size:32,round:!0})),"\xa0",i.createElement(P,{subject:r,body:s,url:t},i.createElement(E,{size:32,round:!0})))}const M={sidebar_position:0,slug:"/"},z=void 0,D={unversionedId:"Introduction",id:"Introduction",title:"Introduction",description:"<Social",source:"@site/docs/10-Introduction.md",sourceDirName:".",slug:"/",permalink:"/OpenAI-Whisper-Transcriber-Sample/",draft:!1,editUrl:"https://github.com/gloveboxes/OpenAI-Whisper-Transcriber-Sample/tree/master/docs/docs/10-Introduction.md",tags:[],version:"current",sidebarPosition:0,frontMatter:{sidebar_position:0,slug:"/"},sidebar:"tutorialSidebar",next:{title:"Whisper server setup",permalink:"/OpenAI-Whisper-Transcriber-Sample/Whisper-Server/Whisper-Server-Setup"}},F={},H=[{value:"What is OpenAI Whisper?",id:"what-is-openai-whisper",level:2},{value:"What are OpenAI Functions",id:"what-are-openai-functions",level:2},{value:"OpenAI Function Examples",id:"openai-function-examples",level:3},{value:"Running OpenAI Whisper Sample",id:"running-openai-whisper-sample",level:2},{value:"Solution Architecture",id:"solution-architecture",level:2}],R={toc:H},Z="wrapper";function q(e){let{components:t,...r}=e;return(0,a.kt)(Z,(0,o.Z)({},R,r,{components:t,mdxType:"MDXLayout"}),(0,a.kt)(_,{page_url:"https://gloveboxes.github.io/OpenAI-Whisper-Transcriber-Sample",image_url:"https://gloveboxes.github.io/OpenAI-Whisper-Transcriber-Sample/assets/images/whispering-wide-66e027604c6c49af3c4a05b6144b2f40.jpeg",title:"OpenAI Whisper Transcriber",description:"\ud83c\udfed Get started with OpenAI Whisper Speech to Text Transcription",hashtags:"OpenAI",hashtag:"",mdxType:"Social"}),(0,a.kt)("p",null,(0,a.kt)("img",{src:n(9979).Z,width:"1024",height:"533"})),(0,a.kt)("h1",{id:"build-a-home-assistant-with-openai-whisper-and-functions"},"Build a home assistant with OpenAI Whisper and Functions"),(0,a.kt)("p",null,"OpenAI Whisper is a speech-to-text transcription library that uses the ",(0,a.kt)("a",{parentName:"p",href:"https://openai.com/research/whisper"},"OpenAI Whisper")," models. "),(0,a.kt)("p",null,"The whisper model is available as a cloud ",(0,a.kt)("a",{parentName:"p",href:"https://platform.openai.com/docs/guides/speech-to-text"},"Speech to text API")," from OpenAI or you can run the Whisper model locally. This sample demonstrates how to run the Whisper model locally with the ",(0,a.kt)("a",{parentName:"p",href:"https://pypi.org/project/openai-whisper/"},"openai-whisper")," library to transcribe audio files."),(0,a.kt)("h2",{id:"what-is-openai-whisper"},"What is OpenAI Whisper?"),(0,a.kt)("p",null,"The OpenAI Whisper model is an Open Source speech-to-text transcription model that is trained on 680,000 hours of multilingual and multitask supervised data collected from the web. "),(0,a.kt)("p",null,"OpenAI describes Whisper as an",(0,a.kt)("a",{parentName:"p",href:"https://kikaben.com/transformers-encoder-decoder/"},"encoder-decoder transformer"),", a type of neural network that can use context gleaned from input data to learn associations that can then be translated into the model's output."),(0,a.kt)("p",null,"Quotes from the ",(0,a.kt)("a",{parentName:"p",href:"https://openai.com/research/whisper"},"OpenAI Whisper")," webpage:"),(0,a.kt)("blockquote",null,(0,a.kt)("p",{parentName:"blockquote"},"We\u2019ve trained and are open-sourcing a neural net called Whisper that approaches human level robustness and accuracy on English speech recognition.")),(0,a.kt)("blockquote",null,(0,a.kt)("p",{parentName:"blockquote"},"Whisper is an automatic speech recognition (ASR) system trained on 680,000 hours of multilingual and multitask supervised data collected from the web. We show that the use of such a large and diverse dataset leads to improved robustness to accents, background noise and technical language. Moreover, it enables transcription in multiple languages, as well as translation from those languages into English. We are open-sourcing models and inference code to serve as a foundation for building useful applications and for further research on robust speech processing.")),(0,a.kt)("h2",{id:"what-are-openai-functions"},"What are OpenAI Functions"),(0,a.kt)("p",null,"OpenAI Function is a way to describe functions to gpt-3.5-turbo-0613 and gpt-4-0613 models and later, and have the model intelligently choose to output a JSON object containing arguments to call those functions. The Chat Completions API does not call the function; instead, the model generates JSON that you can use to call the function in your code."),(0,a.kt)("p",null,"It's important to note that the model does not call the function, it generates the arguments to call the function. The function is called by the client code - ie your code!"),(0,a.kt)("p",null,"You can read more about OpenAI Functions in the ",(0,a.kt)("a",{parentName:"p",href:"https://platform.openai.com/docs/guides/gpt/function-calling"},"OpenAI Functions documentation"),"."),(0,a.kt)("h3",{id:"openai-function-examples"},"OpenAI Function Examples"),(0,a.kt)("p",null,"Here are two examples of OpenAI Functions. Take a moment to review the following JSON OpenAI Function definitions, you'll see a function name, description, parameters and and a series of properties that describe the function and its schema. You can define and pass multiple function definitions to the OpenAI Chat Completion API."),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-json"},'{\n    "name": "get_current_weather",\n    "description": "Get the current weather in a given location",\n    "parameters": {\n        "type": "object",\n        "properties": {\n            "location": {\n                "type": "string",\n                "description": "The city and state, e.g. San Francisco, CA"\n            },\n            "unit": {\n                "type": "string",\n                "enum": ["celsius", "fahrenheit"]\n            }\n        },\n        "required": ["location"]\n    }\n}\n')),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-json"},'light_state = {\n    "name": "set_light_state",\n    "description": "Turn a light on or off and sets it to a given color and brightness",\n    "parameters": {\n        "type": "object",\n        "properties": {\n            "device": {\n                "type": "string",\n                "description": "The name of the light"\n            },\n            "state": {\n                "type": "string",\n                "enum": ["on", "off"]\n            },\n            "brightness": {\n                "type": "string",\n                "enum": ["low", "medium", "high"]\n            },\n            "color": {\n                "type": "string",\n                "enum": ["red", "white", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "magenta", "lime", "indigo", "teal", "olive", "brown", "black", "grey", "silver", "gold", "bronze", "platinum", "rainbow"]\n            }\n        },\n        "required": ["device"]\n    }\n}\n')),(0,a.kt)("p",null,"The function definition along with the prompt is passed to the OpenAI Chat Completion API. The GPT model then attempts to populate a JSON object matching one of the function definition passed in. If there is a successful match, the chat completion API returns the function name and the JSON object/entity. "),(0,a.kt)("p",null,"It's then up to your app to decide what to do with the returned data. Your app might be an agent that calls the function, or it might save the extracted entity to a database for later processing."),(0,a.kt)("h2",{id:"running-openai-whisper-sample"},"Running OpenAI Whisper Sample"),(0,a.kt)("p",null,"The Whisper model runs best on an NVidia GPU from WSL2 or Linux. The sample code will run on a CPU, both Intel and Apple Silicon are supported, but transcription will be slower. If you are running the model on a CPU then it's recommended to use smaller Whisper models for the transcriptions."),(0,a.kt)("h2",{id:"solution-architecture"},"Solution Architecture"),(0,a.kt)("p",null,"The solution is divided into two parts:"),(0,a.kt)("ol",null,(0,a.kt)("li",{parentName:"ol"},"A Whisper service, that wraps the ",(0,a.kt)("a",{parentName:"li",href:"https://pypi.org/project/openai-whisper/"},"openai-whisper")," library and loads the Whisper model, and exposes the model as a REST API."),(0,a.kt)("li",{parentName:"ol"},"A Whisper client, that calls the Whisper service to transcribe audio files. There are two clients:",(0,a.kt)("ol",{parentName:"li"},(0,a.kt)("li",{parentName:"ol"},"A GUI client that runs on Windows, macOS, and Linux."),(0,a.kt)("li",{parentName:"ol"},"A Web client.")))),(0,a.kt)("p",null,"The advantage of this architecture is the model is loaded once by the Whisper service, a relatively time-consuming process, and then called multiple times by the Whisper clients."),(0,a.kt)("p",null,(0,a.kt)("img",{src:n(5675).Z,width:"1920",height:"1080"})))}q.isMDXComponent=!0},4184:(e,t)=>{var n;!function(){"use strict";var r={}.hasOwnProperty;function o(){for(var e=[],t=0;t<arguments.length;t++){var n=arguments[t];if(n){var i=typeof n;if("string"===i||"number"===i)e.push(n);else if(Array.isArray(n)){if(n.length){var a=o.apply(null,n);a&&e.push(a)}}else if("object"===i){if(n.toString!==Object.prototype.toString&&!n.toString.toString().includes("[native code]")){e.push(n.toString());continue}for(var s in n)r.call(n,s)&&n[s]&&e.push(s)}}}return e.join(" ")}e.exports?(o.default=o,e.exports=o):void 0===(n=function(){return o}.apply(t,[]))||(e.exports=n)}()},5675:(e,t,n)=>{"use strict";n.d(t,{Z:()=>r});const r=n.p+"assets/images/architecture-c4e0fe57c3b85cc80ecfae7b0249b08f.png"},9979:(e,t,n)=>{"use strict";n.d(t,{Z:()=>r});const r=n.p+"assets/images/whispering-wide-66e027604c6c49af3c4a05b6144b2f40.jpeg"}}]);