/**
 * Deux essais pour résoudre le jour 6 de Advent of Code 2021
 */

import java.util.*;
import java.nio.file.*;
import java.io.IOException;

public class d06 {
    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("06.txt"));
            Map<Integer, Long> lanternfish = new HashMap<>();
            for (String line : lines) {
                String[] timers = line.split(",");
                for (String timer : timers) {
                    int time = Integer.parseInt(timer);
                    lanternfish.put(time, lanternfish.getOrDefault(time, 0L) + 1);
                }
            }
            for (int day = 0; day < 256; day++) {
                if(day == 80){
                    long total = 0;
                    for (long count : lanternfish.values()) {
                        total += count;
                    }
                    System.out.println("Total lanternfish: " + total);
                }
                Map<Integer, Long> newLanternfish = new HashMap<>();
                for (int time : lanternfish.keySet()) {
                    long count = lanternfish.get(time);
                    if (time == 0) {
                        newLanternfish.put(6, newLanternfish.getOrDefault(6, 0L) + count);
                        newLanternfish.put(8, newLanternfish.getOrDefault(8, 0L) + count);
                    } else {
                        newLanternfish.put(time - 1, newLanternfish.getOrDefault(time - 1, 0L) + count);
                    }
                }
                lanternfish = newLanternfish;
            }
            long total = 0;
            for (long count : lanternfish.values()) {
                total += count;
            }
            System.out.println("Total lanternfish: " + total);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}