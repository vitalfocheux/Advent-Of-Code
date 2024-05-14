/**
 * Un essai pour résoudre le jour 1 du défi de l'Avent de 2020
 */

import java.util.*;
import java.nio.file.*;
import java.io.IOException;

public class d01 {
    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("01.txt"));
            List<Integer> numbers = new ArrayList<>();
            for (String line : lines) {
                numbers.add(Integer.parseInt(line));
            }

            // Part 1: Find two numbers in your list that add up to 2020
            for (int i = 0; i < numbers.size(); i++) {
                for (int j = i + 1; j < numbers.size(); j++) {
                    if (numbers.get(i) + numbers.get(j) == 2020) {
                        System.out.println("Part 1: " + numbers.get(i) * numbers.get(j));
                    }
                }
            }

            // Part 2: Find three numbers in your list that add up to 2020
            for (int i = 0; i < numbers.size(); i++) {
                for (int j = i + 1; j < numbers.size(); j++) {
                    for (int k = j + 1; k < numbers.size(); k++) {
                        if (numbers.get(i) + numbers.get(j) + numbers.get(k) == 2020) {
                            System.out.println("Part 2: " + numbers.get(i) * numbers.get(j) * numbers.get(k));
                        }
                    }
                }
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}