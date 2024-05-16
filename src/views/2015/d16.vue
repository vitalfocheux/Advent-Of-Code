<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';

  const messages = ["Un essai pour résoudre le jour 16 de l'Advent of Code 2015 avec Github Copilot"]
</script>

<template>
    <Navbar />

    <HeaderAI :msg= "messages"/>

    <main>
        <h1>Day 16 - Aunt Sue</h1>
        <h2>Part one</h2>
        <p>
            Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card. However, there's a small problem: she signed it "From, Aunt Sue".

            You have 500 Aunts named "Sue".

            So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the gift. You open the present and, as luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine! Just what you wanted. Or needed, as the case may be.

            The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample, as well as how many distinct kinds of those compounds there are. According to the instructions, these are what the MFCSAM can detect:

            children, by human DNA age analysis.
            cats. It doesn't differentiate individual breeds.
            Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
            goldfish. No other kinds of fish.
            trees, all in one group.
            cars, presumably by exhaust or gasoline or something.
            perfumes, which is handy, since many of your Aunts Sue wear a few kinds.
            In fact, many of your Aunts Sue have many of these. You put the wrapping from the gift into the MFCSAM. It beeps inquisitively at you a few times and then prints out a message on ticker tape:

            children: 3
            cats: 7
            samoyeds: 2
            pomeranians: 3
            akitas: 0
            vizslas: 0
            goldfish: 5
            trees: 3
            cars: 2
            perfumes: 1
            You make a list of the things you can remember about each Aunt Sue. Things missing from your list aren't zero - you simply don't remember the value.

            What is the number of the Sue that got you the gift?
        </p>
        <textarea v-model="sueDescriptions" placeholder="Enter Sue descriptions here"></textarea>
        <button @click="findMatchingSue">Find Sue</button>
        <p>Matching Sue: <span v-if="matchingSue !== 0">{{ matchingSue }}</span></p>
        <h2>Part two</h2>
        <p>
            As you're about to send the thank you note, something in the MFCSAM's instructions catches your eye. Apparently, it has an outdated retroencabulator, and so the output from the machine isn't exact values - some of them indicate ranges.

            In particular, the cats and trees readings indicates that there are greater than that many (due to the unpredictable nuclear decay of cat dander and tree pollen), while the pomeranians and goldfish readings indicate that there are fewer than that many (due to the modial interaction of magnetoreluctance).

            What is the number of the real Aunt Sue?
        </p>
        <textarea v-model="sueDescriptionsPart2" placeholder="Enter Sue descriptions here"></textarea>
        <button @click="findMatchingSuePart2">Find Sue</button>
        <p>Matching Sue: <span v-if="matchingSuePart2">{{ matchingSuePart2 }}</span></p>
    </main>

</template>

<script>
    import { useRouter } from 'vue-router';

    export default {

        data() {
            return {
                sueDescriptions: '',
                matchingSue: 0,
                sueDescriptionsPart2: '',
                matchingSuePart2: 0
            };
        },


        setup() {
            const router = useRouter();
            return { router };
        },

        methods: {
            findMatchingSue() {
                const descriptions = this.sueDescriptions.split('\n');
                const sues = descriptions.map(description => {
                    const match = description.match(/Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)/);
                    if (match) {
                        const [, number, thing1, amount1, thing2, amount2, thing3, amount3] = match;
                        return { 
                            number: Number(number), 
                            things: {
                                [thing1]: Number(amount1),
                                [thing2]: Number(amount2),
                                [thing3]: Number(amount3)
                            }
                        };
                    }
                });

                const mySue = {
                    children: 3,
                    cats: 7,
                    samoyeds: 2,
                    pomeranians: 3,
                    akitas: 0,
                    vizslas: 0,
                    goldfish: 5,
                    trees: 3,
                    cars: 2,
                    perfumes: 1
                };

                for (let sue of sues) {
                    let match = true;
                    for (let thing in sue.things) {
                        if (sue.things[thing] !== mySue[thing]) {
                            match = false;
                            break;
                        }
                    }
                    if (match) {
                        this.matchingSue = sue.number;
                        break;
                    }
                }
            },
            findMatchingSuePart2() {
                const descriptions = this.sueDescriptionsPart2.split('\n');
                const sues = descriptions.map(description => {
                    const match = description.match(/Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)/);
                    if (match) {
                        const [, number, thing1, amount1, thing2, amount2, thing3, amount3] = match;
                        return { 
                            number: Number(number), 
                            things: {
                                [thing1]: Number(amount1),
                                [thing2]: Number(amount2),
                                [thing3]: Number(amount3)
                            }
                        };
                    }
                });

                const mySuePart2 = {
                    children: 3,
                    cats: 7,
                    samoyeds: 2,
                    pomeranians: 3,
                    akitas: 0,
                    vizslas: 0,
                    goldfish: 5,
                    trees: 3,
                    cars: 2,
                    perfumes: 1
                };

                for (let sue of sues) {
                    let match = true;
                    for (let thing in sue.things) {
                        if (thing === 'cats' || thing === 'trees') {
                            if (sue.things[thing] <= mySuePart2[thing]) {
                                match = false;
                                break;
                            }
                        } else if (thing === 'pomeranians' || thing === 'goldfish') {
                            if (sue.things[thing] >= mySuePart2[thing]) {
                                match = false;
                                break;
                            }
                        } else if (sue.things[thing] !== mySuePart2[thing]) {
                            match = false;
                            break;
                        }
                    }
                    if (match) {
                        this.matchingSuePart2 = sue.number;
                        break;
                    }
                }
            }
        }
    }
</script>