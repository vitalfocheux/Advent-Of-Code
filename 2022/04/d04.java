/**
 * Un essai pour résoudre le jour 4 du défi de l'Avent 2022.
 */

import java.util.*;
import java.nio.file.*;
import java.io.IOException;

public class d04 {
    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("04.txt"));
            int fullyContained = 0;
            int overlaps = 0;
            for (String line : lines) {
                String[] pairs = line.split(",");
                String[] pair1 = pairs[0].split("-");
                String[] pair2 = pairs[1].split("-");
                int start1 = Integer.parseInt(pair1[0]);
                int end1 = Integer.parseInt(pair1[1]);
                int start2 = Integer.parseInt(pair2[0]);
                int end2 = Integer.parseInt(pair2[1]);
                if ((start1 >= start2 && end1 <= end2) || (start2 >= start1 && end2 <= end1)) {
                    fullyContained++;
                }
                if ((start1 >= start2 && start1 <= end2) || (end1 >= start2 && end1 <= end2) ||
                    (start2 >= start1 && start2 <= end1) || (end2 >= start1 && end2 <= end1)) {
                    overlaps++;
                }
            }
            System.out.println("Fully contained pairs: " + fullyContained);
            System.out.println("Overlapping pairs: " + overlaps);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}