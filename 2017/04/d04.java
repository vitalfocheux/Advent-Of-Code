/**
 * Un essai pour résoudre le jour 4 du défi de l'Avent 2017.
 */

import java.nio.file.*;
import java.io.*;
import java.util.*;

public class d04 {
    public static void main(String[] args) {
        List<String> lines = new ArrayList<>();
        try {
            lines = Files.readAllLines(Paths.get("04.txt"));
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("Part 1: " + solvePart1(lines));
        System.out.println("Part 2: " + solvePart2(lines));
    }

    private static int solvePart1(List<String> lines) {
        int validPhrases = 0;
        for (String line : lines) {
            Set<String> words = new HashSet<>(Arrays.asList(line.split("\\s+")));
            if (words.size() == line.split("\\s+").length) {
                validPhrases++;
            }
        }
        return validPhrases;
    }

    private static int solvePart2(List<String> lines) {
        int validPhrases = 0;
        for (String line : lines) {
            String[] words = line.split("\\s+");
            for (int i = 0; i < words.length; i++) {
                char[] chars = words[i].toCharArray();
                Arrays.sort(chars);
                words[i] = new String(chars);
            }
            Set<String> uniqueWords = new HashSet<>(Arrays.asList(words));
            if (uniqueWords.size() == words.length) {
                validPhrases++;
            }
        }
        return validPhrases;
    }
}