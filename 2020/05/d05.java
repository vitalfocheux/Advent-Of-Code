/**
 * Un essai pour résoudre le jour 5 de l'Avent de Code 2020.
 */

import java.util.*;
import java.nio.file.*;
import java.io.IOException;

public class d05 {
    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("05.txt"));
            List<Integer> seats = new ArrayList<>();

            for (String line : lines) {
                int row = Integer.parseInt(line.substring(0, 7).replace('B', '1').replace('F', '0'), 2);
                int col = Integer.parseInt(line.substring(7).replace('R', '1').replace('L', '0'), 2);
                seats.add(row * 8 + col);
            }

            // Part 1: Find the highest seat ID
            int highestSeatId = Collections.max(seats);
            System.out.println("Part 1: " + highestSeatId);

            // Part 2: Find your seat
            Collections.sort(seats);
            int yourSeatId = 0;
            for (int i = 0; i < seats.size() - 1; i++) {
                if (seats.get(i + 1) - seats.get(i) > 1) {
                    yourSeatId = seats.get(i) + 1;
                    break;
                }
            }
            System.out.println("Part 2: " + yourSeatId);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}