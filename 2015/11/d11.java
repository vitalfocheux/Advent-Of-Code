/**
 * Un essai pour résoudre le jour 11 de l'année 2015
 */
public class d11 {
    public static void main(String[] args) {
        String password = "vzbxkghb"; // Votre input ici

        password = getNextPassword(password);
        System.out.println("Part 1: " + password);

        password = getNextPassword(password);
        System.out.println("Part 2: " + password);
    }

    private static String getNextPassword(String password) {
        do {
            password = incrementPassword(password);
        } while (!isValidPassword(password));
        return password;
    }

    private static String incrementPassword(String password) {
        char[] chars = password.toCharArray();
        for (int i = chars.length - 1; i >= 0; i--) {
            if (chars[i] == 'z') {
                chars[i] = 'a';
            } else {
                chars[i]++;
                break;
            }
        }
        return new String(chars);
    }

    private static boolean isValidPassword(String password) {
        if (password.matches(".*[iol].*")) return false;

        if (!password.matches(".*(.)\\1.*(.)\\2.*")) return false;

        for (int i = 0; i < password.length() - 2; i++) {
            if (password.charAt(i) + 1 == password.charAt(i + 1) && password.charAt(i) + 2 == password.charAt(i + 2)) {
                return true;
            }
        }
        return false;
    }
}