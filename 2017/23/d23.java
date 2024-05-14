/**
 * Un essai pour la partie 1
 * Plusieurs essai pour la partie 2
 */

import java.nio.file.*;
import java.io.*;
import java.util.*;

public class d23 {
    static Map<String, Long> registers = new HashMap<>();
    static List<String[]> instructions;
    static int mulCount = 0;

    public static void main(String[] args) {
        try {
            instructions = new ArrayList<>();
            List<String> lines = Files.readAllLines(Paths.get("23.txt"));
            for (String line : lines) {
                instructions.add(line.split(" "));
            }

            // Part 1
            int i = 0;
            while (i >= 0 && i < instructions.size()) {
                i += execute(instructions.get(i));
            }
            System.out.println("Part 1: " + mulCount);

            int b = 65 * 100 + 100000;
            int c = b + 17000;
            int res = 0;
            for(int k = b; k <= c; k += 17) {
                if(!prime(k)) res++;
            }
            System.out.println("Part 2: " + res);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static int execute(String[] instruction) {
        long x = getValue(instruction[1]);
        long y = instruction.length > 2 ? getValue(instruction[2]) : 0;
        switch (instruction[0]) {
            case "set":
                registers.put(instruction[1], y);
                break;
            case "sub":
                registers.put(instruction[1], x - y);
                break;
            case "mul":
                registers.put(instruction[1], x * y);
                mulCount++;
                break;
            case "jnz":
                if (x != 0) {
                    return (int) y;
                }
                break;
        }
        return 1;
    }

    static long getValue(String s) {
        if (Character.isAlphabetic(s.charAt(0))) {
            return registers.getOrDefault(s, 0L);
        } else {
            return Long.parseLong(s);
        }
    }

    static boolean prime(int n) {
        int i = 2;
        while(i*i <= n) {
            if(n % i == 0) return false;
            i++;
        }
        return true;
    }
}