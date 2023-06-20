"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[737],{4137:(e,r,t)=>{t.d(r,{Zo:()=>c,kt:()=>g});var n=t(7294);function o(e,r,t){return r in e?Object.defineProperty(e,r,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[r]=t,e}function a(e,r){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);r&&(n=n.filter((function(r){return Object.getOwnPropertyDescriptor(e,r).enumerable}))),t.push.apply(t,n)}return t}function i(e){for(var r=1;r<arguments.length;r++){var t=null!=arguments[r]?arguments[r]:{};r%2?a(Object(t),!0).forEach((function(r){o(e,r,t[r])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):a(Object(t)).forEach((function(r){Object.defineProperty(e,r,Object.getOwnPropertyDescriptor(t,r))}))}return e}function p(e,r){if(null==e)return{};var t,n,o=function(e,r){if(null==e)return{};var t,n,o={},a=Object.keys(e);for(n=0;n<a.length;n++)t=a[n],r.indexOf(t)>=0||(o[t]=e[t]);return o}(e,r);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(n=0;n<a.length;n++)t=a[n],r.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(o[t]=e[t])}return o}var s=n.createContext({}),l=function(e){var r=n.useContext(s),t=r;return e&&(t="function"==typeof e?e(r):i(i({},r),e)),t},c=function(e){var r=l(e.components);return n.createElement(s.Provider,{value:r},e.children)},m="mdxType",u={inlineCode:"code",wrapper:function(e){var r=e.children;return n.createElement(n.Fragment,{},r)}},h=n.forwardRef((function(e,r){var t=e.components,o=e.mdxType,a=e.originalType,s=e.parentName,c=p(e,["components","mdxType","originalType","parentName"]),m=l(t),h=o,g=m["".concat(s,".").concat(h)]||m[h]||u[h]||a;return t?n.createElement(g,i(i({ref:r},c),{},{components:t})):n.createElement(g,i({ref:r},c))}));function g(e,r){var t=arguments,o=r&&r.mdxType;if("string"==typeof e||o){var a=t.length,i=new Array(a);i[0]=h;var p={};for(var s in r)hasOwnProperty.call(r,s)&&(p[s]=r[s]);p.originalType=e,p[m]="string"==typeof e?e:o,i[1]=p;for(var l=2;l<a;l++)i[l]=t[l];return n.createElement.apply(null,i)}return n.createElement.apply(null,t)}h.displayName="MDXCreateElement"},1181:(e,r,t)=>{t.r(r),t.d(r,{assets:()=>s,contentTitle:()=>i,default:()=>u,frontMatter:()=>a,metadata:()=>p,toc:()=>l});var n=t(7462),o=(t(7294),t(4137));const a={},i="Whisper Anywhere Access",p={unversionedId:"Proxies/Whisper-ngrok",id:"Proxies/Whisper-ngrok",title:"Whisper Anywhere Access",description:"If you want to access the Whisper Server running in WSL or Desktop Linux from a different computer or over the internet then you can use ngrok.",source:"@site/docs/50-Proxies/35-Whisper-ngrok.md",sourceDirName:"50-Proxies",slug:"/Proxies/Whisper-ngrok",permalink:"/OpenAI-Whisper-Transcriber-Sample/Proxies/Whisper-ngrok",draft:!1,editUrl:"https://github.com/gloveboxes/OpenAI-Whisper-Transcriber-Sample/tree/main/docs/50-Proxies/35-Whisper-ngrok.md",tags:[],version:"current",sidebarPosition:35,frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Whisper Intranet Access",permalink:"/OpenAI-Whisper-Transcriber-Sample/Proxies/Whisper-intranet"},next:{title:"Testing with Postman",permalink:"/OpenAI-Whisper-Transcriber-Sample/Testing/Whisper-Postman"}},s={},l=[{value:"Install ngrok",id:"install-ngrok",level:2}],c={toc:l},m="wrapper";function u(e){let{components:r,...a}=e;return(0,o.kt)(m,(0,n.Z)({},c,a,{components:r,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"whisper-anywhere-access"},"Whisper Anywhere Access"),(0,o.kt)("p",null,"If you want to access the Whisper Server running in WSL or Desktop Linux from a different computer or over the internet then you can use ",(0,o.kt)("a",{parentName:"p",href:"https://ngrok.com/"},"ngrok"),"."),(0,o.kt)("h2",{id:"install-ngrok"},"Install ngrok"),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("p",{parentName:"li"},"Follow the instructions to install ",(0,o.kt)("a",{parentName:"p",href:"https://ngrok.com/download"},"ngrok")," for your operating system.")),(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("p",{parentName:"li"},"From a terminal window, navigate to the folder containing the ",(0,o.kt)("inlineCode",{parentName:"p"},"ngrok")," executable.")),(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("p",{parentName:"li"},"Connect your ngrok account by running ",(0,o.kt)("inlineCode",{parentName:"p"},"ngrok config add-authtoken <token>")," where ",(0,o.kt)("inlineCode",{parentName:"p"},"<token>")," is your ngrok authentication token.")),(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("p",{parentName:"li"},"Run the following command to start the ",(0,o.kt)("inlineCode",{parentName:"p"},"ngrok")," proxy app."),(0,o.kt)("pre",{parentName:"li"},(0,o.kt)("code",{parentName:"pre",className:"language-bash"},"./ngrok http 5500\n")),(0,o.kt)("p",{parentName:"li"},"The app will start, showing the IP addresses that app is using."),(0,o.kt)("p",{parentName:"li"},(0,o.kt)("img",{src:t(1826).Z,width:"984",height:"283"})),(0,o.kt)("p",{parentName:"li"},"Ngrok is now listening for REST API calls and will forward them to the Whisper Transcriber Service running in WSL listening on port 5500.")),(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("p",{parentName:"li"},"Update the ",(0,o.kt)("inlineCode",{parentName:"p"},"Whisper server address")," in the Whisper GUI app to the ",(0,o.kt)("inlineCode",{parentName:"p"},"Forwarding")," address shown in the ",(0,o.kt)("inlineCode",{parentName:"p"},"ngrok")," app."),(0,o.kt)("p",{parentName:"li"},(0,o.kt)("img",{src:t(167).Z,width:"1213",height:"538"})))))}u.isMDXComponent=!0},1826:(e,r,t)=>{t.d(r,{Z:()=>n});const n=t.p+"assets/images/ngrok_client-6ea3cad2f116eccee67d47d366b30aff.png"},167:(e,r,t)=>{t.d(r,{Z:()=>n});const n=t.p+"assets/images/openai_whisper_gui_ngrok-66a212b7ab2e414eeb87ae054cc3dbb7.png"}}]);