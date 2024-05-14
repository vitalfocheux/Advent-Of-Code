/**
 * Un essai pour résoudre le jour 25 du AoC 2017.
 */

import java.util.*;

public class d25 {
    static Map<Integer, Integer> tape = new HashMap<>();
    static int cursor = 0;
    static char state = 'A';
    static int steps = 12172063;

    public static void main(String[] args) {
        for (int i = 0; i < steps; i++) {
            step();
        }

        long checksum = tape.values().stream().filter(v -> v == 1).count();
        System.out.println("Part 1: " + checksum);
        System.out.println("Part 2: Congratulations!");
    }

    static void step() {
        switch (state) {
            case 'A':
                if (tape.getOrDefault(cursor, 0) == 0) {
                    tape.put(cursor, 1);
                    cursor++;
                    state = 'B';
                } else {
                    tape.put(cursor, 0);
                    cursor--;
                    state = 'C';
                }
                break;
            case 'B':
                if (tape.getOrDefault(cursor, 0) == 0) {
                    tape.put(cursor, 1);
                    cursor--;
                    state = 'A';
                } else {
                    cursor--;
                    state = 'D';
                }
                break;
            case 'C':
                if (tape.getOrDefault(cursor, 0) == 0) {
                    tape.put(cursor, 1);
                    cursor++;
                    state = 'D';
                } else {
                    tape.put(cursor, 0);
                    cursor++;
                    state = 'C';
                }
                break;
            case 'D':
                if (tape.getOrDefault(cursor, 0) == 0) {
                    cursor--;
                    state = 'B';
                } else {
                    tape.put(cursor, 0);
                    cursor++;
                    state = 'E';
                }
                break;
            case 'E':
                if (tape.getOrDefault(cursor, 0) == 0) {
                    tape.put(cursor, 1);
                    cursor++;
                    state = 'C';
                } else {
                    cursor--;
                    state = 'F';
                }
                break;
            case 'F':
                if (tape.getOrDefault(cursor, 0) == 0) {
                    tape.put(cursor, 1);
                    cursor--;
                    state = 'E';
                } else {
                    cursor++;
                    state = 'A';
                }
                break;
        }
    }
}