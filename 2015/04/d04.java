/**
 * Un essai pour résoudre le jour 4 du défi de programmation de l'Avent de 2015.
 */

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class d04 {
    public static void main(String[] args) {
        String secretKey = "iwrupvqb";
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            int number = 1;
            boolean foundPart1 = false;
            while (true) {
                String input = secretKey + number;
                byte[] digest = md.digest(input.getBytes());
                String hash = toHexString(digest);
                if (!foundPart1 && hash.startsWith("00000")) {
                    System.out.println("Part 1: " + number);
                    foundPart1 = true;
                }
                if (hash.startsWith("000000")) {
                    System.out.println("Part 2: " + number);
                    break;
                }
                number++;
            }
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
    }

    private static String toHexString(byte[] bytes) {
        StringBuilder sb = new StringBuilder();
        for (byte b : bytes) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }
}