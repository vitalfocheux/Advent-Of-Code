/**
 * Un essai pour résoudre le jour 5 de l'Avent de Code 2016.
 */

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;
import java.math.BigInteger;

public class d05 {
    public static void main(String[] args) throws NoSuchAlgorithmException {
        String input = "abbhdwsy";
        MessageDigest md = MessageDigest.getInstance("MD5");
        char[] password1 = new char[8];
        char[] password2 = new char[8];
        Arrays.fill(password2, ' ');
        int count1 = 0, count2 = 0;

        for (int i = 0; count1 < 8 || count2 < 8; i++) {
            String s = input + i;
            md.update(s.getBytes());
            byte[] digest = md.digest();
            String hash = String.format("%032x", new BigInteger(1, digest));

            if (hash.startsWith("00000")) {
                if (count1 < 8) {
                    password1[count1++] = hash.charAt(5);
                }
                if (Character.isDigit(hash.charAt(5))) {
                    int pos = Character.getNumericValue(hash.charAt(5));
                    if (pos < 8 && password2[pos] == ' ') {
                        password2[pos] = hash.charAt(6);
                        count2++;
                    }
                }
            }
            md.reset();
        }

        System.out.println("Part 1: " + new String(password1));
        System.out.println("Part 2: " + new String(password2));
    }
}