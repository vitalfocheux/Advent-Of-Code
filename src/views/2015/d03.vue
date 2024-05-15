<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Un essai pour résoudre le jour 3 de l'Advent of Code 2015 avec Github Copilot"]
</script>

<template>
    <Navbar />

    <HeaderAI :msg="messages" />

    <main>
        <h1>Day 3 - Perfectly Spherical Houses in a Vacuum</h1>
        <h2>Part one</h2>
        <p>
            Santa is delivering presents to an infinite two-dimensional grid of houses.

            He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

            However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

            For example:

            > delivers presents to 2 houses: one at the starting location, and one to the east.
            ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
            ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
        </p>
        <input type="text" v-model="moves" placeholder="Enter Santa's moves here">
        <button @click="solvePuzzle">Solve Puzzle</button>
        <p>Number of houses that receive at least one present:<span v-if="houses !== null">{{ houses.size }}</span></p>
        <h2>Part two</h2>
        <p>
            The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

            Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

            This year, how many houses receive at least one present?

            For example:

            ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
            ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
            ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
        </p>
        <input type="text" v-model="moves" placeholder="Enter Santa's moves here">
        <button @click="solvePuzzlePartTwo">Solve Puzzle Part Two</button>
        <p>Number of houses that receive at least one present:<span v-if="houses2 !== null">{{ houses2.size }}</span></p>
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
        moves: '',
        houses: null,
        houses2: null
      }
    },
    methods: {
        solvePuzzle() {
            let x = 0, y = 0;
            this.houses = new Set(['0,0']);
            for (let i = 0; i < this.moves.length; i++) {
                switch (this.moves[i]) {
                case '^': y++; break;
                case 'v': y--; break;
                case '>': x++; break;
                case '<': x--; break;
                }
                this.houses.add(`${x},${y}`);
            }
        },
        solvePuzzlePartTwo() {
            let x = [0, 0], y = [0, 0];
            this.houses2 = new Set(['0,0']);
            for (let i = 0; i < this.moves.length; i++) {
                const j = i % 2;
                switch (this.moves[i]) {
                case '^': y[j]++; break;
                case 'v': y[j]--; break;
                case '>': x[j]++; break;
                case '<': x[j]--; break;
                }
                this.houses2.add(`${x[j]},${y[j]}`);
            }
        }
    }
  }
</script>