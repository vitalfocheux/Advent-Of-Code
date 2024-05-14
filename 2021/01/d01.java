/**
 * Un essai pour résoudre le jour 1 de l'Avent de Code 2021.
 */

import java.util.*;
import java.nio.file.*;
import java.io.IOException;

public class d01 {
    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("01.txt"));
            List<Integer> numbers = new ArrayList<>();

            // Parse the input and fill the list
            for (String line : lines) {
                numbers.add(Integer.parseInt(line));
            }

            // Part 1: Determine how many times the next number is greater than the previous number
            int countPart1 = countIncreases(numbers);
            System.out.println("Part 1: " + countPart1);

            // Part 2: Determine how many times the sum of a three-measurement sliding window is greater than the previous sum
            int countPart2 = countWindowSumIncreases(numbers, 3);
            System.out.println("Part 2: " + countPart2);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static int countIncreases(List<Integer> numbers) {
        int count = 0;
        for (int i = 1; i < numbers.size(); i++) {
            if (numbers.get(i) > numbers.get(i - 1)) {
                count++;
            }
        }
        return count;
    }

    static int countWindowSumIncreases(List<Integer> numbers, int windowSize) {
        int count = 0;
        int previousSum = 0;
        for (int i = 0; i <= numbers.size() - windowSize; i++) {
            int currentSum = 0;
            for (int j = i; j < i + windowSize; j++) {
                currentSum += numbers.get(j);
            }
            if (i != 0 && currentSum > previousSum) {
                count++;
            }
            previousSum = currentSum;
        }
        return count;
    }
}