/**
 * Un essai pour résoudre le jour 16 de l'Avent de Code 2016.
 */
public class d16 {
    public static void main(String[] args) {
        String input = "10010000000110000";
        int lengthPart1 = 272;
        int lengthPart2 = 35651584;

        System.out.println("Part 1: " + generateChecksum(input, lengthPart1));
        System.out.println("Part 2: " + generateChecksum(input, lengthPart2));
    }

    private static String generateChecksum(String input, int length) {
        StringBuilder data = new StringBuilder(input);
        while (data.length() < length) {
            StringBuilder b = new StringBuilder(data).reverse();
            for (int i = 0; i < b.length(); i++) {
                b.setCharAt(i, b.charAt(i) == '0' ? '1' : '0');
            }
            data.append("0").append(b);
        }
        data.setLength(length);

        StringBuilder checksum;
        do {
            checksum = new StringBuilder();
            for (int i = 0; i < data.length(); i += 2) {
                checksum.append(data.charAt(i) == data.charAt(i + 1) ? '1' : '0');
            }
            data = checksum;
        } while (checksum.length() % 2 == 0);

        return checksum.toString();
    }
}