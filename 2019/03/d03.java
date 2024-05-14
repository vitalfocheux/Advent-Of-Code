/**
 * Un essai pour résoudre le jour 3 de l'Avent de Code 2019.
 */

import java.nio.file.*;
import java.util.*;
import java.io.*;

public class d03 {
    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("03.txt"));
            String[] wire1 = lines.get(0).split(",");
            String[] wire2 = lines.get(1).split(",");

            Map<Point, Integer> wire1Steps = getSteps(wire1);
            Map<Point, Integer> wire2Steps = getSteps(wire2);

            Set<Point> intersections = new HashSet<>(wire1Steps.keySet());
            intersections.retainAll(wire2Steps.keySet());

            int minDistance = intersections.stream().mapToInt(p -> Math.abs(p.x) + Math.abs(p.y)).min().getAsInt();
            System.out.println("Part 1: " + minDistance);

            int minSteps = intersections.stream().mapToInt(p -> wire1Steps.get(p) + wire2Steps.get(p)).min().getAsInt();
            System.out.println("Part 2: " + minSteps);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static Map<Point, Integer> getSteps(String[] wire) {
        Map<Point, Integer> steps = new HashMap<>();
        int x = 0, y = 0, totalSteps = 0;
        for (String move : wire) {
            char direction = move.charAt(0);
            int distance = Integer.parseInt(move.substring(1));
            for (int i = 0; i < distance; i++) {
                switch (direction) {
                    case 'U': y++; break;
                    case 'D': y--; break;
                    case 'L': x--; break;
                    case 'R': x++; break;
                }
                totalSteps++;
                steps.putIfAbsent(new Point(x, y), totalSteps);
            }
        }
        return steps;
    }

    static class Point {
        int x, y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Point point = (Point) o;
            return x == point.x && y == point.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }
}