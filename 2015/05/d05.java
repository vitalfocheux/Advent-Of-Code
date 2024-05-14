/**
 * Un essai pour résoudre le jour 5 du défi de l'Avent de 2015.
 */

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Pattern;

public class d05 {
    public static void main(String[] args) {
        String inputFilePath = "05.txt";
        try {
            BufferedReader reader = new BufferedReader(new FileReader(inputFilePath));
            String line;
            int countPart1 = 0;
            int countPart2 = 0;
            while ((line = reader.readLine()) != null) {
                if (isValidPart1(line)) {
                    countPart1++;
                }
                if (isValidPart2(line)) {
                    countPart2++;
                }
            }
            System.out.println("Part 1: " + countPart1);
            System.out.println("Part 2: " + countPart2);
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static boolean isValidPart1(String s) {
        String vowels = "aeiou";
        String[] forbidden = {"ab", "cd", "pq", "xy"};
        if (s.chars().filter(ch -> vowels.indexOf(ch) >= 0).count() < 3) {
            return false;
        }
        if (!Pattern.compile("(.)\\1").matcher(s).find()) {
            return false;
        }
        for (String f : forbidden) {
            if (s.contains(f)) {
                return false;
            }
        }
        return true;
    }

    private static boolean isValidPart2(String s) {
        if (!Pattern.compile("(..).*\\1").matcher(s).find()) {
            return false;
        }
        if (!Pattern.compile("(.).\\1").matcher(s).find()) {
            return false;
        }
        return true;
    }
}