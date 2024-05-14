/**
 * Un essai pour résoudre le jour 20 du AoC 2015
 */
public class d20 {
    public static void main(String[] args) {
        int target = 36000000;
        int[] houses1 = new int[target / 10];
        int[] houses2 = new int[target / 10];

        for (int i = 1; i < houses1.length; i++) {
            for (int j = i; j < houses1.length; j += i) {
                houses1[j] += i * 10;
                if (j / i <= 50) {
                    houses2[j] += i * 11;
                }
            }
        }

        for (int i = 0; i < houses1.length; i++) {
            if (houses1[i] >= target) {
                System.out.println("Part 1: " + i);
                break;
            }
        }

        for (int i = 0; i < houses2.length; i++) {
            if (houses2[i] >= target) {
                System.out.println("Part 2: " + i);
                break;
            }
        }
    }
}