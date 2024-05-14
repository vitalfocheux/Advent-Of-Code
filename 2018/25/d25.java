/**
 * Un essai pour résoudre le jour 25 du AoC 2018.
 */

import java.nio.file.*;
import java.util.*;
import java.io.*;

public class d25 {
    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("25.txt"));
            List<int[]> points = new ArrayList<>();
            for (String line : lines) {
                points.add(Arrays.stream(line.split(",")).mapToInt(Integer::parseInt).toArray());
            }

            int[] constellation = new int[points.size()];
            int numConstellations = 0;
            for (int i = 0; i < points.size(); i++) {
                if (constellation[i] == 0) {
                    numConstellations++;
                    dfs(points, constellation, i, numConstellations);
                }
            }

            System.out.println("Number of constellations: " + numConstellations);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static void dfs(List<int[]> points, int[] constellation, int i, int numConstellations) {
        constellation[i] = numConstellations;
        for (int j = 0; j < points.size(); j++) {
            if (constellation[j] == 0 && distance(points.get(i), points.get(j)) <= 3) {
                dfs(points, constellation, j, numConstellations);
            }
        }
    }

    static int distance(int[] a, int[] b) {
        return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]) + Math.abs(a[2] - b[2]) + Math.abs(a[3] - b[3]);
    }
}