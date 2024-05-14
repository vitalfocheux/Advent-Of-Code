/**
 * Un essai pour résoudre le jour 3 du AoC 2020
 */

import java.util.*;
import java.nio.file.*;
import java.io.IOException;

public class d03 {
    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("03.txt"));
            int[][] slopes = {{1, 1}, {3, 1}, {5, 1}, {7, 1}, {1, 2}};
            long result = 1;

            for (int[] slope : slopes) {
                int x = 0, y = 0, trees = 0;
                while (y < lines.size()) {
                    if (lines.get(y).charAt(x) == '#') {
                        trees++;
                    }
                    x = (x + slope[0]) % lines.get(0).length();
                    y += slope[1];
                }
                if(slope[0] == 3 && slope[1] == 1) {
                    System.out.println("Part 1: " + trees);
                }
                result *= trees;
            }

            System.out.println("Result: " + result);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}