/**
 * Un essai pour résoudre le jour 2 du défi de l'Avent 2020.
 */

import java.util.*;
import java.nio.file.*;
import java.io.IOException;

public class d02 {
    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("02.txt"));
            int validPasswordsPart1 = 0;
            int validPasswordsPart2 = 0;

            for (String line : lines) {
                String[] parts = line.split(" ");
                String[] range = parts[0].split("-");
                char letter = parts[1].charAt(0);
                String password = parts[2];

                // Part 1: Count how many passwords are valid according to their policy
                long count = password.chars().filter(ch -> ch == letter).count();
                if (count >= Integer.parseInt(range[0]) && count <= Integer.parseInt(range[1])) {
                    validPasswordsPart1++;
                }

                // Part 2: The policy indicates two positions in the password, where at least one must contain the given letter
                if (password.charAt(Integer.parseInt(range[0]) - 1) == letter ^ password.charAt(Integer.parseInt(range[1]) - 1) == letter) {
                    validPasswordsPart2++;
                }
            }

            System.out.println("Part 1: " + validPasswordsPart1);
            System.out.println("Part 2: " + validPasswordsPart2);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}