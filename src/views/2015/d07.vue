<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';

  const messages = ["Deux essais pour la partie 1 avec Github Copilot, il n'avais pas réussi a bien optimisé",
                    "Un essai pour la partie 2 avec Github Copilot"]
</script>

<template>
    <Navbar />

    <HeaderAI :msg= "messages"/>

    <main>
        <h1>Day 7 - Some Assembly Required</h1>
        <h2>Part one</h2>
        <p>
            This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

            Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

            The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

            For example:

            123 -> x means that the signal 123 is provided to wire x.
            x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
            p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
            NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
            Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

            For example, here is a simple circuit:

            123 -> x
            456 -> y
            x AND y -> d
            x OR y -> e
            x LSHIFT 2 -> f
            y RSHIFT 2 -> g
            NOT x -> h
            NOT y -> i
            After it is run, these are the signals on the wires:

            d: 72
            e: 507
            f: 492
            g: 114
            h: 65412
            i: 65079
            x: 123
            y: 456
            In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?
        </p>
        <textarea v-model="instructions" placeholder="Enter instructions here, one per line"></textarea>
        <button @click="calculateSignal()">Calculate Signal</button>
        <p>Signal on wire a: <span v-if="signal !== null">{{ signal }}</span></p>
        <h2>Part two</h2>
        <p>
            Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?
        </p>
        <textarea v-model="instructions" placeholder="Enter instructions here, one per line"></textarea>
        <button @click="calculateSignal(true)">Calculate Signal for Part 2</button>
        <p>Signal on wire a: <span v-if="signal !== null"> {{ signal2 }}</span></p>
    </main>

</template>

<script>
    import { useRouter } from 'vue-router';

    export default {

        data() {
            return {
                instructions: '',
                signal: null,
                signal2: null
            };
        },


        setup() {
            const router = useRouter();
            return { router };
        },

        methods: {
            calculateSignal(resetB=false) {
                const instructionsArray = this.instructions.split('\n');
                const wires = {};
                const instructions = {};

                // Transform the array of instructions into an object
                for (let instruction of instructionsArray) {
                    const [left, right] = instruction.split(' -> ');
                    instructions[right] = left;
                }

                if (resetB) {
                    instructions['b'] = String(this.signal);
                }

                // Use a helper function to calculate the signal for a wire
                const getSignal = (wire) => {
                    if (wires[wire] !== undefined) return wires[wire];
                    if (!isNaN(wire)) return Number(wire);
                    const instruction = instructions[wire];
                    wires[wire] = this.executeInstruction(instruction, wires, getSignal);
                    return wires[wire];
                };

                resetB ? this.signal2 = getSignal('a') : this.signal = getSignal('a');
            },
            executeInstruction(instruction, wires, getSignal) {
                if (/^\d+$/.test(instruction)) return Number(instruction);
                if (wires[instruction]) return wires[instruction];
                const parts = instruction.split(' ');
                if (parts.length === 1) return getSignal(parts[0]);
                if (parts[1] === 'AND') return getSignal(parts[0]) & getSignal(parts[2]);
                if (parts[1] === 'OR') return getSignal(parts[0]) | getSignal(parts[2]);
                if (parts[1] === 'LSHIFT') return getSignal(parts[0]) << getSignal(parts[2]);
                if (parts[1] === 'RSHIFT') return getSignal(parts[0]) >> getSignal(parts[2]);
                if (parts[0] === 'NOT') return ~getSignal(parts[1]) & 0xffff;
                return false;
            }
        }
    }
</script>