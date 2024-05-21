<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Un essai pour résoudre le jour 8 de l'Advent of Code 2017 avec Github Copilot"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 8 - I Heard You Like Registers</h1>
    <h2>Part one</h2>
    <p>
        You receive a signal directly from the CPU. Because of your recent assistance with jump instructions, it would like you to compute the result of a series of unusual register instructions.

        Each instruction consists of several parts: the register to modify, whether to increase or decrease that register's value, the amount by which to increase or decrease it, and a condition. If the condition fails, skip the instruction without modifying the register. The registers all start at 0. The instructions look like this:

        b inc 5 if a > 1
        a inc 1 if b < 5
        c dec -10 if a >= 1
        c inc -20 if c == 10
        These instructions would be processed as follows:

        Because a starts at 0, it is not greater than 1, and so b is not modified.
        a is increased by 1 (to 1) because b is less than 5 (it is 0).
        c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
        c is increased by -20 (to -10) because c is equal to 10.
        After this process, the largest value in any register is 1.

        You might also encounter <= (less than or equal to) or != (not equal to). However, the CPU doesn't have the bandwidth to tell you what all the registers are named, and leaves that to you to determine.

        What is the largest value in any register after completing the instructions in your puzzle input?
    </p>
    <textarea v-model="instructionList" placeholder="Enter instruction list here"></textarea>
    <button @click="executeInstructions">Execute Instructions</button>
    <p>Highest Value: {{ highestValue }}</p>
    <h2>Part two</h2>
    <p>
        To be safe, the CPU also needs to know the highest value held in any register during this process so that it can decide how much memory to allocate to these operations. For example, in the above instructions, the highest value ever held was 10 (in register c after the third instruction was evaluated).
    </p>
    <textarea v-model="instructionListPartTwo" placeholder="Enter instruction list here"></textarea>
    <button @click="executeInstructionsPartTwo">Execute Instructions</button>
    <p>Highest Value Ever: {{ highestValueEver }}</p>
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
        instructionList: '',
        highestValue: null,
        instructionListPartTwo: '',
        highestValueEver: null,
      }
    },
    methods: {
        executeInstructions() {
            const instructions = this.instructionList.split('\n');
            const registers = {};

            instructions.forEach(instruction => {
                const [reg, op, val, , condReg, condOp, condVal] = instruction.split(' ');

                if (!registers[reg]) registers[reg] = 0;
                if (!registers[condReg]) registers[condReg] = 0;

                if (eval(`${registers[condReg]} ${condOp} ${condVal}`)) {
                registers[reg] += op === 'inc' ? Number(val) : -Number(val);
                }
            });

            this.highestValue = Math.max(...Object.values(registers));
        },
        executeInstructionsPartTwo() {
            const instructions = this.instructionListPartTwo.split('\n');
            const registers = {};
            let highestValueEver = -Infinity;

            instructions.forEach(instruction => {
                const [reg, op, val, , condReg, condOp, condVal] = instruction.split(' ');

                if (!registers[reg]) registers[reg] = 0;
                if (!registers[condReg]) registers[condReg] = 0;

                if (eval(`${registers[condReg]} ${condOp} ${condVal}`)) {
                registers[reg] += op === 'inc' ? Number(val) : -Number(val);
                highestValueEver = Math.max(highestValueEver, registers[reg]);
                }
            });

            this.highestValueEver = highestValueEver;
        },
    }
  }
</script>