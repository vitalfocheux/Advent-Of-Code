<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Un essai pour résoudre le jour 19 de l'Advent of Code 2017 avec Github Copilot"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 19 - A Series of Tubes</h1>
    <h2>Part one</h2>
    <p>
        Somehow, a network packet got lost and ended up here. It's trying to follow a routing diagram (your puzzle input), but it's confused about where to go.

        Its starting point is just off the top of the diagram. Lines (drawn with |, -, and +) show the path it needs to take, starting by going down onto the only line connected to the top of the diagram. It needs to follow this path until it reaches the end (located somewhere within the diagram) and stop there.

        Sometimes, the lines cross over each other; in these cases, it needs to continue going the same direction, and only turn left or right when there's no other option. In addition, someone has left letters on the line; these also don't change its direction, but it can use them to keep track of where it's been. For example:

            |          
            |  +--+    
            A  |  C    
        F---|----E|--+ 
            |  |  |  D 
            +B-+  +--+ 

        Given this diagram, the packet needs to take the following path:

        Starting at the only line touching the top of the diagram, it must go down, pass through A, and continue onward to the first +.
        Travel right, up, and right, passing through B in the process.
        Continue down (collecting C), right, and up (collecting D).
        Finally, go all the way left through E and stopping at F.
        Following the path to the end, the letters it sees on its path are ABCDEF.

        The little packet looks up at you, hoping you can help it find the way. What letters will it see (in the order it would see them) if it follows the path? (The routing diagram is very wide; make sure you view it without line wrapping.)
    </p>
    <textarea v-model="routingDiagram" placeholder="Enter routing diagram here"></textarea>
    <button @click="followPath">Follow Path</button>
    <p>Letters encountered: {{ lettersEncountered }}</p>
    <h2>Part two</h2>
    <p>
        The packet is curious how many steps it needs to go.

        For example, using the same routing diagram from the example above...

            |          
            |  +--+    
            A  |  C    
        F---|--|-E---+ 
            |  |  |  D 
            +B-+  +--+ 

        ...the packet would go:

        6 steps down (including the first line at the top of the diagram).
        3 steps right.
        4 steps up.
        3 steps right.
        4 steps down.
        3 steps right.
        2 steps up.
        13 steps left (including the F it stops on).
        This would result in a total of 38 steps.

        How many steps does the packet need to go?
    </p>
    <textarea v-model="routingDiagram2" placeholder="Enter routing diagram here"></textarea>
    <button @click="followPath2">Follow Path</button>
    <p>Number of steps taken: {{ numStepsTaken }}</p>
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
        routingDiagram: '',
        lettersEncountered: '',
        routingDiagram2: '',
        numStepsTaken: null,
      }
    },
    methods: {
        followPath() {
            const lines = this.routingDiagram.split('\n');
            let direction = 'down';
            let row = 0;
            let col = lines[0].indexOf('|');
            let lettersEncountered = '';

            while (true) {
                const currentChar = lines[row][col];

                if (/[A-Z]/.test(currentChar)) {
                lettersEncountered += currentChar;
                }

                if (currentChar === '+') {
                if (direction === 'up' || direction === 'down') {
                    direction = lines[row][col - 1] === ' ' ? 'right' : 'left';
                } else {
                    direction = lines[row - 1] && lines[row - 1][col] === ' ' ? 'down' : 'up';
                }
                }

                switch (direction) {
                case 'up':
                    row--;
                    break;
                case 'down':
                    row++;
                    break;
                case 'left':
                    col--;
                    break;
                case 'right':
                    col++;
                    break;
                }

                if (!lines[row] || lines[row][col] === ' ') {
                break;
                }
            }

            this.lettersEncountered = lettersEncountered;
        },
        followPath2() {
            const lines = this.routingDiagram2.split('\n');
            let direction = 'down';
            let row = 0;
            let col = lines[0].indexOf('|');
            let numStepsTaken = 0;

            while (true) {
                const currentChar = lines[row][col];

                if (currentChar === '+') {
                if (direction === 'up' || direction === 'down') {
                    direction = lines[row][col - 1] === ' ' ? 'right' : 'left';
                } else {
                    direction = lines[row - 1] && lines[row - 1][col] === ' ' ? 'down' : 'up';
                }
                }

                switch (direction) {
                case 'up':
                    row--;
                    break;
                case 'down':
                    row++;
                    break;
                case 'left':
                    col--;
                    break;
                case 'right':
                    col++;
                    break;
                }

                numStepsTaken++;

                if (!lines[row] || lines[row][col] === ' ') {
                break;
                }
            }

            this.numStepsTaken = numStepsTaken;
        },
    }
  }
</script>