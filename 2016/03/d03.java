/**
 * Un essai pour résoudre le jour 3 de l'Avent de Code 2016.
 */

import java.nio.file.*;
import java.io.IOException;
import java.util.*;

public class d03 {
    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get("03.txt"));
        int[][] triangles = new int[lines.size()][3];
        for (int i = 0; i < lines.size(); i++) {
            String[] parts = lines.get(i).trim().split("\\s+");
            for (int j = 0; j < 3; j++) {
                triangles[i][j] = Integer.parseInt(parts[j]);
            }
        }

        int validTriangles1 = 0;
        for (int[] triangle : triangles) {
            if (isValidTriangle(triangle[0], triangle[1], triangle[2])) {
                validTriangles1++;
            }
        }
        System.out.println("Part 1: " + validTriangles1);

        int validTriangles2 = 0;
        for (int i = 0; i < triangles.length; i += 3) {
            for (int j = 0; j < 3; j++) {
                if (isValidTriangle(triangles[i][j], triangles[i + 1][j], triangles[i + 2][j])) {
                    validTriangles2++;
                }
            }
        }
        System.out.println("Part 2: " + validTriangles2);
    }

    private static boolean isValidTriangle(int a, int b, int c) {
        return a + b > c && b + c > a && c + a > b;
    }
}