/**
 * Un essai pour résoudre le jour 10 de l'Avent de Code 2020.
 */

import java.util.*;
import java.nio.file.*;
import java.io.IOException;

public class d10 {
    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("10.txt"));
            List<Integer> adapters = new ArrayList<>();
            for (String line : lines) {
                adapters.add(Integer.parseInt(line));
            }

            // Part 1: Count the number of 1-jolt differences and 3-jolt differences
            int diff1 = 0, diff3 = 1; // diff3 starts from 1 because of the device's built-in adapter
            Collections.sort(adapters);
            int prev = 0;
            for (int adapter : adapters) {
                if (adapter - prev == 1) diff1++;
                else if (adapter - prev == 3) diff3++;
                prev = adapter;
            }
            System.out.println("Part 1: " + diff1 * diff3);

            // Part 2: Count the total number of distinct ways to arrange the adapters
            long[] dp = new long[adapters.get(adapters.size() - 1) + 1];
            dp[0] = 1;
            for (int adapter : adapters) {
                for (int i = 1; i <= 3; i++) {
                    if (adapter - i >= 0) dp[adapter] += dp[adapter - i];
                }
            }
            System.out.println("Part 2: " + dp[dp.length - 1]);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}