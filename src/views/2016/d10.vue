<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Un essai pour résoudre le jour 10 de l'Advent of Code 2016 avec Github Copilot"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 10 - Balance Bots</h1>
    <h2>Part one</h2>
    <p>
        You come upon a factory in which many robots are zooming around handing small microchips to each other.

        Upon closer examination, you notice that each bot only proceeds when it has two microchips, and once it does, it gives each one to a different bot or puts it in a marked "output" bin. Sometimes, bots take microchips from "input" bins, too.

        Inspecting one of the microchips, it seems like they each contain a single number; the bots must use some logic to decide what to do with each chip. You access the local control computer and download the bots' instructions (your puzzle input).

        Some of the instructions specify that a specific-valued microchip should be given to a specific bot; the rest of the instructions indicate what a given bot should do with its lower-value or higher-value chip.

        For example, consider the following instructions:

        value 5 goes to bot 2
        bot 2 gives low to bot 1 and high to bot 0
        value 3 goes to bot 1
        bot 1 gives low to output 1 and high to bot 0
        bot 0 gives low to output 2 and high to output 0
        value 2 goes to bot 2
        Initially, bot 1 starts with a value-3 chip, and bot 2 starts with a value-2 chip and a value-5 chip.
        Because bot 2 has two microchips, it gives its lower one (2) to bot 1 and its higher one (5) to bot 0.
        Then, bot 1 has two microchips; it puts the value-2 chip in output 1 and gives the value-3 chip to bot 0.
        Finally, bot 0 has two microchips; it puts the 3 in output 2 and the 5 in output 0.
        In the end, output bin 0 contains a value-5 microchip, output bin 1 contains a value-2 microchip, and output bin 2 contains a value-3 microchip. In this configuration, bot number 2 is responsible for comparing value-5 microchips with value-2 microchips.

        Based on your instructions, what is the number of the bot that is responsible for comparing value-61 microchips with value-17 microchips?
    </p>
    <textarea v-model="inputPart1" placeholder="Enter instructions, one line per instruction"></textarea>
    <button @click="solvePart1">Solve Part 1</button>
    <p>Bot comparing 61 and 17: <span v-if="botComparing !== ''">{{ botComparing }}</span></p>
    <h2>Part two</h2>
    <p>
        What do you get if you multiply together the values of one chip in each of outputs 0, 1, and 2?
    </p>
    <textarea v-model="inputPart2" placeholder="Enter instructions, one line per instruction"></textarea>
    <button @click="solvePart2">Solve Part 2</button>
    <p>Product of values in outputs 0, 1, and 2: <span v-if="outputProduct !== 0">{{ outputProduct }}</span></p>
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
        inputPart1: '',
        botComparing: '',
        inputPart2: '',
        outputProduct: 0
      }
    },
    methods: {
        solvePart1() {
            const lines = this.inputPart1.split('\n').filter(line => line.trim() !== '');
            const bots = {};
            const instructions = [];

            for (const line of lines) {
                if (line.startsWith('value')) {
                    const [_, value, bot] = line.match(/value (\d+) goes to bot (\d+)/);
                    if (!bots[bot]) bots[bot] = [];
                    bots[bot].push(Number(value));
                } else {
                    instructions.push(line);
                }
            }

            while (instructions.length > 0) {
                for (let i = 0; i < instructions.length; i++) {
                    const [_, bot, lowTo, low, highTo, high] = instructions[i].match(/bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)/);
                    if (bots[bot] && bots[bot].length === 2) {
                        bots[bot].sort((a, b) => a - b);
                        if (bots[bot][0] === 17 && bots[bot][1] === 61) {
                            this.botComparing = bot;
                            return;
                        }
                        if (!bots[low]) bots[low] = [];
                        bots[low].push(bots[bot][0]);
                        if (!bots[high]) bots[high] = [];
                        bots[high].push(bots[bot][1]);
                        instructions.splice(i, 1);
                        break;
                    }
                }
            }
        },
        solvePart2() {
            const lines = this.inputPart2.split('\n').filter(line => line.trim() !== '');
            const bots = {};
            const outputs = {};
            const instructions = [];

            for (const line of lines) {
                if (line.startsWith('value')) {
                    const [_, value, bot] = line.match(/value (\d+) goes to bot (\d+)/);
                    if (!bots[bot]) bots[bot] = [];
                    bots[bot].push(Number(value));
                } else {
                    instructions.push(line);
                }
            }

            while (instructions.length > 0) {
                for (let i = 0; i < instructions.length; i++) {
                    const [_, bot, lowTo, low, highTo, high] = instructions[i].match(/bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)/);
                    if (bots[bot] && bots[bot].length === 2) {
                        bots[bot].sort((a, b) => a - b);
                        if (lowTo === 'output') {
                            if (!outputs[low]) outputs[low] = [];
                            outputs[low].push(bots[bot][0]);
                        } else {
                            if (!bots[low]) bots[low] = [];
                            bots[low].push(bots[bot][0]);
                        }
                        if (highTo === 'output') {
                            if (!outputs[high]) outputs[high] = [];
                            outputs[high].push(bots[bot][1]);
                        } else {
                            if (!bots[high]) bots[high] = [];
                            bots[high].push(bots[bot][1]);
                        }
                        instructions.splice(i, 1);
                        break;
                    }
                }
            }

            this.outputProduct = outputs[0][0] * outputs[1][0] * outputs[2][0];
        }
    }
  }
</script>