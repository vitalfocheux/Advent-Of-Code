<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Un essai pour résoudre le jour 4 de l'Advent of Code 2017 avec Github Copilot"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 4 - High-Entropy Passphrases</h1>
    <h2>Part one</h2>
    <p>
        A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

        To ensure security, a valid passphrase must contain no duplicate words.

        For example:

        aa bb cc dd ee is valid.
        aa bb cc dd aa is not valid - the word aa appears more than once.
        aa bb cc dd aaa is valid - aa and aaa count as different words.
        The system's full passphrase list is available as your puzzle input. How many passphrases are valid?
    </p>
    <textarea v-model="passphrases" placeholder="Enter passphrases here"></textarea>
    <button @click="countValidPassphrases">Count Valid Passphrases</button>
    <p>Valid Passphrases: <span v-if="validPassphrases !== null">{{ validPassphrases }}</span></p>
    <h2>Part two</h2>
    <p>
        For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

        For example:

        abcde fghij is a valid passphrase.
        abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
        a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
        iiii oiii ooii oooi oooo is valid.
        oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
        Under this new system policy, how many passphrases are valid?
    </p>
    <textarea v-model="passphrasesPartTwo" placeholder="Enter passphrases here"></textarea>
    <button @click="countValidPassphrasesPartTwo">Count Valid Passphrases</button>
    <p>Valid Passphrases: <span v-if="countValidPassphrasesPartTwo !== null">{{ validPassphrasesPartTwo }}</span></p>
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
        passphrases: '',
        validPassphrases: null,
        passphrasesPartTwo: '',
        validPassphrasesPartTwo: null,
      }
    },
    methods: {
        countValidPassphrases() {
            const phrases = this.passphrases.split('\n');
            let validCount = 0;

            for (const phrase of phrases) {
                const words = phrase.split(' ');
                const uniqueWords = [...new Set(words)];
                if (words.length === uniqueWords.length) {
                validCount++;
                }
            }

            this.validPassphrases = validCount;
        },
        countValidPassphrasesPartTwo() {
            const phrases = this.passphrasesPartTwo.split('\n');
            let validCount = 0;

            for (const phrase of phrases) {
                const words = phrase.split(' ').map(word => word.split('').sort().join(''));
                const uniqueWords = [...new Set(words)];
                if (words.length === uniqueWords.length) {
                validCount++;
                }
            }

            this.validPassphrasesPartTwo = validCount;
        },
    }
  }
</script>