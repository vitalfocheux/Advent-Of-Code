/**
 * Un essai pour résoudre le jour 10 du défi de l'Avent 2018.
 */

import java.nio.file.*;
import java.util.*;
import java.util.regex.*;
import java.io.*;

public class d10 {
    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("10.txt"));
            Pattern pattern = Pattern.compile("position=<\\s*([-\\d]+),\\s*([-\\d]+)> velocity=<\\s*([-\\d]+),\\s*([-\\d]+)>");
            List<Point> points = new ArrayList<>();

            for (String line : lines) {
                Matcher matcher = pattern.matcher(line);
                if (matcher.matches()) {
                    int x = Integer.parseInt(matcher.group(1));
                    int y = Integer.parseInt(matcher.group(2));
                    int dx = Integer.parseInt(matcher.group(3));
                    int dy = Integer.parseInt(matcher.group(4));
                    points.add(new Point(x, y, dx, dy));
                }
            }

            int seconds = 0;
            while (true) {
                int minX = points.stream().mapToInt(p -> p.x).min().getAsInt();
                int maxX = points.stream().mapToInt(p -> p.x).max().getAsInt();
                int minY = points.stream().mapToInt(p -> p.y).min().getAsInt();
                int maxY = points.stream().mapToInt(p -> p.y).max().getAsInt();

                if (Math.abs(maxX - minX) < 70 && Math.abs(maxY - minY) < 20) {
                    char[][] sky = new char[maxY - minY + 1][maxX - minX + 1];
                    for (char[] row : sky) {
                        Arrays.fill(row, '.');
                    }
                    for (Point point : points) {
                        sky[point.y - minY][point.x - minX] = '#';
                    }

                    System.out.println("After " + seconds + " seconds:");
                    for (char[] row : sky) {
                        System.out.println(row);
                    }

                    break;
                }

                for (Point point : points) {
                    point.move();
                }

                seconds++;
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static class Point {
        int x, y, dx, dy;

        Point(int x, int y, int dx, int dy) {
            this.x = x;
            this.y = y;
            this.dx = dx;
            this.dy = dy;
        }

        void move() {
            x += dx;
            y += dy;
        }
    }
}