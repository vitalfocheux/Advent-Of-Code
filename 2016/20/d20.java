/**
 * Un essai pour résoudre le jour 20 de l'Avent de Code 2016.
 */

import java.util.*;
import java.io.*;

public class d20 {
    public static void main(String[] args) throws IOException {
        List<Range> ranges = new ArrayList<>();
        Scanner scanner = new Scanner(new File("20.txt"));
        while (scanner.hasNextLine()) {
            String[] parts = scanner.nextLine().split("-");
            ranges.add(new Range(Long.parseLong(parts[0]), Long.parseLong(parts[1])));
        }
        scanner.close();

        Collections.sort(ranges);

        long lowest = 0;
        long allowed = 0;
        long max = 0;
        for (Range range : ranges) {
            if (range.start > max + 1) {
                if (lowest == 0) {
                    lowest = max + 1;
                }
                allowed += range.start - max - 1;
            }
            max = Math.max(max, range.end);
        }

        System.out.println("Part 1: " + lowest);
        System.out.println("Part 2: " + allowed);
    }

    static class Range implements Comparable<Range> {
        long start;
        long end;

        Range(long start, long end) {
            this.start = start;
            this.end = end;
        }

        @Override
        public int compareTo(Range other) {
            return Long.compare(this.start, other.start);
        }
    }
}