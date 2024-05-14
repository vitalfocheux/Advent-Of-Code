/**
 * Un essai pour résoudre le jour 13 du AoC 2016.
 */

import java.util.*;

public class d13 {
    private static final int INPUT = 1358;

    public static void main(String[] args) {
        System.out.println("Part 1: " + bfs(new int[]{1, 1}, new int[]{31, 39}, false));
        System.out.println("Part 2: " + bfs(new int[]{1, 1}, new int[]{0, 0}, true));
    }

    private static int bfs(int[] start, int[] target, boolean part2) {
        Queue<int[]> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        queue.add(new int[]{start[0], start[1], 0});
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0], y = current[1], steps = current[2];
            if (x < 0 || y < 0 || visited.contains(x + "," + y) || !isOpenSpace(x, y)) continue;
            if (!part2 && x == target[0] && y == target[1]) return steps;
            visited.add(x + "," + y);
            if (part2 && steps == 50) continue;
            queue.add(new int[]{x + 1, y, steps + 1});
            queue.add(new int[]{x - 1, y, steps + 1});
            queue.add(new int[]{x, y + 1, steps + 1});
            queue.add(new int[]{x, y - 1, steps + 1});
        }
        return visited.size();
    }

    private static boolean isOpenSpace(int x, int y) {
        int sum = x*x + 3*x + 2*x*y + y + y*y + INPUT;
        return Integer.bitCount(sum) % 2 == 0;
    }
}