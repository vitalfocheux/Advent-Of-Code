/**
 * Deux essais pour la partie 1
 * Un essai pour la partie 2
 */

import java.util.*;
import java.nio.file.*;
import java.io.IOException;

public class d09 {
    private static final int[][] DIRECTIONS = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("09.txt"));
            int[][] heightmap = new int[lines.size()][lines.get(0).length()];
            for (int i = 0; i < lines.size(); i++) {
                for (int j = 0; j < lines.get(i).length(); j++) {
                    heightmap[i][j] = lines.get(i).charAt(j) - '0';
                }
            }
            int riskLevel = 0;
            for (int i = 0; i < heightmap.length; i++) {
                for (int j = 0; j < heightmap[i].length; j++) {
                    if (isLowPoint(heightmap, i, j)) {
                        riskLevel += heightmap[i][j] + 1;
                    }
                }
            }
            System.out.println("Risk level: " + riskLevel);

            List<Integer> basinSizes = new ArrayList<>();
            boolean[][] visited = new boolean[heightmap.length][heightmap[0].length];
            for (int i = 0; i < heightmap.length; i++) {
                for (int j = 0; j < heightmap[i].length; j++) {
                    if (isLowPoint(heightmap, i, j)) {
                        basinSizes.add(dfs(heightmap, visited, i, j));
                    }
                }
            }
            Collections.sort(basinSizes);
            int result = basinSizes.get(basinSizes.size() - 1) * basinSizes.get(basinSizes.size() - 2) * basinSizes.get(basinSizes.size() - 3);
            System.out.println("Result: " + result);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static boolean isLowPoint(int[][] heightmap, int i, int j) {
        for (int[] direction : DIRECTIONS) {
            int x = i + direction[0];
            int y = j + direction[1];
            if (x >= 0 && x < heightmap.length && y >= 0 && y < heightmap[0].length && heightmap[x][y] <= heightmap[i][j]) {
                return false;
            }
        }
        return true;
    }

    private static int dfs(int[][] heightmap, boolean[][] visited, int i, int j) {
        if (i < 0 || i >= heightmap.length || j < 0 || j >= heightmap[0].length || visited[i][j] || heightmap[i][j] == 9) {
            return 0;
        }
        visited[i][j] = true;
        int size = 1;
        for (int[] direction : DIRECTIONS) {
            size += dfs(heightmap, visited, i + direction[0], j + direction[1]);
        }
        return size;
    }
}