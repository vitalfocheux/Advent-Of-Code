/**
 * Un essai pour résoudre le jour 17 de l'Avent de Code 2015.
 */

import java.util.*;
import java.io.*;

public class d17 {
    static int[] containers;
    static int validCombinations = 0;
    static int minContainers = Integer.MAX_VALUE;
    static int minContainerCombinations = 0;

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(new File("17.txt"));
        List<Integer> list = new ArrayList<>();
        while (scanner.hasNextInt()) {
            list.add(scanner.nextInt());
        }
        scanner.close();
        containers = list.stream().mapToInt(i -> i).toArray();

        findCombinations(0, 0, 0);

        System.out.println("Part 1: " + validCombinations);
        System.out.println("Part 2: " + minContainerCombinations);
    }

    static void findCombinations(int start, int sum, int usedContainers) {
        if (sum == 150) {
            validCombinations++;
            if (usedContainers < minContainers) {
                minContainers = usedContainers;
                minContainerCombinations = 1;
            } else if (usedContainers == minContainers) {
                minContainerCombinations++;
            }
            return;
        }
        if (sum > 150 || start == containers.length) {
            return;
        }
        findCombinations(start + 1, sum + containers[start], usedContainers + 1);
        findCombinations(start + 1, sum, usedContainers);
    }
}