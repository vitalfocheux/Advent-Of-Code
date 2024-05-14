/**
 * Un essai pour résoudre le jour 14 du défi 2018.
 */

import java.util.*;

public class d14 {
    public static void main(String[] args) {
        int input = 330121;

        // Part 1
        List<Integer> scores = new ArrayList<>(Arrays.asList(3, 7));
        int elf1 = 0, elf2 = 1;
        while (scores.size() < input + 10) {
            int sum = scores.get(elf1) + scores.get(elf2);
            if (sum >= 10) scores.add(sum / 10);
            scores.add(sum % 10);
            elf1 = (elf1 + scores.get(elf1) + 1) % scores.size();
            elf2 = (elf2 + scores.get(elf2) + 1) % scores.size();
        }
        for (int i = input; i < input + 10; i++) {
            System.out.print(scores.get(i));
        }
        System.out.println();

        // Part 2
        scores.clear();
        scores.addAll(Arrays.asList(3, 7));
        elf1 = 0;
        elf2 = 1;
        String inputStr = Integer.toString(input);
        int inputLen = inputStr.length();
        while (true) {
            int sum = scores.get(elf1) + scores.get(elf2);
            if (sum >= 10) scores.add(sum / 10);
            if (scores.size() >= inputLen && match(scores, inputStr, scores.size() - inputLen)) break;
            scores.add(sum % 10);
            if (scores.size() >= inputLen && match(scores, inputStr, scores.size() - inputLen)) break;
            elf1 = (elf1 + scores.get(elf1) + 1) % scores.size();
            elf2 = (elf2 + scores.get(elf2) + 1) % scores.size();
        }
        System.out.println(scores.size() - inputLen);
    }

    static boolean match(List<Integer> scores, String inputStr, int index) {
        for (int i = 0; i < inputStr.length(); i++) {
            if (scores.get(index + i) != inputStr.charAt(i) - '0') {
                return false;
            }
        }
        return true;
    }
}