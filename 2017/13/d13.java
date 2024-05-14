/**
 * Un essai pour résoudre le jour 13 de l'Avent de Code 2017.
 */

import java.nio.file.*;
import java.io.*;
import java.util.*;

public class d13 {
    public static void main(String[] args) {
        Map<Integer, Integer> firewall = new HashMap<>();
        try {
            for (String line : Files.readAllLines(Paths.get("13.txt"))) {
                String[] parts = line.split(": ");
                int depth = Integer.parseInt(parts[0]);
                int range = Integer.parseInt(parts[1]);
                firewall.put(depth, range);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        int severity = 0;
        for (int depth : firewall.keySet()) {
            if (depth % ((firewall.get(depth) - 1) * 2) == 0) {
                severity += depth * firewall.get(depth);
            }
        }
        System.out.println("Part 1: " + severity);

        int delay = 0;
        while (true) {
            boolean caught = false;
            for (int depth : firewall.keySet()) {
                if ((depth + delay) % ((firewall.get(depth) - 1) * 2) == 0) {
                    caught = true;
                    break;
                }
            }
            if (!caught) {
                break;
            }
            delay++;
        }
        System.out.println("Part 2: " + delay);
    }
}