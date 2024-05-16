<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Un essai pour résoudre le jour 3 de l'Advent of Code 2016 avec Github Copilot"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 3 - Squares With Three Sides</h1>
    <h2>Part one</h2>
    <p>
        Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.

        Or are they?

        The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones.

        In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.

        In your puzzle input, how many of the listed triangles are possible?
    </p>
    <textarea v-model="input" placeholder="Enter triangle sides, one line per triangle"></textarea>
    <button @click="solve">Solve</button>
    <p>Number of possible triangles: <span v-if="possibleTriangles !== 0">{{ possibleTriangles }}</span></p>
    <h2>Part two</h2>
    <p>
        Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.

        For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

        101 301 501
        102 302 502
        103 303 503
        201 401 601
        202 402 602
        203 403 603
        In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?
    </p>
    <textarea v-model="input2" placeholder="Enter triangle sides, one line per triangle"></textarea>
    <button @click="solvePart2">Solve Part 2</button>
    <p>Number of possible triangles for Part 2: <span v-if="possibleTriangles2 !== 0">{{ possibleTriangles2 }}</span></p>
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
        possibleTriangles: 0,
        input2: '',
        possibleTriangles2: 0
      }
    },
    methods: {
        solve() {
            const lines = this.input.split('\n');
            let count = 0;
            for (const line of lines) {
                const sides = line.trim().split(/\s+/).map(Number).sort((a, b) => a - b);
                if (sides[0] + sides[1] > sides[2]) {
                    count++;
                }
            }
            this.possibleTriangles = count;
        },
        solvePart2() {
            const lines = this.input2.split('\n').filter(line => line.trim() !== '');
            let count = 0;
            const triangles = [];
            for (let i = 0; i < lines.length; i += 3) {
                const triangle1 = [], triangle2 = [], triangle3 = [];
                for (let j = 0; j < 3; j++) {
                    const sides = lines[i + j].trim().split(/\s+/).map(Number);
                    triangle1.push(sides[0]);
                    triangle2.push(sides[1]);
                    triangle3.push(sides[2]);
                }
                triangles.push(triangle1, triangle2, triangle3);
            }
            for (const triangle of triangles) {
                const sides = triangle.sort((a, b) => a - b);
                if (sides[0] + sides[1] > sides[2]) {
                    count++;
                }
            }
            this.possibleTriangles2 = count;
        }
    }
  }
</script>