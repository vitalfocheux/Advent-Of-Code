/**
 * Un essai pour résoudre le jour 15 de l'Avent de Code 2017.
 */
public class d15 {
    private static final long FACTOR_A = 16807;
    private static final long FACTOR_B = 48271;
    private static final long DIVISOR = 2147483647;
    private static final int PAIRS = 40000000;
    private static final int PAIRS_P2 = 5000000;

    public static void main(String[] args) {
        long startA = 679;
        long startB = 771;

        // Part 1
        long valueA = startA;
        long valueB = startB;
        int matches = 0;
        for (int i = 0; i < PAIRS; i++) {
            valueA = (valueA * FACTOR_A) % DIVISOR;
            valueB = (valueB * FACTOR_B) % DIVISOR;
            if ((valueA & 0xFFFF) == (valueB & 0xFFFF)) {
                matches++;
            }
        }
        System.out.println("Part 1: " + matches);

        // Part 2
        valueA = startA;
        valueB = startB;
        matches = 0;
        for (int i = 0; i < PAIRS_P2; i++) {
            do {
                valueA = (valueA * FACTOR_A) % DIVISOR;
            } while (valueA % 4 != 0);
            do {
                valueB = (valueB * FACTOR_B) % DIVISOR;
            } while (valueB % 8 != 0);
            if ((valueA & 0xFFFF) == (valueB & 0xFFFF)) {
                matches++;
            }
        }
        System.out.println("Part 2: " + matches);
    }
}