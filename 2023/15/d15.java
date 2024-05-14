/**
 * Un essai pour la partie 1
 */

import java.nio.file.*;
import java.util.*;

public class d15 {
    public static void main(String[] args) throws Exception {
        String sequence = new String(Files.readAllBytes(Paths.get("15.txt"))).trim();
        String[] steps = sequence.split(",");

        int sum = 0;
        for (String step : steps) {
            sum += hash(step);
        }

        System.out.println("Sum of HASH results: " + sum);
    }

    private static int hash(String s) {
        int value = 0;
        for (char c : s.toCharArray()) {
            value += (int) c;
            value *= 17;
            value %= 256;
        }
        return value;
    }
}