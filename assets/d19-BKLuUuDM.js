import{o,c as a,b as i,a as s,w as h,v as f,d as p,t as u,e as E,F as c,u as m}from"./index-bEcdERby.js";import{N as v}from"./Navbar-BPawfkg-.js";import{H as d}from"./HeaderAI-Cqe6IO_o.js";const g=s("h1",null,"Day 19 - An Elephant Named Joseph",-1),b=s("h2",null,"Part one",-1),y=s("p",null," The Elves contact you over a highly secure emergency channel. Back at the North Pole, the Elves are busy misunderstanding White Elephant parties. Each Elf brings a present. They all sit in a circle, numbered starting with position 1. Then, starting with the first Elf, they take turns stealing all the presents from the Elf to their left. An Elf with no presents is removed from the circle and does not take turns. For example, with five Elves (numbered 1 to 5): 1 5 2 4 3 Elf 1 takes Elf 2's present. Elf 2 has no presents and is skipped. Elf 3 takes Elf 4's present. Elf 4 has no presents and is also skipped. Elf 5 takes Elf 1's two presents. Neither Elf 1 nor Elf 2 have any presents, so both are skipped. Elf 3 takes Elf 5's three presents. So, with five Elves, the Elf that sits starting in position 3 gets all the presents. With the number of Elves given in your puzzle input, which Elf gets all the presents? ",-1),w={key:0},_=s("h2",null,"Part two",-1),k=s("p",null," Realizing the folly of their present-exchange rules, the Elves agree to instead steal presents from the Elf directly across the circle. If two Elves are across the circle, the one on the left (from the perspective of the stealer) is stolen from. The other rules remain unchanged: Elves with no presents are removed from the circle entirely, and the other elves move in slightly to keep the circle evenly spaced. For example, with five Elves (again numbered 1 to 5): The Elves sit in a circle; Elf 1 goes first: 1 5 2 4 3 Elves 3 and 4 are across the circle; Elf 3's present is stolen, being the one to the left. Elf 3 leaves the circle, and the rest of the Elves move in: 1 1 5 2 --> 5 2 4 - 4 Elf 2 steals from the Elf directly across the circle, Elf 5: 1 1 - 2 --> 2 4 4 Next is Elf 4 who, choosing between Elves 1 and 2, steals from Elf 1: - 2 2 --> 4 4 Finally, Elf 2 steals from Elf 4: 2 --> 2 - So, with five Elves, the Elf that sits starting in position 2 gets all the presents. With the number of Elves given in your puzzle input, which Elf now gets all the presents? ",-1),P={setup(){return{router:m()}},data(){return{numberOfElves:0,elfWithAllPresents:0,numberOfElvesPart2:0,elfWithAllPresentsPart2:0}},methods:{solvePart1(){let t=Array.from({length:this.numberOfElves},(l,e)=>e+1);for(;t.length>1;)Math.floor(t.length/2),t.length%2===0?t=t.filter((l,e)=>e%2===0):(t=t.filter((l,e)=>e%2===0),t.shift());this.elfWithAllPresents=t[0]}}},T=Object.assign(P,{__name:"d19",setup(t){const l=["Un essai pour la partie 1 avec Github Copilot","La partie 2 ne fonctionne pas"];return(e,r)=>(o(),a(c,null,[i(v),i(d,{msg:l}),s("main",null,[g,b,y,h(s("input",{"onUpdate:modelValue":r[0]||(r[0]=n=>e.numberOfElves=n),type:"number",placeholder:"Enter number of elves"},null,512),[[f,e.numberOfElves,void 0,{number:!0}]]),s("button",{onClick:r[1]||(r[1]=(...n)=>e.solvePart1&&e.solvePart1(...n))},"Solve Part 1"),s("p",null,[p("Elf with all presents: "),e.elfWithAllPresents!==0?(o(),a("span",w,u(e.elfWithAllPresents),1)):E("",!0)]),_,k])],64))}});export{T as default};
