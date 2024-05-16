import{o as i,c as r,b as c,a as o,w as u,v as m,e as d,t as h,f as p,F as H,u as f}from"./index-BTma9csY.js";import{N as O}from"./Navbar-CGnvLcvR.js";import{H as b}from"./HeaderAI-DYW4lw9P.js";const g=o("h1",null,"Day 19 - Medicine for Rudolph",-1),w=o("h2",null,"Part one",-1),y=o("p",null," Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very brightly, and he needs medicine. Red-Nosed Reindeer biology isn't similar to regular reindeer biology; Rudolph is going to need custom-made medicine. Unfortunately, Red-Nosed Reindeer chemistry isn't similar to regular reindeer chemistry, either. The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission plant, capable of constructing any Red-Nosed Reindeer molecule you need. It works by starting with some input molecule and then doing a series of replacements, one per step, until it has the right molecule. However, the machine has to be calibrated before it can be used. Calibration involves determining the number of molecules that can be generated in one step from a given starting point. For example, imagine a simpler machine that supports only the following replacements: H => HO H => OH O => HH Given the replacements above and starting with HOH, the following molecules could be generated: HOOH (via H => HO on the first H). HOHO (via H => HO on the second H). OHOH (via H => OH on the first H). HOOH (via H => OH on the second H). HHHH (via O => HH). So, in the example above, there are 4 distinct molecules (not five, because HOOH appears twice) after one replacement from HOH. Santa's favorite molecule, HOHOHO, can become 7 distinct molecules (over nine replacements: six from H, and three from O). The machine replaces without regard for the surrounding characters. For example, given the string H2O, the transition H => OO would result in OO2O. Your puzzle input describes all of the possible replacements and, at the bottom, the medicine molecule for which you need to calibrate the machine. How many distinct molecules can be created after all the different ways you can do one replacement on the medicine molecule? ",-1),v={key:0},R=o("h2",null,"Part two",-1),M=o("p",null," Now that the machine is calibrated, you're ready to begin molecule fabrication. Molecule fabrication always begins with just a single electron, e, and applying replacements one at a time, just like the ones during calibration. For example, suppose you have the following replacements: e => H e => O H => HO H => OH O => HH If you'd like to make HOH, you start with e, and then make the following replacements: e => O to get O O => HH to get HH H => OH (on the second H) to get HOH So, you could make HOH after 3 steps. Santa's favorite molecule, HOHOHO, can be made in 6 steps. How long will it take to make the medicine? Given the available replacements and the medicine molecule in your puzzle input, what is the fewest number of steps to go from e to the medicine molecule? ",-1),N={data(){return{replacementRules:"",startMolecule:"",numberOfPossibleMolecules:0}},setup(){return{router:f()}},methods:{calculatePossibleMolecules(){const a=this.replacementRules.split(`
`).map(e=>e.split(" => ")),l=this.startMolecule,t=new Set;for(const[e,n]of a){let s=l.indexOf(e);for(;s!==-1;)t.add(l.slice(0,s)+n+l.slice(s+e.length)),s=l.indexOf(e,s+1)}this.numberOfPossibleMolecules=t.size}}},S=Object.assign(N,{__name:"d19",setup(a){const l=["Un essai pour la partie 1 avec Github Copilot","La partie 2 ne fonctionne pas"];return(t,e)=>(i(),r(H,null,[c(O),c(b,{msg:l}),o("main",null,[g,w,y,u(o("textarea",{"onUpdate:modelValue":e[0]||(e[0]=n=>t.replacementRules=n),placeholder:"Enter replacement rules here"},null,512),[[m,t.replacementRules]]),u(o("input",{"onUpdate:modelValue":e[1]||(e[1]=n=>t.startMolecule=n),placeholder:"Enter start molecule here"},null,512),[[m,t.startMolecule]]),o("button",{onClick:e[2]||(e[2]=(...n)=>t.calculatePossibleMolecules&&t.calculatePossibleMolecules(...n))},"Calculate"),o("p",null,[d("Number of possible molecules: "),t.numberOfPossibleMolecules!==0?(i(),r("span",v,h(t.numberOfPossibleMolecules),1)):p("",!0)]),R,M])],64))}});export{S as default};
