/**
 * Un essai pour la partie 1
 * Deux essais pour la partie 2
 */

import java.util.*;

public class d03 {
    public static void main(String[] args) {
        int input = 277678; // Remplacez par votre entrée

        System.out.println("Part 1: " + solvePart1(input));
        System.out.println("Part 2: " + solvePart2(input));
    }

    private static int solvePart1(int input) {
        int ring = (int) Math.ceil((Math.sqrt(input) - 1) / 2);
        int maxRingValue = (2 * ring + 1) * (2 * ring + 1);
        int ringDist = maxRingValue - input;
        int sideDist = ringDist % (2 * ring);
        return ring + Math.abs(sideDist - ring);
    }

    private static int solvePart2(int input) {
        int[][] grid = new int[101][101];
        int x = 50, y = 50;
        int[][] dirs = {{0, 1}, {-1, 0}, {0, -1}, {1, 0}};
        int dir = 0, steps = 1;

        grid[x][y] = 1;

        while (true) {
            for (int i = 0; i < 2; i++) {
                for (int j = 0; j < steps; j++) {
                    x += dirs[dir][0];
                    y += dirs[dir][1];

                    int sum = 0;
                    for (int dx = -1; dx <= 1; dx++) {
                        for (int dy = -1; dy <= 1; dy++) {
                            sum += grid[x + dx][y + dy];
                        }
                    }

                    grid[x][y] = sum;

                    if (sum > input) {
                        return sum;
                    }
                }
                dir = (dir + 1) % 4;
            }
            steps++;
        }
    }

    private static int getAdjacentSum(int[] position, Map<String, Integer> values) {
        int sum = 0;
        for (int dx = -1; dx <= 1; dx++) {
            for (int dy = -1; dy <= 1; dy++) {
                String key = (position[0] + dx) + "," + (position[1] + dy);
                sum += values.getOrDefault(key, 0);
            }
        }
        return sum;
    }

    private static int[] turnLeft(int[] direction) {
        if (direction[0] == 0 && direction[1] == 1) {
            return new int[]{1, 0};
        } else if (direction[0] == 1 && direction[1] == 0) {
            return new int[]{0, -1};
        } else if (direction[0] == 0 && direction[1] == -1) {
            return new int[]{-1, 0};
        } else {
            return new int[]{0, 1};
        }
    }
}