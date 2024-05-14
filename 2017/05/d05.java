/**
 * Un essai pour résoudre le jour 5 du défi de l'Avent 2017.
 */

import java.nio.file.*;
import java.io.*;
import java.util.*;

public class d05 {
    public static void main(String[] args) {
        List<Integer> jumps = new ArrayList<>();
        try {
            for (String line : Files.readAllLines(Paths.get("05.txt"))) {
                jumps.add(Integer.parseInt(line));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("Part 1: " + solvePart1(new ArrayList<>(jumps)));
        System.out.println("Part 2: " + solvePart2(new ArrayList<>(jumps)));
    }

    private static int solvePart1(List<Integer> jumps) {
        int steps = 0;
        int i = 0;
        while (i >= 0 && i < jumps.size()) {
            int jump = jumps.get(i);
            jumps.set(i, jump + 1);
            i += jump;
            steps++;
        }
        return steps;
    }

    private static int solvePart2(List<Integer> jumps) {
        int steps = 0;
        int i = 0;
        while (i >= 0 && i < jumps.size()) {
            int jump = jumps.get(i);
            if (jump >= 3) {
                jumps.set(i, jump - 1);
            } else {
                jumps.set(i, jump + 1);
            }
            i += jump;
            steps++;
        }
        return steps;
    }
}