/**
 * Un essai pour résoudre le jour 11 du AoC 2017
 */

import java.nio.file.*;
import java.io.*;
import java.util.*;

public class d11 {
    public static void main(String[] args) {
        String input = "";
        try {
            input = new String(Files.readAllBytes(Paths.get("11.txt"))).trim();
        } catch (IOException e) {
            e.printStackTrace();
        }

        String[] directions = input.split(",");
        int x = 0, y = 0, z = 0;
        int maxDistance = 0;

        for (String direction : directions) {
            switch (direction) {
                case "n":
                    y++;
                    z--;
                    break;
                case "ne":
                    x++;
                    z--;
                    break;
                case "se":
                    x++;
                    y--;
                    break;
                case "s":
                    y--;
                    z++;
                    break;
                case "sw":
                    x--;
                    z++;
                    break;
                case "nw":
                    x--;
                    y++;
                    break;
            }
            maxDistance = Math.max(maxDistance, (Math.abs(x) + Math.abs(y) + Math.abs(z)) / 2);
        }

        int finalDistance = (Math.abs(x) + Math.abs(y) + Math.abs(z)) / 2;
        System.out.println("Part 1: " + finalDistance);
        System.out.println("Part 2: " + maxDistance);
    }
}