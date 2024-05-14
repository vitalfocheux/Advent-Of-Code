/**
 * Un essai pour résoudre le jour 9 du défi de l'Avent 2018.
 */

import java.util.*;

public class d09 {
    public static void main(String[] args) {
        int numPlayers = 455;
        int lastMarble = 71223;

        // Part 1
        System.out.println("Part 1: " + playMarbleGame(numPlayers, lastMarble));

        // Part 2
        System.out.println("Part 2: " + playMarbleGame(numPlayers, lastMarble * 100));
    }

    static long playMarbleGame(int numPlayers, int lastMarble) {
        List<Long> marbles = new ArrayList<>();
        marbles.add(0L);
        long[] scores = new long[numPlayers];
        int currentIndex = 0;

        for (int i = 1; i <= lastMarble; i++) {
            if (i % 23 == 0) {
                currentIndex = (currentIndex - 7 + marbles.size()) % marbles.size();
                scores[i % numPlayers] += i + marbles.remove(currentIndex);
            } else {
                currentIndex = (currentIndex + 2) % marbles.size();
                marbles.add(currentIndex, (long) i);
            }
        }

        return Arrays.stream(scores).max().getAsLong();
    }
}