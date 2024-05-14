/**
 * Un essai pour résoudre le jour 6 de l'Avent de Code 2019.
 */

import java.nio.file.*;
import java.util.*;
import java.io.IOException;

public class d06 {
    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("06.txt"));
            Map<String, String> orbits = new HashMap<>();
            for (String line : lines) {
                String[] objects = line.split("\\)");
                orbits.put(objects[1], objects[0]);
            }

            // Part 1
            int totalOrbits = 0;
            for (String object : orbits.keySet()) {
                totalOrbits += countOrbits(orbits, object);
            }
            System.out.println("Part 1: " + totalOrbits);

            // Part 2
            String start = orbits.get("YOU");
            String end = orbits.get("SAN");
            int transfers = findTransfers(orbits, start, end);
            System.out.println("Part 2: " + transfers);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static int countOrbits(Map<String, String> orbits, String object) {
        int count = 0;
        while (orbits.containsKey(object)) {
            object = orbits.get(object);
            count++;
        }
        return count;
    }

    static int findTransfers(Map<String, String> orbits, String start, String end) {
        Map<String, Integer> distances = new HashMap<>();
        Queue<String> queue = new LinkedList<>();
        queue.add(start);
        distances.put(start, 0);
        while (!queue.isEmpty()) {
            String object = queue.remove();
            if (object.equals(end)) {
                return distances.get(object);
            }
            if (orbits.containsKey(object) && !distances.containsKey(orbits.get(object))) {
                distances.put(orbits.get(object), distances.get(object) + 1);
                queue.add(orbits.get(object));
            }
            for (String next : orbits.keySet()) {
                if (orbits.get(next).equals(object) && !distances.containsKey(next)) {
                    distances.put(next, distances.get(object) + 1);
                    queue.add(next);
                }
            }
        }
        return -1;
    }
}