<script setup>
  import Navbar from '@/components/Navbar.vue';
  import HeaderAI from '@/components/HeaderAI.vue';

  const messages = ["Un essai pour résoudre le jour 21 de l'Advent of Code 2015 avec Github Copilot"]
</script>

<template>
    <Navbar />

    <HeaderAI :msg= "messages"/>

    <main>
        <h1>Day 21 - RPG Simulator 20XX</h1>
        <h2>Part one</h2>
        <p>
            Little Henry Case got a new video game for Christmas. It's an RPG, and he's stuck on a boss. He needs to know what equipment to buy at the shop. He hands you the controller.

            In this game, the player (you) and the enemy (the boss) take turns attacking. The player always goes first. Each attack reduces the opponent's hit points by at least 1. The first character at or below 0 hit points loses.

            Damage dealt by an attacker each turn is equal to the attacker's damage score minus the defender's armor score. An attacker always does at least 1 damage. So, if the attacker has a damage score of 8, and the defender has an armor score of 3, the defender loses 5 hit points. If the defender had an armor score of 300, the defender would still lose 1 hit point.

            Your damage score and armor score both start at zero. They can be increased by buying items in exchange for gold. You start with no items and have as much gold as you need. Your total damage or armor is equal to the sum of those stats from all of your items. You have 100 hit points.

            Here is what the item shop is selling:

            Weapons:    Cost  Damage  Armor
            Dagger        8     4       0
            Shortsword   10     5       0
            Warhammer    25     6       0
            Longsword    40     7       0
            Greataxe     74     8       0

            Armor:      Cost  Damage  Armor
            Leather      13     0       1
            Chainmail    31     0       2
            Splintmail   53     0       3
            Bandedmail   75     0       4
            Platemail   102     0       5

            Rings:      Cost  Damage  Armor
            Damage +1    25     1       0
            Damage +2    50     2       0
            Damage +3   100     3       0
            Defense +1   20     0       1
            Defense +2   40     0       2
            Defense +3   80     0       3
            You must buy exactly one weapon; no dual-wielding. Armor is optional, but you can't use more than one. You can buy 0-2 rings (at most one for each hand). You must use any items you buy. The shop only has one of each item, so you can't buy, for example, two rings of Damage +3.

            For example, suppose you have 8 hit points, 5 damage, and 5 armor, and that the boss has 12 hit points, 7 damage, and 2 armor:

            The player deals 5-2 = 3 damage; the boss goes down to 9 hit points.
            The boss deals 7-5 = 2 damage; the player goes down to 6 hit points.
            The player deals 5-2 = 3 damage; the boss goes down to 6 hit points.
            The boss deals 7-5 = 2 damage; the player goes down to 4 hit points.
            The player deals 5-2 = 3 damage; the boss goes down to 3 hit points.
            The boss deals 7-5 = 2 damage; the player goes down to 2 hit points.
            The player deals 5-2 = 3 damage; the boss goes down to 0 hit points.
            In this scenario, the player wins! (Barely.)

            You have 100 hit points. The boss's actual stats are in your puzzle input. What is the least amount of gold you can spend and still win the fight?
        </p>
        <input v-model.number="bossHitPoints" placeholder="Enter boss hit points">
        <input v-model.number="bossDamage" placeholder="Enter boss damage">
        <input v-model.number="bossArmor" placeholder="Enter boss armor">
        <button @click="calculateMinGold">Calculate</button>
        <p>Minimum gold to spend: <span v-if="minGold !== 0">{{ minGold }}</span></p>
        <h2>Part two</h2>
        <p>
            Turns out the shopkeeper is working with the boss, and can persuade you to buy whatever items he wants. The other rules still apply, and he still only has one of each item.

            What is the most amount of gold you can spend and still lose the fight?
        </p>
        <input v-model.number="bossHitPointsPart2" placeholder="Enter boss hit points">
        <input v-model.number="bossDamagePart2" placeholder="Enter boss damage">
        <input v-model.number="bossArmorPart2" placeholder="Enter boss armor">
        <button @click="calculateMaxGold">Calculate</button>
        <p>Maximum gold to spend: <span v-if="maxGold !== 0">{{ maxGold }}</span></p>
    </main>

</template>

<script>
    import { useRouter } from 'vue-router';

    export default {

        data() {
            return {
                bossHitPoints: 0,
                bossDamage: 0,
                bossArmor: 0,
                minGold: 0,
                bossHitPointsPart2: 0,
                bossDamagePart2: 0,
                bossArmorPart2: 0,
                maxGold: 0
            };
        },


        setup() {
            const router = useRouter();
            return { router };
        },

        methods: {
            calculateMinGold() {
                // Define the items in the shop
                const weapons = [[8, 4], [10, 5], [25, 6], [40, 7], [74, 8]];
                const armor = [[0, 0], [13, 1], [31, 2], [53, 3], [75, 4], [102, 5]];
                const rings = [[0, 0, 0], [0, 0, 0], [25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]];

                let minGold = Infinity;

                // Try all combinations of items
                for (let w of weapons) {
                    for (let a of armor) {
                        for (let r1 of rings) {
                            for (let r2 of rings) {
                                if (r1 !== r2) {
                                    const cost = w[0] + a[0] + r1[0] + r2[0];
                                    const damage = w[1] + r1[1] + r2[1];
                                    const playerArmor = a[1] + r1[2] + r2[2];

                                    // Check if you can win the fight
                                    if (Math.ceil(this.bossHitPoints / Math.max(1, damage - this.bossArmor)) <= Math.ceil(100 / Math.max(1, this.bossDamage - playerArmor))) {
                                        minGold = Math.min(minGold, cost);
                                    }
                                }
                            }
                        }
                    }
                }

                this.minGold = minGold;
            },
            calculateMaxGold() {
                // Define the items in the shop
                const weapons = [[8, 4], [10, 5], [25, 6], [40, 7], [74, 8]];
                const armor = [[0, 0], [13, 1], [31, 2], [53, 3], [75, 4], [102, 5]];
                const rings = [[0, 0, 0], [0, 0, 0], [25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]];

                let maxGold = 0;

                // Try all combinations of items
                for (let w of weapons) {
                    for (let a of armor) {
                        for (let r1 of rings) {
                            for (let r2 of rings) {
                                if (r1 !== r2) {
                                    const cost = w[0] + a[0] + r1[0] + r2[0];
                                    const damage = w[1] + r1[1] + r2[1];
                                    const playerArmor = a[1] + r1[2] + r2[2];

                                    // Check if you lose the fight
                                    if (Math.ceil(this.bossHitPointsPart2 / Math.max(1, damage - this.bossArmorPart2)) > Math.ceil(100 / Math.max(1, this.bossDamagePart2 - playerArmor))) {
                                        maxGold = Math.max(maxGold, cost);
                                    }
                                }
                            }
                        }
                    }
                }

                this.maxGold = maxGold;
            }
        }
    }
</script>