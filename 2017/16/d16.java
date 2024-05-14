/**
 * Un essai pour résoudre le jour 16 du AoC 2017
 */

import java.util.*;
import java.io.*;
import java.nio.file.*;

public class d16 {
    public static void main(String[] args) {
        String input;
        try{
            input = Files.readAllLines(Paths.get("16.txt")).get(0);

            List<Character> programs = new ArrayList<>();
            for (char c = 'a'; c <= 'p'; c++) {
                programs.add(c);
            }

            String[] moves = input.split(",");
            for (int i = 0; i < moves.length; i++) {
                char move = moves[i].charAt(0);
                String[] params = moves[i].substring(1).split("/");
                if (move == 's') {
                    int count = Integer.parseInt(params[0]);
                    Collections.rotate(programs, count);
                } else if (move == 'x') {
                    int a = Integer.parseInt(params[0]);
                    int b = Integer.parseInt(params[1]);
                    Collections.swap(programs, a, b);
                } else if (move == 'p') {
                    int a = programs.indexOf(params[0].charAt(0));
                    int b = programs.indexOf(params[1].charAt(0));
                    Collections.swap(programs, a, b);
                }
            }

            System.out.println("Part 1: " + programs.toString().replaceAll("[\\[\\], ]", ""));

            // Pour la partie 2, nous devons trouver un cycle dans les permutations des programmes
            List<String> seen = new ArrayList<>();
            int cycle = 0;
            while (true) {
                String prog = programs.toString().replaceAll("[\\[\\], ]", "");
                if (seen.contains(prog)) {
                    break;
                }
                seen.add(prog);
                for (int i = 0; i < moves.length; i++) {
                    char move = moves[i].charAt(0);
                    String[] params = moves[i].substring(1).split("/");
                    if (move == 's') {
                        int count = Integer.parseInt(params[0]);
                        Collections.rotate(programs, count);
                    } else if (move == 'x') {
                        int a = Integer.parseInt(params[0]);
                        int b = Integer.parseInt(params[1]);
                        Collections.swap(programs, a, b);
                    } else if (move == 'p') {
                        int a = programs.indexOf(params[0].charAt(0));
                        int b = programs.indexOf(params[1].charAt(0));
                        Collections.swap(programs, a, b);
                    }
                }
                cycle++;
            }

            System.out.println("Part 2: " + seen.get((1000000000 % cycle) - 1));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}