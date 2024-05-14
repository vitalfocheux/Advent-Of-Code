/**
 * Un essai pour résoudre le jour 6 du AoC 2016
 */

import java.nio.file.*;
import java.io.IOException;
import java.util.*;

public class d06 {
    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get("06.txt"));
        int length = lines.get(0).length();
        Map<Character, Integer>[] frequency = new Map[length];
        for (int i = 0; i < length; i++) {
            frequency[i] = new HashMap<>();
        }

        for (String line : lines) {
            for (int i = 0; i < length; i++) {
                frequency[i].put(line.charAt(i), frequency[i].getOrDefault(line.charAt(i), 0) + 1);
            }
        }

        StringBuilder message1 = new StringBuilder();
        StringBuilder message2 = new StringBuilder();
        for (int i = 0; i < length; i++) {
            char char1 = Collections.max(frequency[i].entrySet(), Map.Entry.comparingByValue()).getKey();
            char char2 = Collections.min(frequency[i].entrySet(), Map.Entry.comparingByValue()).getKey();
            message1.append(char1);
            message2.append(char2);
        }

        System.out.println("Part 1: " + message1);
        System.out.println("Part 2: " + message2);
    }
}