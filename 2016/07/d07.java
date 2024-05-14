/**
 * Un essai pour résoudre le jour 7 du défi de l'Avent 2016.
 */

import java.nio.file.*;
import java.io.IOException;
import java.util.*;
import java.util.regex.*;

public class d07 {
    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get("07.txt"));
        int tlsCount = 0, sslCount = 0;
        for (String line : lines) {
            List<String> outside = new ArrayList<>(), inside = new ArrayList<>();
            Matcher m = Pattern.compile("(\\w+)\\[(\\w+)\\]").matcher(line);
            while (m.find()) {
                outside.add(m.group(1));
                inside.add(m.group(2));
            }
            outside.add(line.substring(line.lastIndexOf(']') + 1));
            if (supportsTLS(outside, inside)) {
                tlsCount++;
            }
            if (supportsSSL(outside, inside)) {
                sslCount++;
            }
        }
        System.out.println("Part 1: " + tlsCount);
        System.out.println("Part 2: " + sslCount);
    }

    private static boolean supportsTLS(List<String> outside, List<String> inside) {
        return outside.stream().anyMatch(d07::containsABBA) && inside.stream().noneMatch(d07::containsABBA);
    }

    private static boolean containsABBA(String s) {
        for (int i = 0; i < s.length() - 3; i++) {
            if (s.charAt(i) == s.charAt(i + 3) && s.charAt(i + 1) == s.charAt(i + 2) && s.charAt(i) != s.charAt(i + 1)) {
                return true;
            }
        }
        return false;
    }

    private static boolean supportsSSL(List<String> outside, List<String> inside) {
        return outside.stream().anyMatch(s -> containsABA(s, inside));
    }

    private static boolean containsABA(String s, List<String> inside) {
        for (int i = 0; i < s.length() - 2; i++) {
            if (s.charAt(i) == s.charAt(i + 2) && s.charAt(i) != s.charAt(i + 1)) {
                String aba = s.substring(i, i + 3);
                String bab = "" + aba.charAt(1) + aba.charAt(0) + aba.charAt(1);
                if (inside.stream().anyMatch(str -> str.contains(bab))) {
                    return true;
                }
            }
        }
        return false;
    }
}