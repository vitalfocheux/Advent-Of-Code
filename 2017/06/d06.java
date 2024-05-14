/**
 * Un essai pour résoudre le jour 6 du AoC 2017.
 */

import java.nio.file.*;
import java.io.*;
import java.util.*;

public class d06 {
    public static void main(String[] args) {
        List<Integer> banks = new ArrayList<>();
        try {
            for (String line : Files.readAllLines(Paths.get("06.txt"))) {
                for (String num : line.split("\\s+")) {
                    banks.add(Integer.parseInt(num));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("Part 1: " + solvePart1(new ArrayList<>(banks)));
        System.out.println("Part 2: " + solvePart2(new ArrayList<>(banks)));
    }

    private static int solvePart1(List<Integer> banks) {
        Set<String> seen = new HashSet<>();
        while (seen.add(banks.toString())) {
            redistribute(banks);
        }
        return seen.size();
    }

    private static int solvePart2(List<Integer> banks) {
        Map<String, Integer> seen = new HashMap<>();
        while (!seen.containsKey(banks.toString())) {
            seen.put(banks.toString(), seen.size());
            redistribute(banks);
        }
        return seen.size() - seen.get(banks.toString());
    }

    private static void redistribute(List<Integer> banks) {
        int maxIndex = 0;
        for (int i = 1; i < banks.size(); i++) {
            if (banks.get(i) > banks.get(maxIndex)) {
                maxIndex = i;
            }
        }
        int blocks = banks.get(maxIndex);
        banks.set(maxIndex, 0);
        for (int i = 0; i < blocks; i++) {
            banks.set((maxIndex + 1 + i) % banks.size(), banks.get((maxIndex + 1 + i) % banks.size()) + 1);
        }
    }
}