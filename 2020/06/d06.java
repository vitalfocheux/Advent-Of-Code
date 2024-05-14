/**
 * Un essai pour résoudre le jour 6 de l'Avent de Code 2020.
 */

import java.util.*;
import java.nio.file.*;
import java.io.IOException;
import java.util.stream.Collectors;

public class d06 {
    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("06.txt"));
            List<Set<Character>> groupAnswersPart1 = new ArrayList<>();
            List<Set<Character>> groupAnswersPart2 = new ArrayList<>();
            Set<Character> currentGroupAnswersPart1 = new HashSet<>();
            Set<Character> currentGroupAnswersPart2 = new HashSet<>();
            boolean newGroup = true;

            for (String line : lines) {
                if (line.isEmpty()) {
                    groupAnswersPart1.add(currentGroupAnswersPart1);
                    groupAnswersPart2.add(currentGroupAnswersPart2);
                    currentGroupAnswersPart1 = new HashSet<>();
                    currentGroupAnswersPart2 = new HashSet<>();
                    newGroup = true;
                } else {
                    for (char c : line.toCharArray()) {
                        currentGroupAnswersPart1.add(c);
                        if (newGroup) {
                            currentGroupAnswersPart2.add(c);
                        }
                    }
                    if (!newGroup) {
                        currentGroupAnswersPart2.retainAll(line.chars().mapToObj(c -> (char) c).collect(Collectors.toSet()));
                    }
                    newGroup = false;
                }
            }
            groupAnswersPart1.add(currentGroupAnswersPart1);
            groupAnswersPart2.add(currentGroupAnswersPart2);

            // Part 1: Count the total number of questions to which anyone in each group answered "yes"
            int sumPart1 = groupAnswersPart1.stream().mapToInt(Set::size).sum();
            System.out.println("Part 1: " + sumPart1);

            // Part 2: Count the total number of questions to which everyone in each group answered "yes"
            int sumPart2 = groupAnswersPart2.stream().mapToInt(Set::size).sum();
            System.out.println("Part 2: " + sumPart2);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}