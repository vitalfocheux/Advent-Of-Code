<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
</script>

<template>
    <Navbar />

    <HeaderAI msg="Un essai pour résoudre le jour 2 de l'Advent of Code 2015 avec Github Copilot" />

    <main>
        <h1>Day 2 - I Was Told There Wold Be No Match</h1>
        <h2>Part one</h2>
        <p>
            The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

            Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

            For example:

            A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
            A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
            All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
        </p>
        <textarea v-model="giftDimensions" placeholder="Enter gift dimensions here"></textarea>
        <button @click="solvePuzzle">Solve Puzzle</button>
        <p>Total square feet of wrapping paper needed: <span v-if="totalPaper !== null">{{ totalPaper }}</span></p>
        <h2>Part two</h2>
        <p>
            The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

            The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

            For example:

            A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
            A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.
            How many total feet of ribbon should they order?
        </p>
        <textarea v-model="giftDimensions" placeholder="Enter gift dimensions here"></textarea>
        <button @click="solvePuzzlePartTwo">Solve Puzzle Part Two</button>
        <p>Total length of ribbon needed: <span v-if="totalRibbon !== null">{{ totalRibbon }}</span></p>
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
        giftDimensions: '',
        totalPaper: null,
        totalRibbon: null
      }
    },
    methods: {
        solvePuzzle() {
            const gifts = this.giftDimensions.split('\n');
            this.totalPaper = 0;
            for (let i = 0; i < gifts.length; i++) {
                const dimensions = gifts[i].split('x').map(Number);
                const [l, w, h] = dimensions;
                const areas = [l*w, w*h, h*l];
                const slack = Math.min(...areas);
                const paper = 2 * areas.reduce((a, b) => a + b, 0) + slack;
                this.totalPaper += paper;
            }
        },
        solvePuzzlePartTwo() {
            const gifts = this.giftDimensions.split('\n');
            this.totalRibbon = 0;
            for (let i = 0; i < gifts.length; i++) {
                const dimensions = gifts[i].split('x').map(Number);
                dimensions.sort((a, b) => a - b);
                const [l, w, h] = dimensions;
                const ribbon = 2 * (l + w) + l * w * h;
                this.totalRibbon += ribbon;
            }
        }
    }
  }
</script>