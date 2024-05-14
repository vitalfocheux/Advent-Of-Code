/**
 * Un essai pour résoudre le jour 6 du défi de l'Avent 2022.
 */

import java.util.*;
import java.nio.file.*;
import java.io.IOException;

public class d06 {
    public static void main(String[] args) {
        try {
            String data = Files.readString(Paths.get("06.txt")).trim();
            System.out.println("First packet marker: " + findMarker(data, 4));
            System.out.println("First message marker: " + findMarker(data, 14));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static int findMarker(String data, int length) {
        for (int i = length - 1; i < data.length(); i++) {
            Set<Character> set = new HashSet<>();
            for (int j = i - length + 1; j <= i; j++) {
                set.add(data.charAt(j));
            }
            if (set.size() == length) {
                return i + 1;
            }
        }
        return -1;
    }
}