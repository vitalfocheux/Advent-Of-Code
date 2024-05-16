<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';

  const messages = ["Un essai pour résoudre le jour 9 de l'Advent of Code 2015 avec Github Copilot"]
</script>

<template>
    <Navbar />

    <HeaderAI :msg= "messages"/>

    <main>
        <h1>Day 9 - All in a Single Night</h1>
        <h2>Part one</h2>
        <p>
            Every year, Santa manages to deliver all of his presents in a single night.

            This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

            For example, given the following distances:

            London to Dublin = 464
            London to Belfast = 518
            Dublin to Belfast = 141
            The possible routes are therefore:

            Dublin -> London -> Belfast = 982
            London -> Dublin -> Belfast = 605
            London -> Belfast -> Dublin = 659
            Dublin -> Belfast -> London = 659
            Belfast -> Dublin -> London = 605
            Belfast -> London -> Dublin = 982
            The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

            What is the distance of the shortest route?
        </p>
        <textarea v-model="distances" placeholder="Enter distances here, one per line"></textarea>
        <button @click="calculateShortestDistance">Calculate Shortest Distance</button>
        <p>Shortest Distance: <span v-if="shortestDistance !== null">{{ shortestDistance }}</span></p>
        <h2>Part two</h2>
        <p>
            The next year, just to show off, Santa decides to take the route with the longest distance instead.

            He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

            For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

            What is the distance of the longest route?
        </p>
        <textarea v-model="distances" placeholder="Enter distances here, one per line"></textarea>
        <button @click="calculateLongestDistance">Calculate Longest Distance</button>
        <p>Longest Distance: <span v-if="longestDistance !== null">{{ longestDistance }}</span></p>
    </main>

</template>

<script>
    import { useRouter } from 'vue-router';
    import { permutations } from 'itertools'

    export default {

        data() {
            return {
                distances: '',
                shortestDistance: null,
                longestDistance: null
            };
        },


        setup() {
            const router = useRouter();
            return { router };
        },

        methods: {
            calculateShortestDistance() {
                const distancesArray = this.distances.split('\n');
                const cities = new Set();
                const distances = {};

                for (let distance of distancesArray) {
                    const [citiesStr, distanceStr] = distance.split(' = ');
                    const [city1, city2] = citiesStr.split(' to ');
                    cities.add(city1);
                    cities.add(city2);
                    if (!distances[city1]) distances[city1] = {};
                    if (!distances[city2]) distances[city2] = {};
                    distances[city1][city2] = Number(distanceStr);
                    distances[city2][city1] = Number(distanceStr);
                }

                let shortestDistance = Infinity;

                for (let permutation of permutations(Array.from(cities))) {
                    let distance = 0;
                    for (let i = 0; i < permutation.length - 1; i++) {
                    distance += distances[permutation[i]][permutation[i + 1]];
                    }
                    if (distance < shortestDistance) shortestDistance = distance;
                }

                this.shortestDistance = shortestDistance;
            },
            calculateLongestDistance() {
                const distancesArray = this.distances.split('\n');
                const cities = new Set();
                const distances = {};

                for (let distance of distancesArray) {
                    const [citiesStr, distanceStr] = distance.split(' = ');
                    const [city1, city2] = citiesStr.split(' to ');
                    cities.add(city1);
                    cities.add(city2);
                    if (!distances[city1]) distances[city1] = {};
                    if (!distances[city2]) distances[city2] = {};
                    distances[city1][city2] = Number(distanceStr);
                    distances[city2][city1] = Number(distanceStr);
                }

                let longestDistance = 0;

                for (let permutation of permutations(Array.from(cities))) {
                    let distance = 0;
                    for (let i = 0; i < permutation.length - 1; i++) {
                    distance += distances[permutation[i]][permutation[i + 1]];
                    }
                    if (distance > longestDistance) longestDistance = distance;
                }

                this.longestDistance = longestDistance;
            }
        }
    }
</script>