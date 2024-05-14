/**
 * Un essai pour résoudre le jour 16 de l'Avent de Code 2015.
 */

import java.util.*;
import java.io.*;

class Sue {
    int number;
    Map<String, Integer> items = new HashMap<>();

    Sue(int number) {
        this.number = number;
    }
}

public class d16 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("16.txt"));
        List<Sue> sues = new ArrayList<>();
        String line;
        while ((line = reader.readLine()) != null) {
            String[] parts = line.split(" ");
            int number = Integer.parseInt(parts[1].substring(0, parts[1].length() - 1));
            Sue sue = new Sue(number);
            for (int i = 2; i < parts.length; i += 2) {
                String item = parts[i].substring(0, parts[i].length() - 1);
                int count = Integer.parseInt(parts[i + 1].replace(",", ""));
                sue.items.put(item, count);
            }
            sues.add(sue);
        }
        reader.close();

        Map<String, Integer> clues = new HashMap<>();
        clues.put("children", 3);
        clues.put("cats", 7);
        clues.put("samoyeds", 2);
        clues.put("pomeranians", 3);
        clues.put("akitas", 0);
        clues.put("vizslas", 0);
        clues.put("goldfish", 5);
        clues.put("trees", 3);
        clues.put("cars", 2);
        clues.put("perfumes", 1);

        for (Sue sue : sues) {
            boolean match = true;
            for (Map.Entry<String, Integer> clue : clues.entrySet()) {
                if (sue.items.containsKey(clue.getKey()) && !sue.items.get(clue.getKey()).equals(clue.getValue())) {
                    match = false;
                    break;
                }
            }
            if (match) {
                System.out.println("Part 1: " + sue.number);
                break;
            }
        }

        for (Sue sue : sues) {
            boolean match = true;
            for (Map.Entry<String, Integer> clue : clues.entrySet()) {
                if (sue.items.containsKey(clue.getKey())) {
                    if (clue.getKey().equals("cats") || clue.getKey().equals("trees")) {
                        if (sue.items.get(clue.getKey()) <= clue.getValue()) {
                            match = false;
                            break;
                        }
                    } else if (clue.getKey().equals("pomeranians") || clue.getKey().equals("goldfish")) {
                        if (sue.items.get(clue.getKey()) >= clue.getValue()) {
                            match = false;
                            break;
                        }
                    } else if (!sue.items.get(clue.getKey()).equals(clue.getValue())) {
                        match = false;
                        break;
                    }
                }
            }
            if (match) {
                System.out.println("Part 2: " + sue.number);
                break;
            }
        }
    }
}