/**
 * Un essai pour résoudre le jour 25 de l'advent of Code 2015
 */
public class d25 {
    public static void main(String[] args) {
        int row = 2981;
        int column = 3075;

        long code = 20151125;
        int codePosition = calculateCodePosition(row, column);
        for (int i = 1; i < codePosition; i++) {
            code = (code * 252533) % 33554393;
        }

        System.out.println("The code at position (" + row + ", " + column + ") is: " + code);
    }

    private static int calculateCodePosition(int row, int column) {
        return (row + column - 1) * (row + column - 2) / 2 + column;
    }
}