<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Deux essais pour la partie 1 avec Github Copilot",
                    "La partie 2 ne fonctionne pas"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 17 - Two Steps Forward</h1>
    <h2>Part one</h2>
    <p>
        You're trying to access a secure vault protected by a 4x4 grid of small rooms connected by doors. You start in the top-left room (marked S), and you can access the vault (marked V) once you reach the bottom-right room:

        #########
        #S| | | #
        #-#-#-#-#
        # | | | #
        #-#-#-#-#
        # | | | #
        #-#-#-#-#
        # | | |  
        ####### V
        Fixed walls are marked with #, and doors are marked with - or |.

        The doors in your current room are either open or closed (and locked) based on the hexadecimal MD5 hash of a passcode (your puzzle input) followed by a sequence of uppercase characters representing the path you have taken so far (U for up, D for down, L for left, and R for right).

        Only the first four characters of the hash are used; they represent, respectively, the doors up, down, left, and right from your current position. Any b, c, d, e, or f means that the corresponding door is open; any other character (any number or a) means that the corresponding door is closed and locked.

        To access the vault, all you need to do is reach the bottom-right room; reaching this room opens the vault and all doors in the maze.

        For example, suppose the passcode is hijkl. Initially, you have taken no steps, and so your path is empty: you simply find the MD5 hash of hijkl alone. The first four characters of this hash are ced9, which indicate that up is open (c), down is open (e), left is open (d), and right is closed and locked (9). Because you start in the top-left corner, there are no "up" or "left" doors to be open, so your only choice is down.

        Next, having gone only one step (down, or D), you find the hash of hijklD. This produces f2bc, which indicates that you can go back up, left (but that's a wall), or right. Going right means hashing hijklDR to get 5745 - all doors closed and locked. However, going up instead is worthwhile: even though it returns you to the room you started in, your path would then be DU, opening a different set of doors.

        After going DU (and then hashing hijklDU to get 528e), only the right door is open; after going DUR, all doors lock. (Fortunately, your actual passcode is not hijkl).

        Passcodes actually used by Easter Bunny Vault Security do allow access to the vault if you know the right path. For example:

        If your passcode were ihgpwlah, the shortest path would be DDRRRD.
        With kglvqrro, the shortest path would be DDUDRLRRUDRD.
        With ulqzkmiv, the shortest would be DRURDRUDDLLDLUURRDULRLDUUDDDRR.
        Given your vault's passcode, what is the shortest path (the actual path, not just the length) to reach the vault?
    </p>
    <input v-model="passcode" placeholder="Enter passcode" type="text">
    <button @click="solvePart1">Solve Part 1</button>
    <p>Shortest path to reach the vault: <span v-if="shortestPath !== ''">{{ shortestPath }}</span></p>
    <h2>Part two</h2>
    <p>
        You're curious how robust this security solution really is, and so you decide to find longer and longer paths which still provide access to the vault. You remember that paths always end the first time they reach the bottom-right room (that is, they can never pass through it, only end in it).

        For example:

        If your passcode were ihgpwlah, the longest path would take 370 steps.
        With kglvqrro, the longest path would be 492 steps long.
        With ulqzkmiv, the longest path would be 830 steps long.
        What is the length of the longest path that reaches the vault?
    </p>
 </main>

</template>

<script>
  import { useRouter } from 'vue-router'
  import md5 from 'js-md5'

  export default {
    setup() {
      const router = useRouter()
      return { router }
    },

    data() {
      return {
        passcode: '',
        shortestPath: '',
        passcodePart2: '',
        longestPathLength: 0
      }
    },
    methods: {
        solvePart1() {
            const open = 'bcdef';
            const queue = [{ x: 0, y: 0, path: '' }];

            while (queue.length) {
                const { x, y, path } = queue.shift();
                if (x === 3 && y === 3) {
                    this.shortestPath = path;
                    return;
                }

                const hash = md5(this.passcode + path);
                if (y > 0 && open.includes(hash[0])) queue.push({ x, y: y - 1, path: path + 'U' });
                if (y < 3 && open.includes(hash[1])) queue.push({ x, y: y + 1, path: path + 'D' });
                if (x > 0 && open.includes(hash[2])) queue.push({ x: x - 1, y, path: path + 'L' });
                if (x < 3 && open.includes(hash[3])) queue.push({ x: x + 1, y, path: path + 'R' });
            }
            this.shortestPath = 'No path found';
        }
    }
  }
</script>