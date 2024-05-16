<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Un essai pour résoudre le jour 7 de l'Advent of Code 2016 avec Github Copilot"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 7 - Internet Protocol Version 7</h1>
    <h2>Part one</h2>
    <p>
        While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).

        An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.

        For example:

        abba[mnop]qrst supports TLS (abba outside square brackets).
        abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
        aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
        ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
        How many IPs in your puzzle input support TLS?
    </p>
    <textarea v-model="input" placeholder="Enter IP addresses, one line per address"></textarea>
    <button @click="solve">Solve</button>
    <p>Number of IPs that support TLS: <span v-if="tlsSupportingIPs !== 0">{{ tlsSupportingIPs }}</span></p>
    <h2>Part two</h2>
    <p>
        You would also like to know which IPs support SSL (super-secret listening).

        An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.

        For example:

        aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
        xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
        aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
        zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).
        How many IPs in your puzzle input support SSL?
    </p>
    <textarea v-model="input2" placeholder="Enter IP addresses, one line per address"></textarea>
    <button @click="solvePart2">Solve Part 2</button>
    <p>Number of IPs that support SSL: <span v-if="sslSupportingIPs !== 0">{{ sslSupportingIPs }}</span></p>
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
        tlsSupportingIPs: 0,
        input2: '',
        sslSupportingIPs: 0
      }
    },
    methods: {
        hasABBA(str) {
            for (let i = 0; i < str.length - 3; i++) {
                if (str[i] === str[i + 3] && str[i + 1] === str[i + 2] && str[i] !== str[i + 1]) {
                    return true;
                }
            }
            return false;
        },
        solve() {
            const lines = this.input.split('\n').filter(line => line.trim() !== '');
            let count = 0;
            for (const line of lines) {
                const parts = line.split(/[\[\]]/);
                const outsideBrackets = parts.filter((_, i) => i % 2 === 0);
                const insideBrackets = parts.filter((_, i) => i % 2 === 1);
                if (outsideBrackets.some(this.hasABBA) && !insideBrackets.some(this.hasABBA)) {
                    count++;
                }
            }
            this.tlsSupportingIPs = count;
        },
        getABAs(str) {
            const abas = [];
            for (let i = 0; i < str.length - 2; i++) {
                if (str[i] === str[i + 2] && str[i] !== str[i + 1]) {
                    abas.push(str.slice(i, i + 3));
                }
            }
            return abas;
        },
        solvePart2() {
            const lines = this.input2.split('\n').filter(line => line.trim() !== '');
            let count = 0;
            for (const line of lines) {
                const parts = line.split(/[\[\]]/);
                const outsideBrackets = parts.filter((_, i) => i % 2 === 0);
                const insideBrackets = parts.filter((_, i) => i % 2 === 1);
                const abas = outsideBrackets.flatMap(this.getABAs);
                const babs = insideBrackets.flatMap(this.getABAs).map(aba => aba[1] + aba[0] + aba[1]);
                if (abas.some(aba => babs.includes(aba))) {
                    count++;
                }
            }
            this.sslSupportingIPs = count;
        }
    }
  }
</script>