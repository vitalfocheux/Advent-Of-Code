/**
 * Un essai pour la partie 1
 * Deux essais pour la partie 2
 */

import java.nio.file.*;
import java.util.*;
import java.io.*;

public class d24 {
    static List<int[]> components = new ArrayList<>();
    static int maxStrength = 0;
    static int maxLength = 0;
    static int maxStrengthOfMaxLength = 0;

    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("24.txt"));
            for (String line : lines) {
                String[] parts = line.split("/");
                components.add(new int[]{Integer.parseInt(parts[0]), Integer.parseInt(parts[1])});
            }

            buildBridge(0, 0, 0, new boolean[components.size()]);

            System.out.println("Part 1: " + maxStrength);
            System.out.println("Part 2: " + maxStrengthOfMaxLength);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static void buildBridge(int strength, int length, int port, boolean[] used) {
        if (length > maxLength) {
            maxLength = length;
            maxStrengthOfMaxLength = strength;
        } else if (length == maxLength) {
            maxStrengthOfMaxLength = Math.max(maxStrengthOfMaxLength, strength);
        }
        maxStrength = Math.max(maxStrength, strength);

        for (int i = 0; i < components.size(); i++) {
            if (used[i]) continue;
            int[] component = components.get(i);
            if (component[0] == port || component[1] == port) {
                used[i] = true;
                buildBridge(strength + component[0] + component[1], length + 1, component[0] == port ? component[1] : component[0], used);
                used[i] = false;
            }
        }
    }
}