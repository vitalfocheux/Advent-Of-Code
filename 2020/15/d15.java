/**
 * Un essai pour résoudre le jour 15 du défi 2020.
 */

import java.util.*;

public class d15 {
    public static void main(String[] args) {
        List<Integer> startingNumbers = Arrays.asList(0,12,6,13,20,1,17); // Replace with your starting numbers

        // Part 1: Play the number game until the 2020th number is spoken
        int lastNumberSpokenPart1 = playNumberGame(startingNumbers, 2020);
        System.out.println("Part 1: " + lastNumberSpokenPart1);

        // Part 2: Continue playing the number game until the 30000000th number is spoken
        int lastNumberSpokenPart2 = playNumberGame(startingNumbers, 30000000);
        System.out.println("Part 2: " + lastNumberSpokenPart2);
    }

    static int playNumberGame(List<Integer> startingNumbers, int turns) {
        Map<Integer, Integer> lastTurnSpoken = new HashMap<>();
        for (int i = 0; i < startingNumbers.size() - 1; i++) {
            lastTurnSpoken.put(startingNumbers.get(i), i + 1);
        }
        int lastNumberSpoken = startingNumbers.get(startingNumbers.size() - 1);
        for (int turn = startingNumbers.size(); turn < turns; turn++) {
            int nextNumberSpoken = lastTurnSpoken.containsKey(lastNumberSpoken) ? turn - lastTurnSpoken.get(lastNumberSpoken) : 0;
            lastTurnSpoken.put(lastNumberSpoken, turn);
            lastNumberSpoken = nextNumberSpoken;
        }
        return lastNumberSpoken;
    }
}