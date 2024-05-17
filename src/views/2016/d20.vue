<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Un essai pour résoudre le jour 20 de l'Advent of Code 2016 avec Github Copilot"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 20 - Firewall Rules</h1>
    <h2>Part one</h2>
    <p>
        You'd like to set up a small hidden computer here so you can use it to get back into the network later. However, the corporate firewall only allows communication with certain external IP addresses.

        You've retrieved the list of blocked IPs from the firewall, but the list seems to be messy and poorly maintained, and it's not clear which IPs are allowed. Also, rather than being written in dot-decimal notation, they are written as plain 32-bit integers, which can have any value from 0 through 4294967295, inclusive.

        For example, suppose only the values 0 through 9 were valid, and that you retrieved the following blacklist:

        5-8
        0-2
        4-7
        The blacklist specifies ranges of IPs (inclusive of both the start and end value) that are not allowed. Then, the only IPs that this firewall allows are 3 and 9, since those are the only numbers not in any range.

        Given the list of blocked IPs you retrieved from the firewall (your puzzle input), what is the lowest-valued IP that is not blocked?
    </p>
    <textarea v-model="blacklist" placeholder="Enter blacklist here"></textarea>
    <button @click="solvePart1">Solve Part 1</button>
    <p>Lowest unblocked IP: <span v-if="lowestUnblockedIp !== null">{{ lowestUnblockedIp }}</span></p>
    <h2>Part two</h2>
    <p>
        How many IPs are allowed by the blacklist?
    </p>
    <textarea v-model="blacklistPart2" placeholder="Enter blacklist here"></textarea>
    <button @click="solvePart2">Solve Part 2</button>
    <p>Number of allowed IPs: <span v-if="numberOfAllowedIps !== 0">{{ numberOfAllowedIps }}</span></p>
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
        blacklist: '',
        lowestUnblockedIp: null,
        blacklistPart2: '',
        numberOfAllowedIps: 0
      }
    },
    methods: {
        solvePart1() {
            const ranges = this.blacklist.split('\n')
                .map(line => line.split('-').map(Number))
                .sort((a, b) => a[0] - b[0] || a[1] - b[1]);

            let ip = 0;
            for (const [start, end] of ranges) {
                if (ip < start) {
                this.lowestUnblockedIp = ip;
                return;
                }
                if (ip <= end) {
                ip = end + 1;
                }
            }
            this.lowestUnblockedIp = ip;
        },
        solvePart2() {
            const ranges = this.blacklistPart2.split('\n')
                .map(line => line.split('-').map(Number))
                .sort((a, b) => a[0] - b[0] || a[1] - b[1]);

            let ip = 0;
            let allowedIps = 0;
            for (const [start, end] of ranges) {
                if (ip < start) {
                allowedIps += start - ip;
                }
                if (ip <= end) {
                ip = end + 1;
                }
            }
            this.numberOfAllowedIps = allowedIps;
        },
    }
  }
</script>