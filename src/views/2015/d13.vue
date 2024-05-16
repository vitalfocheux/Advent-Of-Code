<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';

  const messages = ["Un essai pour la partie 1 avec Github Copilot",
                    "Cinq essais pour la partie 2 avec Github Copilot"]
</script>

<template>
    <Navbar />

    <HeaderAI :msg= "messages"/>

    <main>
        <h1>Day 13 - Knights of the Dinner Table</h1>
        <h2>Part one</h2>
        <p>
            In years past, the holiday feast with your family hasn't gone so well. Not everyone gets along! This year, you resolve, will be different. You're going to find the optimal seating arrangement and avoid all those awkward conversations.

            You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they were to find themselves sitting next to each other person. You have a circular table that will be just big enough to fit everyone comfortably, and so each person will have exactly two neighbors.

            For example, suppose you have only four attendees planned, and you calculate their potential happiness as follows:

            Alice would gain 54 happiness units by sitting next to Bob.
            Alice would lose 79 happiness units by sitting next to Carol.
            Alice would lose 2 happiness units by sitting next to David.
            Bob would gain 83 happiness units by sitting next to Alice.
            Bob would lose 7 happiness units by sitting next to Carol.
            Bob would lose 63 happiness units by sitting next to David.
            Carol would lose 62 happiness units by sitting next to Alice.
            Carol would gain 60 happiness units by sitting next to Bob.
            Carol would gain 55 happiness units by sitting next to David.
            David would gain 46 happiness units by sitting next to Alice.
            David would lose 7 happiness units by sitting next to Bob.
            David would gain 41 happiness units by sitting next to Carol.
            Then, if you seat Alice next to David, Alice would lose 2 happiness units (because David talks so much), but David would gain 46 happiness units (because Alice is such a good listener), for a total change of 44.

            If you continue around the table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). The arrangement looks like this:

                +41 +46
            +55   David    -2
            Carol       Alice
            +60    Bob    +54
                -7  +83
            After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most optimal, with a total change in happiness of 330.

            What is the total change in happiness for the optimal seating arrangement of the actual guest list?
        </p>
        <textarea v-model="input" placeholder="Enter input here"></textarea>
        <button @click="calculateOptimalHappiness">Calculate</button>
        <p>Optimal happiness: <span v-if="optimalHappiness !== 0">{{ optimalHappiness }}</span></p>
        <h2>Part two</h2>
        <p>
            In all the commotion, you realize that you forgot to seat yourself. At this point, you're pretty apathetic toward the whole thing, and your happiness wouldn't really go up or down regardless of who you sit next to. You assume everyone else would be just as ambivalent about sitting next to you, too.

            So, add yourself to the list, and give all happiness relationships that involve you a score of 0.

            What is the total change in happiness for the optimal seating arrangement that actually includes yourself?
        </p>
        <textarea v-model="input" placeholder="Enter input here"></textarea>
        <button @click="calculateOptimalHappiness2">Calculate</button>
        <p>Optimal happiness: <span v-if="optimalHappiness2 !== 0">{{ optimalHappiness2 }}</span></p>
    </main>

</template>

<script>
    import { useRouter } from 'vue-router';

    export default {

        data() {
            return {
                input: '',
                optimalHappiness: 0,
                optimalHappiness2: 0
            };
        },


        setup() {
            const router = useRouter();
            return { router };
        },

        methods: {
            calculateOptimalHappiness() {
                const lines = this.input.split('\n');
                const happinessMap = {};
                const people = new Set();

                lines.forEach(line => {
                    const [person, , action, units, , , , , , , neighbor] = line.split(' ');
                    const happinessUnits = action === 'gain' ? parseInt(units) : -parseInt(units);
                    if (!happinessMap[person]) happinessMap[person] = {};
                    happinessMap[person][neighbor.slice(0, -1)] = happinessUnits;
                    people.add(person);
                });

                const peopleArr = Array.from(people);
                const permutations = this.permute(peopleArr);
                let maxHappiness = -Infinity;

                permutations.forEach(permutation => {
                    let totalHappiness = 0;
                    for (let i = 0; i < permutation.length; i++) {
                        const leftNeighbor = permutation[(i - 1 + permutation.length) % permutation.length];
                        const rightNeighbor = permutation[(i + 1) % permutation.length];
                        totalHappiness += happinessMap[permutation[i]][leftNeighbor];
                        totalHappiness += happinessMap[permutation[i]][rightNeighbor];
                    }
                    maxHappiness = Math.max(maxHappiness, totalHappiness);
                });

                this.optimalHappiness = maxHappiness;
            },
            permute(arr) {
                if (arr.length <= 1) return [arr];
                const permutations = [];
                arr.forEach((el, i) =>
                    this.permute(arr.slice(0, i).concat(arr.slice(i + 1))).forEach(permutation => {
                    permutations.push([el].concat(permutation));
                    })
                );
                return permutations;
            },
            calculateOptimalHappiness2() {
                const lines = this.input.split('\n');
                const happinessMap = {};
                const people = new Set();

                lines.forEach(line => {
                    const [person, , action, units, , , , , , , neighbor] = line.split(' ');
                    const happinessUnits = action === 'gain' ? parseInt(units) : -parseInt(units);
                    if (!happinessMap[person]) happinessMap[person] = {};
                    happinessMap[person][neighbor.slice(0, -1)] = happinessUnits;
                    people.add(person);
                });

                const peopleArr = Array.from(people);
                const n = peopleArr.length;
                const dp = Array(n).fill().map(() => Array(1 << n).fill(-Infinity));
                const happiness = Array(n).fill().map(() => Array(n).fill(0));

                for (let i = 0; i < n; i++) {
                    for (let j = 0; j < n; j++) {
                        if (i !== j) {
                            happiness[i][j] = happinessMap[peopleArr[i]][peopleArr[j]] + happinessMap[peopleArr[j]][peopleArr[i]];
                        }
                    }
                }

                for (let i = 0; i < n; i++) {
                    dp[i][1 << i] = 0;
                }

                for (let mask = 0; mask < (1 << n); mask++) {
                    for (let i = 0; i < n; i++) {
                        if ((mask & (1 << i)) !== 0) {
                            for (let j = 0; j < n; j++) {
                                if (i !== j && (mask & (1 << j)) !== 0) {
                                    dp[i][mask] = Math.max(dp[i][mask], dp[j][mask ^ (1 << i)] + happiness[j][i]);
                                }
                            }
                        }
                    }
                }

                let optimalHappiness2 = -Infinity;
                for (let i = 0; i < n; i++) {
                    optimalHappiness2 = Math.max(optimalHappiness2, dp[i][(1 << n) - 1]);
                }

                this.optimalHappiness2 = optimalHappiness2;
            }
        }
    }
</script>