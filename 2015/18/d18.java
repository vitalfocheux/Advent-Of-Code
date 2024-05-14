/**
 * Un essai pour résoudre le jour 18 de l'Avent de Code 2015.
 */

import java.util.*;
import java.io.*;

public class d18 {
    public static void main(String[] args) throws IOException {
        char[][] grid = new char[100][100];
        Scanner scanner = new Scanner(new File("18.txt"));
        for (int i = 0; i < 100; i++) {
            grid[i] = scanner.nextLine().toCharArray();
        }
        scanner.close();

        for (int i = 0; i < 100; i++) {
            grid = nextStep(grid, false);
        }
        System.out.println("Part 1: " + countLights(grid));

        // Reset grid for part 2
        scanner = new Scanner(new File("18.txt"));
        for (int i = 0; i < 100; i++) {
            grid[i] = scanner.nextLine().toCharArray();
        }
        scanner.close();

        for (int i = 0; i < 100; i++) {
            grid = nextStep(grid, true);
        }
        System.out.println("Part 2: " + countLights(grid));
    }

    static char[][] nextStep(char[][] grid, boolean cornersStuck) {
        char[][] newGrid = new char[100][100];
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                int on = countOnNeighbors(grid, i, j);
                if (grid[i][j] == '#' && (on == 2 || on == 3)) {
                    newGrid[i][j] = '#';
                } else if (grid[i][j] == '.' && on == 3) {
                    newGrid[i][j] = '#';
                } else {
                    newGrid[i][j] = '.';
                }
            }
        }
        if (cornersStuck) {
            newGrid[0][0] = '#';
            newGrid[0][99] = '#';
            newGrid[99][0] = '#';
            newGrid[99][99] = '#';
        }
        return newGrid;
    }

    static int countOnNeighbors(char[][] grid, int x, int y) {
        int on = 0;
        for (int i = Math.max(0, x - 1); i <= Math.min(99, x + 1); i++) {
            for (int j = Math.max(0, y - 1); j <= Math.min(99, y + 1); j++) {
                if ((i != x || j != y) && grid[i][j] == '#') {
                    on++;
                }
            }
        }
        return on;
    }

    static int countLights(char[][] grid) {
        int on = 0;
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                if (grid[i][j] == '#') {
                    on++;
                }
            }
        }
        return on;
    }
}