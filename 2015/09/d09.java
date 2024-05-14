/**
 * Un essai pour résoudre le jour 9 de l'Avent of Code 2015.
 */

import java.util.*;
import java.io.*;

public class d09 {
    private static HashMap<String, Integer> distances = new HashMap<>();
    private static ArrayList<String> cities = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("09.txt"));
        String line;
        while ((line = reader.readLine()) != null) {
            String[] parts = line.split(" = ");
            String[] cities = parts[0].split(" to ");
            distances.put(cities[0] + "," + cities[1], Integer.parseInt(parts[1]));
            distances.put(cities[1] + "," + cities[0], Integer.parseInt(parts[1]));
            if (!d09.cities.contains(cities[0])) d09.cities.add(cities[0]);
            if (!d09.cities.contains(cities[1])) d09.cities.add(cities[1]);
        }
        reader.close();

        int shortest = Integer.MAX_VALUE;
        int longest = Integer.MIN_VALUE;

        ArrayList<String> permutations = getPermutations(d09.cities);
        for (String route : permutations) {
            String[] cities = route.split(",");
            int distance = 0;
            for (int i = 0; i < cities.length - 1; i++) {
                distance += distances.get(cities[i] + "," + cities[i + 1]);
            }
            shortest = Math.min(shortest, distance);
            longest = Math.max(longest, distance);
        }

        System.out.println("Part 1: " + shortest);
        System.out.println("Part 2: " + longest);
    }

    private static ArrayList<String> getPermutations(ArrayList<String> cities) {
        ArrayList<String> permutations = new ArrayList<>();
        getPermutations("", new ArrayList<>(cities), permutations);
        return permutations;
    }

    private static void getPermutations(String prefix, ArrayList<String> cities, ArrayList<String> permutations) {
        int n = cities.size();
        if (n == 0) permutations.add(prefix);
        else {
            for (int i = 0; i < n; i++) {
                ArrayList<String> newCities = new ArrayList<>(cities);
                newCities.remove(i);
                getPermutations(prefix + (prefix.equals("") ? "" : ",") + cities.get(i), newCities, permutations);
            }
        }
    }
}