/**
 * Un essai pour résoudre le jour 1 de l'Avent de Code 2022.
 */

import java.util.*;
import java.nio.file.*;
import java.io.IOException;

public class d01 {
    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("01.txt"));
            List<Integer> calories = new ArrayList<>();
            List<Integer> elfCalories = new ArrayList<>();
            for (String line : lines) {
                if (line.isEmpty()) {
                    elfCalories.add(calories.stream().mapToInt(Integer::intValue).sum());
                    calories.clear();
                } else {
                    calories.add(Integer.parseInt(line));
                }
            }
            elfCalories.add(calories.stream().mapToInt(Integer::intValue).sum());
            elfCalories.sort(Collections.reverseOrder());
            System.out.println("Max calories: " + elfCalories.get(0));
            System.out.println("Top 3 calories: " + (elfCalories.get(0) + elfCalories.get(1) + elfCalories.get(2)));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}