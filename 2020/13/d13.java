/**
 * Un essai pour résoudre le jour 13 de l'Avent de Code 2020
 */

import java.util.*;
import java.nio.file.*;
import java.io.IOException;

public class d13 {
    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("13.txt"));
            int earliestDeparture = Integer.parseInt(lines.get(0));
            String[] busIds = lines.get(1).split(",");

            // Part 1: Find the earliest bus you can take
            int minWaitTime = Integer.MAX_VALUE;
            int earliestBusId = -1;
            for (String busId : busIds) {
                if (!busId.equals("x")) {
                    int id = Integer.parseInt(busId);
                    int waitTime = id - (earliestDeparture % id);
                    if (waitTime < minWaitTime) {
                        minWaitTime = waitTime;
                        earliestBusId = id;
                    }
                }
            }
            System.out.println("Part 1: " + (minWaitTime * earliestBusId));

            // Part 2: Find the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list
            long timestamp = 0;
            long increment = 1;
            for (int i = 0; i < busIds.length; i++) {
                if (!busIds[i].equals("x")) {
                    int busId = Integer.parseInt(busIds[i]);
                    while ((timestamp + i) % busId != 0) {
                        timestamp += increment;
                    }
                    increment *= busId;
                }
            }
            System.out.println("Part 2: " + timestamp);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}