<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Un essai pour résoudre le jour 11 de l'Advent of Code 2017 avec Github Copilot"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 11 - Hex Ed</h1>
    <h2>Part one</h2>
    <p>
        Crossing the bridge, you've barely reached the other side of the stream when a program comes up to you, clearly in distress. "It's my child process," she says, "he's gotten lost in an infinite grid!"

        Fortunately for her, you have plenty of experience with infinite grids.

        Unfortunately for you, it's a hex grid.

        The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be found to the north, northeast, southeast, south, southwest, and northwest:

        \ n  /
        nw +--+ ne
        /    \
        -+      +-
        \    /
        sw +--+ se
        / s  \
        You have the path the child process took. Starting where he started, you need to determine the fewest number of steps required to reach him. (A "step" means to move from the hex you are in to any adjacent hex.)

        For example:

        ne,ne,ne is 3 steps away.
        ne,ne,sw,sw is 0 steps away (back where you started).
        ne,ne,s,s is 2 steps away (se,se).
        se,sw,se,sw,sw is 3 steps away (s,s,sw).
    </p>
    <input v-model="directionsInput" placeholder="Enter directions here">
    <button @click="calculateMinimumSteps">Calculate Minimum Steps</button>
    <p>Minimum Steps: {{ minimumSteps }}</p>
    <h2>Part two</h2>
    <p>
        How many steps away is the furthest he ever got from his starting position?
    </p>
    <input v-model="directionsInputPartTwo" placeholder="Enter directions here">
    <button @click="calculateMaximumDistance">Calculate Maximum Distance</button>
    <p>Maximum Distance: {{ maximumDistance }}</p>
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
        directionsInput: '',
        minimumSteps: null,
        directionsInputPartTwo: '',
        maximumDistance: null
      }
    },
    methods: {
        calculateMinimumSteps() {
            const directions = this.directionsInput.split(',');
            let x = 0, y = 0, z = 0;

            directions.forEach(direction => {
                switch (direction) {
                case 'n':  y++; z--; break;
                case 'ne': x++; z--; break;
                case 'se': x++; y--; break;
                case 's':  y--; z++; break;
                case 'sw': x--; z++; break;
                case 'nw': x--; y++; break;
                }
            });

            this.minimumSteps = (Math.abs(x) + Math.abs(y) + Math.abs(z)) / 2;
        },
        calculateMaximumDistance() {
            const directions = this.directionsInputPartTwo.split(',');
            let x = 0, y = 0, z = 0;
            let maxDistance = 0;

            directions.forEach(direction => {
                switch (direction) {
                case 'n':  y++; z--; break;
                case 'ne': x++; z--; break;
                case 'se': x++; y--; break;
                case 's':  y--; z++; break;
                case 'sw': x--; z++; break;
                case 'nw': x--; y++; break;
                }

                const currentDistance = (Math.abs(x) + Math.abs(y) + Math.abs(z)) / 2;
                maxDistance = Math.max(maxDistance, currentDistance);
            });

            this.maximumDistance = maxDistance;
        },
    }
  }
</script>