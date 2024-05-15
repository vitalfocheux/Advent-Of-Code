<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Un essai pour résoudre le jour 5 de l'Advent of Code 2015 avec Github Copilot"]
</script>

<template>
    <Navbar />

    <HeaderAI :msg="messages" />

    <main>
        <h1>Day 5 - Doesn't He Have Intern-Elves For This?</h1>
        <h2>Part one</h2>
        <p>
            Santa needs help figuring out which strings in his text file are naughty or nice.

            A nice string is one with all of the following properties:

            It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
            It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
            It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
            For example:

            ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
            aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
            jchzalrnumimnmhp is naughty because it has no double letter.
            haegwjzuvuyypxyu is naughty because it contains the string xy.
            dvszwmarrgswjxmb is naughty because it contains only one vowel.
            How many strings are nice?    
        </p>
        <textarea v-model="strings" placeholder="Enter strings here, one per line"></textarea>
        <button @click="countNiceStrings">Count Nice Strings</button>
        <p>Number of nice strings: <span v-if="niceStringsCount !== null">{{ niceStringsCount }}</span></p>
        <h2>Part two</h2>
        <p>
            Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

            Now, a nice string is one with all of the following properties:

            It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
            It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
            For example:

            qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
            xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
            uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
            ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
            How many strings are nice under these new rules?
        </p>
        <textarea v-model="strings" placeholder="Enter strings here, one per line"></textarea>
    <button @click="countNiceStringsPartTwo">Count Nice Strings Part Two</button>
    <p>Number of nice strings (part two): <span v-if="niceStringsCountPartTwo !== null">{{ niceStringsCountPartTwo }}</span></p>
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
        strings: '',
        niceStringsCount: null,
        niceStringsCountPartTwo: null
      }
    },
    methods: {
        countNiceStrings() {
            const stringsArray = this.strings.split('\n');
            this.niceStringsCount = stringsArray.filter(string => this.isNice(string)).length;
        },
        isNice(string) {
            const hasThreeVowels = (string.match(/[aeiou]/g) || []).length >= 3;
            const hasDoubleLetter = /([a-z])\1/.test(string);
            const hasForbiddenSubstring = /(ab|cd|pq|xy)/.test(string);
            return hasThreeVowels && hasDoubleLetter && !hasForbiddenSubstring;
        },
        countNiceStringsPartTwo() {
            const stringsArray = this.strings.split('\n');
            this.niceStringsCountPartTwo = stringsArray.filter(string => this.isNicePartTwo(string)).length;
        },
        isNicePartTwo(string) {
            const hasPairTwice = /([a-z]{2}).*\1/.test(string);
            const hasRepeatWithOneBetween = /([a-z]).\1/.test(string);
            return hasPairTwice && hasRepeatWithOneBetween;
        }
    }
  }
</script>