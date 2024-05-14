/**
 * Un essai pour résoudre le jour 12 du AoC 2016.
 */

import java.nio.file.*;
import java.io.IOException;
import java.util.*;

public class d12 {
    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get("12.txt"));
        System.out.println("Part 1: " + run(lines, new int[4]));
        System.out.println("Part 2: " + run(lines, new int[]{0, 0, 1, 0}));
    }

    private static int run(List<String> lines, int[] registers) {
        int i = 0;
        while (i < lines.size()) {
            String[] parts = lines.get(i).split(" ");
            switch (parts[0]) {
                case "cpy":
                    int value = isNumeric(parts[1]) ? Integer.parseInt(parts[1]) : registers[parts[1].charAt(0) - 'a'];
                    registers[parts[2].charAt(0) - 'a'] = value;
                    break;
                case "inc":
                    registers[parts[1].charAt(0) - 'a']++;
                    break;
                case "dec":
                    registers[parts[1].charAt(0) - 'a']--;
                    break;
                case "jnz":
                    value = isNumeric(parts[1]) ? Integer.parseInt(parts[1]) : registers[parts[1].charAt(0) - 'a'];
                    if (value != 0) {
                        i += Integer.parseInt(parts[2]) - 1;
                    }
                    break;
            }
            i++;
        }
        return registers[0];
    }

    private static boolean isNumeric(String str) {
        return str.matches("-?\\d+");
    }
}