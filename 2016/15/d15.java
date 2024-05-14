/**
 * Un essai pour résoudre le jour 15 de l'Avent de Code 2016.
 */
public class d15 {
    public static void main(String[] args) {
        int[][] discs = {{17, 5}, {19, 8}, {7, 1}, {13, 7}, {5, 1}, {3, 0}};
        System.out.println("Part 1: " + findTime(discs));

        int[][] discsPart2 = {{17, 5}, {19, 8}, {7, 1}, {13, 7}, {5, 1}, {3, 0}, {11, 0}};
        System.out.println("Part 2: " + findTime(discsPart2));
    }

    private static int findTime(int[][] discs) {
        int time = 0;
        while (true) {
            boolean success = true;
            for (int i = 0; i < discs.length; i++) {
                int positions = discs[i][0];
                int start = discs[i][1];
                if ((start + time + i + 1) % positions != 0) {
                    success = false;
                    break;
                }
            }
            if (success) {
                return time;
            }
            time++;
        }
    }
}