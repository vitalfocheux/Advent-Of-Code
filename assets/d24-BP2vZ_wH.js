import{o as f,c as b,b as d,a as s,w as p,v as c,t as m,F as y,u as B}from"./index-bEcdERby.js";import{N as S}from"./Navbar-BPawfkg-.js";import{H as w}from"./HeaderAI-Cqe6IO_o.js";const v=s("h1",null,"Day 24 - Electromagnetic Moat",-1),k=s("h2",null,"Part one",-1),C=s("p",null," The CPU itself is a large, black building surrounded by a bottomless pit. Enormous metal tubes extend outward from the side of the building at regular intervals and descend down into the void. There's no way to cross, but you need to get inside. No way, of course, other than building a bridge out of the magnetic components strewn about nearby. Each component has two ports, one on each end. The ports come in all different types, and only matching types can be connected. You take an inventory of the components by their port types (your puzzle input). Each port is identified by the number of pins it uses; more pins mean a stronger connection for your bridge. A 3/7 component, for example, has a type-3 port on one side, and a type-7 port on the other. Your side of the pit is metallic; a perfect surface to connect a magnetic, zero-pin port. Because of this, the first port you use must be of type 0. It doesn't matter what type of port you end with; your goal is just to make the bridge as strong as possible. The strength of a bridge is the sum of the port types in each component. For example, if your bridge is made of components 0/3, 3/7, and 7/4, your bridge has a strength of 0+3 + 3+7 + 7+4 = 24. For example, suppose you had the following components: 0/2 2/2 2/3 3/4 3/5 0/1 10/1 9/10 With them, you could make the following valid bridges: 0/1 0/1--10/1 0/1--10/1--9/10 0/2 0/2--2/3 0/2--2/3--3/4 0/2--2/3--3/5 0/2--2/2 0/2--2/2--2/3 0/2--2/2--2/3--3/4 0/2--2/2--2/3--3/5 (Note how, as shown by 10/1, order of ports within a component doesn't matter. However, you may only use each port on a component once.) Of these bridges, the strongest one is 0/1--10/1--9/10; it has a strength of 0+1 + 1+10 + 10+9 = 31. What is the strength of the strongest bridge you can make with the components you have available? ",-1),I=s("h2",null,"Part two",-1),L=s("p",null," The bridge you've built isn't long enough; you can't jump the rest of the way. In the example above, there are two longest bridges: 0/2--2/2--2/3--3/4 0/2--2/2--2/3--3/5 Of them, the one which uses the 3/5 component is stronger; its strength is 0+2 + 2+2 + 2+3 + 3+5 = 19. What is the strength of the longest bridge you can make? If you can make multiple bridges of the longest length, pick the strongest one. ",-1),N={setup(){return{router:B()}},data(){return{components:"",strongestBridge:null,componentsInput:"",longestStrongestBridge:null}},methods:{calculateStrongestBridge(){const n=this.components.split(`
`).map(r=>r.split("/").map(Number));this.strongestBridge=this.findStrongestBridge(n,0)},findStrongestBridge(n,r){let t=0;for(let o=0;o<n.length;o++){const e=n[o];if(e.includes(r)){const i=[...n];i.splice(o,1);const a=e[0]===r?e[1]:e[0],l=e[0]+e[1]+this.findStrongestBridge(i,a);t=Math.max(t,l)}}return t},calculateLongestStrongestBridge(){const n=this.componentsInput.split(`
`).map(r=>r.split("/").map(Number));this.longestStrongestBridge=this.findLongestStrongestBridge(n,0).strength},findLongestStrongestBridge(n,r){let t=0,o=0;for(let e=0;e<n.length;e++){const i=n[e];if(i.includes(r)){const a=[...n];a.splice(e,1);const l=i[0]===r?i[1]:i[0],h=this.findLongestStrongestBridge(a,l),g=1+h.length,u=i[0]+i[1]+h.strength;(g>o||g===o&&u>t)&&(o=g,t=u)}}return{length:o,strength:t}}}},P=Object.assign(N,{__name:"d24",setup(n){const r=["Un essai pour résoudre le jour 24 de l'Advent of Code avec Github Copilot"];return(t,o)=>(f(),b(y,null,[d(S),d(w,{msg:r}),s("main",null,[v,k,C,p(s("textarea",{"onUpdate:modelValue":o[0]||(o[0]=e=>t.components=e),placeholder:"Enter components here"},null,512),[[c,t.components]]),s("button",{onClick:o[1]||(o[1]=(...e)=>t.calculateStrongestBridge&&t.calculateStrongestBridge(...e))},"Calculate Strongest Bridge"),s("p",null,"Strength of the strongest bridge: "+m(t.strongestBridge),1),I,L,p(s("textarea",{"onUpdate:modelValue":o[2]||(o[2]=e=>t.componentsInput=e),placeholder:"Enter components here"},null,512),[[c,t.componentsInput]]),s("button",{onClick:o[3]||(o[3]=(...e)=>t.calculateLongestStrongestBridge&&t.calculateLongestStrongestBridge(...e))},"Calculate Longest Strongest Bridge"),s("p",null,"Strength of the longest strongest bridge: "+m(t.longestStrongestBridge),1)])],64))}});export{P as default};
