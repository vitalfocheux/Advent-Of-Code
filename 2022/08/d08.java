/**
 * La partie 1 ne fonctionne pas
 * Un essai pour la partie 2
 */

import java.util.*;
import java.nio.file.*;
import java.io.IOException;

public class d08 {
    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("08.txt"));
            int[][] map = new int[lines.size()][lines.get(0).length()];
            for (int i = 0; i < lines.size(); i++) {
                for (int j = 0; j < lines.get(i).length(); j++) {
                    map[i][j] = Character.getNumericValue(lines.get(i).charAt(j));
                }
            }
            int visibleTrees = 0;
            int maxScenicScore = 0;
            for (int i = 0; i < map.length; i++) {
                for (int j = 0; j < map[i].length; j++) {
                    if (isVisible(map, i, j)) {
                        visibleTrees++;
                    }
                    maxScenicScore = Math.max(maxScenicScore, getScenicScore(map, i, j));
                }
            }
            System.out.println("Visible trees: " + visibleTrees);
            System.out.println("Max scenic score: " + maxScenicScore);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static boolean isVisible(int[][] map, int i, int j) {
        int height = map[i][j];
        for (int k = j - 1; k >= 0; k--) {
            if (map[i][k] >= height) {
                return false;
            }
        }
        for (int k = j + 1; k < map[i].length; k++) {
            if (map[i][k] >= height) {
                return false;
            }
        }
        for (int k = i - 1; k >= 0; k--) {
            if (map[k][j] >= height) {
                return false;
            }
        }
        for (int k = i + 1; k < map.length; k++) {
            if (map[k][j] >= height) {
                return false;
            }
        }
        return true;
    }

    private static int getScenicScore(int[][] map, int i, int j) {
        int height = map[i][j];
        int up = 0, down = 0, left = 0, right = 0;
        for (int k = j - 1; k >= 0; k--) {
            left++;
            if (map[i][k] >= height) {
                break;
            }
        }
        for (int k = j + 1; k < map[i].length; k++) {
            right++;
            if (map[i][k] >= height) {
                break;
            }
        }
        for (int k = i - 1; k >= 0; k--) {
            up++;
            if (map[k][j] >= height) {
                break;
            }
        }
        for (int k = i + 1; k < map.length; k++) {
            down++;
            if (map[k][j] >= height) {
                break;
            }
        }
        return up * down * left * right;
    }
}