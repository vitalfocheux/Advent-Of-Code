/**
 * Un essai pour résoudre le jour 15 de l'année 2015
 */

import java.util.*;
import java.io.*;

class Ingredient {
    int capacity;
    int durability;
    int flavor;
    int texture;
    int calories;

    Ingredient(int capacity, int durability, int flavor, int texture, int calories) {
        this.capacity = capacity;
        this.durability = durability;
        this.flavor = flavor;
        this.texture = texture;
        this.calories = calories;
    }
}

public class d15 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("15.txt"));
        List<Ingredient> ingredients = new ArrayList<>();
        String line;
        while ((line = reader.readLine()) != null) {
            String[] parts = line.split(" ");
            int capacity = Integer.parseInt(parts[2].substring(0, parts[2].length() - 1));
            int durability = Integer.parseInt(parts[4].substring(0, parts[4].length() - 1));
            int flavor = Integer.parseInt(parts[6].substring(0, parts[6].length() - 1));
            int texture = Integer.parseInt(parts[8].substring(0, parts[8].length() - 1));
            int calories = Integer.parseInt(parts[10]);
            ingredients.add(new Ingredient(capacity, durability, flavor, texture, calories));
        }
        reader.close();

        int maxScore = 0;
        int maxScore500Calories = 0;
        for (int i = 0; i <= 100; i++) {
            for (int j = 0; j <= 100 - i; j++) {
                for (int k = 0; k <= 100 - i - j; k++) {
                    int l = 100 - i - j - k;
                    int capacity = Math.max(0, i * ingredients.get(0).capacity + j * ingredients.get(1).capacity + k * ingredients.get(2).capacity + l * ingredients.get(3).capacity);
                    int durability = Math.max(0, i * ingredients.get(0).durability + j * ingredients.get(1).durability + k * ingredients.get(2).durability + l * ingredients.get(3).durability);
                    int flavor = Math.max(0, i * ingredients.get(0).flavor + j * ingredients.get(1).flavor + k * ingredients.get(2).flavor + l * ingredients.get(3).flavor);
                    int texture = Math.max(0, i * ingredients.get(0).texture + j * ingredients.get(1).texture + k * ingredients.get(2).texture + l * ingredients.get(3).texture);
                    int calories = i * ingredients.get(0).calories + j * ingredients.get(1).calories + k * ingredients.get(2).calories + l * ingredients.get(3).calories;
                    int score = capacity * durability * flavor * texture;
                    maxScore = Math.max(maxScore, score);
                    if (calories == 500) {
                        maxScore500Calories = Math.max(maxScore500Calories, score);
                    }
                }
            }
        }

        System.out.println("Part 1: " + maxScore);
        System.out.println("Part 2: " + maxScore500Calories);
    }
}