import{o as l,c as n,b as i,a as t,w as u,v as h,d,t as m,e as w,F as b,u as c}from"./index-DqfKCZJy.js";import{N as f}from"./Navbar-DzpSwXSp.js";import{H as y}from"./HeaderAI-CRuXBWid.js";import{m as p}from"./md5-DFal9VNF.js";const v=t("h1",null,"Day 4 - The Ideal Stocking Stuffer",-1),z=t("h2",null,"Part one",-1),k=t("p",null," Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys. To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash. For example: If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so. If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef.... ",-1),P={key:0},g=t("h2",null,"Part two",-1),N=t("p",null," Now find one that starts with six zeroes. ",-1),T={key:0},D={setup(){return{router:c()}},data(){return{secretKey:"",lowestNumber:null,lowestNumberPartTwo:null}},methods:{solvePuzzle(){let s=0;for(;;){if(p(this.secretKey+s).startsWith("00000")){this.lowestNumber=s;break}s++}},solvePuzzlePartTwo(){let s=0;for(;;){if(p(this.secretKey+s).startsWith("000000")){this.lowestNumberPartTwo=s;break}s++}}}},V=Object.assign(D,{__name:"d04",setup(s){const a=["Un essai pour résoudre le jour 4 de l'Advent of Code 2015 avec Github Copilot"];return(e,o)=>(l(),n(b,null,[i(f),i(y,{msg:a}),t("main",null,[v,z,k,u(t("input",{type:"text","onUpdate:modelValue":o[0]||(o[0]=r=>e.secretKey=r),placeholder:"Enter secret key here"},null,512),[[h,e.secretKey]]),t("button",{onClick:o[1]||(o[1]=(...r)=>e.solvePuzzle&&e.solvePuzzle(...r))},"Solve Puzzle"),t("p",null,[d("Lowest number that produces a hash starting with five zeroes: "),e.lowestNumber!==null?(l(),n("span",P,m(e.lowestNumber),1)):w("",!0)]),g,N,u(t("input",{type:"text","onUpdate:modelValue":o[2]||(o[2]=r=>e.secretKey=r),placeholder:"Enter secret key here"},null,512),[[h,e.secretKey]]),t("button",{onClick:o[3]||(o[3]=(...r)=>e.solvePuzzlePartTwo&&e.solvePuzzlePartTwo(...r))},"Solve Puzzle Part Two"),t("p",null,[d("Lowest number that produces a hash starting with six zeroes: "),e.lowestNumberPartTwo!==null?(l(),n("span",T,m(e.lowestNumberPartTwo),1)):w("",!0)])])],64))}});export{V as default};
