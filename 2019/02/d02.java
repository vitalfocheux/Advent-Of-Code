/**
 * Un essai pour résoudre le jour 2 du défi de l'Avent de Code 2019.
 */

import java.nio.file.*;
import java.util.*;
import java.io.IOException;

public class d02 {
    public static void main(String[] args) {
        try {
            String input = new String(Files.readAllBytes(Paths.get("02.txt")));
            int[] program = Arrays.stream(input.split(",")).mapToInt(Integer::parseInt).toArray();

            // Part 1
            int[] memory = Arrays.copyOf(program, program.length);
            memory[1] = 12;
            memory[2] = 2;
            runProgram(memory);
            System.out.println("Part 1: " + memory[0]);

            // Part 2
            outer: for (int noun = 0; noun <= 99; noun++) {
                for (int verb = 0; verb <= 99; verb++) {
                    memory = Arrays.copyOf(program, program.length);
                    memory[1] = noun;
                    memory[2] = verb;
                    runProgram(memory);
                    if (memory[0] == 19690720) {
                        System.out.println("Part 2: " + (100 * noun + verb));
                        break outer;
                    }
                }
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static void runProgram(int[] memory) {
        for (int pc = 0; pc < memory.length; ) {
            switch (memory[pc]) {
                case 1:
                    memory[memory[pc + 3]] = memory[memory[pc + 1]] + memory[memory[pc + 2]];
                    pc += 4;
                    break;
                case 2:
                    memory[memory[pc + 3]] = memory[memory[pc + 1]] * memory[memory[pc + 2]];
                    pc += 4;
                    break;
                case 99:
                    return;
                default:
                    throw new IllegalArgumentException("Unknown opcode: " + memory[pc]);
            }
        }
    }
}