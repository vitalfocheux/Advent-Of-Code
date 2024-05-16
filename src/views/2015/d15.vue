<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';

  const messages = ["Deux essais pour la partie 1 avec Github Copilot",
                    "Un essai pour la partie 2 avec Github Copilot"]
</script>

<template>
    <Navbar />

    <HeaderAI :msg= "messages"/>

    <main>
        <h1>Day 15 - Science for Hungry People</h1>
        <h2>Part one</h2>
        <p>
            Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.

            Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:

            capacity (how well it helps the cookie absorb milk)
            durability (how well it keeps the cookie intact when full of milk)
            flavor (how tasty it makes the cookie)
            texture (how it improves the feel of the cookie)
            calories (how many calories it adds to the cookie)
            You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.

            For instance, suppose you have these two ingredients:

            Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
            Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
            Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:

            A capacity of 44*-1 + 56*2 = 68
            A durability of 44*-2 + 56*3 = 80
            A flavor of 44*6 + 56*-2 = 152
            A texture of 44*3 + 56*-1 = 76
            Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

            Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?
        </p>
        <textarea v-model="ingredientDescriptions" placeholder="Enter ingredient descriptions here"></textarea>
        <button @click="calculateHighestScoringCookie">Calculate</button>
        <p>Highest Scoring Cookie: <span v-if="highestScoringCookie !== 0">{{ highestScoringCookie }}</span></p>
        <h2>Part two</h2>
        <p>
            Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe that has exactly 500 calories per cookie (so they can use it as a meal replacement). Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system).

            For example, given the ingredients above, if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500. The total score would go down, though: only 57600000, the best you can do in such trying circumstances.

            Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make with a calorie total of 500?
        </p>
        <textarea v-model="ingredientDescriptions" placeholder="Enter ingredient descriptions here"></textarea>
        <button @click="calculateHighestScoringCookie2">Calculate</button>
        <p>Highest Scoring Cookie: <span v-if="highestScoringCookie2 !== 0">{{ highestScoringCookie2 }}</span></p>
    </main>

</template>

<script>
    import { useRouter } from 'vue-router';

    export default {

        data() {
            return {
                ingredientDescriptions: '',
                highestScoringCookie: 0,
                highestScoringCookie2: 0,
            };
        },


        setup() {
            const router = useRouter();
            return { router };
        },

        methods: {
            calculateHighestScoringCookie() {
                const descriptions = this.ingredientDescriptions.split('\n');
                const ingredients = descriptions.map(description => {
                    const match = description.match(/(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)/);
                    if (match) {
                        const [, name, capacity, durability, flavor, texture, calories] = match;
                        return { 
                            name, 
                            capacity: Number(capacity), 
                            durability: Number(durability), 
                            flavor: Number(flavor), 
                            texture: Number(texture), 
                            calories: Number(calories) 
                        };
                    }
                });

                let maxScore = 0;

                for (let i = 0; i <= 100; i++) {
                    for (let j = 0; j <= 100 - i; j++) {
                        for (let k = 0; k <= 100 - i - j; k++) {
                            const l = 100 - i - j - k;
                            const amounts = [i, j, k, l];
                            const score = this.calculateCookieScore(ingredients, amounts);
                            maxScore = Math.max(maxScore, score);
                        }
                    }
                }

                this.highestScoringCookie = maxScore;
            },

            calculateCookieScore(ingredients, amounts) {
                let capacity = 0, durability = 0, flavor = 0, texture = 0;

                for (let i = 0; i < ingredients.length; i++) {
                    capacity += ingredients[i].capacity * amounts[i];
                    durability += ingredients[i].durability * amounts[i];
                    flavor += ingredients[i].flavor * amounts[i];
                    texture += ingredients[i].texture * amounts[i];
                }

                capacity = Math.max(0, capacity);
                durability = Math.max(0, durability);
                flavor = Math.max(0, flavor);
                texture = Math.max(0, texture);

                return capacity * durability * flavor * texture;
            },
            calculateHighestScoringCookie2() {
                const descriptions = this.ingredientDescriptions.split('\n');
                const ingredients = descriptions.map(description => {
                    const match = description.match(/(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)/);
                    if (match) {
                        const [, name, capacity, durability, flavor, texture, calories] = match;
                        return { 
                            name, 
                            capacity: Number(capacity), 
                            durability: Number(durability), 
                            flavor: Number(flavor), 
                            texture: Number(texture), 
                            calories: Number(calories) 
                        };
                    }
                });

                let maxScore = 0;

                for (let i = 0; i <= 100; i++) {
                    for (let j = 0; j <= 100 - i; j++) {
                        for (let k = 0; k <= 100 - i - j; k++) {
                            const l = 100 - i - j - k;
                            const amounts = [i, j, k, l];
                            const score = this.calculateCookieScore2(ingredients, amounts);
                            const calories = this.calculateTotalCalories2(ingredients, amounts);
                            if (calories === 500) {
                                maxScore = Math.max(maxScore, score);
                            }
                        }
                    }
                }

                this.highestScoringCookie2 = maxScore;
            },

            calculateCookieScore2(ingredients, amounts) {
                let capacity = 0, durability = 0, flavor = 0, texture = 0;

                for (let i = 0; i < ingredients.length; i++) {
                    capacity += ingredients[i].capacity * amounts[i];
                    durability += ingredients[i].durability * amounts[i];
                    flavor += ingredients[i].flavor * amounts[i];
                    texture += ingredients[i].texture * amounts[i];
                }

                capacity = Math.max(0, capacity);
                durability = Math.max(0, durability);
                flavor = Math.max(0, flavor);
                texture = Math.max(0, texture);

                return capacity * durability * flavor * texture;
            },

            calculateTotalCalories2(ingredients, amounts) {
                let totalCalories = 0;

                for (let i = 0; i < ingredients.length; i++) {
                    totalCalories += ingredients[i].calories * amounts[i];
                }

                return totalCalories;
            }
        }
    }
</script>