<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Un essai pour résoudre le jour 2 de l'Advent of Code 2017 avec Github Copilot"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 2 - Corruption Checksum</h1>
    <h2>Part one</h2>
    <p>
        As you walk through the door, a glowing humanoid shape yells in your direction. "You there! Your state appears to be idle. Come help us repair the corruption in this spreadsheet - if we take another millisecond, we'll have to display an hourglass cursor!"

        The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum. For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.

        For example, given the following spreadsheet:

        5 1 9 5
        7 5 3
        2 4 6 8
        The first row's largest and smallest values are 9 and 1, and their difference is 8.
        The second row's largest and smallest values are 7 and 3, and their difference is 4.
        The third row's difference is 6.
        In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

        What is the checksum for the spreadsheet in your puzzle input?
    </p>
    <textarea v-model="grid" placeholder="Enter grid here"></textarea>
    <button @click="solveChecksum">Solve Checksum</button>
    <p>Checksum: <span v-if="checksum !== null">{{ checksum }}</span></p>
    <h2>Part two</h2>
    <p>
        "Great work; looks like we're on the right track after all. Here's a star for your effort." However, the program seems a little worried. Can programs be worried?

        "Based on what we're seeing, it looks like all the User wanted is some information about the evenly divisible values in the spreadsheet. Unfortunately, none of us are equipped for that kind of calculation - most of us specialize in bitwise operations."

        It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - that is, where the result of the division operation is a whole number. They would like you to find those numbers on each line, divide them, and add up each line's result.

        For example, given the following spreadsheet:

        5 9 2 8
        9 4 7 3
        3 8 6 5
        In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
        In the second row, the two numbers are 9 and 3; the result is 3.
        In the third row, the result is 2.
        In this example, the sum of the results would be 4 + 3 + 2 = 9.

        What is the sum of each row's result in your puzzle input?
    </p>
    <textarea v-model="gridPartTwo" placeholder="Enter grid here"></textarea>
    <button @click="solveChecksumPartTwo">Solve Checksum</button>
    <p>Checksum: <span  v-if="checksumPartTwo">{{ checksumPartTwo }}</span></p>
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
        grid: '',
        checksum: null,
        gridPartTwo: '',
        checksumPartTwo: null,
      }
    },
    methods: {
        solveChecksum() {
            const rows = this.grid.split('\n');
            let sum = 0;
            for (const row of rows) {
                const numbers = row.split(/\s+/).map(Number);
                const min = Math.min(...numbers);
                const max = Math.max(...numbers);
                sum += max - min;
            }
            this.checksum = sum;
        },
        solveChecksumPartTwo() {
            const rows = this.gridPartTwo.split('\n');
            let total = 0;
            for (const row of rows) {
                const numbers = row.split(/\s+/).map(Number);
                for (let i = 0; i < numbers.length; i++) {
                for (let j = i + 1; j < numbers.length; j++) {
                    if (numbers[i] % numbers[j] === 0) {
                    total += numbers[i] / numbers[j];
                    } else if (numbers[j] % numbers[i] === 0) {
                    total += numbers[j] / numbers[i];
                    }
                }
                }
            }
            this.checksumPartTwo = total;
        },
    }
  }
</script>