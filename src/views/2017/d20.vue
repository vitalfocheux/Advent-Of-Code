<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';
  const messages = ["Un essai pour la partie 1 avec Github Copilot",
                    "Deux essais pour la partie 2 avec Github Copilot"]
</script>

<template>
  <Navbar />

  <HeaderAI :msg="messages" />

  <main>
    <h1>Day 20 - Particle Swarm</h1>
    <h2>Part one</h2>
    <p>
       {{ part1 }} 
    </p>
    <textarea v-model="particles" placeholder="Enter particles here"></textarea>
    <button @click="findClosestParticle">Find Closest Particle</button>
    <p>Particle that will stay closest to the origin in the long term: {{ closestParticle }}</p>
    <h2>Part two</h2>
    <p>
        {{ part2 }}
    </p>
    <textarea v-model="particles2" placeholder="Enter particles here"></textarea>
    <button @click="resolveCollisions">Resolve Collisions</button>
    <p>Number of particles left after all collisions are resolved: {{ remainingParticles }}</p>
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
        part1: 'Suddenly, the GPU contacts you, asking for help. Someone has asked it to simulate too many particles, and it won\'t be able to finish them all in time to render the next frame at this rate.\nIt transmits to you a buffer (your puzzle input) listing each particle in order (starting with particle 0, then particle 1, particle 2, and so on). For each particle, it provides the X, Y, and Z coordinates for the particle\'s position (p), velocity (v), and acceleration (a), each in the format <X,Y,Z>.\nEach tick, all particles are updated simultaneously. A particle\'s properties are updated in the following order:\nIncrease the X velocity by the X acceleration.Increase the Y velocity by the Y acceleration.\nIncrease the Z velocity by the Z acceleration.\nIncrease the X position by the X velocity.\nIncrease the Y position by the Y velocity.\nIncrease the Z position by the Z velocity.\nBecause of seemingly tenuous rationale involving z-buffering, the GPU would like to know which particle will stay closest to position <0,0,0> in the long term. Measure this using the Manhattan distance, which in this situation is simply the sum of the absolute values of a particle\'s X, Y, and Z position.\nFor example, suppose you are only given two particles, both of which stay entirely on the X-axis (for simplicity). Drawing the current states of particles 0 and 1 (in that order) with an adjacent a number line and diagram of current X positions (marked in parentheses), the following would take place:\np=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4\np=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>                         (0)(1)\np=< 4,0,0>, v=< 1,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4\np=< 2,0,0>, v=<-2,0,0>, a=<-2,0,0>                      (1)   (0)\np=< 4,0,0>, v=< 0,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4\np=<-2,0,0>, v=<-4,0,0>, a=<-2,0,0>          (1)               (0)\np=< 3,0,0>, v=<-1,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4\np=<-8,0,0>, v=<-6,0,0>, a=<-2,0,0>                         (0)   \nAt this point, particle 1 will never be closer to <0,0,0> than particle 0, and so, in the long run, particle 0 will stay closest.\nWhich particle will stay closest to position <0,0,0> in the long term?',
        part2: 'To simplify the problem further, the GPU would like to remove any particles that collide. Particles collide if their positions ever exactly match. Because particles are updated simultaneously, more than two particles can collide at the same time and place. Once particles collide, they are removed and cannot collide with anything else after that tick.\nFor example:\np=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>    \np=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3\np=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>    (0)   (1)   (2)            (3)\np=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>\np=<-3,0,0>, v=< 3,0,0>, a=< 0,0,0>\np=<-2,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3\np=<-1,0,0>, v=< 1,0,0>, a=< 0,0,0>             (0)(1)(2)      (3)   \np=< 2,0,0>, v=<-1,0,0>, a=< 0,0,0>\np=< 0,0,0>, v=< 3,0,0>, a=< 0,0,0>    \np=< 0,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3\np=< 0,0,0>, v=< 1,0,0>, a=< 0,0,0>                       X (3)      \np=< 1,0,0>, v=<-1,0,0>, a=< 0,0,0>\n------destroyed by collision------  \n------destroyed by collision------    -6 -5 -4 -3 -2 -1  0  1  2  3\n------destroyed by collision------                      (3)         \np=< 0,0,0>, v=<-1,0,0>, a=< 0,0,0>\nIn this example, particles 0, 1, and 2 are simultaneously destroyed at the time and place marked X. On the next tick, particle 3 passes through unharmed.\nHow many particles are left after all collisions are resolved?',
        particles: '',
        closestParticle: null,
        particles2: '',
        remainingParticles: null,
      }
    },
    methods: {
        findClosestParticle() {
            const lines = this.particles.split('\n');
            const particles = lines.map((line, index) => {
                const [p, v, a] = line.match(/<([^>]+)>/g).map(s => s.slice(1, -1).split(',').map(Number));
                return { index, p, v, a };
            });

            particles.sort((a, b) => {
                const distA = a.a.reduce((sum, val) => sum + Math.abs(val), 0);
                const distB = b.a.reduce((sum, val) => sum + Math.abs(val), 0);
                return distA - distB;
            });

            this.closestParticle = particles[0].index;
        },
        resolveCollisions() {
            const lines = this.particles2.split('\n');
            let particles = lines.map((line, index) => {
                const [p, v, a] = line.match(/<([^>]+)>/g).map(s => s.slice(1, -1).split(',').map(Number));
                return { index, p, v, a };
            });

            for (let i = 0; i < 1000; i++) {
                let positions = {};

                // Update velocities and positions
                particles.forEach(particle => {
                particle.v = particle.v.map((val, index) => val + particle.a[index]);
                particle.p = particle.p.map((val, index) => val + particle.v[index]);
                const position = particle.p.join(',');
                positions[position] = (positions[position] || 0) + 1;
                });

                // Resolve collisions
                particles = particles.filter(particle => {
                const position = particle.p.join(',');
                return positions[position] === 1;
                });

                // Reset positions for the next iteration
                positions = {};
            }

            this.remainingParticles = particles.length;
        },
    }
  }
</script>