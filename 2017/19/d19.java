/**
 * Un essai pour résoudre le jour 19 du AoC 2017.
 */

import java.util.*;
import java.io.*;
import java.nio.file.*;

public class d19 {
    public static void main(String[] args) {
        try{
            List<String> diagram = Files.readAllLines(Paths.get("19.txt"));
            int x = 0, y = 0, dx = 0, dy = 1;
            for (int i = 0; i < diagram.get(0).length(); i++) {
                if (diagram.get(0).charAt(i) == '|') {
                    x = i;
                    break;
                }
            }

            StringBuilder letters = new StringBuilder();
            int steps = 0;
            while (true) {
                steps++;
                x += dx;
                y += dy;
                if (y < 0 || y >= diagram.size() || x < 0 || x >= diagram.get(y).length() || diagram.get(y).charAt(x) == ' ') {
                    break;
                }
                char c = diagram.get(y).charAt(x);
                if (Character.isAlphabetic(c)) {
                    letters.append(c);
                } else if (c == '+') {
                    if (dx == 0) {
                        dx = dy;
                        dy = 0;
                        if (x + dx < 0 || x + dx >= diagram.get(y).length() || diagram.get(y).charAt(x + dx) == ' ') {
                            dx = -dx;
                        }
                    } else {
                        dy = dx;
                        dx = 0;
                        if (y + dy < 0 || y + dy >= diagram.size() || x >= diagram.get(y + dy).length() || diagram.get(y + dy).charAt(x) == ' ') {
                            dy = -dy;
                        }
                    }
                }
            }

            System.out.println("Part 1: " + letters.toString());
            System.out.println("Part 2: " + steps);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}