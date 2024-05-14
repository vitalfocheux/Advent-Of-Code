/**
 * Un essai pour résoudre le jour 6 du défi 2015
 */

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class d06 {
    private static final int SIZE = 1000;
    private static final Pattern PATTERN = Pattern.compile("(turn on|turn off|toggle) (\\d+),(\\d+) through (\\d+),(\\d+)");

    public static void main(String[] args) {
        int[][] gridPart1 = new int[SIZE][SIZE];
        int[][] gridPart2 = new int[SIZE][SIZE];
        String inputFilePath = "06.txt";
        try {
            BufferedReader reader = new BufferedReader(new FileReader(inputFilePath));
            String line;
            while ((line = reader.readLine()) != null) {
                Matcher matcher = PATTERN.matcher(line);
                if (matcher.matches()) {
                    String command = matcher.group(1);
                    int x1 = Integer.parseInt(matcher.group(2));
                    int y1 = Integer.parseInt(matcher.group(3));
                    int x2 = Integer.parseInt(matcher.group(4));
                    int y2 = Integer.parseInt(matcher.group(5));
                    for (int x = x1; x <= x2; x++) {
                        for (int y = y1; y <= y2; y++) {
                            switch (command) {
                                case "turn on":
                                    gridPart1[x][y] = 1;
                                    gridPart2[x][y]++;
                                    break;
                                case "turn off":
                                    gridPart1[x][y] = 0;
                                    gridPart2[x][y] = Math.max(0, gridPart2[x][y] - 1);
                                    break;
                                case "toggle":
                                    gridPart1[x][y] ^= 1;
                                    gridPart2[x][y] += 2;
                                    break;
                            }
                        }
                    }
                }
            }
            reader.close();
            System.out.println("Part 1: " + countLights(gridPart1));
            System.out.println("Part 2: " + countBrightness(gridPart2));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static int countLights(int[][] grid) {
        int count = 0;
        for (int[] row : grid) {
            for (int light : row) {
                count += light;
            }
        }
        return count;
    }

    private static int countBrightness(int[][] grid) {
        int brightness = 0;
        for (int[] row : grid) {
            for (int light : row) {
                brightness += light;
            }
        }
        return brightness;
    }
}