/**
 * Un essai pour résoudre le jour 19 du AoC 2015
 */

import java.util.*;
import java.io.*;

public class d19 {
    private static HashMap<String, ArrayList<String>> replacements = new HashMap<>();
    private static String molecule;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("19.txt"));
        String line;
        while (!(line = reader.readLine()).isEmpty()) {
            String[] parts = line.split(" => ");
            if (!replacements.containsKey(parts[0])) {
                replacements.put(parts[0], new ArrayList<>());
            }
            replacements.get(parts[0]).add(parts[1]);
        }
        molecule = reader.readLine();
        reader.close();

        HashSet<String> molecules = new HashSet<>();
        for (int i = 0; i < molecule.length(); i++) {
            for (String key : replacements.keySet()) {
                if (molecule.startsWith(key, i)) {
                    for (String replacement : replacements.get(key)) {
                        molecules.add(molecule.substring(0, i) + replacement + molecule.substring(i + key.length()));
                    }
                }
            }
        }

        System.out.println("Part 1: " + molecules.size());

        int steps = 0;
        while (!molecule.equals("e")) {
            for (String key : replacements.keySet()) {
                for (String replacement : replacements.get(key)) {
                    int index = molecule.indexOf(replacement);
                    if (index != -1) {
                        molecule = molecule.substring(0, index) + key + molecule.substring(index + replacement.length());
                        steps++;
                        break;
                    }
                }
            }
        }

        System.out.println("Part 2: " + steps);
    }
}