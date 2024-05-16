<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';

  const messages = ["Un essai pour résoudre le jour 11 de l'Advent of Code 2015 avec Github Copilot"]
</script>

<template>
    <Navbar />

    <HeaderAI :msg= "messages"/>

    <main>
        <h1>Day 11 - Corporate Policy</h1>
        <h2>Part one</h2>
        <p>
            Santa's previous password expired, and he needs help choosing a new one.

            To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

            Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

            Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

            Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
            Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
            Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
            For example:

            hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
            abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
            abbcegjk fails the third requirement, because it only has one double letter (bb).
            The next password after abcdefgh is abcdffaa.
            The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
            Given Santa's current password (your puzzle input), what should his next password be?
        </p>
        <input v-model="password" placeholder="Enter initial password here">
        <button @click="generateNextValidPassword">Generate Next Valid Password</button>
        <p>Next Valid Password: <span v-if="nextPassword !== null">{{ nextPassword }}</span></p>
        <h2>Part two</h2>
        <p>
            Santa's password expired again. What's the next one?
        </p>
        <input v-model="password" placeholder="Enter initial password here">
        <button @click="generateSecondValidPassword">Generate Second Valid Password</button>
        <p>Second Valid Password: <span v-if="secondPassword !== null">{{ secondPassword }}</span></p>
    </main>

</template>

<script>
    import { useRouter } from 'vue-router';

    export default {

        data() {
            return {
                password: '',
                nextPassword: null,
                secondPassword: null
            };
        },


        setup() {
            const router = useRouter();
            return { router };
        },

        methods: {
            isValidPassword(password) {
                return /(.)\1.*(.)\2/.test(password) && 
                        /i|o|l/.test(password) === false && 
                        /abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz/.test(password);
            },
            incrementString(str) {
                let arr = str.split('');
                for (let i = arr.length - 1; i >= 0; i--) {
                    if (arr[i] !== 'z') {
                    arr[i] = String.fromCharCode(arr[i].charCodeAt(0) + 1);
                    break;
                    } else {
                    arr[i] = 'a';
                    }
                }
                return arr.join('');
            },
            generateNextValidPassword() {
                let newPassword = this.incrementString(this.password);
                while (!this.isValidPassword(newPassword)) {
                    newPassword = this.incrementString(newPassword);
                }
                this.nextPassword = newPassword;
            },
            generateSecondValidPassword() {
                let newPassword = this.incrementString(this.password);
                while (!this.isValidPassword(newPassword)) {
                    newPassword = this.incrementString(newPassword);
                }
                newPassword = this.incrementString(newPassword);
                while (!this.isValidPassword(newPassword)) {
                    newPassword = this.incrementString(newPassword);
                }
                this.secondPassword = newPassword;
            }
        }
    }
</script>