import{o as c,c as h,b as m,a as u,w as d,v as f,d as b,t as y,e as w,F as g,u as x}from"./index-bEcdERby.js";import{N as v}from"./Navbar-BPawfkg-.js";import{H as k}from"./HeaderAI-Cqe6IO_o.js";const N=u("h1",null,"Day 8 - Two-Factor Authentication",-1),P=u("h2",null,"Part one",-1),A=u("p",null," You come across a door implementing what you can only assume is an implementation of two-factor authentication after a long game of requirements telephone. To get past the door, you first swipe a keycard (no problem; there was one on a nearby desk). Then, it displays a code on a little screen, and you type that code on a keypad. Then, presumably, the door unlocks. Unfortunately, the screen has been smashed. After a few minutes, you've taken everything apart and figured out how it works. Now you just have to work out what the screen would have displayed. The magnetic strip on the card you swiped encodes a series of instructions for the screen; these instructions are your puzzle input. The screen is 50 pixels wide and 6 pixels tall, all of which start off, and is capable of three somewhat peculiar operations: rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall. rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels. Pixels that would fall off the right end appear at the left end of the row. rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by B pixels. Pixels that would fall off the bottom appear at the top of the column. For example, here is a simple sequence on a smaller screen: rect 3x2 creates a small rectangle in the top-left corner: ###.... ###.... ....... rotate column x=1 by 1 rotates the second column down by one pixel: #.#.... ###.... .#..... rotate row y=0 by 4 rotates the top row right by four pixels: ....#.# ###.... .#..... rotate column x=1 by 1 again rotates the second column down by one pixel, causing the bottom pixel to wrap back to the top: .#..#.# #.#.... .#..... As you can see, this display technology is extremely powerful, and will soon dominate the tiny-code-displaying-screen market. That's what the advertisement on the back of the display tries to convince you, anyway. There seems to be an intermediate check of the voltage used by the display: after you swipe your card, if the screen did work, how many pixels should be lit? ",-1),T={key:0},B=u("h2",null,"Part two",-1),_=u("p",null," You notice that the screen is only capable of displaying capital letters; in the font it uses, each letter is 5 pixels wide and 6 tall. After you swipe your card, what code is the screen trying to display? ",-1),C={key:0},D={setup(){return{router:x()}},data(){return{input:"",litPixels:0,inputPart2:"",screenDisplay:""}},methods:{solve(){const r=this.input.split(`
`).filter(e=>e.trim()!==""),l=Array(6).fill().map(()=>Array(50).fill(!1));for(const e of r){const t=e.split(" ");if(t[0]==="rect"){const[o,i]=t[1].split("x").map(Number);for(let n=0;n<i;n++)for(let s=0;s<o;s++)l[n][s]=!0}else if(t[1]==="row"){const o=Number(t[2].split("=")[1]),i=Number(t[4]),n=[...l[o]];l[o]=n.map((s,a,p)=>p[(a-i+p.length)%p.length])}else if(t[1]==="column"){const o=Number(t[2].split("=")[1]),i=Number(t[4]),s=[...l.map(a=>a[o])];for(let a=0;a<s.length;a++)l[(a+i)%s.length][o]=s[a]}}this.litPixels=l.flat().filter(e=>e).length},executeInstruction(r,l){const e=l.split(" ");if(e[0]==="rect"){const[t,o]=e[1].split("x").map(Number);for(let i=0;i<o;i++)for(let n=0;n<t;n++)r[i][n]=!0}else if(e[1]==="row"){const t=Number(e[2].split("=")[1]),o=Number(e[4]),i=[...r[t]];r[t]=i.map((n,s,a)=>a[(s-o+a.length)%a.length])}else if(e[1]==="column"){const t=Number(e[2].split("=")[1]),o=Number(e[4]),n=[...r.map(s=>s[t])];for(let s=0;s<n.length;s++)r[(s+o)%n.length][t]=n[s]}},solvePart2(){const r=this.inputPart2.split(`
`).filter(e=>e.trim()!==""),l=Array(6).fill().map(()=>Array(50).fill(!1));for(const e of r)this.executeInstruction(l,e);this.screenDisplay=l.map(e=>e.map(t=>t?"#":" ").join("")).join(`
`)}}},U=Object.assign(D,{__name:"d08",setup(r){const l=["Trois essais pour la partie 1 avec Github Copilot","Un essai pour la partie 2 avec Github Copilot"];return(e,t)=>(c(),h(g,null,[m(v),m(k,{msg:l}),u("main",null,[N,P,A,d(u("textarea",{"onUpdate:modelValue":t[0]||(t[0]=o=>e.input=o),placeholder:"Enter instructions, one line per instruction"},null,512),[[f,e.input]]),u("button",{onClick:t[1]||(t[1]=(...o)=>e.solve&&e.solve(...o))},"Solve"),u("p",null,[b("Number of lit pixels: "),e.litPixels!==0?(c(),h("span",T,y(e.litPixels),1)):w("",!0)]),B,_,d(u("textarea",{"onUpdate:modelValue":t[2]||(t[2]=o=>e.inputPart2=o),placeholder:"Enter instructions, one line per instruction"},null,512),[[f,e.inputPart2]]),u("button",{onClick:t[3]||(t[3]=(...o)=>e.solvePart2&&e.solvePart2(...o))},"Solve Part 2"),e.screenDisplay!==""?(c(),h("pre",C,y(e.screenDisplay),1)):w("",!0)])],64))}});export{U as default};