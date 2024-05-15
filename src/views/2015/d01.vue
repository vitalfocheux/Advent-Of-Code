<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
</script>

<template>
    <Navbar />

    <HeaderAI msg="Un essai pour résoudre le jour 1 de l'Advent of Code 2015 avec Github Copilot" />

    <main>
      <h1>Day 1 - Not Quite Lisp</h1>
      <h2>Part one</h2>
      <p>
        Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and he's fresh out! To save Christmas, he needs you to collect fifty stars by December 25th.

        Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

        Here's an easy puzzle to warm you up.

        Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

        An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

        The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

        For example:

        (()) and ()() both result in floor 0.
        ((( and (()(()( both result in floor 3.
        ))((((( also results in floor 3.
        ()) and ))( both result in floor -1 (the first basement level).
        ))) and )())()) both result in floor -3.
        To what floor do the instructions take Santa?
      </p>
      <input type="text" v-model="instructions" placeholder="Enter instructions here">
      <button @click="solvePuzzle">Solve Puzzle</button>
      <p>Santa is on floor: <span v-if="floor !== null">{{ floor }}</span></p>
      <h2>Part two</h2>
      <p>
        Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

        For example:

        ) causes him to enter the basement at character position 1.
        ()()) causes him to enter the basement at character position 5.
        What is the position of the character that causes Santa to first enter the basement?
      </p>
      <input type="text" v-model="instructions" placeholder="Enter instructions here">
      <button @click="solvePuzzlePartTwo">Solve Puzzle Part Two</button>
      <p>Santa first enters the basement at character position: <span v-if="basementPosition !== null">{{ basementPosition }}</span></p>
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
        floor: null,
        basementPosition: null
      }
    },
    methods: {
      solvePuzzle() {
        this.floor = 0;
        for (let i = 0; i < this.instructions.length; i++) {
          (this.instructions[i] === '(') ? this.floor++ : this.floor--;
        }
      },
      solvePuzzlePartTwo() {
        this.floor = 0;
        for (let i = 0; i < this.instructions.length; i++) {
          if (this.instructions[i] === '(') {
            this.floor++;
          } else if (this.instructions[i] === ')') {
            this.floor--;
          }
          if (this.floor === -1) {
            this.basementPosition = i + 1;
            break;
          }
        }
        floor = null;
      }
    }
  }
</script>