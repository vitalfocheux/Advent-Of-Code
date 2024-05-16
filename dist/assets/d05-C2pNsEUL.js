import{o as i,c as n,b as h,a as s,w as d,v as l,d as p,t as c,e as u,F as w,u as m}from"./index-DqfKCZJy.js";import{N as g}from"./Navbar-DzpSwXSp.js";import{H as v}from"./HeaderAI-CRuXBWid.js";import{m as f}from"./md5-DFal9VNF.js";const y=s("h1",null,"Day 5 - How About a Nice Game of Chess?",-1),D=s("h2",null,"Part one",-1),I=s("p",null," You are faced with a security door designed by Easter Bunny engineers that seem to have acquired most of their security knowledge by watching hacking movies. The eight-character password for the door is generated one character at a time by finding the MD5 hash of some Door ID (your puzzle input) and an increasing integer index (starting with 0). A hash indicates the next character in the password if its hexadecimal representation starts with five zeroes. If it does, the sixth character in the hash is the next character of the password. For example, if the Door ID is abc: The first index which produces a hash that starts with five zeroes is 3231929, which we find by hashing abc3231929; the sixth character of the hash, and thus the first character of the password, is 1. 5017308 produces the next interesting hash, which starts with 000008f82..., so the second character of the password is 8. The third time a hash starts with five zeroes is for abc5278568, discovering the character f. In this example, after continuing this search a total of eight times, the password is 18f47a30. Given the actual Door ID, what is the password? ",-1),b={key:0},_=s("h2",null,"Part two",-1),k=s("p",null,' As the door slides open, you are presented with a second door that uses a slightly more inspired security mechanism. Clearly unimpressed by the last version (in what movie is the password decrypted in order?!), the Easter Bunny engineers have worked out a better solution. Instead of simply filling in the password from left to right, the hash now also indicates the position within the password to fill. You still look for hashes that begin with five zeroes; however, now, the sixth character represents the position (0-7), and the seventh character is the character to put in that position. A hash result of 000001f means that f is the second character in the password. Use only the first result for each position, and ignore invalid positions. For example, if the Door ID is abc: The first interesting hash is from abc3231929, which produces 0000015...; so, 5 goes in position 1: _5______. In the previous method, 5017308 produced an interesting hash; however, it is ignored, because it specifies an invalid position (8). The second interesting hash is at index 5357525, which produces 000004e...; so, e goes in position 4: _5__e___. You almost choke on your popcorn as the final character falls into place, producing the password 05ace8e3. Given the actual Door ID and this new method, what is the password? Be extra proud of your solution if it uses a cinematic "decrypting" animation. ',-1),P={key:0},A={setup(){return{router:m()}},data(){return{doorID:"",password:"",doorID2:"",password2:"--------"}},methods:{solve(){let o="";for(let r=0;o.length<8;r++){const e=f(this.doorID+r);e.startsWith("00000")&&(o+=e[5])}this.password=o},solvePart2(){let o=Array(8).fill(null);for(let r=0;o.includes(null);r++){const e=f(this.doorID2+r);if(e.startsWith("00000")){const t=parseInt(e[5],16);t<8&&o[t]===null&&(o[t]=e[6])}}this.password2=o.join("")}}},z=Object.assign(A,{__name:"d05",setup(o){const r=["Un essai pour résoudre le jour 5 de l'Advent of Code 2016 avec Github Copilot"];return(e,t)=>(i(),n(w,null,[h(g),h(v,{msg:r}),s("main",null,[y,D,I,d(s("input",{"onUpdate:modelValue":t[0]||(t[0]=a=>e.doorID=a),placeholder:"Enter door ID"},null,512),[[l,e.doorID]]),s("button",{onClick:t[1]||(t[1]=(...a)=>e.solve&&e.solve(...a))},"Solve"),s("p",null,[p("Password: "),e.password!==""?(i(),n("span",b,c(e.password),1)):u("",!0)]),_,k,d(s("input",{"onUpdate:modelValue":t[2]||(t[2]=a=>e.doorID2=a),placeholder:"Enter door ID"},null,512),[[l,e.doorID2]]),s("button",{onClick:t[3]||(t[3]=(...a)=>e.solvePart2&&e.solvePart2(...a))},"Solve Part 2"),s("p",null,[p("Password for Part 2: "),e.password2!="--------"?(i(),n("span",P,c(e.password2),1)):u("",!0)])])],64))}});export{z as default};
