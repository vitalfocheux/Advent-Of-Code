<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';

  const messages = ["Un essai pour résoudre le jour 17 de l'Advent of Code 2015 avec Github Copilot"]
</script>

<template>
    <Navbar />

    <HeaderAI :msg= "messages"/>

    <main>
        <h1>Day 17 - No Such Thing as Too Much</h1>
        <h2>Part one</h2>
        <p>
            The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

            For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it:

            15 and 10
            20 and 5 (the first 5)
            20 and 5 (the second 5)
            15, 5, and 5
            Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?
        </p>
        <textarea v-model="containerSizes" placeholder="Enter container sizes here"></textarea>
        <button @click="calculateCombinations">Calculate</button>
        <p>Number of combinations: <span v-if="numberOfCombinations !== 0">{{ numberOfCombinations }}</span></p>
        <h2>Part two</h2>
        <p>
            While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving department is requesting as many containers as you can spare.

            Find the minimum number of containers that can exactly fit all 150 liters of eggnog. How many different ways can you fill that number of containers and still hold exactly 150 litres?

            In the example above, the minimum number of containers was two. There were three ways to use that many containers, and so the answer there would be 3.
        </p>
        <textarea v-model="containerSizesPart2" placeholder="Enter container sizes here"></textarea>
        <button @click="calculateMinCombinations">Calculate</button>
        <p>Number of minimum combinations: <span v-if="numberOfMinCombinations !== 0">{{ numberOfMinCombinations }}</span></p>
    </main>

</template>

<script>
    import { useRouter } from 'vue-router';

    export default {

        data() {
            return {
                containerSizes: '',
                numberOfCombinations: 0,
                containerSizesPart2: '',
                numberOfMinCombinations: 0
            };
        },


        setup() {
            const router = useRouter();
            return { router };
        },

        methods: {
            calculateCombinations() {
                const sizes = this.containerSizes.split('\n').map(Number);
                const target = 150;
                this.numberOfCombinations = this.countCombinations(sizes, target);
            },

            countCombinations(sizes, target, i = 0) {
                if (target === 0) return 1;
                if (target < 0 || i === sizes.length) return 0;
                return this.countCombinations(sizes, target - sizes[i], i + 1) + this.countCombinations(sizes, target, i + 1);
            },
            calculateMinCombinations() {
                const sizes = this.containerSizesPart2.split('\n').map(Number);
                const target = 150;
                const combinations = this.findAllCombinations(sizes, target);
                const minSize = Math.min(...combinations.map(c => c.length));
                this.numberOfMinCombinations = combinations.filter(c => c.length === minSize).length;
            },

            findAllCombinations(sizes, target, i = 0, combo = []) {
                if (target === 0) return [combo];
                if (target < 0 || i === sizes.length) return [];
                return [
                    ...this.findAllCombinations(sizes, target - sizes[i], i + 1, [...combo, sizes[i]]),
                    ...this.findAllCombinations(sizes, target, i + 1, combo)
                ];
            }
        }
    }
</script>