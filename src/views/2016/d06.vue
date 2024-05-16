<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Un essai pour résoudre le jour 6 de l'Advent of Code 2016 avec Github Copilot"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 6 - Signals and Noise</h1>
    <h2>Part one</h2>
    <p>
        Something is jamming your communications with Santa. Fortunately, your signal is only partially jammed, and protocol in situations like this is to switch to a simple repetition code to get the message through.

        In this model, the same message is sent repeatedly. You've recorded the repeating message signal (your puzzle input), but the data seems quite corrupted - almost too badly to recover. Almost.

        All you need to do is figure out which character is most frequent for each position. For example, suppose you had recorded the following messages:

        eedadn
        drvtee
        eandsr
        raavrd
        atevrs
        tsrnev
        sdttsa
        rasrtv
        nssdts
        ntnada
        svetve
        tesnvt
        vntsnd
        vrdear
        dvrsen
        enarar
        The most common character in the first column is e; in the second, a; in the third, s, and so on. Combining these characters returns the error-corrected message, easter.

        Given the recording in your puzzle input, what is the error-corrected version of the message being sent?
    </p>
    <textarea v-model="input" placeholder="Enter the recorded message, one line per transmission"></textarea>
    <button @click="solve">Solve</button>
    <p>Original message: <span v-if="originalMessage !== ''">{{ originalMessage }}</span></p>
    <h2>Part two</h2>
    <p>
        Of course, that would be the message - if you hadn't agreed to use a modified repetition code instead.

        In this modified code, the sender instead transmits what looks like random data, but for each character, the character they actually want to send is slightly less likely than the others. Even after signal-jamming noise, you can look at the letter distributions in each column and choose the least common letter to reconstruct the original message.

        In the above example, the least common character in the first column is a; in the second, d, and so on. Repeating this process for the remaining characters produces the original message, advent.

        Given the recording in your puzzle input and this new decoding methodology, what is the original message that Santa is trying to send?
    </p>
    <textarea v-model="input2" placeholder="Enter the recorded message, one line per transmission"></textarea>
    <button @click="solvePart2">Solve Part 2</button>
    <p>Original message for Part 2: {{ originalMessage2 }}</p>
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
        input: '',
        originalMessage: '',
        input2: '',
        originalMessage2: ''
      }
    },
    methods: {
        solve() {
            const lines = this.input.split('\n').filter(line => line.trim() !== '');
            let message = '';
            for (let i = 0; i < lines[0].length; i++) {
                const frequency = Array(26).fill(0);
                for (const line of lines) {
                    frequency[line[i].charCodeAt(0) - 'a'.charCodeAt(0)]++;
                }
                const maxFreq = Math.max(...frequency);
                message += String.fromCharCode(frequency.indexOf(maxFreq) + 'a'.charCodeAt(0));
            }
            this.originalMessage = message;
        },
        solvePart2() {
            const lines = this.input2.split('\n').filter(line => line.trim() !== '');
            let message = '';
            for (let i = 0; i < lines[0].length; i++) {
                const frequency = Array(26).fill(0);
                for (const line of lines) {
                    frequency[line[i].charCodeAt(0) - 'a'.charCodeAt(0)]++;
                }
                const minFreq = Math.min(...frequency.filter(freq => freq > 0));
                message += String.fromCharCode(frequency.indexOf(minFreq) + 'a'.charCodeAt(0));
            }
            this.originalMessage2 = message;
        }
    }
  }
</script>