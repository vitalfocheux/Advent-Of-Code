/**
 * Un essai pour la partie 1
 * La partie 2 n'est pas optimisé
 */

import java.nio.file.*;
import java.util.*;
import java.io.IOException;
import java.util.stream.IntStream;

public class d16 {
    public static void main(String[] args) {
        try {
            String input = new String(Files.readAllBytes(Paths.get("16.txt"))).trim();

            // Part 1
            String result = fft(input, 100);
            System.out.println("Part 1: " + result.substring(0, 8));

            // Part 2
            String longInput = String.join("", Collections.nCopies(10000, input));
            int offset = Integer.parseInt(longInput.substring(0, 7));
            result = fft(longInput, 100);
            System.out.println("Part 2: " + result.substring(offset, offset + 8));

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static String fft(String input, int phases) {
        int[] digits = input.chars().map(c -> c - '0').toArray();
        int[] pattern = {0, 1, 0, -1};

        for (int phase = 0; phase < phases; phase++) {
            for (int i = 0; i < digits.length; i++) {
                final int index = i;
                digits[i] = Math.abs(IntStream.range(0, digits.length).map(j -> digits[j] * pattern[((j + 1) / (index + 1)) % pattern.length]).sum()) % 10;
            }
        }

        StringBuilder sb = new StringBuilder(digits.length);
        for (int digit : digits) {
            sb.append(digit);
        }
        return sb.toString();
    }
}