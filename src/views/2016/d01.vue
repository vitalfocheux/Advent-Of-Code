<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Un essai pour résoudre le jour 1 de l'Advent of Code 2016 avec Github Copilot"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 1 - No Time for a Taxicab</h1>
    <h2>Part one</h2>
    <p>
      Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.

      Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

      You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.

      The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

      There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?

      For example:

      Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
      R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
      R5, L5, R5, R3 leaves you 12 blocks away.
      How many blocks away is Easter Bunny HQ?
    </p>
    <textarea v-model="input" placeholder="Enter instructions, separated by commas"></textarea>
    <button @click="solve">Solve</button>
    <p>Distance: <span v-if="distance !== null">{{ distance }}</span></p>
    <h2>Part two</h2>
    <p>
      Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

      For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

      How many blocks away is the first location you visit twice?
    </p>
    <textarea v-model="input2" placeholder="Enter instructions, separated by commas"></textarea>
    <button @click="solvePart2">Solve Part 2</button>
    <p>Distance to first location visited twice: <span v-if="distance2 !== null">{{ distance2 }}</span></p>
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
        distance: null,
        input2: '',
        distance2: null
      }
    },
    methods: {
      solve() {
        const instructions = this.input.split(',').map(s => s.trim());
        let direction = 0; // 0: north, 1: east, 2: south, 3: west
        let x = 0, y = 0;
        for (const instruction of instructions) {
          const turn = instruction[0];
          const blocks = Number(instruction.slice(1));
          direction = (direction + (turn === 'R' ? 1 : 3)) % 4;
          switch (direction) {
            case 0: y += blocks; break;
            case 1: x += blocks; break;
            case 2: y -= blocks; break;
            case 3: x -= blocks; break;
          }
        }
        this.distance = Math.abs(x) + Math.abs(y);
      },
      solvePart2() {
        const instructions = this.input2.split(',').map(s => s.trim());
        let direction = 0; // 0: north, 1: east, 2: south, 3: west
        let x = 0, y = 0;
        const visited = new Set(['0,0']);
        for (const instruction of instructions) {
          const turn = instruction[0];
          const blocks = Number(instruction.slice(1));
          direction = (direction + (turn === 'R' ? 1 : 3)) % 4;
          for (let i = 0; i < blocks; i++) {
            switch (direction) {
              case 0: y++; break;
              case 1: x++; break;
              case 2: y--; break;
              case 3: x--; break;
            }
            const location = `${x},${y}`;
            if (visited.has(location)) {
              this.distance2 = Math.abs(x) + Math.abs(y);
              return;
            }
            visited.add(location);
          }
        }
      }
    }
  }
</script>