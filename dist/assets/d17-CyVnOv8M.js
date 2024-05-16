import{o as s,c as r,b as l,a as i,w as u,v as m,e as c,t as h,f as d,F as b,u as f}from"./index-BTma9csY.js";import{N as p}from"./Navbar-CGnvLcvR.js";import{H as C}from"./HeaderAI-DYW4lw9P.js";const g=i("h1",null,"Day 17 - No Such Thing as Too Much",-1),y=i("h2",null,"Part one",-1),v=i("p",null," The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers. For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it: 15 and 10 20 and 5 (the first 5) 20 and 5 (the second 5) 15, 5, and 5 Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog? ",-1),w={key:0},N=i("h2",null,"Part two",-1),S=i("p",null," While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving department is requesting as many containers as you can spare. Find the minimum number of containers that can exactly fit all 150 liters of eggnog. How many different ways can you fill that number of containers and still hold exactly 150 litres? In the example above, the minimum number of containers was two. There were three ways to use that many containers, and so the answer there would be 3. ",-1),M={key:0},O={data(){return{containerSizes:"",numberOfCombinations:0,containerSizesPart2:"",numberOfMinCombinations:0}},setup(){return{router:f()}},methods:{calculateCombinations(){const e=this.containerSizes.split(`
`).map(Number),t=150;this.numberOfCombinations=this.countCombinations(e,t)},countCombinations(e,t,n=0){return t===0?1:t<0||n===e.length?0:this.countCombinations(e,t-e[n],n+1)+this.countCombinations(e,t,n+1)},calculateMinCombinations(){const e=this.containerSizesPart2.split(`
`).map(Number),n=this.findAllCombinations(e,150),o=Math.min(...n.map(a=>a.length));this.numberOfMinCombinations=n.filter(a=>a.length===o).length},findAllCombinations(e,t,n=0,o=[]){return t===0?[o]:t<0||n===e.length?[]:[...this.findAllCombinations(e,t-e[n],n+1,[...o,e[n]]),...this.findAllCombinations(e,t,n+1,o)]}}},A=Object.assign(O,{__name:"d17",setup(e){const t=["Un essai pour résoudre le jour 17 de l'Advent of Code 2015 avec Github Copilot"];return(n,o)=>(s(),r(b,null,[l(p),l(C,{msg:t}),i("main",null,[g,y,v,u(i("textarea",{"onUpdate:modelValue":o[0]||(o[0]=a=>n.containerSizes=a),placeholder:"Enter container sizes here"},null,512),[[m,n.containerSizes]]),i("button",{onClick:o[1]||(o[1]=(...a)=>n.calculateCombinations&&n.calculateCombinations(...a))},"Calculate"),i("p",null,[c("Number of combinations: "),n.numberOfCombinations!==0?(s(),r("span",w,h(n.numberOfCombinations),1)):d("",!0)]),N,S,u(i("textarea",{"onUpdate:modelValue":o[2]||(o[2]=a=>n.containerSizesPart2=a),placeholder:"Enter container sizes here"},null,512),[[m,n.containerSizesPart2]]),i("button",{onClick:o[3]||(o[3]=(...a)=>n.calculateMinCombinations&&n.calculateMinCombinations(...a))},"Calculate"),i("p",null,[c("Number of minimum combinations: "),n.numberOfMinCombinations!==0?(s(),r("span",M,h(n.numberOfMinCombinations),1)):d("",!0)])])],64))}});export{A as default};
