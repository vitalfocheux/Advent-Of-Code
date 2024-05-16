<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Un essai pour résoudre le jour 4 de l'Advent of Code 2016 avec Github Copilot"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 4 - Security Through Obscurity</h1>
    <h2>Part one</h2>
    <p>
        Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.

        Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.

        A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization. For example:

        aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
        a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
        not-a-real-room-404[oarel] is a real room.
        totally-real-room-200[decoy] is not.
        Of the real rooms from the list above, the sum of their sector IDs is 1514.

        What is the sum of the sector IDs of the real rooms?
    </p>
    <textarea v-model="input" placeholder="Enter room names, one line per room"></textarea>
    <button @click="solve">Solve</button>
    <p>Sum of sector IDs of real rooms: <span v-if="sumOfRealRoomIDs !== 0">{{ sumOfRealRoomIDs }}</span></p>
    <h2>Part two</h2>
    <p>
        With all the decoy data out of the way, it's time to decrypt this list and get moving.

        The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.

        To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.

        For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

        What is the sector ID of the room where North Pole objects are stored?
    </p>
    <textarea v-model="input2" placeholder="Enter room names, one line per room"></textarea>
    <button @click="solvePart2">Solve Part 2</button>
    <p>Northpole room sector ID: <span v-if="northpoleRoomID !== 0">{{ northpoleRoomID }}</span></p>
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
        input: '',
        sumOfRealRoomIDs: 0,
        input2: '',
        northpoleRoomID: 0
      }
    },
    methods: {
        solve() {
            const lines = this.input.split('\n').filter(line => line.trim() !== '');
            let sum = 0;
            for (const line of lines) {
                const match = line.match(/^([a-z-]+)-(\d+)\[([a-z]+)\]$/);
                if (match) {
                    const name = match[1];
                    const sectorID = Number(match[2]);
                    const checksum = match[3];
                    const frequency = Array(26).fill(0);
                    for (const char of name) {
                        if (char !== '-') {
                            frequency[char.charCodeAt(0) - 'a'.charCodeAt(0)]++;
                        }
                    }
                    const computedChecksum = frequency
                        .map((freq, i) => ({ letter: String.fromCharCode(i + 'a'.charCodeAt(0)), freq }))
                        .sort((a, b) => b.freq - a.freq || a.letter.localeCompare(b.letter))
                        .slice(0, 5)
                        .map(item => item.letter)
                        .join('');
                    if (computedChecksum === checksum) {
                        sum += sectorID;
                    }
                }
            }
            this.sumOfRealRoomIDs = sum;
        },
        solvePart2() {
            const lines = this.input2.split('\n').filter(line => line.trim() !== '');
            for (const line of lines) {
                const match = line.match(/^([a-z-]+)-(\d+)\[([a-z]+)\]$/);
                if (match) {
                    const name = match[1];
                    const sectorID = Number(match[2]);
                    const checksum = match[3];
                    let decryptedName = '';
                    for (const char of name) {
                        if (char === '-') {
                            decryptedName += ' ';
                        } else {
                            decryptedName += String.fromCharCode((char.charCodeAt(0) - 'a'.charCodeAt(0) + sectorID) % 26 + 'a'.charCodeAt(0));
                        }
                    }
                    if (decryptedName.includes('northpole')) {
                        this.northpoleRoomID = sectorID;
                        break;
                    }
                }
            }
        }
    }
  }
</script>