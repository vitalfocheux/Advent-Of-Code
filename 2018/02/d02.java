import java.nio.file.*;
import java.io.*;
import java.util.*;

public class d02 {
    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("02.txt"));

            // Part 1
            int twoCount = 0;
            int threeCount = 0;
            for (String line : lines) {
                Map<Character, Integer> counts = new HashMap<>();
                for (char c : line.toCharArray()) {
                    counts.put(c, counts.getOrDefault(c, 0) + 1);
                }
                if (counts.values().contains(2)) twoCount++;
                if (counts.values().contains(3)) threeCount++;
            }
            System.out.println("Part 1: " + twoCount * threeCount);

            // Part 2
            for (int i = 0; i < lines.size(); i++) {
                for (int j = i + 1; j < lines.size(); j++) {
                    String common = commonChars(lines.get(i), lines.get(j));
                    if (common.length() == lines.get(i).length() - 1) {
                        System.out.println("Part 2: " + common);
                        return;
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static String commonChars(String a, String b) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) == b.charAt(i)) {
                sb.append(a.charAt(i));
            }
        }
        return sb.toString();
    }
}