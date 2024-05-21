<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Un essai pour résoudre le jour 24 de l'Advent of Code avec Github Copilot"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 24 - Electromagnetic Moat</h1>
    <h2>Part one</h2>
    <p>
        The CPU itself is a large, black building surrounded by a bottomless pit. Enormous metal tubes extend outward from the side of the building at regular intervals and descend down into the void. There's no way to cross, but you need to get inside.

        No way, of course, other than building a bridge out of the magnetic components strewn about nearby.

        Each component has two ports, one on each end. The ports come in all different types, and only matching types can be connected. You take an inventory of the components by their port types (your puzzle input). Each port is identified by the number of pins it uses; more pins mean a stronger connection for your bridge. A 3/7 component, for example, has a type-3 port on one side, and a type-7 port on the other.

        Your side of the pit is metallic; a perfect surface to connect a magnetic, zero-pin port. Because of this, the first port you use must be of type 0. It doesn't matter what type of port you end with; your goal is just to make the bridge as strong as possible.

        The strength of a bridge is the sum of the port types in each component. For example, if your bridge is made of components 0/3, 3/7, and 7/4, your bridge has a strength of 0+3 + 3+7 + 7+4 = 24.

        For example, suppose you had the following components:

        0/2
        2/2
        2/3
        3/4
        3/5
        0/1
        10/1
        9/10
        With them, you could make the following valid bridges:

        0/1
        0/1--10/1
        0/1--10/1--9/10
        0/2
        0/2--2/3
        0/2--2/3--3/4
        0/2--2/3--3/5
        0/2--2/2
        0/2--2/2--2/3
        0/2--2/2--2/3--3/4
        0/2--2/2--2/3--3/5
        (Note how, as shown by 10/1, order of ports within a component doesn't matter. However, you may only use each port on a component once.)

        Of these bridges, the strongest one is 0/1--10/1--9/10; it has a strength of 0+1 + 1+10 + 10+9 = 31.

        What is the strength of the strongest bridge you can make with the components you have available?
    </p>
    <textarea v-model="components" placeholder="Enter components here"></textarea>
    <button @click="calculateStrongestBridge">Calculate Strongest Bridge</button>
    <p>Strength of the strongest bridge: {{ strongestBridge }}</p>
    <h2>Part two</h2>
    <p>
        The bridge you've built isn't long enough; you can't jump the rest of the way.

        In the example above, there are two longest bridges:

        0/2--2/2--2/3--3/4
        0/2--2/2--2/3--3/5
        Of them, the one which uses the 3/5 component is stronger; its strength is 0+2 + 2+2 + 2+3 + 3+5 = 19.

        What is the strength of the longest bridge you can make? If you can make multiple bridges of the longest length, pick the strongest one.
    </p>
    <textarea v-model="componentsInput" placeholder="Enter components here"></textarea>
    <button @click="calculateLongestStrongestBridge">Calculate Longest Strongest Bridge</button>
    <p>Strength of the longest strongest bridge: {{ longestStrongestBridge }}</p>
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
        components: '',
        strongestBridge: null,
        componentsInput: '',
        longestStrongestBridge: null,
      }
    },
    methods: {
        calculateStrongestBridge() {
            const components = this.components.split('\n').map(line => line.split('/').map(Number));
            this.strongestBridge = this.findStrongestBridge(components, 0);
        },
        findStrongestBridge(components, port) {
            let maxStrength = 0;
            for (let i = 0; i < components.length; i++) {
                const component = components[i];
                if (component.includes(port)) {
                    const remainingComponents = [...components];
                    remainingComponents.splice(i, 1);
                    const nextPort = component[0] === port ? component[1] : component[0];
                    const strength = component[0] + component[1] + this.findStrongestBridge(remainingComponents, nextPort);
                    maxStrength = Math.max(maxStrength, strength);
                }
            }
            return maxStrength;
        },
        calculateLongestStrongestBridge() {
            const components = this.componentsInput.split('\n').map(line => line.split('/').map(Number));
            this.longestStrongestBridge = this.findLongestStrongestBridge(components, 0).strength;
        },
        findLongestStrongestBridge(components, port) {
            let maxStrength = 0;
            let maxLength = 0;
            for (let i = 0; i < components.length; i++) {
                const component = components[i];
                if (component.includes(port)) {
                    const remainingComponents = [...components];
                    remainingComponents.splice(i, 1);
                    const nextPort = component[0] === port ? component[1] : component[0];
                    const result = this.findLongestStrongestBridge(remainingComponents, nextPort);
                    const length = 1 + result.length;
                    const strength = component[0] + component[1] + result.strength;
                    if (length > maxLength || (length === maxLength && strength > maxStrength)) {
                        maxLength = length;
                        maxStrength = strength;
                    }
                }
            }
            return { length: maxLength, strength: maxStrength };
        },
    }
  }
</script>