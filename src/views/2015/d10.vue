<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';

  const messages = ["Un essai pour résoudre le jour 10 de l'Advent of Code 2015 avec Github Copilot"]
</script>

<template>
    <Navbar />

    <HeaderAI :msg= "messages"/>

    <main>
        <h1>Day 10 - Elves Look, Elves Say</h1>
        <h2>Part one</h2>
        <p>
            Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence. For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

            Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step, take the previous value, and replace each run of digits (like 111) with the number of digits (3) followed by the digit itself (1).

            For example:

            1 becomes 11 (1 copy of digit 1).
            11 becomes 21 (2 copies of digit 1).
            21 becomes 1211 (one 2 followed by one 1).
            1211 becomes 111221 (one 1, one 2, and two 1s).
            111221 becomes 312211 (three 1s, two 2s, and one 1).
            Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?
        </p>
        <input v-model="input" placeholder="Enter initial input here">
        <button @click="calculateLengthAfterLookAndSay()">Calculate Length After Look and Say</button>
        <p>Result Length: <span v-if="resultLength !== null">{{ resultLength }}</span></p>
        <h2>Part two</h2>
        <p>
            Neat, right? You might also enjoy hearing John Conway talking about this sequence (that's Conway of Conway's Game of Life fame).

            Now, starting again with the digits in your puzzle input, apply this process 50 times. What is the length of the new result?
        </p>
        <input v-model="input" placeholder="Enter initial input here">
        <button @click="calculateLengthAfterLookAndSay(50)">Calculate Length After Look and Say</button>
        <p>Result Length: <span v-if="resultLength2 !== null">{{ resultLength2 }}</span></p>
    </main>

</template>

<script>
    import { useRouter } from 'vue-router';

    export default {

        data() {
            return {
                input: '',
                resultLength: null,
                resultLength2: null
            };
        },


        setup() {
            const router = useRouter();
            return { router };
        },

        methods: {
            lookAndSay(input) {
                return input.replace(/(\d)\1*/g, match => match.length + match[0]);
            },
            calculateLengthAfterLookAndSay(n=40) {
                let result = this.input;
                for (let i = 0; i < n; i++) {
                    result = this.lookAndSay(result);
                }
                n === 40 ? this.resultLength = result.length : this.resultLength2 = result.length;
            }
        }
    }
</script>