<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Un essai pour résoudre le jour 14 de l'Advent of Code 2016 avec Github Copilot"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 14 - One-Time Pad</h1>
    <h2>Part one</h2>
    <p>
        In order to communicate securely with Santa while you're on this mission, you've been using a one-time pad that you generate using a pre-agreed algorithm. Unfortunately, you've run out of keys in your one-time pad, and so you need to generate some more.

        To generate keys, you first get a stream of random data by taking the MD5 of a pre-arranged salt (your puzzle input) and an increasing integer index (starting with 0, and represented in decimal); the resulting MD5 hash should be represented as a string of lowercase hexadecimal digits.

        However, not all of these MD5 hashes are keys, and you need 64 new keys for your one-time pad. A hash is a key only if:

        It contains three of the same character in a row, like 777. Only consider the first such triplet in a hash.
        One of the next 1000 hashes in the stream contains that same character five times in a row, like 77777.
        Considering future hashes for five-of-a-kind sequences does not cause those hashes to be skipped; instead, regardless of whether the current hash is a key, always resume testing for keys starting with the very next hash.

        For example, if the pre-arranged salt is abc:

        The first index which produces a triple is 18, because the MD5 hash of abc18 contains ...cc38887a5.... However, index 18 does not count as a key for your one-time pad, because none of the next thousand hashes (index 19 through index 1018) contain 88888.
        The next index which produces a triple is 39; the hash of abc39 contains eee. It is also the first key: one of the next thousand hashes (the one at index 816) contains eeeee.
        None of the next six triples are keys, but the one after that, at index 92, is: it contains 999 and index 200 contains 99999.
        Eventually, index 22728 meets all of the criteria to generate the 64th key.
        So, using our example salt of abc, index 22728 produces the 64th key.

        Given the actual salt in your puzzle input, what index produces your 64th one-time pad key?
    </p>
    <input v-model="inputPart1" placeholder="Enter salt" type="text">
    <button @click="solvePart1">Solve Part 1</button>
    <p>Index that produces the 64th one-time pad key: <span v-if="index64thKey !== 0">{{ index64thKey }}</span></p>
    <h2>Part two</h2>
    <p>
        Of course, in order to make this process even more secure, you've also implemented key stretching.

        Key stretching forces attackers to spend more time generating hashes. Unfortunately, it forces everyone else to spend more time, too.

        To implement key stretching, whenever you generate a hash, before you use it, you first find the MD5 hash of that hash, then the MD5 hash of that hash, and so on, a total of 2016 additional hashings. Always use lowercase hexadecimal representations of hashes.

        For example, to find the stretched hash for index 0 and salt abc:

        Find the MD5 hash of abc0: 577571be4de9dcce85a041ba0410f29f.
        Then, find the MD5 hash of that hash: eec80a0c92dc8a0777c619d9bb51e910.
        Then, find the MD5 hash of that hash: 16062ce768787384c81fe17a7a60c7e3.
        ...repeat many times...
        Then, find the MD5 hash of that hash: a107ff634856bb300138cac6568c0f24.
        So, the stretched hash for index 0 in this situation is a107ff.... In the end, you find the original hash (one use of MD5), then find the hash-of-the-previous-hash 2016 times, for a total of 2017 uses of MD5.

        The rest of the process remains the same, but now the keys are entirely different. Again for salt abc:

        The first triple (222, at index 5) has no matching 22222 in the next thousand hashes.
        The second triple (eee, at index 10) hash a matching eeeee at index 89, and so it is the first key.
        Eventually, index 22551 produces the 64th key (triple fff with matching fffff at index 22859.
        Given the actual salt in your puzzle input and using 2016 extra MD5 calls of key stretching, what index now produces your 64th one-time pad key?
    </p>
    <input v-model="inputPart2" placeholder="Enter salt" type="text">
    <button @click="solvePart2">Solve Part 2</button>
    <p>Index that produces the 64th one-time pad key with key stretching: <span v-if="index64thKeyStretched !== 0">{{ index64thKeyStretched }}</span></p>
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
        inputPart1: '',
        index64thKey: 0,
        inputPart2: '',
        index64thKeyStretched: 0
      }
    },
    methods: {
        solvePart1() {
            const salt = this.inputPart1;
            const hashes = [];
            let keys = 0;

            for (let i = 0; keys < 64; i++) {
                if (!hashes[i]) {
                    hashes[i] = md5(salt + i);
                }

                const tripleMatch = hashes[i].match(/(.)\1\1/);
                if (!tripleMatch) continue;

                for (let j = i + 1; j <= i + 1000; j++) {
                    if (!hashes[j]) {
                        hashes[j] = md5(salt + j);
                    }

                    if (hashes[j].includes(tripleMatch[1].repeat(5))) {
                        keys++;
                        if (keys === 64) {
                            this.index64thKey = i;
                            return;
                        }
                        break;
                    }
                }
            }
        },
        solvePart2() {
            const salt = this.inputPart2;
            const hashes = [];
            let keys = 0;

            for (let i = 0; keys < 64; i++) {
                if (!hashes[i]) {
                    let hash = md5(salt + i);
                    for (let j = 0; j < 2016; j++) {
                        hash = md5(hash);
                    }
                    hashes[i] = hash;
                }

                const tripleMatch = hashes[i].match(/(.)\1\1/);
                if (!tripleMatch) continue;

                for (let j = i + 1; j <= i + 1000; j++) {
                    if (!hashes[j]) {
                        let hash = md5(salt + j);
                        for (let k = 0; k < 2016; k++) {
                            hash = md5(hash);
                        }
                        hashes[j] = hash;
                    }

                    if (hashes[j].includes(tripleMatch[1].repeat(5))) {
                        keys++;
                        if (keys === 64) {
                            this.index64thKeyStretched = i;
                            return;
                        }
                        break;
                    }
                }
            }
        }
    }
  }
</script>