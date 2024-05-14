/**
 * Un essai pour résoudre le jour 10 du AoC 2017.
 */

import java.nio.file.*;
import java.io.*;
import java.util.*;

public class d10 {
    public static void main(String[] args) {
        String input = "";
        try {
            input = new String(Files.readAllBytes(Paths.get("10.txt"))).trim();
        } catch (IOException e) {
            e.printStackTrace();
        }

        List<Integer> lengthsPart1 = new ArrayList<>();
        for (String num : input.split(",")) {
            lengthsPart1.add(Integer.parseInt(num));
        }
        List<Integer> listPart1 = new ArrayList<>();
        for (int i = 0; i < 256; i++) {
            listPart1.add(i);
        }
        knotHash(listPart1, lengthsPart1, 1);
        System.out.println("Part 1: " + listPart1.get(0) * listPart1.get(1));

        List<Integer> lengthsPart2 = new ArrayList<>();
        for (char c : input.toCharArray()) {
            lengthsPart2.add((int) c);
        }
        lengthsPart2.addAll(Arrays.asList(17, 31, 73, 47, 23));
        List<Integer> listPart2 = new ArrayList<>();
        for (int i = 0; i < 256; i++) {
            listPart2.add(i);
        }
        knotHash(listPart2, lengthsPart2, 64);
        StringBuilder hash = new StringBuilder();
        for (int i = 0; i < 16; i++) {
            int xor = 0;
            for (int j = 0; j < 16; j++) {
                xor ^= listPart2.get(i * 16 + j);
            }
            hash.append(String.format("%02x", xor));
        }
        System.out.println("Part 2: " + hash);
    }

    private static void knotHash(List<Integer> list, List<Integer> lengths, int rounds) {
        int position = 0;
        int skipSize = 0;
        for (int round = 0; round < rounds; round++) {
            for (int length : lengths) {
                reverse(list, position, length);
                position = (position + length + skipSize) % list.size();
                skipSize++;
            }
        }
    }

    private static void reverse(List<Integer> list, int position, int length) {
        for (int i = 0; i < length / 2; i++) {
            int temp = list.get((position + i) % list.size());
            list.set((position + i) % list.size(), list.get((position + length - 1 - i) % list.size()));
            list.set((position + length - 1 - i) % list.size(), temp);
        }
    }
}