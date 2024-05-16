<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Un essai pour résoudre le jour 2 de l'Advent of Code 2016 avec Github Copilot"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 2 - Bathroom Security</h1>
    <h2>Part one</h2>
    <p>
        You arrive at Easter Bunny Headquarters under cover of darkness. However, you left in such a rush that you forgot to use the bathroom! Fancy office buildings like this one usually have keypad locks on their bathrooms, so you search the front desk for the code.

        "In order to improve security," the document you find says, "bathroom codes will no longer be written down. Instead, please memorize and follow the procedure below to access the bathrooms."

        The document goes on to explain that each button to be pressed can be found by starting on the previous button and moving to adjacent buttons on the keypad: U moves up, D moves down, L moves left, and R moves right. Each line of instructions corresponds to one button, starting at the previous button (or, for the first line, the "5" button); press whatever button you're on at the end of each line. If a move doesn't lead to a button, ignore it.

        You can't hold it much longer, so you decide to figure out the code as you walk to the bathroom. You picture a keypad like this:

        1 2 3
        4 5 6
        7 8 9
        Suppose your instructions are:

        ULL
        RRDDD
        LURDL
        UUUUD
        You start at "5" and move up (to "2"), left (to "1"), and left (you can't, and stay on "1"), so the first button is 1.
        Starting from the previous button ("1"), you move right twice (to "3") and then down three times (stopping at "9" after two moves and ignoring the third), ending up with 9.
        Continuing from "9", you move left, up, right, down, and left, ending with 8.
        Finally, you move up four times (stopping at "2"), then down once, ending with 5.
        So, in this example, the bathroom code is 1985.

        Your puzzle input is the instructions from the document you found at the front desk. What is the bathroom code?
    </p>
    <textarea v-model="input" placeholder="Enter instructions, one line per instruction"></textarea>
    <button @click="solve">Solve</button>
    <p>Bathroom code: <span v-if="bathroomCode !== ''">{{ bathroomCode }}</span></p>
    <h2>Part two</h2>
    <p>
        You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many fancy conference rooms and water coolers on this floor) and go to punch in the code. Much to your bladder's dismay, the keypad is not at all like you imagined it. Instead, you are confronted with the result of hundreds of man-hours of bathroom-keypad-design meetings:

            1
        2 3 4
        5 6 7 8 9
        A B C
            D
        You still start at "5" and stop when you're at an edge, but given the same instructions as above, the outcome is very different:

        You start at "5" and don't move at all (up and left are both edges), ending at 5.
        Continuing from "5", you move right twice and down three times (through "6", "7", "B", "D", "D"), ending at D.
        Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at B.
        Finally, after five more moves, you end at 3.
        So, given the actual keypad layout, the code would be 5DB3.

        Using the same instructions in your puzzle input, what is the correct bathroom code?
    </p>
    <textarea v-model="input2" placeholder="Enter instructions, one line per instruction"></textarea>
    <button @click="solvePart2">Solve Part 2</button>
    <p>Bathroom code for Part 2: <span v-if="bathroomCode2 !== ''">{{ bathroomCode2 }}</span></p>
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
        bathroomCode: '',
        input2: '',
        bathroomCode2: ''
      }
    },
    methods: {
        solve() {
            const instructions = this.input.split('\n');
            let x = 1, y = 1; // Start at '5'
            const keypad = [
                ['1', '2', '3'],
                ['4', '5', '6'],
                ['7', '8', '9']
            ];
            let code = '';
            for (const instruction of instructions) {
                for (const move of instruction) {
                    switch (move) {
                        case 'U': y = Math.max(y - 1, 0); break;
                        case 'D': y = Math.min(y + 1, 2); break;
                        case 'L': x = Math.max(x - 1, 0); break;
                        case 'R': x = Math.min(x + 1, 2); break;
                    }
                }
                code += keypad[y][x];
            }
            this.bathroomCode = code;
        },
        solvePart2() {
            const instructions = this.input2.split('\n');
            let x = 0, y = 2; // Start at '5'
            const keypad = [
                [null, null, '1', null, null],
                [null, '2', '3', '4', null],
                ['5', '6', '7', '8', '9'],
                [null, 'A', 'B', 'C', null],
                [null, null, 'D', null, null]
            ];
            let code = '';
            for (const instruction of instructions) {
                for (const move of instruction) {
                    let newX = x, newY = y;
                    switch (move) {
                        case 'U': newY = Math.max(y - 1, 0); break;
                        case 'D': newY = Math.min(y + 1, 4); break;
                        case 'L': newX = Math.max(x - 1, 0); break;
                        case 'R': newX = Math.min(x + 1, 4); break;
                    }
                    if (keypad[newY][newX] !== null) {
                        x = newX;
                        y = newY;
                    }
                }
                code += keypad[y][x];
            }
            this.bathroomCode2 = code;
        }
    }
  }
</script>