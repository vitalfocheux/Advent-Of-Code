import{o as u,c as h,b as l,a as r,t as s,w as c,v as i,F as g,u as d}from"./index-bEcdERby.js";import{N as p}from"./Navbar-BPawfkg-.js";import{H as m}from"./HeaderAI-Cqe6IO_o.js";const f=r("h1",null,"Day 9 - Stream Processing",-1),b=r("h2",null,"Part one",-1),w=r("h2",null,"Part two",-1),y={setup(){return{router:d()}},data(){return{part1:`A large stream blocks your path. According to the locals, it's not safe to cross the stream at the moment because it's full of garbage. You look down at the stream; rather than water, you discover that it's a stream of characters.
You sit for a while and record part of the stream (your puzzle input). The characters represent groups - sequences that begin with { and end with }. Within a group, there are zero or more other things, separated by commas: either another group or garbage. Since groups can contain other groups, a } only closes the most-recently-opened unclosed group - that is, they are nestable. Your puzzle input represents a single, large group which itself contains many smaller ones.
Sometimes, instead of a group, you will find garbage. Garbage begins with < and ends with >. Between those angle brackets, almost any character can appear, including { and }. Within garbage, < has no special meaning.
In a futile attempt to clean up the garbage, some program has canceled some of the characters within it using !: inside garbage, any character that comes after ! should be ignored, including <, >, and even another !.
You don't see any characters that deviate from these rules. Outside garbage, you only find well-formed groups, and garbage always terminates according to the rules above.
Here are some self-contained pieces of garbage:
<>, empty garbage.
<random characters>, garbage containing random characters.
<<<<>, because the extra < are ignored.
<{!>}>, because the first > is canceled.
<!!>, because the second ! is canceled, allowing the > to terminate the garbage.
<!!!>>, because the second ! and the first > are canceled.
<{o"i!a,<{i<a>, which ends at the first >.
Here are some examples of whole streams and the number of groups they contain:
{}, 1 group.
{{{}}}, 3 groups.
{{},{}}, also 3 groups.
{{{},{},{{}}}}, 6 groups.
{<{},{},{{}}>}, 1 group (which itself contains garbage).
{<a>,<a>,<a>,<a>}, 1 group.
{{<a>},{<a>},{<a>},{<a>}}, 5 groups.
{{<!>},{<!>},{<!>},{<a>}}, 2 groups (since all but the last > are canceled).
Your goal is to find the total score for all groups in your input. Each group is assigned a score which is one more than the score of the group that immediately contains it. (The outermost group gets a score of 1.)
{}, score of 1.
{{{}}}, score of 1 + 2 + 3 = 6.
{{},{}}, score of 1 + 2 + 2 = 5.
{{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
{<a>,<a>,<a>,<a>}, score of 1.
{{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3.
What is the total score for all groups in your input?`,part2:`Now, you're ready to remove the garbage. 
To prove you've removed it, you need to count all of the characters within the garbage. The leading and trailing < and > don't count, nor do any canceled characters or the ! doing the canceling.
<>, 0 characters.
<random characters>, 17 characters.
<<<<>, 3 characters.
<{!>}>, 2 characters.
<!!>, 0 characters.
<!!!>>, 0 characters.
<{o"i!a,<{i<a>, 10 characters.
How many non-canceled characters are within the garbage in your puzzle input?`,streamInput:"",totalScore:null,streamInputPartTwo:"",garbageCharacters:null}},methods:{calculateTotalScore(){let o=0,n=0,e=!1,a=!1;for(const t of this.streamInput){if(a){a=!1;continue}if(t==="!")a=!0;else if(t===">")e=!1;else{if(e)continue;t==="<"?e=!0:t==="{"?(o++,n+=o):t==="}"&&o--}}this.totalScore=n},countGarbageCharacters(){let o=!1,n=!1,e=0;for(const a of this.streamInputPartTwo){if(n){n=!1;continue}a==="!"?n=!0:a===">"?o=!1:o?e++:a==="<"&&(o=!0)}this.garbageCharacters=e}}},S=Object.assign(y,{__name:"d09",setup(o){const n=["Un essai pour résoudre le jour 9 de l'Advent of Code 2017 avec Github Copilot"];return(e,a)=>(u(),h(g,null,[l(p),l(m,{msg:n}),r("main",null,[f,b,r("p",null,s(e.part1),1),c(r("textarea",{"onUpdate:modelValue":a[0]||(a[0]=t=>e.streamInput=t),placeholder:"Enter stream here"},null,512),[[i,e.streamInput]]),r("button",{onClick:a[1]||(a[1]=(...t)=>e.calculateTotalScore&&e.calculateTotalScore(...t))},"Calculate Total Score"),r("p",null,"Total Score: "+s(e.totalScore),1),w,r("p",null,s(e.part2),1),c(r("textarea",{"onUpdate:modelValue":a[2]||(a[2]=t=>e.streamInputPartTwo=t),placeholder:"Enter stream here"},null,512),[[i,e.streamInputPartTwo]]),r("button",{onClick:a[3]||(a[3]=(...t)=>e.countGarbageCharacters&&e.countGarbageCharacters(...t))},"Count Garbage Characters"),r("p",null,"Garbage Characters: "+s(e.garbageCharacters),1)])],64))}});export{S as default};
