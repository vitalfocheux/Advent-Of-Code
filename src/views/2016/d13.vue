<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Un essai pour résoudre le jour 13 de l'Advent of Code 2016 avec Github Copilot"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 13 - A Maze of Twisty Little Cubicles</h1>
    <h2>Part one</h2>
    <p>
        You arrive at the first floor of this new building to discover a much less welcoming environment than the shiny atrium of the last one. Instead, you are in a maze of twisty little cubicles, all alike.

        Every location in this area is addressed by a pair of non-negative integers (x,y). Each such coordinate is either a wall or an open space. You can't move diagonally. The cube maze starts at 0,0 and seems to extend infinitely toward positive x and y; negative values are invalid, as they represent a location outside the building. You are in a small waiting area at 1,1.

        While it seems chaotic, a nearby morale-boosting poster explains, the layout is actually quite logical. You can determine whether a given x,y coordinate will be a wall or an open space using a simple system:

        Find x*x + 3*x + 2*x*y + y + y*y.
        Add the office designer's favorite number (your puzzle input).
        Find the binary representation of that sum; count the number of bits that are 1.
        If the number of bits that are 1 is even, it's an open space.
        If the number of bits that are 1 is odd, it's a wall.
        For example, if the office designer's favorite number were 10, drawing walls as # and open spaces as ., the corner of the building containing 0,0 would look like this:

        0123456789
        0 .#.####.##
        1 ..#..#...#
        2 #....##...
        3 ###.#.###.
        4 .##..#..#.
        5 ..##....#.
        6 #...##.###
        Now, suppose you wanted to reach 7,4. The shortest route you could take is marked as O:

        0123456789
        0 .#.####.##
        1 .O#..#...#
        2 #OOO.##...
        3 ###O#.###.
        4 .##OO#OO#.
        5 ..##OOO.#.
        6 #...##.###
        Thus, reaching 7,4 would take a minimum of 11 steps (starting from your current location, 1,1).

        What is the fewest number of steps required for you to reach 31,39?
    </p>
    <input v-model.number="inputPart1" placeholder="Enter favorite number" type="number">
    <button @click="solvePart1">Solve Part 1</button>
    <p>Minimum number of steps: <span v-if="minSteps !== 0">{{ minSteps }}</span></p>
    <h2>Part two</h2>
    <p>
        How many locations (distinct x,y coordinates, including your starting location) can you reach in at most 50 steps?
    </p>
    <input v-model.number="inputPart2" placeholder="Enter favorite number" type="number">
    <button @click="solvePart2">Solve Part 2</button>
    <p>Number of distinct positions: {{ distinctPositions }}</p>
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
        inputPart1: 0,
        minSteps: 0,
        inputPart2: 0,
        distinctPositions: 0
      }
    },
    methods: {
        solvePart1() {
            const favoriteNumber = this.inputPart1;
            const target = { x: 31, y: 39 };
            const visited = new Set();
            const queue = [{ position: { x: 1, y: 1 }, steps: 0 }];

            while (queue.length > 0) {
                const { position, steps } = queue.shift();
                const positionStr = `${position.x},${position.y}`;

                if (visited.has(positionStr)) continue;
                visited.add(positionStr);

                if (position.x === target.x && position.y === target.y) {
                    this.minSteps = steps;
                    return;
                }

                const neighbors = this.getNeighbors(position, favoriteNumber);
                for (const neighbor of neighbors) {
                    queue.push({ position: neighbor, steps: steps + 1 });
                }
            }
        },
        isWall(position, favoriteNumber) {
            const { x, y } = position;
            const value = x*x + 3*x + 2*x*y + y + y*y + favoriteNumber;
            const binary = value.toString(2);
            const bitCount = binary.split('').reduce((count, bit) => count + (bit === '1' ? 1 : 0), 0);
            return bitCount % 2 !== 0;
        },
        getNeighbors(position, favoriteNumber) {
            const { x, y } = position;
            const directions = [{ dx: 1, dy: 0 }, { dx: -1, dy: 0 }, { dx: 0, dy: 1 }, { dx: 0, dy: -1 }];
            const neighbors = [];

            for (const { dx, dy } of directions) {
                const neighbor = { x: x + dx, y: y + dy };
                if (neighbor.x >= 0 && neighbor.y >= 0 && !this.isWall(neighbor, favoriteNumber)) {
                    neighbors.push(neighbor);
                }
            }

            return neighbors;
        },
        solvePart2() {
            const favoriteNumber = this.inputPart2;
            const visited = new Set();
            const queue = [{ position: { x: 1, y: 1 }, steps: 0 }];

            while (queue.length > 0) {
                const { position, steps } = queue.shift();
                const positionStr = `${position.x},${position.y}`;

                if (visited.has(positionStr) || steps > 50) continue;
                visited.add(positionStr);

                const neighbors = this.getNeighbors2(position, favoriteNumber);
                for (const neighbor of neighbors) {
                    queue.push({ position: neighbor, steps: steps + 1 });
                }
            }

            this.distinctPositions = visited.size;
        },
        isWall2(position, favoriteNumber) {
            const { x, y } = position;
            const value = x*x + 3*x + 2*x*y + y + y*y + favoriteNumber;
            const binary = value.toString(2);
            const bitCount = binary.split('').reduce((count, bit) => count + (bit === '1' ? 1 : 0), 0);
            return bitCount % 2 !== 0;
        },
        getNeighbors2(position, favoriteNumber) {
            const { x, y } = position;
            const directions = [{ dx: 1, dy: 0 }, { dx: -1, dy: 0 }, { dx: 0, dy: 1 }, { dx: 0, dy: -1 }];
            const neighbors = [];

            for (const { dx, dy } of directions) {
                const neighbor = { x: x + dx, y: y + dy };
                if (neighbor.x >= 0 && neighbor.y >= 0 && !this.isWall2(neighbor, favoriteNumber)) {
                    neighbors.push(neighbor);
                }
            }

            return neighbors;
        }
    }
  }
</script>