/**
 * Un essai pour résoudre le jour 4 de l'Avent de Code 2018.
 */

import java.nio.file.*;
import java.io.*;
import java.util.*;
import java.util.regex.*;
import java.util.stream.*;

public class d04 {
    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("04.txt"));
            Collections.sort(lines);

            Map<Integer, int[]> sleepTimes = new HashMap<>();
            int currentGuard = -1;
            int sleepStart = -1;

            for (String line : lines) {
                Matcher matcher = Pattern.compile("\\[(\\d+)-(\\d+)-(\\d+) (\\d+):(\\d+)\\] (.*)").matcher(line);
                if (matcher.matches()) {
                    int minute = Integer.parseInt(matcher.group(5));
                    String action = matcher.group(6);

                    if (action.startsWith("Guard")) {
                        currentGuard = Integer.parseInt(action.split(" ")[1].substring(1));
                        sleepTimes.putIfAbsent(currentGuard, new int[60]);
                    } else if (action.equals("falls asleep")) {
                        sleepStart = minute;
                    } else if (action.equals("wakes up")) {
                        for (int i = sleepStart; i < minute; i++) {
                            sleepTimes.get(currentGuard)[i]++;
                        }
                    }
                }
            }

            // Part 1
            int sleepiestGuard = sleepTimes.entrySet().stream()
                .max(Comparator.comparingInt(e -> Arrays.stream(e.getValue()).sum()))
                .get()
                .getKey();
            int sleepiestMinute = Arrays.stream(sleepTimes.get(sleepiestGuard)).boxed().collect(Collectors.toList()).indexOf(Arrays.stream(sleepTimes.get(sleepiestGuard)).max().getAsInt());
            System.out.println("Part 1: " + sleepiestGuard * sleepiestMinute);

            // Part 2
            int mostFrequentlyAsleepGuard = sleepTimes.entrySet().stream()
                .max(Comparator.comparingInt(e -> Arrays.stream(e.getValue()).max().getAsInt()))
                .get()
                .getKey();
            int mostFrequentlyAsleepMinute = Arrays.stream(sleepTimes.get(mostFrequentlyAsleepGuard)).boxed().collect(Collectors.toList()).indexOf(Arrays.stream(sleepTimes.get(mostFrequentlyAsleepGuard)).max().getAsInt());
            System.out.println("Part 2: " + mostFrequentlyAsleepGuard * mostFrequentlyAsleepMinute);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}