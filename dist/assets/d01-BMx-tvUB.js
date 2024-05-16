import{o as l,c as u,b as h,a as s,w as y,v as p,d as m,t as b,e as f,F as v,u as w}from"./index-DqfKCZJy.js";import{N as g}from"./Navbar-DzpSwXSp.js";import{H as R}from"./HeaderAI-CRuXBWid.js";const E=s("h1",null,"Day 1 - No Time for a Taxicab",-1),N=s("h2",null,"Part one",-1),T=s("p",null,` Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th. Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck! You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further. The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection. There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination? For example: Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away. R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away. R5, L5, R5, R3 leaves you 12 blocks away. How many blocks away is Easter Bunny HQ? `,-1),D={key:0},z=s("h2",null,"Part two",-1),B=s("p",null," Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice. For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East. How many blocks away is the first location you visit twice? ",-1),C={key:0},H={setup(){return{router:w()}},data(){return{input:"",distance:null,input2:"",distance2:null}},methods:{solve(){const r=this.input.split(",").map(o=>o.trim());let a=0,e=0,t=0;for(const o of r){const n=o[0],i=Number(o.slice(1));switch(a=(a+(n==="R"?1:3))%4,a){case 0:t+=i;break;case 1:e+=i;break;case 2:t-=i;break;case 3:e-=i;break}}this.distance=Math.abs(e)+Math.abs(t)},solvePart2(){const r=this.input2.split(",").map(n=>n.trim());let a=0,e=0,t=0;const o=new Set(["0,0"]);for(const n of r){const i=n[0],k=Number(n.slice(1));a=(a+(i==="R"?1:3))%4;for(let c=0;c<k;c++){switch(a){case 0:t++;break;case 1:e++;break;case 2:t--;break;case 3:e--;break}const d=`${e},${t}`;if(o.has(d)){this.distance2=Math.abs(e)+Math.abs(t);return}o.add(d)}}}}},_=Object.assign(H,{__name:"d01",setup(r){const a=["Un essai pour résoudre le jour 1 de l'Advent of Code 2016 avec Github Copilot"];return(e,t)=>(l(),u(v,null,[h(g),h(R,{msg:a}),s("main",null,[E,N,T,y(s("textarea",{"onUpdate:modelValue":t[0]||(t[0]=o=>e.input=o),placeholder:"Enter instructions, separated by commas"},null,512),[[p,e.input]]),s("button",{onClick:t[1]||(t[1]=(...o)=>e.solve&&e.solve(...o))},"Solve"),s("p",null,[m("Distance: "),e.distance!==null?(l(),u("span",D,b(e.distance),1)):f("",!0)]),z,B,y(s("textarea",{"onUpdate:modelValue":t[2]||(t[2]=o=>e.input2=o),placeholder:"Enter instructions, separated by commas"},null,512),[[p,e.input2]]),s("button",{onClick:t[3]||(t[3]=(...o)=>e.solvePart2&&e.solvePart2(...o))},"Solve Part 2"),s("p",null,[m("Distance to first location visited twice: "),e.distance2!==null?(l(),u("span",C,b(e.distance2),1)):f("",!0)])])],64))}});export{_ as default};
