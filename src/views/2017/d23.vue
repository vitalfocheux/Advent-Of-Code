<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Un essai pour la partie 1 avec Github Copilot",
                    "Deux essais pour la partie 2 avec Github Copilot"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 23 - Coprocessor Conflagration</h1>
    <h2>Part one</h2>
    <p>
        You decide to head directly to the CPU and fix the printer from there. As you get close, you find an experimental coprocessor doing so much work that the local programs are afraid it will halt and catch fire. This would cause serious issues for the rest of the computer, so you head in and see what you can do.

        The code it's running seems to be a variant of the kind you saw recently on that tablet. The general functionality seems very similar, but some of the instructions are different:

        set X Y sets register X to the value of Y.
        sub X Y decreases register X by the value of Y.
        mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
        jnz X Y jumps with an offset of the value of Y, but only if the value of X is not zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
        Only the instructions listed above are used. The eight registers here, named a through h, all start at 0.

        The coprocessor is currently set to some kind of debug mode, which allows for testing, but prevents it from doing any meaningful work.

        If you run the program (your puzzle input), how many times is the mul instruction invoked?
    </p>
    <textarea v-model="program" placeholder="Enter program here"></textarea>
    <button @click="runProgram">Run Program</button>
    <p>Number of mul invocations: {{ mulInvocations }}</p>
    <h2>Part two</h2>
    <p>
        Now, it's time to fix the problem.

        The debug mode switch is wired directly to register a. You flip the switch, which makes register a now start at 1 when the program is executed.

        Immediately, the coprocessor begins to overheat. Whoever wrote this program obviously didn't choose a very efficient implementation. You'll need to optimize the program if it has any hope of completing before Santa needs that printer working.

        The coprocessor's ultimate goal is to determine the final value left in register h once the program completes. Technically, if it had that... it wouldn't even need to run the program.

        After setting register a to 1, if the program were to run to completion, what value would be left in register h?
    </p>
    <textarea v-model="program" placeholder="Enter program here"></textarea>
    <button @click="calculateNonPrimes">Calculate Non-Primes</button>
    <p>Number of non-prime numbers: {{ nonPrimes }}</p>
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
        program: '',
        mulInvocations: null,
        b: 0,
        c: 0,
        nonPrimes: null,
      }
    },
    methods: {
        runProgram() {
            const instructions = this.program.split('\n');
            const registers = { a: 0, b: 0, c: 0, d: 0, e: 0, f: 0, g: 0, h: 0 };
            let mulInvocations = 0;
            let i = 0;

            const getValue = x => isNaN(x) ? registers[x] : Number(x);

            while (i >= 0 && i < instructions.length) {
                const [instr, x, y] = instructions[i].split(' ');

                switch (instr) {
                case 'set':
                    registers[x] = getValue(y);
                    break;
                case 'sub':
                    registers[x] -= getValue(y);
                    break;
                case 'mul':
                    registers[x] *= getValue(y);
                    mulInvocations++;
                    break;
                case 'jnz':
                    if (getValue(x) !== 0) {
                    i += getValue(y);
                    continue;
                    }
                    break;
                }

                i++;
            }

            this.mulInvocations = mulInvocations;
        },
        isPrime(n) {
            for (let i = 2; i * i <= n; i++) {
                if (n % i === 0) return false;
            }
            return true;
        },
        calculateNonPrimes() {
            const instructions = this.program.split('\n');
            let b = Number(instructions[0].split(' ')[2]) * Number(instructions[4].split(' ')[2]) - Number(instructions[5].split(' ')[2]);// 100 + 100000;
            let c = b - Number(instructions[7].split(' ')[2]);
            let nonPrimes = 0;

            for (let i = b; i <= c; i += 17) {
                if (!this.isPrime(i)) nonPrimes++;
            }

            this.nonPrimes = nonPrimes;
        },
    }
  }
</script>