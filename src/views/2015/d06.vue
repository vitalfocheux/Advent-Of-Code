<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Trois essais pour résoudre la partie 1 avec Github Copilot",
                "Un essai pour la partie 2 avec Github Copilot"]
</script>

<template>
    <Navbar />

    <HeaderAI :msg= "messages"/>

    <main>
        <h1>Day 6 - Probably a Fire Hazard</h1>
        <h2>Part one</h2>
        <p>
            Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

            Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

            Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

            To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

            For example:

            turn on 0,0 through 999,999 would turn on (or leave on) every light.
            toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
            turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
            After following the instructions, how many lights are lit?
        </p>
        <textarea v-model="instructions" placeholder="Enter instructions here, one per line"></textarea>
        <button @click="countLitLights">Count Lit Lights</button>
        <p >Number of lit lights: <span v-if="litLightsCount !== null">{{ litLightsCount }}</span></p>
        <h2>Part two</h2>
        <p>
            You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

            The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

            The phrase turn on actually means that you should increase the brightness of those lights by 1.

            The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

            The phrase toggle actually means that you should increase the brightness of those lights by 2.

            What is the total brightness of all lights combined after following Santa's instructions?

            For example:

            turn on 0,0 through 0,0 would increase the total brightness by 1.
            toggle 0,0 through 999,999 would increase the total brightness by 2000000.
        </p>
        <textarea v-model="instructions" placeholder="Enter instructions here, one per line"></textarea>
        <button @click="calculateTotalBrightness">Calculate Total Brightness</button>
        <p>Total brightness: <span v-if="totalBrightness !== null">{{ totalBrightness }}</span></p>
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
        litLightsCount: null,
        totalBrightness: null,
        grid: Array(1000).fill().map(() => Array(1000).fill(false))
      }
    },
    methods: {
        countLitLights() {
            const instructionsArray = this.instructions.split('\n');
            const litLights = new Set(); // Use a Set to store the positions of lit lights
            instructionsArray.forEach(instruction => this.executeInstruction(instruction, litLights));
            this.litLightsCount = litLights.size; // The size of the Set is the number of lit lights
        },
        executeInstruction(instruction, litLights) {
            const [action, xStart, yStart, xEnd, yEnd] = instruction.match(/(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)/).slice(1);
            for (let x = +xStart; x <= +xEnd; x++) {
            for (let y = +yStart; y <= +yEnd; y++) {
                const pos = `${x},${y}`; // Use a string to represent the position
                if (action === 'turn on') litLights.add(pos);
                else if (action === 'turn off') litLights.delete(pos);
                else if (action === 'toggle') litLights.has(pos) ? litLights.delete(pos) : litLights.add(pos);
            }
            }
        },
        calculateTotalBrightness() {
            const instructionsArray = this.instructions.split('\n');
            const lights = new Map(); // Use a Map to store the brightness of each light
            instructionsArray.forEach(instruction => this.executeInstruction2(instruction, lights));
            this.totalBrightness = Array.from(lights.values()).reduce((a, b) => a + b, 0); // Sum up the brightness of all lights
        },
        executeInstruction2(instruction, lights) {
        const [action, xStart, yStart, xEnd, yEnd] = instruction.match(/(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)/).slice(1);
        for (let x = +xStart; x <= +xEnd; x++) {
            for (let y = +yStart; y <= +yEnd; y++) {
                const pos = `${x},${y}`; // Use a string to represent the position
                const brightness = lights.get(pos) || 0; // Get the current brightness, default to 0 if not set
                if (action === 'turn on') lights.set(pos, brightness + 1);
                else if (action === 'turn off') lights.set(pos, Math.max(0, brightness - 1));
                else if (action === 'toggle') lights.set(pos, brightness + 2);
            }
        }
        }
    }
  }
</script>