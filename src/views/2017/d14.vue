<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Quatre essais pour la partie 1 avec Github Copilot",
                    "Un essai pour la partie 2 avec Github Copilot"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 14 - Disk Defragmentation</h1>
    <h2>Part one</h2>
    <p>
        Suddenly, a scheduled job activates the system's disk defragmenter. Were the situation different, you might sit and watch it for a while, but today, you just don't have that kind of time. It's soaking up valuable system resources that are needed elsewhere, and so the only option is to help it finish its task as soon as possible.

        The disk in question consists of a 128x128 grid; each square of the grid is either free or used. On this disk, the state of the grid is tracked by the bits in a sequence of knot hashes.

        A total of 128 knot hashes are calculated, each corresponding to a single row in the grid; each hash contains 128 bits which correspond to individual grid squares. Each bit of a hash indicates whether that square is free (0) or used (1).

        The hash inputs are a key string (your puzzle input), a dash, and a number from 0 to 127 corresponding to the row. For example, if your key string were flqrgnkx, then the first row would be given by the bits of the knot hash of flqrgnkx-0, the second row from the bits of the knot hash of flqrgnkx-1, and so on until the last row, flqrgnkx-127.

        The output of a knot hash is traditionally represented by 32 hexadecimal digits; each of these digits correspond to 4 bits, for a total of 4 * 32 = 128 bits. To convert to bits, turn each hexadecimal digit to its equivalent binary value, high-bit first: 0 becomes 0000, 1 becomes 0001, e becomes 1110, f becomes 1111, and so on; a hash that begins with a0c2017... in hexadecimal would begin with 10100000110000100000000101110000... in binary.

        Continuing this process, the first 8 rows and columns for key flqrgnkx appear as follows, using # to denote used squares, and . to denote free ones:

        ##.#.#..-->
        .#.#.#.#   
        ....#.#.   
        #.#.##.#   
        .##.#...   
        ##..#..#   
        .#...#..   
        ##.#.##.-->
        |      |   
        V      V   
        In this example, 8108 squares are used across the entire 128x128 grid.

        Given your actual key string, how many squares are used?
    </p>
    <input v-model="keyString" placeholder="Enter key string here">
    <button @click="calculateUsedSquares">Calculate Used Squares</button>
    <p>Used Squares: {{ usedSquares }}</p>
    <h2>Part two</h2>
    <p>
        Now, all the defragmenter needs to know is the number of regions. A region is a group of used squares that are all adjacent, not including diagonals. Every used square is in exactly one region: lone used squares form their own isolated regions, while several adjacent squares all count as a single region.

        In the example above, the following nine regions are visible, each marked with a distinct digit:

        11.2.3..-->
        .1.2.3.4   
        ....5.6.   
        7.8.55.9   
        .88.5...   
        88..5..8   
        .8...8..   
        88.8.88.-->
        |      |   
        V      V   
        Of particular interest is the region marked 8; while it does not appear contiguous in this small view, all of the squares marked 8 are connected when considering the whole 128x128 grid. In total, in this example, 1242 regions are present.

        How many regions are present given your key string?
    </p>
    <input v-model="keyString2" placeholder="Enter key string here">
    <button @click="calculateRegions">Calculate Regions</button>
    <p>Regions: {{ regions }}</p>
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
        keyString: '',
        usedSquares: null,
        keyString2: '',
        regions: null
      }
    },
    methods: {
        knotHash(input) {
            const lengths = [...input].map(char => char.charCodeAt(0)).concat([17, 31, 73, 47, 23]);
            let list = [...Array(256).keys()];
            let position = 0;
            let skipSize = 0;

            for (let round = 0; round < 64; round++) {
            for (let length of lengths) {
                let sublist = (list.concat(list)).slice(position, position + length).reverse();
                for (let i = 0; i < length; i++) {
                list[(position + i) % list.length] = sublist[i];
                }
                position = (position + length + skipSize) % list.length;
                skipSize++;
            }
            }

            let denseHash = [];
            for (let i = 0; i < 16; i++) {
            denseHash[i] = list.slice(i * 16, i * 16 + 16).reduce((a, b) => a ^ b);
            }

            return denseHash.map(num => num.toString(16).padStart(2, '0')).join('');
        },
        calculateUsedSquares() {
            let usedSquares = 0;

            for (let i = 0; i < 128; i++) {
                let input = `${this.keyString}-${i}`;
                const lengths = [...input].map(char => char.charCodeAt(0)).concat([17, 31, 73, 47, 23]);
                let list = [...Array(256).keys()];
                let position = 0;
                let skipSize = 0;

                for (let round = 0; round < 64; round++) {
                for (let length of lengths) {
                    let sublist = (list.concat(list)).slice(position, position + length).reverse();
                    for (let i = 0; i < length; i++) {
                    list[(position + i) % list.length] = sublist[i];
                    }
                    position = (position + length + skipSize) % list.length;
                    skipSize++;
                }
                }

                let denseHash = [];
                for (let i = 0; i < 16; i++) {
                denseHash[i] = list.slice(i * 16, i * 16 + 16).reduce((a, b) => a ^ b);
                }

                const hash = denseHash.map(num => num.toString(16).padStart(2, '0')).join('');

                usedSquares += [...hash].reduce((count, hex) => count + parseInt(hex, 16).toString(2).padStart(4, '0').split('0').join('').length, 0);
            }

            this.usedSquares = usedSquares;
        },
        calculateRegions() {
            let grid = Array(128).fill().map(() => Array(128).fill(0));

            for (let i = 0; i < 128; i++) {
                let input = `${this.keyString2}-${i}`; 
                const lengths = [...input].map(char => char.charCodeAt(0)).concat([17, 31, 73, 47, 23]);
                let list = [...Array(256).keys()];
                let position = 0;
                let skipSize = 0;

                for (let round = 0; round < 64; round++) {
                for (let length of lengths) {
                    let sublist = (list.concat(list)).slice(position, position + length).reverse();
                    for (let i = 0; i < length; i++) {
                    list[(position + i) % list.length] = sublist[i];
                    }
                    position = (position + length + skipSize) % list.length;
                    skipSize++;
                }
                }

                let denseHash = [];
                for (let i = 0; i < 16; i++) {
                denseHash[i] = list.slice(i * 16, i * 16 + 16).reduce((a, b) => a ^ b);
                }

                const hash = denseHash.map(num => num.toString(16).padStart(2, '0')).join('');
                
                let binary = [...hash].map(hex => parseInt(hex, 16).toString(2).padStart(4, '0')).join('');
                grid[i] = [...binary].map(bit => bit === '1' ? 1 : 0);
            }

            let regions = 0;
            for (let i = 0; i < 128; i++) {
                for (let j = 0; j < 128; j++) {
                if (grid[i][j] === 1) {
                    this.dfs(grid, i, j);
                    regions++;
                }
                }
            }

            this.regions = regions;
        },

        dfs(grid, i, j) {
            if (i < 0 || j < 0 || i >= 128 || j >= 128 || grid[i][j] === 0) return;
            grid[i][j] = 0;
            this.dfs(grid, i - 1, j);
            this.dfs(grid, i + 1, j);
            this.dfs(grid, i, j - 1);
            this.dfs(grid, i, j + 1);
        },
    }
  }
</script>