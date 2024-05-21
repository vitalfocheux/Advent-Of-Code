import{o as d,c as m,b as c,a as i,t as r,w as h,v as u,F as v,u as y}from"./index-bEcdERby.js";import{N as f}from"./Navbar-BPawfkg-.js";import{H as b}from"./HeaderAI-Cqe6IO_o.js";const g=i("h1",null,"Day 20 - Particle Swarm",-1),w=i("h2",null,"Part one",-1),P=i("h2",null,"Part two",-1),k={setup(){return{router:y()}},data(){return{part1:`Suddenly, the GPU contacts you, asking for help. Someone has asked it to simulate too many particles, and it won't be able to finish them all in time to render the next frame at this rate.
It transmits to you a buffer (your puzzle input) listing each particle in order (starting with particle 0, then particle 1, particle 2, and so on). For each particle, it provides the X, Y, and Z coordinates for the particle's position (p), velocity (v), and acceleration (a), each in the format <X,Y,Z>.
Each tick, all particles are updated simultaneously. A particle's properties are updated in the following order:
Increase the X velocity by the X acceleration.Increase the Y velocity by the Y acceleration.
Increase the Z velocity by the Z acceleration.
Increase the X position by the X velocity.
Increase the Y position by the Y velocity.
Increase the Z position by the Z velocity.
Because of seemingly tenuous rationale involving z-buffering, the GPU would like to know which particle will stay closest to position <0,0,0> in the long term. Measure this using the Manhattan distance, which in this situation is simply the sum of the absolute values of a particle's X, Y, and Z position.
For example, suppose you are only given two particles, both of which stay entirely on the X-axis (for simplicity). Drawing the current states of particles 0 and 1 (in that order) with an adjacent a number line and diagram of current X positions (marked in parentheses), the following would take place:
p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>                         (0)(1)
p=< 4,0,0>, v=< 1,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
p=< 2,0,0>, v=<-2,0,0>, a=<-2,0,0>                      (1)   (0)
p=< 4,0,0>, v=< 0,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
p=<-2,0,0>, v=<-4,0,0>, a=<-2,0,0>          (1)               (0)
p=< 3,0,0>, v=<-1,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
p=<-8,0,0>, v=<-6,0,0>, a=<-2,0,0>                         (0)   
At this point, particle 1 will never be closer to <0,0,0> than particle 0, and so, in the long run, particle 0 will stay closest.
Which particle will stay closest to position <0,0,0> in the long term?`,part2:`To simplify the problem further, the GPU would like to remove any particles that collide. Particles collide if their positions ever exactly match. Because particles are updated simultaneously, more than two particles can collide at the same time and place. Once particles collide, they are removed and cannot collide with anything else after that tick.
For example:
p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>    
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>    (0)   (1)   (2)            (3)
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>
p=<-3,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
p=<-1,0,0>, v=< 1,0,0>, a=< 0,0,0>             (0)(1)(2)      (3)   
p=< 2,0,0>, v=<-1,0,0>, a=< 0,0,0>
p=< 0,0,0>, v=< 3,0,0>, a=< 0,0,0>    
p=< 0,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
p=< 0,0,0>, v=< 1,0,0>, a=< 0,0,0>                       X (3)      
p=< 1,0,0>, v=<-1,0,0>, a=< 0,0,0>
------destroyed by collision------  
------destroyed by collision------    -6 -5 -4 -3 -2 -1  0  1  2  3
------destroyed by collision------                      (3)         
p=< 0,0,0>, v=<-1,0,0>, a=< 0,0,0>
In this example, particles 0, 1, and 2 are simultaneously destroyed at the time and place marked X. On the next tick, particle 3 passes through unharmed.
How many particles are left after all collisions are resolved?`,particles:"",closestParticle:null,particles2:"",remainingParticles:null}},methods:{findClosestParticle(){const o=this.particles.split(`
`).map((t,a)=>{const[e,s,n]=t.match(/<([^>]+)>/g).map(l=>l.slice(1,-1).split(",").map(Number));return{index:a,p:e,v:s,a:n}});o.sort((t,a)=>{const e=t.a.reduce((n,l)=>n+Math.abs(l),0),s=a.a.reduce((n,l)=>n+Math.abs(l),0);return e-s}),this.closestParticle=o[0].index},resolveCollisions(){let o=this.particles2.split(`
`).map((t,a)=>{const[e,s,n]=t.match(/<([^>]+)>/g).map(l=>l.slice(1,-1).split(",").map(Number));return{index:a,p:e,v:s,a:n}});for(let t=0;t<1e3;t++){let a={};o.forEach(e=>{e.v=e.v.map((n,l)=>n+e.a[l]),e.p=e.p.map((n,l)=>n+e.v[l]);const s=e.p.join(",");a[s]=(a[s]||0)+1}),o=o.filter(e=>{const s=e.p.join(",");return a[s]===1}),a={}}this.remainingParticles=o.length}}},N=Object.assign(k,{__name:"d20",setup(p){const o=["Un essai pour la partie 1 avec Github Copilot","Deux essais pour la partie 2 avec Github Copilot"];return(t,a)=>(d(),m(v,null,[c(f),c(b,{msg:o}),i("main",null,[g,w,i("p",null,r(t.part1),1),h(i("textarea",{"onUpdate:modelValue":a[0]||(a[0]=e=>t.particles=e),placeholder:"Enter particles here"},null,512),[[u,t.particles]]),i("button",{onClick:a[1]||(a[1]=(...e)=>t.findClosestParticle&&t.findClosestParticle(...e))},"Find Closest Particle"),i("p",null,"Particle that will stay closest to the origin in the long term: "+r(t.closestParticle),1),P,i("p",null,r(t.part2),1),h(i("textarea",{"onUpdate:modelValue":a[2]||(a[2]=e=>t.particles2=e),placeholder:"Enter particles here"},null,512),[[u,t.particles2]]),i("button",{onClick:a[3]||(a[3]=(...e)=>t.resolveCollisions&&t.resolveCollisions(...e))},"Resolve Collisions"),i("p",null,"Number of particles left after all collisions are resolved: "+r(t.remainingParticles),1)])],64))}});export{N as default};
