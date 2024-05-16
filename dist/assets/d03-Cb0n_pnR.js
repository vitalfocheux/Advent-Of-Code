import{o as p,c as d,b as h,a as n,w as m,v as g,d as f,t as b,e as c,F as v,u as y}from"./index-DqfKCZJy.js";import{N as w}from"./Navbar-DzpSwXSp.js";import{H as T}from"./HeaderAI-CRuXBWid.js";const N=n("h1",null,"Day 3 - Squares With Three Sides",-1),k=n("h2",null,"Part one",-1),P=n("p",null,` Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles. Or are they? The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones. In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25. In your puzzle input, how many of the listed triangles are possible? `,-1),S={key:0},V=n("h2",null,"Part two",-1),_=n("p",null," Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated. For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle: 101 301 501 102 302 502 103 303 503 201 401 601 202 402 602 203 403 603 In your puzzle input, and instead reading by columns, how many of the listed triangles are possible? ",-1),C={key:0},E={setup(){return{router:y()}},data(){return{input:"",possibleTriangles:0,input2:"",possibleTriangles2:0}},methods:{solve(){const o=this.input.split(`
`);let i=0;for(const t of o){const e=t.trim().split(/\s+/).map(Number).sort((s,r)=>s-r);e[0]+e[1]>e[2]&&i++}this.possibleTriangles=i},solvePart2(){const o=this.input2.split(`
`).filter(e=>e.trim()!=="");let i=0;const t=[];for(let e=0;e<o.length;e+=3){const s=[],r=[],a=[];for(let l=0;l<3;l++){const u=o[e+l].trim().split(/\s+/).map(Number);s.push(u[0]),r.push(u[1]),a.push(u[2])}t.push(s,r,a)}for(const e of t){const s=e.sort((r,a)=>r-a);s[0]+s[1]>s[2]&&i++}this.possibleTriangles2=i}}},I=Object.assign(E,{__name:"d03",setup(o){const i=["Un essai pour résoudre le jour 3 de l'Advent of Code 2016 avec Github Copilot"];return(t,e)=>(p(),d(v,null,[h(w),h(T,{msg:i}),n("main",null,[N,k,P,m(n("textarea",{"onUpdate:modelValue":e[0]||(e[0]=s=>t.input=s),placeholder:"Enter triangle sides, one line per triangle"},null,512),[[g,t.input]]),n("button",{onClick:e[1]||(e[1]=(...s)=>t.solve&&t.solve(...s))},"Solve"),n("p",null,[f("Number of possible triangles: "),t.possibleTriangles!==0?(p(),d("span",S,b(t.possibleTriangles),1)):c("",!0)]),V,_,m(n("textarea",{"onUpdate:modelValue":e[2]||(e[2]=s=>t.input2=s),placeholder:"Enter triangle sides, one line per triangle"},null,512),[[g,t.input2]]),n("button",{onClick:e[3]||(e[3]=(...s)=>t.solvePart2&&t.solvePart2(...s))},"Solve Part 2"),n("p",null,[f("Number of possible triangles for Part 2: "),t.possibleTriangles2!==0?(p(),d("span",C,b(t.possibleTriangles2),1)):c("",!0)])])],64))}});export{I as default};
