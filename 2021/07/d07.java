/**
 * Un essai pour la partie 1
 * La partie 2 ne foncionne pas
 */

import java.util.*;
import java.nio.file.*;
import java.io.IOException;

public class d07 {
    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("07.txt"));
            List<Integer> positions = new ArrayList<>();
            for (String line : lines) {
                String[] pos = line.split(",");
                for (String p : pos) {
                    positions.add(Integer.parseInt(p));
                }
            }
            Collections.sort(positions);
            int median = positions.get(positions.size() / 2);
            int fuel = 0;
            for (int position : positions) {
                fuel += Math.abs(position - median);
            }
            System.out.println("Total fuel: " + fuel);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}