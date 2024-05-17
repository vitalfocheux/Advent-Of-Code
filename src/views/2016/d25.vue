<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["La partie 1 ne fonctionne pas"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 25 - Clock Signal</h1>
    <h2>Part one</h2>
    <p>
        You open the door and find yourself on the roof. The city sprawls away from you for miles and miles.

        There's not much time now - it's already Christmas, but you're nowhere near the North Pole, much too far to deliver these stars to the sleigh in time.

        However, maybe the huge antenna up here can offer a solution. After all, the sleigh doesn't need the stars, exactly; it needs the timing data they provide, and you happen to have a massive signal generator right here.

        You connect the stars you have to your prototype computer, connect that to the antenna, and begin the transmission.

        Nothing happens.

        You call the service number printed on the side of the antenna and quickly explain the situation. "I'm not sure what kind of equipment you have connected over there," he says, "but you need a clock signal." You try to explain that this is a signal for a clock.

        "No, no, a clock signal - timing information so the antenna computer knows how to read the data you're sending it. An endless, alternating pattern of 0, 1, 0, 1, 0, 1, 0, 1, 0, 1...." He trails off.

        You ask if the antenna can handle a clock signal at the frequency you would need to use for the data from the stars. "There's no way it can! The only antenna we've installed capable of that is on top of a top-secret Easter Bunny installation, and you're definitely not-" You hang up the phone.

        You've extracted the antenna's clock signal generation assembunny code (your puzzle input); it looks mostly compatible with code you worked on just recently.

        This antenna code, being a signal generator, uses one extra instruction:

        out x transmits x (either an integer or the value of a register) as the next value for the clock signal.
        The code takes a value (via register a) that describes the signal to generate, but you're not sure how it's used. You'll have to find the input to produce the right signal through experimentation.

        What is the lowest positive integer that can be used to initialize register a and cause the code to output a clock signal of 0, 1, 0, 1... repeating forever?
    </p>
    <textarea v-model="instructions" placeholder="Enter instructions here"></textarea>
    <button @click="findLowestPositiveInteger">Find Lowest Positive Integer</button>
    <p>Lowest positive integer: <span v-if="lowestPositiveInteger !== null">{{ lowestPositiveInteger }}</span></p>
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
        instructions: '',
        lowestPositiveInteger: null
      }
    },
    methods: {
        findLowestPositiveInteger() {
            let a = 0;
            while (true) {
                const registers = { a, b: 0, c: 0, d: 0 };
                const output = [];
                const instructions = this.instructions.split('\n');
                for (let i = 0; i < instructions.length; i++) {
                    const [instr, x, y] = instructions[i].split(' ');
                    switch (instr) {
                        case 'cpy':
                        registers[y] = isNaN(x) ? registers[x] : Number(x);
                        break;
                        case 'inc':
                        registers[x]++;
                        break;
                        case 'dec':
                        registers[x]--;
                        break;
                        case 'jnz':
                        if ((isNaN(x) ? registers[x] : Number(x)) !== 0) {
                            i += isNaN(y) ? registers[y] : Number(y);
                            i--;
                        }
                        break;
                        case 'out':
                        output.push(isNaN(x) ? registers[x] : Number(x));
                        if (output.length > 10) return;
                        break;
                    }
                }
                if (output.join('') === '0101010101') {
                    this.lowestPositiveInteger = a;
                    console.log(a);
                    return;
                }
                a++;
            }
            
        },
    }
  }
</script>