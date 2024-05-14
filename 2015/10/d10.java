/**
 * Un essai pour résoudre le jour 10 de l'année 2015
 */
public class d10 {
    public static void main(String[] args) {
        String input = "1321131112"; // Votre input ici

        for (int i = 0; i < 40; i++) {
            input = lookAndSay(input);
        }
        System.out.println("Part 1: " + input.length());

        for (int i = 0; i < 10; i++) {
            input = lookAndSay(input);
        }
        System.out.println("Part 2: " + input.length());
    }

    private static String lookAndSay(String input) {
        StringBuilder result = new StringBuilder();
        int i = 0;
        while (i < input.length()) {
            char current = input.charAt(i++);
            int count = 1;
            while (i < input.length() && input.charAt(i) == current) {
                i++;
                count++;
            }
            result.append(count).append(current);
        }
        return result.toString();
    }
}