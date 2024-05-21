<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Un essai pour résoudre le jour 9 de l'Advent of Code 2017 avec Github Copilot"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 9 - Stream Processing</h1>
    <h2>Part one</h2>
    <p>
        {{ part1 }}
    </p>
    <textarea v-model="streamInput" placeholder="Enter stream here"></textarea>
    <button @click="calculateTotalScore">Calculate Total Score</button>
    <p>Total Score: {{ totalScore }}</p>
    <h2>Part two</h2>
    <p>
        {{ part2 }}
    </p>
    <textarea v-model="streamInputPartTwo" placeholder="Enter stream here"></textarea>
    <button @click="countGarbageCharacters">Count Garbage Characters</button>
    <p>Garbage Characters: {{ garbageCharacters }}</p>
  </main>

</template>

<script>
  import { useRouter } from 'vue-router'

  export default {
    setup() {
      const router = useRouter()
      return { router }
    },

    data() {
      return {
        part1: 'A large stream blocks your path. According to the locals, it\'s not safe to cross the stream at the moment because it\'s full of garbage. You look down at the stream; rather than water, you discover that it\'s a stream of characters.\nYou sit for a while and record part of the stream (your puzzle input). The characters represent groups - sequences that begin with { and end with }. Within a group, there are zero or more other things, separated by commas: either another group or garbage. Since groups can contain other groups, a } only closes the most-recently-opened unclosed group - that is, they are nestable. Your puzzle input represents a single, large group which itself contains many smaller ones.\nSometimes, instead of a group, you will find garbage. Garbage begins with < and ends with >. Between those angle brackets, almost any character can appear, including { and }. Within garbage, < has no special meaning.\nIn a futile attempt to clean up the garbage, some program has canceled some of the characters within it using !: inside garbage, any character that comes after ! should be ignored, including <, >, and even another !.\nYou don\'t see any characters that deviate from these rules. Outside garbage, you only find well-formed groups, and garbage always terminates according to the rules above.\nHere are some self-contained pieces of garbage:\n<>, empty garbage.\n<random characters>, garbage containing random characters.\n<<<<>, because the extra < are ignored.\n<{!>}>, because the first > is canceled.\n<!!>, because the second ! is canceled, allowing the > to terminate the garbage.\n<!!!>>, because the second ! and the first > are canceled.\n<{o"i!a,<{i<a>, which ends at the first >.\nHere are some examples of whole streams and the number of groups they contain:\n{}, 1 group.\n{{{}}}, 3 groups.\n{{},{}}, also 3 groups.\n{{{},{},{{}}}}, 6 groups.\n{<{},{},{{}}>}, 1 group (which itself contains garbage).\n{<a>,<a>,<a>,<a>}, 1 group.\n{{<a>},{<a>},{<a>},{<a>}}, 5 groups.\n{{<!>},{<!>},{<!>},{<a>}}, 2 groups (since all but the last > are canceled).\nYour goal is to find the total score for all groups in your input. Each group is assigned a score which is one more than the score of the group that immediately contains it. (The outermost group gets a score of 1.)\n{}, score of 1.\n{{{}}}, score of 1 + 2 + 3 = 6.\n{{},{}}, score of 1 + 2 + 2 = 5.\n{{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.\n{<a>,<a>,<a>,<a>}, score of 1.\n{{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.\n{{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.\n{{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3.\nWhat is the total score for all groups in your input?',
        part2: 'Now, you\'re ready to remove the garbage. \nTo prove you\'ve removed it, you need to count all of the characters within the garbage. The leading and trailing < and > don\'t count, nor do any canceled characters or the ! doing the canceling.\n<>, 0 characters.\n<random characters>, 17 characters.\n<<<<>, 3 characters.\n<{!>}>, 2 characters.\n<!!>, 0 characters.\n<!!!>>, 0 characters.\n<{o\"i!a,<{i<a>, 10 characters.\nHow many non-canceled characters are within the garbage in your puzzle input?',
        streamInput: '',
        totalScore: null,
        streamInputPartTwo: '',
        garbageCharacters: null
      }
    },
    methods: {
        calculateTotalScore() {
            let depth = 0;
            let totalScore = 0;
            let inGarbage = false;
            let ignoreNext = false;

            for (const char of this.streamInput) {
                if (ignoreNext) {
                ignoreNext = false;
                continue;
                }

                if (char === '!') {
                ignoreNext = true;
                } else if (char === '>') {
                inGarbage = false;
                } else if (inGarbage) {
                continue;
                } else if (char === '<') {
                inGarbage = true;
                } else if (char === '{') {
                depth++;
                totalScore += depth;
                } else if (char === '}') {
                depth--;
                }
            }

            this.totalScore = totalScore;
        },
        countGarbageCharacters() {
            let inGarbage = false;
            let ignoreNext = false;
            let garbageCharacters = 0;

            for (const char of this.streamInputPartTwo) {
                if (ignoreNext) {
                ignoreNext = false;
                continue;
                }

                if (char === '!') {
                ignoreNext = true;
                } else if (char === '>') {
                inGarbage = false;
                } else if (inGarbage) {
                garbageCharacters++;
                } else if (char === '<') {
                inGarbage = true;
                }
            }

            this.garbageCharacters = garbageCharacters;
        },
    }
  }
</script>