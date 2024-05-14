/**
 * Un essai pour résoudre le jour 21 du AoC 2015.
 */

import java.util.*;

public class d21 {
    static class Character {
        int hitPoints;
        int damage;
        int armor;

        Character(int hitPoints, int damage, int armor) {
            this.hitPoints = hitPoints;
            this.damage = damage;
            this.armor = armor;
        }
    }

    static class Item {
        String name;
        int cost;
        int damage;
        int armor;

        Item(String name, int cost, int damage, int armor) {
            this.name = name;
            this.cost = cost;
            this.damage = damage;
            this.armor = armor;
        }
    }

    public static void main(String[] args) {
        Character boss = new Character(100, 8, 2);
        Character player = new Character(100, 0, 0);

        Item[] weapons = {
            new Item("Dagger", 8, 4, 0),
            new Item("Shortsword", 10, 5, 0),
            new Item("Warhammer", 25, 6, 0),
            new Item("Longsword", 40, 7, 0),
            new Item("Greataxe", 74, 8, 0)
        };

        Item[] armors = {
            new Item("Leather", 13, 0, 1),
            new Item("Chainmail", 31, 0, 2),
            new Item("Splintmail", 53, 0, 3),
            new Item("Bandedmail", 75, 0, 4),
            new Item("Platemail", 102, 0, 5)
        };

        Item[] rings = {
            new Item("Damage +1", 25, 1, 0),
            new Item("Damage +2", 50, 2, 0),
            new Item("Damage +3", 100, 3, 0),
            new Item("Defense +1", 20, 0, 1),
            new Item("Defense +2", 40, 0, 2),
            new Item("Defense +3", 80, 0, 3)
        };

        int minCost = Integer.MAX_VALUE;
        int maxCost = Integer.MIN_VALUE;

        for (Item weapon : weapons) {
            for (int i = 0; i <= armors.length; i++) {
                for (int j = 0; j <= rings.length; j++) {
                    for (int k = j + 1; k <= rings.length; k++) {
                        int cost = weapon.cost;
                        int damage = player.damage + weapon.damage;
                        int armor = player.armor;

                        if (i < armors.length) {
                            cost += armors[i].cost;
                            armor += armors[i].armor;
                        }

                        if (j < rings.length) {
                            cost += rings[j].cost;
                            damage += rings[j].damage;
                            armor += rings[j].armor;
                        }

                        if (k < rings.length) {
                            cost += rings[k].cost;
                            damage += rings[k].damage;
                            armor += rings[k].armor;
                        }

                        if (wins(new Character(player.hitPoints, damage, armor), new Character(boss.hitPoints, boss.damage, boss.armor))) {
                            minCost = Math.min(minCost, cost);
                        } else {
                            maxCost = Math.max(maxCost, cost);
                        }
                    }
                }
            }
        }

        System.out.println("Part 1: " + minCost);
        System.out.println("Part 2: " + maxCost);
    }

    static boolean wins(Character player, Character boss) {
        int playerTurns = (int) Math.ceil((double) boss.hitPoints / Math.max(1, player.damage - boss.armor));
        int bossTurns = (int) Math.ceil((double) player.hitPoints / Math.max(1, boss.damage - player.armor));
        return playerTurns <= bossTurns;
    }
}