/**
 * Un essai pour résoudre le jour 17 de l'Avent de Code 2017
 */

import java.util.*;

public class d17 {
    public static void main(String[] args) {
        int steps = 382; // Remplacez par votre nombre de pas spécifique

        // Part 1
        List<Integer> buffer = new ArrayList<>();
        buffer.add(0);
        int position = 0;
        for (int i = 1; i <= 2017; i++) {
            position = (position + steps) % buffer.size() + 1;
            buffer.add(position, i);
        }
        System.out.println("Part 1: " + buffer.get((position + 1) % buffer.size()));

        // Part 2
        position = 0;
        int size = 1;
        int valueAfterZero = 0;
        for (int i = 1; i <= 50000000; i++) {
            position = (position + steps) % size + 1;
            if (position == 1) {
                valueAfterZero = i;
            }
            size++;
        }
        System.out.println("Part 2: " + valueAfterZero);
    }
}