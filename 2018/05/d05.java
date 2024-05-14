/**
 * Un essai pour résoudre le jour 5 du défi de l'Avent 2018.
 */

import java.nio.file.*;
import java.io.*;
import java.util.*;

public class d05 {
    public static void main(String[] args) {
        try {
            String polymer = Files.readString(Paths.get("05.txt")).trim();

            // Part 1
            String reducedPolymer = reduce(polymer);
            System.out.println("Part 1: " + reducedPolymer.length());

            // Part 2
            int shortestLength = polymer.length();
            for (char c = 'A'; c <= 'Z'; c++) {
                String removedPolymer = polymer.replaceAll("[" + c + Character.toLowerCase(c) + "]", "");
                String reducedRemovedPolymer = reduce(removedPolymer);
                shortestLength = Math.min(shortestLength, reducedRemovedPolymer.length());
            }
            System.out.println("Part 2: " + shortestLength);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static String reduce(String polymer) {
        StringBuilder sb = new StringBuilder(polymer);
        for (int i = 0; i < sb.length() - 1; i++) {
            if (Math.abs(sb.charAt(i) - sb.charAt(i + 1)) == 32) {
                sb.delete(i, i + 2);
                i = Math.max(i - 2, -1);
            }
        }
        return sb.toString();
    }
}