/**
 * Un essai pour résoudre le jour 14 du défi 2023.
 */

import java.nio.file.*;
import java.util.*;

public class d14 {
    public static void main(String[] args) throws Exception {
        List<String> lines = Files.readAllLines(Paths.get("14.txt"));
        char[][] platform = new char[lines.size()][];
        for (int i = 0; i < lines.size(); i++) {
            platform[i] = lines.get(i).toCharArray();
        }

        // Move all rounded rocks north
        for (int j = 0; j < platform[0].length; j++) {
            int i = 0;
            while (i < platform.length) {
                if (platform[i][j] == 'O') {
                    int k = i - 1;
                    while (k >= 0 && platform[k][j] == '.') {
                        platform[k][j] = 'O';
                        platform[k + 1][j] = '.';
                        k--;
                    }
                }
                i++;
            }
        }

        // Calculate total load
        int totalLoad = 0;
        for (int i = 0; i < platform.length; i++) {
            for (int j = 0; j < platform[i].length; j++) {
                if (platform[i][j] == 'O') {
                    totalLoad += platform.length - i;
                }
            }
        }

        System.out.println("Total load: " + totalLoad);

        lines = Files.readAllLines(Paths.get("14.txt"));
        platform = new char[lines.size()][];
        for (int i = 0; i < lines.size(); i++) {
            platform[i] = lines.get(i).toCharArray();
        }

        Map<String, Integer> memo = new HashMap<>();
        totalLoad = 0;
        for (int cycle = 0; cycle < 1000000000; cycle++) {
            String state = Arrays.deepToString(platform);
            if (memo.containsKey(state)) {
                totalLoad = memo.get(state);
                break;
            }

            // Move all rounded rocks in four directions
            for (int direction = 0; direction < 4; direction++) {
                for (int j = 0; j < platform[0].length; j++) {
                    int i = direction % 2 == 0 ? 0 : platform.length - 1;
                    while (i >= 0 && i < platform.length) {
                        if (platform[i][j] == 'O') {
                            int k = i + (direction % 2 == 0 ? -1 : 1);
                            while (k >= 0 && k < platform.length && platform[k][j] == '.') {
                                platform[k][j] = 'O';
                                platform[k + (direction % 2 == 0 ? 1 : -1)][j] = '.';
                                k += direction % 2 == 0 ? -1 : 1;
                            }
                        }
                        i += direction % 2 == 0 ? 1 : -1;
                    }
                }
                // Rotate the platform 90 degrees clockwise
                platform = rotatePlatform(platform);
            }

            // Calculate total load
            totalLoad = 0;
            for (int i = 0; i < platform.length; i++) {
                for (int j = 0; j < platform[i].length; j++) {
                    if (platform[i][j] == 'O') {
                        totalLoad += platform.length - i;
                    }
                }
            }

            memo.put(state, totalLoad);
        }

        System.out.println("Total load: " + totalLoad);

    }

    private static char[][] rotatePlatform(char[][] platform) {
        int n = platform.length;
        int m = platform[0].length;
        char[][] rotated = new char[m][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                rotated[j][n - i - 1] = platform[i][j];
            }
        }
        return rotated;
    }
}