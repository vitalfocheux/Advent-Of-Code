/**
 * Un essai pour résoudre le jour 14 du AoC 2017.
 */

import java.util.*;

public class d14 {
    private static final int[] SUFFIX = {17, 31, 73, 47, 23};

    public static void main(String[] args) {
        String key = "vbqugkhl";
        boolean[][] grid = new boolean[128][128];
        for (int i = 0; i < 128; i++) {
            String rowKey = key + "-" + i;
            String hash = knotHash(rowKey);
            for (int j = 0; j < 32; j++) {
                int val = Integer.parseInt(hash.substring(j, j + 1), 16);
                for (int k = 0; k < 4; k++) {
                    grid[i][j * 4 + (3 - k)] = (val & (1 << k)) != 0;
                }
            }
        }

        int used = 0;
        for (boolean[] row : grid) {
            for (boolean cell : row) {
                if (cell) {
                    used++;
                }
            }
        }
        System.out.println("Part 1: " + used);

        int regions = 0;
        for (int i = 0; i < 128; i++) {
            for (int j = 0; j < 128; j++) {
                if (grid[i][j]) {
                    regions++;
                    clearRegion(grid, i, j);
                }
            }
        }
        System.out.println("Part 2: " + regions);
    }

    private static void clearRegion(boolean[][] grid, int i, int j) {
        if (i < 0 || j < 0 || i >= 128 || j >= 128 || !grid[i][j]) {
            return;
        }
        grid[i][j] = false;
        clearRegion(grid, i - 1, j);
        clearRegion(grid, i + 1, j);
        clearRegion(grid, i, j - 1);
        clearRegion(grid, i, j + 1);
    }

    private static String knotHash(String input) {
        int[] lengths = new int[input.length() + SUFFIX.length];
        for (int i = 0; i < input.length(); i++) {
            lengths[i] = input.charAt(i);
        }
        System.arraycopy(SUFFIX, 0, lengths, input.length(), SUFFIX.length);

        int[] list = new int[256];
        for (int i = 0; i < list.length; i++) {
            list[i] = i;
        }

        int position = 0;
        int skipSize = 0;
        for (int round = 0; round < 64; round++) {
            for (int length : lengths) {
                reverse(list, position, length);
                position = (position + length + skipSize) % list.length;
                skipSize++;
            }
        }

        StringBuilder hash = new StringBuilder();
        for (int i = 0; i < 16; i++) {
            int xor = 0;
            for (int j = 0; j < 16; j++) {
                xor ^= list[i * 16 + j];
            }
            hash.append(String.format("%02x", xor));
        }
        return hash.toString();
    }

    private static void reverse(int[] list, int position, int length) {
        for (int i = 0; i < length / 2; i++) {
            int temp = list[(position + i) % list.length];
            list[(position + i) % list.length] = list[(position + length - 1 - i) % list.length];
            list[(position + length - 1 - i) % list.length] = temp;
        }
    }
}