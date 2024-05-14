/**
 * Un essai pour la partie 1
 */

import java.util.*;
import java.nio.file.*;
import java.io.IOException;

public class d10 {
    private static final Map<Character, Character> PAIRS = Map.of('(', ')', '[', ']', '{', '}', '<', '>');
    private static final Map<Character, Integer> ERROR_SCORES = Map.of(')', 3, ']', 57, '}', 1197, '>', 25137);
    private static final Map<Character, Integer> COMPLETION_SCORES = Map.of(')', 1, ']', 2, '}', 3, '>', 4);

    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("10.txt"));
            int totalErrorScore = 0;
            List<Integer> completionScores = new ArrayList<>();
            for (String line : lines) {
                Deque<Character> stack = new ArrayDeque<>();
                boolean corrupted = false;
                for (char c : line.toCharArray()) {
                    if (PAIRS.containsKey(c)) {
                        stack.push(c);
                    } else {
                        if (stack.isEmpty() || PAIRS.get(stack.peek()) != c) {
                            totalErrorScore += ERROR_SCORES.get(c);
                            corrupted = true;
                            break;
                        }
                        stack.pop();
                    }
                }
                if (!corrupted) {
                    StringBuilder completion = new StringBuilder();
                    while (!stack.isEmpty()) {
                        completion.append(PAIRS.get(stack.pop()));
                    }
                    int completionScore = 0;
                    for (char c : completion.toString().toCharArray()) {
                        completionScore = completionScore * 5 + COMPLETION_SCORES.get(c);
                    }
                    completionScores.add(completionScore);
                }
            }
            System.out.println("Total error score: " + totalErrorScore);

            Collections.sort(completionScores);
            int middleScore = completionScores.get(completionScores.size() / 2);
            System.out.println("Middle score: " + middleScore);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}