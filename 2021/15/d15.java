/**
 * Un essai pour la partie 1
 * La partie 2 ne fonctionne pas
 */

import java.util.*;
import java.nio.file.*;
import java.io.IOException;

public class d15 {
    private static final int INF = Integer.MAX_VALUE;
    private static final int[][] DIRS = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("15.txt"));
            int n = lines.size();
            int[][] map = new int[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    map[i][j] = lines.get(i).charAt(j) - '0';
                }
            }
            int[][] dist = new int[n][n];
            for (int[] row : dist) {
                Arrays.fill(row, INF);
            }
            dist[0][0] = 0;
            PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> dist[a[0]][a[1]]));
            pq.offer(new int[]{0, 0});
            while (!pq.isEmpty()) {
                int[] curr = pq.poll();
                int i = curr[0], j = curr[1];
                for (int[] dir : DIRS) {
                    int ni = i + dir[0], nj = j + dir[1];
                    if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
                        int alt = dist[i][j] + map[ni][nj];
                        if (alt < dist[ni][nj]) {
                            dist[ni][nj] = alt;
                            pq.offer(new int[]{ni, nj});
                        }
                    }
                }
            }
            System.out.println("Lowest total risk: " + dist[n - 1][n - 1]);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}