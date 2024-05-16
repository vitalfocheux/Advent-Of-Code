<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';

  const messages = ["Un essai pour résoudre le jour 18 de l'Advent of Code 2015 avec Github Copilot"]
</script>

<template>
    <Navbar />

    <HeaderAI :msg= "messages"/>

    <main>
        <h1>Day 18 - Like a GIF For Your Yard</h1>
        <h2>Part one</h2>
        <p>
            After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

            Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few lights, he says, you'll have to resort to animation.

            Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means "off".

            Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".

            For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:

            1B5...
            234...
            ......
            ..123.
            ..8A4.
            ..765.
            The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

            A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
            A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
            All of the lights update simultaneously; they all consider the same current state before moving to the next.

            Here's a few steps from an example configuration of another 6x6 grid:

            Initial state:
            .#.#.#
            ...##.
            #....#
            ..#...
            #.#..#
            ####..

            After 1 step:
            ..##..
            ..##.#
            ...##.
            ......
            #.....
            #.##..

            After 2 steps:
            ..###.
            ......
            ..###.
            ......
            .#....
            .#....

            After 3 steps:
            ...#..
            ......
            ...#..
            ..##..
            ......
            ......

            After 4 steps:
            ......
            ......
            ..##..
            ..##..
            ......
            ......
            After 4 steps, this example has four lights on.

            In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?
        </p>
        <textarea v-model="initialLightsState" placeholder="Enter initial lights state here"></textarea>
        <button @click="calculateLightsAfterSteps">Calculate</button>
        <p>Number of lights on after 100 steps: <span v-if="numberOfLightsOn !== 0">{{ numberOfLightsOn }}</span></p>
        <h2>Part two</h2>
        <p>
            You flip the instructions over; Santa goes on to point out that this is all just an implementation of Conway's Game of Life. At least, it was, until you notice that something's wrong with the grid of lights you bought: four lights, one in each corner, are stuck on and can't be turned off. The example above will actually run like this:

            Initial state:
            ##.#.#
            ...##.
            #....#
            ..#...
            #.#..#
            ####.#

            After 1 step:
            #.##.#
            ####.#
            ...##.
            ......
            #...#.
            #.####

            After 2 steps:
            #..#.#
            #....#
            .#.##.
            ...##.
            .#..##
            ##.###

            After 3 steps:
            #...##
            ####.#
            ..##.#
            ......
            ##....
            ####.#

            After 4 steps:
            #.####
            #....#
            ...#..
            .##...
            #.....
            #.#..#

            After 5 steps:
            ##.###
            .##..#
            .##...
            .##...
            #.#...
            ##...#
            After 5 steps, this example now has 17 lights on.

            In your grid of 100x100 lights, given your initial configuration, but with the four corners always in the on state, how many lights are on after 100 steps?
        </p>
        <textarea v-model="initialLightsStatePart2" placeholder="Enter initial lights state here"></textarea>
        <button @click="calculateLightsAfterStepsPart2">Calculate</button>
        <p>Number of lights on after 100 steps with corners always on: <span v-if="numberOfLightsOnPart2 !== 0">{{ numberOfLightsOnPart2 }}</span></p>
    </main>

</template>

<script>
    import { useRouter } from 'vue-router';

    export default {

        data() {
            return {
                initialLightsState: '',
                numberOfLightsOn: 0,
                initialLightsStatePart2: '',
                numberOfLightsOnPart2: 0
            };
        },


        setup() {
            const router = useRouter();
            return { router };
        },

        methods: {
            calculateLightsAfterSteps() {
                let lights = this.initialLightsState.split('\n').map(row => row.split(''));
                const steps = 100;

                for (let i = 0; i < steps; i++) {
                    lights = this.nextState(lights);
                }

                this.numberOfLightsOn = lights.flat().filter(light => light === '#').length;
            },

            nextState(lights) {
                return lights.map((row, y) => row.map((light, x) => {
                    const neighbors = [
                        [y - 1, x - 1], [y - 1, x], [y - 1, x + 1],
                        [y, x - 1], [y, x + 1],
                        [y + 1, x - 1], [y + 1, x], [y + 1, x + 1]
                    ];
                    const onNeighbors = neighbors.filter(([ny, nx]) => lights[ny] && lights[ny][nx] === '#').length;
                    return light === '#' ? (onNeighbors === 2 || onNeighbors === 3 ? '#' : '.') : (onNeighbors === 3 ? '#' : '.');
                }));
            },
            calculateLightsAfterStepsPart2() {
                let lights = this.initialLightsStatePart2.split('\n').map(row => row.split(''));
                const steps = 100;

                for (let i = 0; i < steps; i++) {
                    lights = this.nextStateWithCorners(lights);
                }

                this.numberOfLightsOnPart2 = lights.flat().filter(light => light === '#').length;
            },

            nextStateWithCorners(lights) {
                const size = lights.length;
                return lights.map((row, y) => row.map((light, x) => {
                    if ((y === 0 || y === size - 1) && (x === 0 || x === size - 1)) return '#';
                    const neighbors = [
                        [y - 1, x - 1], [y - 1, x], [y - 1, x + 1],
                        [y, x - 1], [y, x + 1],
                        [y + 1, x - 1], [y + 1, x], [y + 1, x + 1]
                    ];
                    const onNeighbors = neighbors.filter(([ny, nx]) => lights[ny] && lights[ny][nx] === '#').length;
                    return light === '#' ? (onNeighbors === 2 || onNeighbors === 3 ? '#' : '.') : (onNeighbors === 3 ? '#' : '.');
                }));
            }
        }
    }
</script>