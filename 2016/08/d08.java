/**
 * Un essai pour résoudre le jour 8 du AoC 2016
 */

import java.nio.file.*;
import java.io.IOException;
import java.util.*;

public class d08 {
    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get("08.txt"));
        char[][] screen = new char[6][50];
        for (char[] row : screen) {
            Arrays.fill(row, '.');
        }

        for (String line : lines) {
            String[] parts = line.split(" ");
            if (parts[0].equals("rect")) {
                int x = Integer.parseInt(parts[1].split("x")[0]);
                int y = Integer.parseInt(parts[1].split("x")[1]);
                for (int i = 0; i < y; i++) {
                    for (int j = 0; j < x; j++) {
                        screen[i][j] = '#';
                    }
                }
            } else {
                int index = Integer.parseInt(parts[2].split("=")[1]);
                int shift = Integer.parseInt(parts[4]);
                if (parts[1].equals("row")) {
                    char[] newRow = new char[50];
                    for (int i = 0; i < 50; i++) {
                        newRow[(i + shift) % 50] = screen[index][i];
                    }
                    screen[index] = newRow;
                } else {
                    char[] newColumn = new char[6];
                    for (int i = 0; i < 6; i++) {
                        newColumn[(i + shift) % 6] = screen[i][index];
                    }
                    for (int i = 0; i < 6; i++) {
                        screen[i][index] = newColumn[i];
                    }
                }
            }
        }

        int count = 0;
        for (char[] row : screen) {
            for (char c : row) {
                if (c == '#') {
                    count++;
                }
            }
        }
        System.out.println("Part 1: " + count);

        System.out.println("Part 2: ");
        for (char[] row : screen) {
            System.out.println(row);
        }
    }
}