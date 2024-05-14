/**
 * Un essai pour résoudre le jour 4 du défi de l'Avent de Code 2019
 */
public class d04 {
    public static void main(String[] args) {
        int start = 197487; // Remplacez par votre valeur de départ
        int end = 673251; // Remplacez par votre valeur de fin

        int countPart1 = 0;
        int countPart2 = 0;

        for (int i = start; i <= end; i++) {
            if (isValidPart1(i)) {
                countPart1++;
                if (isValidPart2(i)) {
                    countPart2++;
                }
            }
        }

        System.out.println("Part 1: " + countPart1);
        System.out.println("Part 2: " + countPart2);
    }

    static boolean isValidPart1(int password) {
        char[] digits = Integer.toString(password).toCharArray();
        boolean hasDouble = false;

        for (int i = 0; i < digits.length - 1; i++) {
            if (digits[i] > digits[i + 1]) {
                return false;
            }
            if (digits[i] == digits[i + 1]) {
                hasDouble = true;
            }
        }

        return hasDouble;
    }

    static boolean isValidPart2(int password) {
        char[] digits = Integer.toString(password).toCharArray();
        int[] counts = new int[10];

        for (int i = 0; i < digits.length; i++) {
            counts[digits[i] - '0']++;
        }

        for (int count : counts) {
            if (count == 2) {
                return true;
            }
        }

        return false;
    }
}