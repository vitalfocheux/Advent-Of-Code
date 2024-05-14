/**
 * Un essai pour résoudre le jour 2 du AoC 2016.
 */

import java.nio.file.*;
import java.io.IOException;
import java.util.*;

public class d02 {
    private static final int[][] DIRECTIONS = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    private static final String DIRECTION_CHARS = "UDLR";
    private static final String[] KEYPAD1 = {
        "123",
        "456",
        "789"
    };
    private static final String[] KEYPAD2 = {
        "  1  ",
        " 234 ",
        "56789",
        " ABC ",
        "  D  "
    };

    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get("02.txt"));
        System.out.println("Part 1: " + getCode(lines, KEYPAD1, 1, 1));
        System.out.println("Part 2: " + getCode(lines, KEYPAD2, 0, 2));
    }

    private static String getCode(List<String> lines, String[] keypad, int x, int y) {
        StringBuilder code = new StringBuilder();
        for (String line : lines) {
            for (char c : line.toCharArray()) {
                int dir = DIRECTION_CHARS.indexOf(c);
                int nx = x + DIRECTIONS[dir][0];
                int ny = y + DIRECTIONS[dir][1];
                if (nx >= 0 && nx < keypad.length && ny >= 0 && ny < keypad[nx].length() && keypad[nx].charAt(ny) != ' ') {
                    x = nx;
                    y = ny;
                }
            }
            code.append(keypad[x].charAt(y));
        }
        return code.toString();
    }
}