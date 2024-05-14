/**
 * Un essai pour résoudre le jour 24 de l'Avent de Code 2015.
 */

import java.util.*;
import java.io.*;
import java.nio.file.*;
import java.util.stream.*;

public class d24 {
    private static List<Integer> weights = new ArrayList<>();
    private static int targetWeight;

    public static void main(String[] args) throws IOException {
        weights = Files.lines(Paths.get("24.txt"))
                .map(Integer::parseInt)
                .collect(Collectors.toList());
        Collections.sort(weights, Collections.reverseOrder());

        // Part 1
        targetWeight = weights.stream().mapToInt(Integer::intValue).sum() / 3;
        long quantumEntanglement = findMinimumQE(3);
        System.out.println("Part 1: " + quantumEntanglement);

        // Part 2
        targetWeight = weights.stream().mapToInt(Integer::intValue).sum() / 4;
        quantumEntanglement = findMinimumQE(4);
        System.out.println("Part 2: " + quantumEntanglement);
    }

    private static long findMinimumQE(int groups) {
        for (int i = 1; i <= weights.size(); i++) {
            Set<Set<Integer>> combinations = findCombinations(weights, i, targetWeight);
            if (!combinations.isEmpty()) {
                return combinations.stream()
                        .mapToLong(combination -> combination.stream()
                                .mapToLong(Integer::longValue)
                                .reduce(1, (a, b) -> a * b))
                        .min().getAsLong();
            }
        }
        return -1;
    }

    private static Set<Set<Integer>> findCombinations(List<Integer> weights, int size, int targetWeight) {
        Set<Set<Integer>> combinations = new HashSet<>();
        findCombinations(weights, new LinkedHashSet<>(), combinations, size, targetWeight, 0);
        return combinations;
    }

    private static void findCombinations(List<Integer> weights, Set<Integer> current, Set<Set<Integer>> combinations, int size, int targetWeight, int start) {
        if (current.size() == size) {
            if (current.stream().mapToInt(Integer::intValue).sum() == targetWeight) {
                combinations.add(new HashSet<>(current));
            }
            return;
        }
        for (int i = start; i < weights.size(); i++) {
            current.add(weights.get(i));
            findCombinations(weights, current, combinations, size, targetWeight, i + 1);
            current.remove(weights.get(i));
        }
    }
}