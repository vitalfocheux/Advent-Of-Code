<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Trois essais pour la partie 1 avec Github Copilot",
                    "Un essai pour la partie 2 avec Github Copilot"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 8 - Two-Factor Authentication</h1>
    <h2>Part one</h2>
    <p>
        You come across a door implementing what you can only assume is an implementation of two-factor authentication after a long game of requirements telephone.

        To get past the door, you first swipe a keycard (no problem; there was one on a nearby desk). Then, it displays a code on a little screen, and you type that code on a keypad. Then, presumably, the door unlocks.

        Unfortunately, the screen has been smashed. After a few minutes, you've taken everything apart and figured out how it works. Now you just have to work out what the screen would have displayed.

        The magnetic strip on the card you swiped encodes a series of instructions for the screen; these instructions are your puzzle input. The screen is 50 pixels wide and 6 pixels tall, all of which start off, and is capable of three somewhat peculiar operations:

        rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
        rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels. Pixels that would fall off the right end appear at the left end of the row.
        rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by B pixels. Pixels that would fall off the bottom appear at the top of the column.
        For example, here is a simple sequence on a smaller screen:

        rect 3x2 creates a small rectangle in the top-left corner:

        ###....
        ###....
        .......
        rotate column x=1 by 1 rotates the second column down by one pixel:

        #.#....
        ###....
        .#.....
        rotate row y=0 by 4 rotates the top row right by four pixels:

        ....#.#
        ###....
        .#.....
        rotate column x=1 by 1 again rotates the second column down by one pixel, causing the bottom pixel to wrap back to the top:

        .#..#.#
        #.#....
        .#.....
        As you can see, this display technology is extremely powerful, and will soon dominate the tiny-code-displaying-screen market. That's what the advertisement on the back of the display tries to convince you, anyway.

        There seems to be an intermediate check of the voltage used by the display: after you swipe your card, if the screen did work, how many pixels should be lit?
    </p>
    <textarea v-model="input" placeholder="Enter instructions, one line per instruction"></textarea>
    <button @click="solve">Solve</button>
    <p>Number of lit pixels: <span v-if="litPixels !== 0">{{ litPixels }}</span></p>
    <h2>Part two</h2>
    <p>
        You notice that the screen is only capable of displaying capital letters; in the font it uses, each letter is 5 pixels wide and 6 tall.

        After you swipe your card, what code is the screen trying to display?
    </p>
    <textarea v-model="inputPart2" placeholder="Enter instructions, one line per instruction"></textarea>
    <button @click="solvePart2">Solve Part 2</button>
    <pre v-if="screenDisplay !== ''">{{ screenDisplay }}</pre>
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
        litPixels: 0,
        inputPart2: '',
        screenDisplay: ''
      }
    },
    methods: {
        solve() {
            const lines = this.input.split('\n').filter(line => line.trim() !== '');
            const screen = Array(6).fill().map(() => Array(50).fill(false));
            for (const line of lines) {
                const parts = line.split(' ');
                if (parts[0] === 'rect') {
                    const [width, height] = parts[1].split('x').map(Number);
                    for (let y = 0; y < height; y++) {
                        for (let x = 0; x < width; x++) {
                            screen[y][x] = true;
                        }
                    }
                } else if (parts[1] === 'row') {
                    const row = Number(parts[2].split('=')[1]);
                    const shift = Number(parts[4]);
                    const newRow = [...screen[row]]; // copy the row
                    screen[row] = newRow.map((_, i, arr) => arr[(i - shift + arr.length) % arr.length]);
                } else if (parts[1] === 'column') {
                    const col = Number(parts[2].split('=')[1]);
                    const shift = Number(parts[4]);
                    const column = screen.map(row => row[col]);
                    const newColumn = [...column]; // copy the column
                    for (let i = 0; i < newColumn.length; i++) {
                        screen[(i + shift) % newColumn.length][col] = newColumn[i];
                    }
                }
            }
            this.litPixels = screen.flat().filter(pixel => pixel).length;
        },
        executeInstruction(screen, instruction) {
            const parts = instruction.split(' ');
            if (parts[0] === 'rect') {
                const [width, height] = parts[1].split('x').map(Number);
                for (let y = 0; y < height; y++) {
                    for (let x = 0; x < width; x++) {
                        screen[y][x] = true;
                    }
                }
            } else if (parts[1] === 'row') {
                const row = Number(parts[2].split('=')[1]);
                const shift = Number(parts[4]);
                const newRow = [...screen[row]];
                screen[row] = newRow.map((_, i, arr) => arr[(i - shift + arr.length) % arr.length]);
            } else if (parts[1] === 'column') {
                const col = Number(parts[2].split('=')[1]);
                const shift = Number(parts[4]);
                const column = screen.map(row => row[col]);
                const newColumn = [...column];
                for (let i = 0; i < newColumn.length; i++) {
                    screen[(i + shift) % newColumn.length][col] = newColumn[i];
                }
            }
        },
        solvePart2() {
            const lines = this.inputPart2.split('\n').filter(line => line.trim() !== '');
            const screen = Array(6).fill().map(() => Array(50).fill(false));
            for (const line of lines) {
                this.executeInstruction(screen, line);
            }
            this.screenDisplay = screen.map(row => row.map(pixel => pixel ? '#' : ' ').join('')).join('\n');
        }
    }
  }
</script>