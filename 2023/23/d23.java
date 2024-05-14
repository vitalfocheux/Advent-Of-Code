/**
 * Un essai pour la partie 1
 */

import java.nio.file.*;
import java.util.*;

public class d23 {
    static int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    static char[] arrows = {'^', 'v', '<', '>'};

    public static void main(String[] args) throws Exception {
        List<String> lines = Files.readAllLines(Paths.get("23.txt"));
        char[][] map = new char[lines.size()][lines.get(0).length()];
        int startX = 0, startY = 0, endX = 0, endY = 0;

        for (int i = 0; i < lines.size(); i++) {
            for (int j = 0; j < lines.get(i).length(); j++) {
                map[i][j] = lines.get(i).charAt(j);
                if (map[i][j] == '.') {
                    if (i == 0) {
                        startX = i;
                        startY = j;
                    } else if (i == lines.size() - 1) {
                        endX = i;
                        endY = j;
                    }
                }
            }
        }

        boolean[][] visited = new boolean[lines.size()][lines.get(0).length()];
        int longestHike = dfs(map, visited, startX, startY, endX, endY, 0);

        System.out.println("Longest hike: " + --longestHike);
    }

    private static int dfs(char[][] map, boolean[][] visited, int x, int y, int endX, int endY, int steps) {
        if (x < 0 || x >= map.length || y < 0 || y >= map[0].length || visited[x][y] || map[x][y] == '#') {
            return steps;
        }

        visited[x][y] = true;
        int longestHike = steps;

        for (int i = 0; i < directions.length; i++) {
            int newX = x + directions[i][0], newY = y + directions[i][1];
            if (map[x][y] == arrows[i] || map[x][y] == '.') {
                longestHike = Math.max(longestHike, dfs(map, visited, newX, newY, endX, endY, steps + 1));
            }
        }

        visited[x][y] = false;
        return longestHike;
    }
}