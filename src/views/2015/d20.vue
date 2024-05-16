<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';

  const messages = ["Un essai pour résoudre le jour 20 de l'Advent of Code 2015 avec Github Copilot"]
</script>

<template>
    <Navbar />

    <HeaderAI :msg= "messages"/>

    <main>
        <h1>Day 20 - Infinite Elves and Infinite Houses</h1>
        <h2>Part one</h2>
        <p>
            To keep the Elves busy, Santa has them deliver some presents by hand, door-to-door. He sends them down a street with infinite houses numbered sequentially: 1, 2, 3, 4, 5, and so on.

            Each Elf is assigned a number, too, and delivers presents to houses based on that number:

            The first Elf (number 1) delivers presents to every house: 1, 2, 3, 4, 5, ....
            The second Elf (number 2) delivers presents to every second house: 2, 4, 6, 8, 10, ....
            Elf number 3 delivers presents to every third house: 3, 6, 9, 12, 15, ....
            There are infinitely many Elves, numbered starting with 1. Each Elf delivers presents equal to ten times his or her number at each house.

            So, the first nine houses on the street end up like this:

            House 1 got 10 presents.
            House 2 got 30 presents.
            House 3 got 40 presents.
            House 4 got 70 presents.
            House 5 got 60 presents.
            House 6 got 120 presents.
            House 7 got 80 presents.
            House 8 got 150 presents.
            House 9 got 130 presents.
            The first house gets 10 presents: it is visited only by Elf 1, which delivers 1 * 10 = 10 presents. The fourth house gets 70 presents, because it is visited by Elves 1, 2, and 4, for a total of 10 + 20 + 40 = 70 presents.

            What is the lowest house number of the house to get at least as many presents as the number in your puzzle input?
        </p>
        <input v-model.number="presents" placeholder="Enter number of presents">
        <button @click="calculateHouseNumber">Calculate</button>
        <p>Lowest house number: <span v-if="houseNumber !== 0">{{ houseNumber }}</span></p>
        <h2>Part two</h2>
        <p>
            The Elves decide they don't want to visit an infinite number of houses. Instead, each Elf will stop after delivering presents to 50 houses. To make up for it, they decide to deliver presents equal to eleven times their number at each house.

            With these changes, what is the new lowest house number of the house to get at least as many presents as the number in your puzzle input?
        </p>
        <input v-model.number="presentsPart2" placeholder="Enter number of presents">
        <button @click="calculateHouseNumberPart2">Calculate</button>
        <p>Lowest house number: <span v-if="houseNumberPart2 !== 0">{{ houseNumberPart2 }}</span></p>
    </main>

</template>

<script>
    import { useRouter } from 'vue-router';

    export default {

        data() {
            return {
                presents: 0,
                houseNumber: 0,
                presentsPart2: 0,
                houseNumberPart2: 0,
            };
        },


        setup() {
            const router = useRouter();
            return { router };
        },

        methods: {
            calculateHouseNumber() {
                const houses = new Array(this.presents / 10).fill(0);
                for (let i = 1; i < houses.length; i++) {
                    for (let j = i; j < houses.length; j += i) {
                        houses[j] += i * 10;
                    }
                }
                this.houseNumber = houses.findIndex(house => house >= this.presents);
            },
            calculateHouseNumberPart2() {
                const houses = new Array(this.presentsPart2 / 10).fill(0);
                for (let i = 1; i < houses.length; i++) {
                    let housesDelivered = 0;
                    for (let j = i; j < houses.length && housesDelivered < 50; j += i, housesDelivered++) {
                        houses[j] += i * 11;
                    }
                }
                this.houseNumberPart2 = houses.findIndex(house => house >= this.presentsPart2);
            }
        }
    }
</script>