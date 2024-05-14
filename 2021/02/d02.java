/**
 * Un essai pour résoudre le jour 2 de l'Advent of Code 2021.
 */

import java.util.*;
import java.nio.file.*;
import java.io.IOException;

public class d02 {
    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("02.txt"));
            int horizontalPosition = 0;
            int depth = 0;

            for (String line : lines) {
                String[] parts = line.split(" ");
                String command = parts[0];
                int value = Integer.parseInt(parts[1]);

                switch (command) {
                    case "forward":
                        horizontalPosition += value;
                        break;
                    case "down":
                        depth += value;
                        break;
                    case "up":
                        depth -= value;
                        break;
                }
            }

            int result = horizontalPosition * depth;
            System.out.println("Result: " + result);

        } catch (IOException e) {
            e.printStackTrace();
        }

        try {
            List<String> lines = Files.readAllLines(Paths.get("02.txt"));
            int horizontalPosition = 0;
            int depth = 0;
            int aim = 0;

            for (String line : lines) {
                String[] parts = line.split(" ");
                String command = parts[0];
                int value = Integer.parseInt(parts[1]);

                switch (command) {
                    case "forward":
                        horizontalPosition += value;
                        depth += aim * value;
                        break;
                    case "down":
                        aim += value;
                        break;
                    case "up":
                        aim -= value;
                        break;
                }
            }

            int result = horizontalPosition * depth;
            System.out.println("Result: " + result);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}