/**
 * Un essai pour résoudre le jour 1 de l'Avent de Code 2018.
 */

import java.nio.file.*;
import java.io.*;
import java.util.*;

public class d01 {
    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("01.txt"));
            List<Integer> numbers = new ArrayList<>();
            for (String line : lines) {
                numbers.add(Integer.parseInt(line));
            }

            // Part 1
            int sum = numbers.stream().mapToInt(Integer::intValue).sum();
            System.out.println("Part 1: " + sum);

            // Part 2
            Set<Integer> seen = new HashSet<>();
            int frequency = 0;
            int i = 0;
            while (!seen.contains(frequency)) {
                seen.add(frequency);
                frequency += numbers.get(i);
                i = (i + 1) % numbers.size();
            }
            System.out.println("Part 2: " + frequency);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}