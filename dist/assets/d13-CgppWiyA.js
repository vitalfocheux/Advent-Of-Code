import{o as d,c as g,b as f,a as r,w as y,v as m,d as b,t as w,e as v,F as x,u as C}from"./index-bEcdERby.js";import{N as D}from"./Navbar-BPawfkg-.js";import{H as B}from"./HeaderAI-Cqe6IO_o.js";const k=r("h1",null,"Day 13 - Knights of the Dinner Table",-1),I=r("h2",null,"Part one",-1),N=r("p",null," In years past, the holiday feast with your family hasn't gone so well. Not everyone gets along! This year, you resolve, will be different. You're going to find the optimal seating arrangement and avoid all those awkward conversations. You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they were to find themselves sitting next to each other person. You have a circular table that will be just big enough to fit everyone comfortably, and so each person will have exactly two neighbors. For example, suppose you have only four attendees planned, and you calculate their potential happiness as follows: Alice would gain 54 happiness units by sitting next to Bob. Alice would lose 79 happiness units by sitting next to Carol. Alice would lose 2 happiness units by sitting next to David. Bob would gain 83 happiness units by sitting next to Alice. Bob would lose 7 happiness units by sitting next to Carol. Bob would lose 63 happiness units by sitting next to David. Carol would lose 62 happiness units by sitting next to Alice. Carol would gain 60 happiness units by sitting next to Bob. Carol would gain 55 happiness units by sitting next to David. David would gain 46 happiness units by sitting next to Alice. David would lose 7 happiness units by sitting next to Bob. David would gain 41 happiness units by sitting next to Carol. Then, if you seat Alice next to David, Alice would lose 2 happiness units (because David talks so much), but David would gain 46 happiness units (because Alice is such a good listener), for a total change of 44. If you continue around the table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). The arrangement looks like this: +41 +46 +55 David -2 Carol Alice +60 Bob +54 -7 +83 After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most optimal, with a total change in happiness of 330. What is the total change in happiness for the optimal seating arrangement of the actual guest list? ",-1),O={key:0},E=r("h2",null,"Part two",-1),M=r("p",null," In all the commotion, you realize that you forgot to seat yourself. At this point, you're pretty apathetic toward the whole thing, and your happiness wouldn't really go up or down regardless of who you sit next to. You assume everyone else would be just as ambivalent about sitting next to you, too. So, add yourself to the list, and give all happiness relationships that involve you a score of 0. What is the total change in happiness for the optimal seating arrangement that actually includes yourself? ",-1),T={key:0},V={data(){return{input:"",optimalHappiness:0,optimalHappiness2:0}},setup(){return{router:C()}},methods:{calculateOptimalHappiness(){const u=this.input.split(`
`),n={},a=new Set;u.forEach(o=>{const[l,,t,e,,,,,,,p]=o.split(" "),c=t==="gain"?parseInt(e):-parseInt(e);n[l]||(n[l]={}),n[l][p.slice(0,-1)]=c,a.add(l)});const i=Array.from(a),s=this.permute(i);let h=-1/0;s.forEach(o=>{let l=0;for(let t=0;t<o.length;t++){const e=o[(t-1+o.length)%o.length],p=o[(t+1)%o.length];l+=n[o[t]][e],l+=n[o[t]][p]}h=Math.max(h,l)}),this.optimalHappiness=h},permute(u){if(u.length<=1)return[u];const n=[];return u.forEach((a,i)=>this.permute(u.slice(0,i).concat(u.slice(i+1))).forEach(s=>{n.push([a].concat(s))})),n},calculateOptimalHappiness2(){const u=this.input.split(`
`),n={},a=new Set;u.forEach(t=>{const[e,,p,c,,,,,,,A]=t.split(" "),H=p==="gain"?parseInt(c):-parseInt(c);n[e]||(n[e]={}),n[e][A.slice(0,-1)]=H,a.add(e)});const i=Array.from(a),s=i.length,h=Array(s).fill().map(()=>Array(1<<s).fill(-1/0)),o=Array(s).fill().map(()=>Array(s).fill(0));for(let t=0;t<s;t++)for(let e=0;e<s;e++)t!==e&&(o[t][e]=n[i[t]][i[e]]+n[i[e]][i[t]]);for(let t=0;t<s;t++)h[t][1<<t]=0;for(let t=0;t<1<<s;t++)for(let e=0;e<s;e++)if(t&1<<e)for(let p=0;p<s;p++)e!==p&&t&1<<p&&(h[e][t]=Math.max(h[e][t],h[p][t^1<<e]+o[p][e]));let l=-1/0;for(let t=0;t<s;t++)l=Math.max(l,h[t][(1<<s)-1]);this.optimalHappiness2=l}}},F=Object.assign(V,{__name:"d13",setup(u){const n=["Un essai pour la partie 1 avec Github Copilot","Cinq essais pour la partie 2 avec Github Copilot"];return(a,i)=>(d(),g(x,null,[f(D),f(B,{msg:n}),r("main",null,[k,I,N,y(r("textarea",{"onUpdate:modelValue":i[0]||(i[0]=s=>a.input=s),placeholder:"Enter input here"},null,512),[[m,a.input]]),r("button",{onClick:i[1]||(i[1]=(...s)=>a.calculateOptimalHappiness&&a.calculateOptimalHappiness(...s))},"Calculate"),r("p",null,[b("Optimal happiness: "),a.optimalHappiness!==0?(d(),g("span",O,w(a.optimalHappiness),1)):v("",!0)]),E,M,y(r("textarea",{"onUpdate:modelValue":i[2]||(i[2]=s=>a.input=s),placeholder:"Enter input here"},null,512),[[m,a.input]]),r("button",{onClick:i[3]||(i[3]=(...s)=>a.calculateOptimalHappiness2&&a.calculateOptimalHappiness2(...s))},"Calculate"),r("p",null,[b("Optimal happiness: "),a.optimalHappiness2!==0?(d(),g("span",T,w(a.optimalHappiness2),1)):v("",!0)])])],64))}});export{F as default};