/**
 * Un essai pour résoudre le jour 8 de l'Avent de Code 2017.
 */

import java.nio.file.*;
import java.io.*;
import java.util.*;

public class d08 {
    public static void main(String[] args) {
        Map<String, Integer> registers = new HashMap<>();
        int highestEver = 0;
        try {
            for (String line : Files.readAllLines(Paths.get("08.txt"))) {
                String[] parts = line.split(" ");
                String reg = parts[0];
                int change = Integer.parseInt(parts[2]) * (parts[1].equals("inc") ? 1 : -1);
                String compReg = parts[4];
                int compVal = Integer.parseInt(parts[6]);
                boolean condition = false;
                switch (parts[5]) {
                    case ">":
                        condition = registers.getOrDefault(compReg, 0) > compVal;
                        break;
                    case "<":
                        condition = registers.getOrDefault(compReg, 0) < compVal;
                        break;
                    case ">=":
                        condition = registers.getOrDefault(compReg, 0) >= compVal;
                        break;
                    case "<=":
                        condition = registers.getOrDefault(compReg, 0) <= compVal;
                        break;
                    case "==":
                        condition = registers.getOrDefault(compReg, 0) == compVal;
                        break;
                    case "!=":
                        condition = registers.getOrDefault(compReg, 0) != compVal;
                        break;
                }
                if (condition) {
                    registers.put(reg, registers.getOrDefault(reg, 0) + change);
                    highestEver = Math.max(highestEver, registers.get(reg));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        int highestFinal = registers.values().stream().max(Integer::compare).get();
        System.out.println("Part 1: " + highestFinal);
        System.out.println("Part 2: " + highestEver);
    }
}