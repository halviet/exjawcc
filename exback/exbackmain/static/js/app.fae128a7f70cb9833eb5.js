webpackJsonp([1],{"++C5":function(e,t){e.exports="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTciIGhlaWdodD0iMTciIHZpZXdCb3g9IjAgMCAxNyAxNyIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTExLjMyODMgOC40OTk5NkwxMi43NDI2IDkuOTE0MThMMTUuNTcxIDcuMDg1NzVDMTcuMTMzMSA1LjUyMzY1IDE3LjEzMzEgMi45OTA5OSAxNS41NzEgMS40Mjg5QzE0LjAwODkgLTAuMTMzMiAxMS40NzYyIC0wLjEzMzIgOS45MTQxMyAxLjQyODlMNy4wODU3MSA0LjI1NzMyTDguNDk5OTIgNS42NzE1NEwxMS4zMjgzIDIuODQzMTFDMTIuMTA5NCAyLjA2MjA2IDEzLjM3NTcgMi4wNjIwNiAxNC4xNTY4IDIuODQzMTFDMTQuOTM3OCAzLjYyNDE2IDE0LjkzNzggNC44OTA0OSAxNC4xNTY4IDUuNjcxNTRMMTEuMzI4MyA4LjQ5OTk2WiIgZmlsbD0iI0NDQ0NDQyIvPgo8cGF0aCBkPSJNOC40OTk5NiAxMS4zMjg1TDkuOTE0MTggMTIuNzQyN0w3LjA4NTc1IDE1LjU3MTFDNS41MjM2NSAxNy4xMzMyIDIuOTkwOTkgMTcuMTMzMiAxLjQyODkgMTUuNTcxMUMtMC4xMzMyIDE0LjAwOSAtMC4xMzMyIDExLjQ3NjQgMS40Mjg5IDkuOTE0MjVMNC4yNTczMiA3LjA4NTgzTDUuNjcxNTQgOC41MDAwNEwyLjg0MzExIDExLjMyODVDMi4wNjIwNiAxMi4xMDk1IDIuMDYyMDYgMTMuMzc1OCAyLjg0MzExIDE0LjE1NjlDMy42MjQxNiAxNC45Mzc5IDQuODkwNDkgMTQuOTM3OSA1LjY3MTU0IDE0LjE1NjlMOC40OTk5NiAxMS4zMjg1WiIgZmlsbD0iI0NDQ0NDQyIvPgo8cGF0aCBkPSJNMTEuMzI4NCA3LjA4NTY4QzExLjcxODkgNi42OTUxNiAxMS43MTg5IDYuMDYxOTkgMTEuMzI4NCA1LjY3MTQ3QzEwLjkzNzkgNS4yODA5NCAxMC4zMDQ3IDUuMjgwOTQgOS45MTQxOCA1LjY3MTQ3TDUuNjcxNTQgOS45MTQxMUM1LjI4MTAxIDEwLjMwNDYgNS4yODEwMSAxMC45Mzc4IDUuNjcxNTQgMTEuMzI4M0M2LjA2MjA2IDExLjcxODggNi42OTUyMiAxMS43MTg4IDcuMDg1NzUgMTEuMzI4M0wxMS4zMjg0IDcuMDg1NjhaIiBmaWxsPSIjQ0NDQ0NDIi8+Cjwvc3ZnPgo="},GDaZ:function(e,t){},NHnr:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var i=r("//Fk"),n=r.n(i),a=r("mtWM"),s=r.n(a),c=r("aLYK"),o=r("7+uW"),M={render:function(){var e=this.$createElement,t=this._self._c||e;return t("div",{attrs:{id:"app"}},[t("router-view")],1)},staticRenderFns:[]};var u=r("VU/8")({name:"App"},M,!1,function(e){r("rx3M")},null,null).exports,l=r("/ocq"),p=r("Xxa5"),g=r.n(p),N=r("exGp"),T=r.n(N),D={name:"share-link",methods:{copyPromo:function(){try{navigator.clipboard.writeText(window.location.href),this.triggerPopup()}catch(e){throw e}},triggerPopup:function(){this.$emit("popupCopied")}}},d={render:function(){var e=this.$createElement,t=this._self._c||e;return t("div",{staticClass:"share",on:{click:this.copyPromo}},[t("img",{attrs:{src:r("++C5"),alt:"Share"}})])},staticRenderFns:[]};var I=r("VU/8")(D,d,!1,function(e){r("SNO6")},"data-v-1f4a1fdf",null).exports,x={name:"base-release",props:{release:{type:Object,required:!0}}},h={render:function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"release"},[r("img",{staticClass:"cover",attrs:{src:e.release.cover_resized,alt:e.release.title}}),e._v(" "),r("div",{staticClass:"release__info"},[r("h3",{staticClass:"name"},[e._v(e._s(e.release.title))]),e._v(" "),r("p",{staticClass:"artist"},[e._v(e._s(e.release.name))])])])},staticRenderFns:[]};var f=r("VU/8")(x,h,!1,function(e){r("upL+")},"data-v-4b21d9c6",null).exports,m={name:"platform-link",props:{title:{type:String,required:!0},icon:{type:String,required:!0},url:{type:String,required:!0},vision:{type:Boolean,required:!0}},methods:{redirect:function(){window.location.href=this.url}}},j={render:function(){var e=this,t=e.$createElement,i=e._self._c||t;return e.vision?i("div",{staticClass:"platform__wrapper",on:{click:e.redirect}},[i("div",{staticClass:"platform__info"},[i("img",{attrs:{src:e.icon,alt:e.title}}),e._v(" "),i("span",{staticClass:"platform__name"},[e._v(e._s(e.title))])]),e._v(" "),i("div",{staticClass:"platform__btn"},[i("img",{attrs:{src:r("cXxo"),alt:"Слушать на "+e.title}})])]):e._e()},staticRenderFns:[]};var v=r("VU/8")(m,j,!1,function(e){r("gOzI")},"data-v-1a13c2bc",null).exports,z={components:{PlatformLink:v},props:{link:{type:Array,required:!0}}},A={render:function(){var e=this.$createElement,t=this._self._c||e;return t("div",{staticClass:"list__wrapper"},this._l(this.link,function(e){return t("platform-link",{key:e.id,attrs:{title:e.platform.title,icon:e.platform.icon,url:e.url,vision:e.vision}})}),1)},staticRenderFns:[]};var _=r("VU/8")(z,A,!1,function(e){r("h60C")},"data-v-3da4a30b",null).exports,O={render:function(){this.$createElement;this._self._c;return this._m(0)},staticRenderFns:[function(){var e=this.$createElement,t=this._self._c||e;return t("div",{staticClass:"showmsg"},[t("span",[this._v("Ссылка скопирована!")])])}]};var C={components:{SharedMsg:r("VU/8")({name:"shared-msg"},O,!1,function(e){r("o8Kr")},"data-v-37b940b6",null).exports,PlatformList:_,PlatformLink:v,BaseRelease:f,ShareLink:I},data:function(){return{release:{cover:"",cover_resized:"",id:"",name:"",title:"",url:"",user:"",version:""},link:[],url:window.location.pathname.substring(1).toLowerCase(),showPopup:!1}},methods:{fetchRelease:function(){var e=this;return T()(g.a.mark(function t(){var r,i;return g.a.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return t.prev=0,t.next=3,s.a.get("http://127.0.0.1:8000/api/release/"+e.url);case 3:return r=t.sent,e.release=r.data,t.next=7,s.a.get("http://127.0.0.1:8000/api/link/all?release="+e.release.id);case 7:i=t.sent,e.link=i.data,t.next=14;break;case 11:throw t.prev=11,t.t0=t.catch(0),t.t0;case 14:case"end":return t.stop()}},t,e,[[0,11]])}))()},triggerPopup:function(){var e=this;this.showPopup=!0,setTimeout(function(){e.showPopup=!1},3e3)}},mounted:function(){this.fetchRelease()}},L={render:function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"promo__wrapper"},[r("div",{staticClass:"share__wrapper"},[r("share-link",{on:{popupCopied:e.triggerPopup}})],1),e._v(" "),r("base-release",{attrs:{release:e.release}}),e._v(" "),r("platform-list",{attrs:{link:e.link}}),e._v(" "),e.showPopup?r("shared-msg"):e._e()],1)},staticRenderFns:[]};var w=r("VU/8")(C,L,!1,function(e){r("bQiF")},"data-v-f53bbd1a",null).exports,y={render:function(){this.$createElement;this._self._c;return this._m(0)},staticRenderFns:[function(){var e=this.$createElement,t=this._self._c||e;return t("div",{staticClass:"wrapper"},[t("h1",[this._v("404")]),this._v(" "),t("p",[this._v("Страница не существует")])])}]};var E=r("VU/8")({},y,!1,function(e){r("GDaZ")},"data-v-3b5cc830",null).exports;o.a.use(l.a);var k=new l.a({mode:"history",routes:[{path:"/:url",name:"PromoPage",component:w},{path:"/404",name:"404",component:E}]});o.a.use(c.a,s.a),o.a.config.productionTip=!1,s.a.interceptors.response.use(function(e){return e},function(e){return 404===e.response.status&&k.push({name:"404"}),n.a.reject(e.response)}),new o.a({el:"#app",router:k,components:{App:u},template:"<App/>",axios:s.a})},SNO6:function(e,t){},bQiF:function(e,t){},cXxo:function(e,t){e.exports="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkiIGhlaWdodD0iMTMiIHZpZXdCb3g9IjAgMCAxOSAxMyIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEyLjUzNzggMC44NDMyNjJMMTEuMTI2OSAyLjI2MDc4TDE0LjM5NzIgNS41MTU3NUwwLjc5MjExNCA1LjUyOTQ0TDAuNzk0MTI3IDcuNTI5NDRMMTQuMzYxOSA3LjUxNTc4TDExLjE0NjcgMTAuNzQ2TDEyLjU2NDMgMTIuMTU2OUwxOC4yMDc5IDYuNDg2ODZMMTIuNTM3OCAwLjg0MzI2MloiIGZpbGw9IiNFRUVFRUUiLz4KPC9zdmc+Cg=="},gOzI:function(e,t){},h60C:function(e,t){},o8Kr:function(e,t){},rx3M:function(e,t){},"upL+":function(e,t){}},["NHnr"]);
//# sourceMappingURL=app.fae128a7f70cb9833eb5.js.map