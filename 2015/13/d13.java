/**
 * Un essai pour résoudre le jour 13 du AoC 2015.
 */

import java.util.*;
import java.io.*;

public class d13 {
    private static HashMap<String, Integer> happiness = new HashMap<>();
    private static ArrayList<String> people = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("13.txt"));
        String line;
        while ((line = reader.readLine()) != null) {
            String[] parts = line.split(" ");
            String person1 = parts[0];
            String person2 = parts[10].substring(0, parts[10].length() - 1);
            int happinessChange = Integer.parseInt(parts[3]);
            if (parts[2].equals("lose")) {
                happinessChange *= -1;
            }
            happiness.put(person1 + " " + person2, happinessChange);
            if (!people.contains(person1)) {
                people.add(person1);
            }
        }
        reader.close();

        int maxHappiness = Integer.MIN_VALUE;
        ArrayList<String> arrangement = new ArrayList<>(people);
        do {
            int totalHappiness = 0;
            for (int i = 0; i < arrangement.size(); i++) {
                String person1 = arrangement.get(i);
                String person2 = arrangement.get((i + 1) % arrangement.size());
                totalHappiness += happiness.get(person1 + " " + person2);
                totalHappiness += happiness.get(person2 + " " + person1);
            }
            maxHappiness = Math.max(maxHappiness, totalHappiness);
        } while (nextPermutation(arrangement));

        System.out.println("Part 1: " + maxHappiness);

        for (String person : people) {
            happiness.put("Me " + person, 0);
            happiness.put(person + " Me", 0);
        }
        people.add("Me");

        maxHappiness = Integer.MIN_VALUE;
        arrangement = new ArrayList<>(people);
        do {
            int totalHappiness = 0;
            for (int i = 0; i < arrangement.size(); i++) {
                String person1 = arrangement.get(i);
                String person2 = arrangement.get((i + 1) % arrangement.size());
                totalHappiness += happiness.get(person1 + " " + person2);
                totalHappiness += happiness.get(person2 + " " + person1);
            }
            maxHappiness = Math.max(maxHappiness, totalHappiness);
        } while (nextPermutation(arrangement));

        System.out.println("Part 2: " + maxHappiness);
    }

    private static boolean nextPermutation(ArrayList<String> arrangement) {
        int i = arrangement.size() - 2;
        while (i >= 0 && arrangement.get(i).compareTo(arrangement.get(i + 1)) >= 0) {
            i--;
        }
        if (i < 0) {
            return false;
        }
        int j = arrangement.size() - 1;
        while (arrangement.get(j).compareTo(arrangement.get(i)) <= 0) {
            j--;
        }
        Collections.swap(arrangement, i, j);
        Collections.reverse(arrangement.subList(i + 1, arrangement.size()));
        return true;
    }
}