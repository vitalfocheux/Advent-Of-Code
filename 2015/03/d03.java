/**
 * Un essai pour résoudre le jour 3 du défi 2015
 */

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashSet;
import java.util.Set;

public class d03 {
    public static void main(String[] args) {
        String inputFilePath = "03.txt";
        try {
            BufferedReader reader = new BufferedReader(new FileReader(inputFilePath));
            String line = reader.readLine();
            if (line != null) {
                System.out.println("Part 1: " + part1(line));
                System.out.println("Part 2: " + part2(line));
            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static int part1(String instructions) {
        Set<String> houses = new HashSet<>();
        int x = 0, y = 0;
        houses.add(x + "," + y);
        for (char instruction : instructions.toCharArray()) {
            if (instruction == '^') y++;
            else if (instruction == 'v') y--;
            else if (instruction == '>') x++;
            else if (instruction == '<') x--;
            houses.add(x + "," + y);
        }
        return houses.size();
    }

    private static int part2(String instructions) {
        Set<String> houses = new HashSet<>();
        int[] x = {0, 0}, y = {0, 0};
        houses.add(x[0] + "," + y[0]);
        for (int i = 0; i < instructions.length(); i++) {
            if (instructions.charAt(i) == '^') y[i % 2]++;
            else if (instructions.charAt(i) == 'v') y[i % 2]--;
            else if (instructions.charAt(i) == '>') x[i % 2]++;
            else if (instructions.charAt(i) == '<') x[i % 2]--;
            houses.add(x[i % 2] + "," + y[i % 2]);
        }
        return houses.size();
    }
}