"use strict";(("undefined"!=typeof self?self:global).webpackChunkopen=("undefined"!=typeof self?self:global).webpackChunkopen||[]).push([[376],{69376:(e,n,i)=>{i.r(n),i.d(n,{Album:()=>oe,default:()=>ce,getAlbumType:()=>se});var a=i(67294),t=i.n(a),l=i(47886),d=i(20657),m=i(11414),s=i(1663),o=i(94233);const r={album:"_Nn1qsmaW5fFh0gB8sff",albumWindowedMessage:"whgaqSFaW9_YAsE0qmoh",albumWindowedMessageHeader:"GeaAvTYt0xz8rm5lEZUA",albumWindowedMessageDescription:"lBSUm3vo70uxZM__c0iu",moreAlbumsByArtist:"VhjHR4rvdo0lZbYxkz4h",releasesDropdown:"JE1pe3pRP_mnIFECZCo6",footer:"VtGoS7WczH2FTL5j6DTj"};var c=i(53424),u=i(30947),k=i(55911),v=i(56802),S=i(4236),g=i(59482),N=i(72907),p=i(36685),F=i(76343),b=i(55120),y=i(20246),h=i(4232),E=i(95661),f=i(4383),A=i(98984);const C={kind:"Document",definitions:[{kind:"OperationDefinition",operation:"query",name:{kind:"Name",value:"getAlbumMetadata"},variableDefinitions:[{kind:"VariableDefinition",variable:{kind:"Variable",name:{kind:"Name",value:"uri"}},type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"ID"}}}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"album"},arguments:[{kind:"Argument",name:{kind:"Name",value:"uri"},value:{kind:"Variable",name:{kind:"Name",value:"uri"}}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"uri"}},{kind:"Field",name:{kind:"Name",value:"name"}},{kind:"FragmentSpread",name:{kind:"Name",value:"albumArtists"}},{kind:"FragmentSpread",name:{kind:"Name",value:"albumCoverArt"}},{kind:"FragmentSpread",name:{kind:"Name",value:"albumDiscs"}},{kind:"FragmentSpread",name:{kind:"Name",value:"albumTracksMetadata"}},{kind:"FragmentSpread",name:{kind:"Name",value:"albumReleases"}},{kind:"Field",name:{kind:"Name",value:"type"}},{kind:"Field",name:{kind:"Name",value:"date"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"isoString"}},{kind:"Field",name:{kind:"Name",value:"precision"}}]}},{kind:"Field",name:{kind:"Name",value:"playability"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"playable"}},{kind:"Field",name:{kind:"Name",value:"reason"}}]}},{kind:"Field",name:{kind:"Name",value:"label"}},{kind:"Field",name:{kind:"Name",value:"copyright"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"totalCount"}},{kind:"Field",name:{kind:"Name",value:"items"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"type"}},{kind:"Field",name:{kind:"Name",value:"text"}}]}}]}},{kind:"Field",name:{kind:"Name",value:"courtesyLine"}},{kind:"Field",name:{kind:"Name",value:"saved"}},{kind:"Field",name:{kind:"Name",value:"sharingInfo"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"shareUrl"}},{kind:"Field",name:{kind:"Name",value:"shareId"}}]}},{kind:"FragmentSpread",name:{kind:"Name",value:"moreAlbumsByArtist"}}]}}]}},{kind:"FragmentDefinition",name:{kind:"Name",value:"albumArtists"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Album"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"artists"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"totalCount"}},{kind:"Field",name:{kind:"Name",value:"items"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"uri"}},{kind:"Field",name:{kind:"Name",value:"profile"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"name"}}]}},{kind:"Field",name:{kind:"Name",value:"visuals"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"avatarImage"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"sources"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"url"}},{kind:"Field",name:{kind:"Name",value:"width"}},{kind:"Field",name:{kind:"Name",value:"height"}}]}}]}}]}},{kind:"Field",name:{kind:"Name",value:"sharingInfo"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"shareUrl"}}]}}]}}]}}]}},{kind:"FragmentDefinition",name:{kind:"Name",value:"albumCoverArt"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Album"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"coverArt"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"extractedColors"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"colorRaw"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"hex"}}]}}]}},{kind:"Field",name:{kind:"Name",value:"sources"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"url"}},{kind:"Field",name:{kind:"Name",value:"width"}},{kind:"Field",name:{kind:"Name",value:"height"}}]}}]}}]}},{kind:"FragmentDefinition",name:{kind:"Name",value:"albumDiscs"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Album"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"discs"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"totalCount"}},{kind:"Field",name:{kind:"Name",value:"items"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"number"}},{kind:"Field",name:{kind:"Name",value:"tracks"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"totalCount"}}]}}]}}]}}]}},{kind:"FragmentDefinition",name:{kind:"Name",value:"albumTracksMetadata"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Album"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"tracks"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"totalCount"}},{kind:"Field",name:{kind:"Name",value:"items"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"track"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"playability"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"playable"}},{kind:"Field",name:{kind:"Name",value:"reason"}}]}},{kind:"Field",name:{kind:"Name",value:"duration"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"totalMilliseconds"}}]}}]}}]}}]}}]}},{kind:"FragmentDefinition",name:{kind:"Name",value:"albumReleases"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Album"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"releases"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"totalCount"}},{kind:"Field",name:{kind:"Name",value:"items"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"uri"}},{kind:"Field",name:{kind:"Name",value:"name"}}]}}]}}]}},{kind:"FragmentDefinition",name:{kind:"Name",value:"moreAlbumsByArtist"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Album"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",alias:{kind:"Name",value:"moreAlbumsByArtist"},name:{kind:"Name",value:"artists"},arguments:[{kind:"Argument",name:{kind:"Name",value:"limit"},value:{kind:"IntValue",value:"1"}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"items"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"discography"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"popularReleases"},arguments:[{kind:"Argument",name:{kind:"Name",value:"limit"},value:{kind:"IntValue",value:"10"}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"items"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"releases"},arguments:[{kind:"Argument",name:{kind:"Name",value:"limit"},value:{kind:"IntValue",value:"1"}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"items"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"uri"}},{kind:"Field",name:{kind:"Name",value:"name"}},{kind:"Field",name:{kind:"Name",value:"date"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"year"}}]}},{kind:"Field",name:{kind:"Name",value:"coverArt"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"sources"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"url"}},{kind:"Field",name:{kind:"Name",value:"width"}},{kind:"Field",name:{kind:"Name",value:"height"}}]}}]}},{kind:"Field",name:{kind:"Name",value:"playability"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"playable"}},{kind:"Field",name:{kind:"Name",value:"reason"}}]}},{kind:"Field",name:{kind:"Name",value:"sharingInfo"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"shareId"}},{kind:"Field",name:{kind:"Name",value:"shareUrl"}}]}}]}}]}}]}}]}}]}}]}}]}}]}}]};var w=i(7073),D=i(90110),I=i(19480),T=i(13768),U=i(42811),x=i(53646),M=i(26115),P=i(74594),L=i(32626),V=i(30005),_=i(69518),B=i.n(_),R=i(21691);const W=({releases:e})=>t().createElement(V.v,null,e.map((e=>t().createElement(R.s,{key:e.uri,role:"menuitem",to:B().from(e.uri).toURLPath(!0)},e.name))));var z=i(84242),q=i(80322),Y=i(6479),Z=i.n(Y),H=i(91931),$=i(38894);const j=({children:e,content:n,onIntercept:i=(()=>{})})=>{const a=(0,$.g)();let l;try{l=t().Children.only(e)}catch(n){return t().createElement(t().Fragment,null,e)}return a?t().createElement(H.Nt,{trigger:"click",action:"open",placement:"bottom",offset:[0,20],content:n},t().cloneElement(l,{onClick:i})):t().createElement(t().Fragment,null,e)};var G=i(65858),O=i(16229),K=i(42922),Q=i(70108),X=i(1447);const J={container:"kL_8KemW8DWBQC1sXcG2"},ee=({title:e,description:n})=>{const i=(0,G.I0)(),l=(0,X.qT)(),m=(0,v.o)();return(0,a.useEffect)((()=>{m({intent:"open-upsell",type:"view"})}),[m]),t().createElement(H.yv,null,t().createElement("div",{className:J.container},t().createElement(F.Dy.p,{className:J.title,variant:F.Dy.cello},e),t().createElement(F.Dy.p,{className:J.description,variant:F.Dy.mesto},n),t().createElement("div",{className:J.buttonContainer},t().createElement(O.Y,{className:J.secondaryButton,version:"tertiary",onClick:()=>{m({intent:"close-upsell",type:"click"}),l({type:"close"})}},d.ag.get("action-trigger.button.not-now")),t().createElement(O.Y,{className:J.primaryButton,version:"primary",onClick:()=>{m({intent:"login",type:"click"}),i((0,Q.sX)())}},d.ag.get("login")))))},ne=e=>t().createElement(K.ZP,{value:"tooltip-with-cta"},t().createElement(ee,e));var ie=i(74380),ae=i(18937),te=i(6489);const le=["uri"],de=e=>{let{uri:n}=e,i=Z()(e,le);const a=(0,ie.j5)();return t().createElement(j,{content:t().createElement(ne,{title:d.ag.get("action-trigger.save-library"),description:d.ag.get("action-trigger.save-album")}),onIntercept:()=>a.storeAction(ae.wH,{operation:te.pT.ADD,uris:[n]})},t().createElement(m.H,i))};var me=i(70369);function se(e){switch(e){case w.VZ.Single:return d.ag.get("single");case w.VZ.Ep:return d.ag.get("ep");case w.VZ.Compilation:return d.ag.get("compilation");case w.VZ.Album:default:return d.ag.get("album")}}const oe=({uri:e,album:n})=>{var i,s,A,C,V,_,B,R,Y,Z,H,$,j;const G=(0,l.k6)(),O=(0,v.o)(),K=(0,S.k)(),Q=null===(i=n.moreAlbumsByArtist)||void 0===i||null===(s=i.items[0])||void 0===s||null===(A=s.discography)||void 0===A||null===(C=A.popularReleases)||void 0===C?void 0:C.items,[X,J]=(0,f.Z)(e),ee=parseInt(new URLSearchParams((0,l.TH)().search).get("index")||"0",10),ne=(0,q.Y)(e),{usePlayContextItem:ie,togglePlay:ae,isPlaying:te}=(0,z.n)({uri:ne},{featureIdentifier:"album"}),le=(0,a.useCallback)((async()=>{O({targetUri:e,intent:X?"unsave":"save",type:"click"});try{await J(!X)}catch{}}),[O,e,X,J]),oe=(0,a.useCallback)((()=>new URLSearchParams(G.location.search.slice(1)).get("highlight")||""),[G.location.search]),re=n.uri,ce=n.name,ue=n.type,ke=null===(V=n.date)||void 0===V?void 0:V.isoString,ve=n.tracks.totalCount,Se=((null===(_=n.coverArt)||void 0===_?void 0:_.sources)||[]).map((e=>({url:e.url,width:e.width||void 0,height:e.height||void 0}))),ge=null===(B=n.coverArt)||void 0===B||null===(R=B.extractedColors)||void 0===R?void 0:R.colorRaw.hex,Ne=n.artists.items.map((e=>{var n;return{name:e.profile.name,images:((null===(n=e.visuals.avatarImage)||void 0===n?void 0:n.sources)||[]).map((e=>({url:e.url,width:e.width||void 0,height:e.height||void 0}))),uri:e.uri,id:e.uri}})),pe=n.tracks.items.some((e=>e.track.playability.playable)),Fe=n.playability.reason===w.Ku.CatalogueRestricted,be=(0,a.useMemo)((()=>({total_count:n.discs.totalCount,items:n.discs.items.map((e=>({number:e.number,total_tracks:e.tracks.totalCount})))})),[n.discs]),ye=n.copyright.items,he=n.courtesyLine,Ee=n.tracks.items.reduce(((e,n)=>e+n.track.duration.totalMilliseconds),0),fe=n.tracks.items.length>0?Ee/n.tracks.items.length*n.tracks.totalCount:0,Ae=n.tracks.items.length<n.tracks.totalCount,Ce=oe(),we=K;return(0,x.Y5)(ge||null),t().createElement("section",{className:r.album,"data-testid":"album-page"},t().createElement(me.$,null,d.ag.get("album.page-title",n.name)),t().createElement(c.gF,{backgroundColor:ge},t().createElement(g.W,null,t().createElement(b.$,{size:k.qE.sm,onClick:()=>ae(),disabled:!pe,isPlaying:te,uri:e}),t().createElement(N.i,{text:ce,dragUri:e,dragLabel:ce})),t().createElement(L._P,{menu:t().createElement(h.Y,{uri:n.uri,artistUri:null==Ne||null===(Y=Ne[0])||void 0===Y?void 0:Y.uri,sharingInfo:n.sharingInfo})},t().createElement(c.Oz,{dragUri:re,images:Se,name:ce,placeholderType:"album"})),t().createElement(c.sP,null,t().createElement(c.dy,{small:!0,uppercase:!0},se(ue)),t().createElement(L._P,{menu:t().createElement(h.Y,{uri:n.uri,artistUri:null==Ne||null===(Z=Ne[0])||void 0===Z?void 0:Z.uri,sharingInfo:n.sharingInfo})},t().createElement(c.xd,{dragUri:n.uri,dragLabel:n.name},ce)),t().createElement(c.QS,{creators:Ne,releaseDate:ke,totalTracks:ve,durationMilliseconds:fe,isEstimatedDuration:Ae}))),t().createElement(u.o,{backgroundColor:ge},t().createElement(u.F,null,t().createElement(b.$,{onClick:()=>ae(),disabled:!pe,isPlaying:te,size:k.qE.lg,uri:e}),t().createElement(de,{isAdded:!!X,onClick:le,disabled:!K,size:m.q.md,uri:e}),we?t().createElement(D.o,{uri:e,isFollowing:!!X,onFollow:le,size:D.q.md}):null,t().createElement(y.y,{menu:t().createElement(h.Y,{uri:n.uri,artistUri:null==Ne||null===(H=Ne[0])||void 0===H?void 0:H.uri,sharingInfo:n.sharingInfo})},t().createElement(E.z,{label:d.ag.get("more.label.context",ce)})))),Fe?t().createElement("div",{className:r.albumWindowedMessage},t().createElement(F.Dy,{as:"h2",variant:F.Dy.cello,className:r.albumWindowedMessageHeader},d.ag.get("windowed.product-album-header")),t().createElement("div",{className:r.albumWindowedMessageDescription},d.ag.get("windowed.product-album-description"))):null,t().createElement("div",{className:"contentSpacing"},t().createElement(p.L,{ariaLabel:ce,nrTracks:ve,discs:be,albumUri:re,highlightUri:Ce,scrollToIndex:ee,usePlayContextItem:ie}),t().createElement("div",{className:r.footer},t().createElement(o.k,{copyrights:ye,courtesyLine:he}),n.releases.items.length>0&&t().createElement(L.xV,{menu:t().createElement(W,{releases:n.releases.items})},((e,i,a)=>t().createElement("button",{ref:a,className:r.releasesDropdown,type:"button",onClick:i},t().createElement(F.Dy,{as:"span",variant:F.Dy.mesto},d.ag.get("album-page.more-releases",n.releases.items.length)),e?t().createElement(M.q,{className:r.chevron,iconSize:16}):t().createElement(P.m,{className:r.chevron,iconSize:16})))))),(null==Q?void 0:Q.length)>0&&t().createElement("div",{className:"contentSpacing"},t().createElement(I.P,{className:r.moreAlbumsByArtist,title:d.ag.get("album-page.more-by-artist",null==Ne||null===($=Ne[0])||void 0===$?void 0:$.name),total:Q.length,seeAllUri:`${null==Ne||null===(j=Ne[0])||void 0===j?void 0:j.uri.replace("artist","app:artist")}:discography`,seeAllLabel:d.ag.get("artist-page.show-discography"),alwaysShowSeeAll:!0},Q.map((e=>{var n,i,a,l,d;return t().createElement(T.i,{key:null===(n=e.releases)||void 0===n||null===(i=n.items)||void 0===i||null===(a=i[0])||void 0===a?void 0:a.uri,entity:(0,U.B$)(e.releases.items[0],null==Ne||null===(l=Ne[0])||void 0===l?void 0:l.uri,null==Ne||null===(d=Ne[0])||void 0===d?void 0:d.name)})})))))},re=t().memo((()=>{var e;const{albumId:n}=(0,l.UO)(),i=`spotify:album:${n}`,a=(m={uri:i},o={cacheTime:15*A.y},(0,A.a)(C,m,o));var m,o;return a.loading||null===(e=a.data)||void 0===e||!e.album?t().createElement(s.h,{errorMessage:d.ag.get("error.not_found.title.album")}):t().createElement(oe,{uri:i,album:a.data.album})})),ce=re},38894:(e,n,i)=>{i.d(n,{g:()=>l});var a=i(65858),t=i(29255);const l=()=>(0,a.v9)(t.Gg).isAnonymous}}]);
//# sourceMappingURL=376.js.map