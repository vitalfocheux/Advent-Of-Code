/**
 * Un essai pour résoudre le jour 1 de l'Avent de Code 2019.
 */

import java.nio.file.*;
import java.io.IOException;
import java.util.List;
import java.util.stream.Collectors;

public class d01 {
    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("01.txt"));
            List<Integer> masses = lines.stream().map(Integer::parseInt).collect(Collectors.toList());

            int totalFuelPart1 = masses.stream().mapToInt(d01::calculateFuel).sum();
            System.out.println("Part 1: " + totalFuelPart1);

            int totalFuelPart2 = masses.stream().mapToInt(d01::calculateTotalFuel).sum();
            System.out.println("Part 2: " + totalFuelPart2);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static int calculateFuel(int mass) {
        return mass / 3 - 2;
    }

    static int calculateTotalFuel(int mass) {
        int totalFuel = 0;
        while (mass > 0) {
            mass = calculateFuel(mass);
            if (mass > 0) {
                totalFuel += mass;
            }
        }
        return totalFuel;
    }
}