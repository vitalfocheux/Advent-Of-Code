/**
 * Un essai pour résoudre le jour 22 du AoC 2017.
 */

import java.nio.file.*;
import java.io.*;
import java.util.*;

public class d22 {
    static Map<String, Character> grid = new HashMap<>();
    static int direction = 0; // 0: up, 1: right, 2: down, 3: left
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {-1, 0, 1, 0};
    static int x = 0, y = 0;
    static int infections = 0;

    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("22.txt"));
            for (int i = 0; i < lines.size(); i++) {
                for (int j = 0; j < lines.get(i).length(); j++) {
                    grid.put(j + "," + i, lines.get(i).charAt(j));
                }
            }
            x = lines.get(0).length() / 2;
            y = lines.size() / 2;

            // Part 1
            for (int i = 0; i < 10000; i++) {
                burst1();
            }
            System.out.println("Part 1: " + infections);

            // Reset for part 2
            direction = 0;
            x = lines.get(0).length() / 2;
            y = lines.size() / 2;
            infections = 0;

            // Part 2
            for (int i = 0; i < 10000000; i++) {
                burst2();
            }
            System.out.println("Part 2: " + infections);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static void burst1() {
        if (grid.getOrDefault(x + "," + y, '.') == '#') {
            direction = (direction + 1) % 4;
            grid.put(x + "," + y, '.');
        } else {
            direction = (direction + 3) % 4;
            grid.put(x + "," + y, '#');
            infections++;
        }
        x += dx[direction];
        y += dy[direction];
    }

    static void burst2() {
        switch (grid.getOrDefault(x + "," + y, '.')) {
            case '#':
                direction = (direction + 1) % 4;
                grid.put(x + "," + y, 'F');
                break;
            case '.':
                direction = (direction + 3) % 4;
                grid.put(x + "," + y, 'W');
                break;
            case 'W':
                grid.put(x + "," + y, '#');
                infections++;
                break;
            case 'F':
                direction = (direction + 2) % 4;
                grid.put(x + "," + y, '.');
                break;
        }
        x += dx[direction];
        y += dy[direction];
    }
}