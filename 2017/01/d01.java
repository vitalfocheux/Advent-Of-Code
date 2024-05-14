/**
 * Un essai pour résoudre le jour 1 de l'année 2017
 */

import java.nio.file.*;
import java.io.*;

public class d01 {
    public static void main(String[] args) {
        String input = "";
        try {
            input = new String(Files.readAllBytes(Paths.get("01.txt"))).trim();
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("Part 1: " + solvePart1(input));
        System.out.println("Part 2: " + solvePart2(input));
    }

    private static int solvePart1(String input) {
        int sum = 0;
        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) == input.charAt((i + 1) % input.length())) {
                sum += Character.getNumericValue(input.charAt(i));
            }
        }
        return sum;
    }

    private static int solvePart2(String input) {
        int sum = 0;
        int step = input.length() / 2;
        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) == input.charAt((i + step) % input.length())) {
                sum += Character.getNumericValue(input.charAt(i));
            }
        }
        return sum;
    }
}