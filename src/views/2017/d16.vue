<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Un essai pour résoudre le jour 16 de l'Advent of Code 2017 avec Github Copilot"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 16 - Permutation Promenade</h1>
    <h2>Part one</h2>
    <p>
        You come upon a very unusual sight; a group of programs here appear to be dancing.

        There are sixteen programs in total, named a through p. They start by standing in a line: a stands in position 0, b stands in position 1, and so on until p, which stands in position 15.

        The programs' dance consists of a sequence of dance moves:

        Spin, written sX, makes X programs move from the end to the front, but maintain their order otherwise. (For example, s3 on abcde produces cdeab).
        Exchange, written xA/B, makes the programs at positions A and B swap places.
        Partner, written pA/B, makes the programs named A and B swap places.
        For example, with only five programs standing in a line (abcde), they could do the following dance:

        s1, a spin of size 1: eabcd.
        x3/4, swapping the last two programs: eabdc.
        pe/b, swapping programs e and b: baedc.
        After finishing their dance, the programs end up in order baedc.

        You watch the dance for a while and record their dance moves (your puzzle input). In what order are the programs standing after their dance?
    </p>
    <input v-model="danceMoves" placeholder="Enter dance moves here">
    <button @click="performDance">Perform Dance</button>
    <p>Order of programs: {{ order }}</p>
    <h2>Part two</h2>
    <p>
        Now that you're starting to get a feel for the dance moves, you turn your attention to the dance as a whole.

        Keeping the positions they ended up in from their previous dance, the programs perform it again and again: including the first dance, a total of one billion (1000000000) times.

        In the example above, their second dance would begin with the order baedc, and use the same dance moves:

        s1, a spin of size 1: cbaed.
        x3/4, swapping the last two programs: cbade.
        pe/b, swapping programs e and b: ceadb.
        In what order are the programs standing after their billion dances?
    </p>
    <input v-model="danceMoves2" placeholder="Enter dance moves here">
    <button @click="performDance2">Perform Dance</button>
    <p>Order of programs: {{ order2 }}</p>
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
        danceMoves: '',
        order: null,
        danceMoves2: '',
        order2: null,
      }
    },
    methods: {
        performDance() {
            let programs = 'abcdefghijklmnop'.split('');
            const moves = this.danceMoves.split(',');

            moves.forEach(move => {
                const type = move[0];
                const params = move.substring(1).split('/');

                switch (type) {
                case 's':
                    const size = parseInt(params[0]);
                    programs = [...programs.slice(-size), ...programs.slice(0, -size)];
                    break;
                case 'x':
                    const posA = parseInt(params[0]);
                    const posB = parseInt(params[1]);
                    [programs[posA], programs[posB]] = [programs[posB], programs[posA]];
                    break;
                case 'p':
                    const indexA = programs.indexOf(params[0]);
                    const indexB = programs.indexOf(params[1]);
                    [programs[indexA], programs[indexB]] = [programs[indexB], programs[indexA]];
                    break;
                }
            });

            this.order = programs.join('');
        },
        performDance2() {
            let programs = 'abcdefghijklmnop'.split('');
            const moves = this.danceMoves2.split(',');
            const seen = {};
            let cycleLength = 0;

            for (let i = 0; i < 1000000000; i++) {
                const key = programs.join('');

                if (seen[key]) {
                cycleLength = i;
                break;
                }

                seen[key] = true;

                moves.forEach(move => {
                const type = move[0];
                const params = move.substring(1).split('/');

                switch (type) {
                    case 's':
                    const size = parseInt(params[0]);
                    programs = [...programs.slice(-size), ...programs.slice(0, -size)];
                    break;
                    case 'x':
                    const posA = parseInt(params[0]);
                    const posB = parseInt(params[1]);
                    [programs[posA], programs[posB]] = [programs[posB], programs[posA]];
                    break;
                    case 'p':
                    const indexA = programs.indexOf(params[0]);
                    const indexB = programs.indexOf(params[1]);
                    [programs[indexA], programs[indexB]] = [programs[indexB], programs[indexA]];
                    break;
                }
                });
            }

            const finalOrder = Object.keys(seen)[1000000000 % cycleLength];
            this.order2 = finalOrder;
        },
    }
  }
</script>