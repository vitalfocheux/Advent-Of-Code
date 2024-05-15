<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Un essai pour résoudre le jour 4 de l'Advent of Code 2015 avec Github Copilot"]
</script>

<template>
    <Navbar />

    <HeaderAI :msg="messages" />

    <main>
        <h1>Day 4 - The Ideal Stocking Stuffer</h1>
        <h2>Part one</h2>
        <p>
            Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

            To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

            For example:

            If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
            If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
        </p>
        <input type="text" v-model="secretKey" placeholder="Enter secret key here">
        <button @click="solvePuzzle">Solve Puzzle</button>
        <p>Lowest number that produces a hash starting with five zeroes: <span v-if="lowestNumber !== null">{{ lowestNumber }}</span></p>
        <h2>Part two</h2>
        <p>
            Now find one that starts with six zeroes.
        </p>
        <input type="text" v-model="secretKey" placeholder="Enter secret key here">
        <button @click="solvePuzzlePartTwo">Solve Puzzle Part Two</button>
        <p>Lowest number that produces a hash starting with six zeroes: <span v-if="lowestNumberPartTwo !== null">{{ lowestNumberPartTwo }}</span></p>
    </main>

</template>

<script>
  import { useRouter } from 'vue-router'
  import md5 from 'js-md5'

  export default {
    setup() {
      const router = useRouter()
      return { router }
    },

    data() {
      return {
        secretKey: '',
        lowestNumber: null,
        lowestNumberPartTwo: null
      }
    },
    methods: {
        solvePuzzle() {
            let number = 0;
            while (true) {
                const hash = md5(this.secretKey + number);
                if (hash.startsWith('00000')) {
                    this.lowestNumber = number;
                    break;
                }
                number++;
            }
        },
        solvePuzzlePartTwo() {
            let number = 0;
            while (true) {
                const hash = md5(this.secretKey + number);
                if (hash.startsWith('000000')) {
                this.lowestNumberPartTwo = number;
                break;
                }
                number++;
            }
        }
    }
  }
</script>