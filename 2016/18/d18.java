/**
 * Un essai pour résoudre le jour 18 du AoC 2016.
 */
public class d18 {
    public static void main(String[] args) {
        String input = "...^^^^^..^...^...^^^^^^...^.^^^.^.^.^^.^^^.....^.^^^...^^^^^^.....^.^^...^^^^^...^.^^^.^^......^^^^";
        int rowsPart1 = 40;
        int rowsPart2 = 400000;

        System.out.println("Part 1: " + countSafeTiles(input, rowsPart1));
        System.out.println("Part 2: " + countSafeTiles(input, rowsPart2));
    }

    private static int countSafeTiles(String firstRow, int numRows) {
        char[][] rows = new char[numRows][];
        rows[0] = firstRow.toCharArray();
        for (int i = 1; i < numRows; i++) {
            rows[i] = new char[firstRow.length()];
            for (int j = 0; j < firstRow.length(); j++) {
                char left = j > 0 ? rows[i - 1][j - 1] : '.';
                char center = rows[i - 1][j];
                char right = j < firstRow.length() - 1 ? rows[i - 1][j + 1] : '.';
                rows[i][j] = isTrap(left, center, right) ? '^' : '.';
            }
        }

        int safeTiles = 0;
        for (char[] row : rows) {
            for (char tile : row) {
                if (tile == '.') {
                    safeTiles++;
                }
            }
        }
        return safeTiles;
    }

    private static boolean isTrap(char left, char center, char right) {
        return (left == '^' && center == '^' && right == '.')
            || (center == '^' && right == '^' && left == '.')
            || (left == '^' && center == '.' && right == '.')
            || (right == '^' && center == '.' && left == '.');
    }
}