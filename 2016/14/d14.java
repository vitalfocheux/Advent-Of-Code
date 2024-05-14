/**
 * Un essai pour résoudre le jour 14 du AoC 2016.
 */

import java.security.*;
import java.util.*;

public class d14 {
    private static final String INPUT = "ngcjuoqr";

    public static void main(String[] args) throws NoSuchAlgorithmException {
        System.out.println("Part 1: " + find64thKey(INPUT, 1));
        System.out.println("Part 2: " + find64thKey(INPUT, 2017));
    }

    private static int find64thKey(String input, int iterations) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("MD5");
        List<String> keys = new ArrayList<>();
        int index = 0;

        while (keys.size() < 64) {
            String hash = getHash(input + index, md, iterations);
            String triplet = containsTriplet(hash);
            if (triplet != null) {
                for (int i = 1; i <= 1000; i++) {
                    String futureHash = getHash(input + (index + i), md, iterations);
                    if (futureHash.contains(triplet)) {
                        keys.add(hash);
                        break;
                    }
                }
            }
            index++;
        }

        return index - 1;
    }

    private static String getHash(String input, MessageDigest md, int iterations) {
        byte[] bytes = input.getBytes();
        for (int i = 0; i < iterations; i++) {
            bytes = md.digest(bytes);
            input = toHexString(bytes);
        }
        return input;
    }

    private static String toHexString(byte[] bytes) {
        StringBuilder sb = new StringBuilder();
        for (byte b : bytes) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }

    private static String containsTriplet(String hash) {
        for (int i = 0; i < hash.length() - 2; i++) {
            if (hash.charAt(i) == hash.charAt(i + 1) && hash.charAt(i) == hash.charAt(i + 2)) {
                return String.valueOf(hash.charAt(i)).repeat(5);
            }
        }
        return null;
    }
}