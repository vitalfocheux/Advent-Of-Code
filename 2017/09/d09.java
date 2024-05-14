/**
 * Un essai pour résoudre le jour 9 du AoC 2017
 */

import java.nio.file.*;
import java.io.*;

public class d09 {
    public static void main(String[] args) {
        String input = "";
        try {
            input = new String(Files.readAllBytes(Paths.get("09.txt")));
        } catch (IOException e) {
            e.printStackTrace();
        }

        int totalScore = 0;
        int garbageCount = 0;
        int depth = 0;
        boolean garbage = false;
        boolean ignore = false;

        for (char c : input.toCharArray()) {
            if (ignore) {
                ignore = false;
            } else if (c == '!') {
                ignore = true;
            } else if (garbage) {
                if (c == '>') {
                    garbage = false;
                } else {
                    garbageCount++;
                }
            } else if (c == '<') {
                garbage = true;
            } else if (c == '{') {
                depth++;
                totalScore += depth;
            } else if (c == '}') {
                depth--;
            }
        }

        System.out.println("Part 1: " + totalScore);
        System.out.println("Part 2: " + garbageCount);
    }
}