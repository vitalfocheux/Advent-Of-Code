/**
 * Premier essai code pas du tout optimisé
 * Second essai avec code optimisé qui fonctionne
 */

import java.util.*;

public class d19 {
    public static void main(String[] args) {
        int numElves = 3004953;

        System.out.println("Part 1: " + yankeeSwap(numElves));
        System.out.println("Part 2: " + yankeeSwapAcross(numElves));
    }

    private static int yankeeSwap(int numElves) {
        List<Integer> elves = new LinkedList<>();
        for (int i = 1; i <= numElves; i++) {
            elves.add(i);
        }

        ListIterator<Integer> it = elves.listIterator();
        while (elves.size() > 1) {
            it.next();
            if (!it.hasNext()) {
                it = elves.listIterator();
            }
            it.next();
            it.remove();
            if (!it.hasNext()) {
                it = elves.listIterator();
            }
        }

        return elves.get(0);
    }

    private static int yankeeSwapAcross(int numElves) {
        LinkedList<Integer> left = new LinkedList<>();
        LinkedList<Integer> right = new LinkedList<>();
        for (int i = 1; i <= numElves; i++) {
            if (i <= numElves / 2) {
                left.add(i);
            } else {
                right.add(i);
            }
        }

        while (left.size() + right.size() > 1) {
            if (left.size() > right.size()) {
                left.removeLast();
            } else {
                right.removeFirst();
            }
            right.addLast(left.removeFirst());
            if (left.size() < right.size()) {
                left.addLast(right.removeFirst());
            }
        }

        return left.isEmpty() ? right.getFirst() : left.getFirst();
    }
}