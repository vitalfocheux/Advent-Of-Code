/**
 * Un essai pour résoudre le jour 8 de l'Avent de Code 2019.
 */

import java.nio.file.*;
import java.io.IOException;
import java.util.Arrays;

public class d08 {
    public static void main(String[] args) {
        try {
            String input = new String(Files.readAllBytes(Paths.get("08.txt"))).trim();
            int width = 25;
            int height = 6;
            int size = width * height;
            int layers = input.length() / size;

            // Part 1
            int minZeros = Integer.MAX_VALUE;
            int product = 0;
            for (int i = 0; i < layers; i++) {
                int zeros = 0;
                int ones = 0;
                int twos = 0;
                for (int j = 0; j < size; j++) {
                    char pixel = input.charAt(i * size + j);
                    if (pixel == '0') zeros++;
                    if (pixel == '1') ones++;
                    if (pixel == '2') twos++;
                }
                if (zeros < minZeros) {
                    minZeros = zeros;
                    product = ones * twos;
                }
            }
            System.out.println("Part 1: " + product);

            // Part 2
            char[] image = new char[size];
            Arrays.fill(image, '2');
            for (int i = 0; i < layers; i++) {
                for (int j = 0; j < size; j++) {
                    char pixel = input.charAt(i * size + j);
                    if (image[j] == '2') {
                        image[j] = pixel;
                    }
                }
            }
            System.out.println("Part 2:");
            for (int i = 0; i < height; i++) {
                for (int j = 0; j < width; j++) {
                    System.out.print(image[i * width + j] == '0' ? ' ' : '#');
                }
                System.out.println();
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}