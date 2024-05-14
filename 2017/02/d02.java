/**
 * Un essai pour résoudre le jour 2 du AoC 2017.
 */

import java.nio.file.*;
import java.io.*;
import java.util.*;

public class d02 {
    public static void main(String[] args) {
        List<String> lines = new ArrayList<>();
        try {
            lines = Files.readAllLines(Paths.get("02.txt"));
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("Part 1: " + solvePart1(lines));
        System.out.println("Part 2: " + solvePart2(lines));
    }

    private static int solvePart1(List<String> lines) {
        int sum = 0;
        for (String line : lines) {
            String[] parts = line.split("\\s+");
            int min = Integer.MAX_VALUE;
            int max = Integer.MIN_VALUE;
            for (String part : parts) {
                int number = Integer.parseInt(part);
                min = Math.min(min, number);
                max = Math.max(max, number);
            }
            sum += max - min;
        }
        return sum;
    }

    private static int solvePart2(List<String> lines) {
        int sum = 0;
        for (String line : lines) {
            String[] parts = line.split("\\s+");
            for (int i = 0; i < parts.length; i++) {
                for (int j = i + 1; j < parts.length; j++) {
                    int a = Integer.parseInt(parts[i]);
                    int b = Integer.parseInt(parts[j]);
                    if (a % b == 0) {
                        sum += a / b;
                    } else if (b % a == 0) {
                        sum += b / a;
                    }
                }
            }
        }
        return sum;
    }
}