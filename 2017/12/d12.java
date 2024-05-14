/**
 * Un essai pour résoudre le jour 12 du AoC 2017.
 */

import java.nio.file.*;
import java.io.*;
import java.util.*;

public class d12 {
    public static void main(String[] args) {
        Map<Integer, List<Integer>> connections = new HashMap<>();
        try {
            for (String line : Files.readAllLines(Paths.get("12.txt"))) {
                String[] parts = line.split(" <-> ");
                int program = Integer.parseInt(parts[0]);
                List<Integer> connected = new ArrayList<>();
                for (String conn : parts[1].split(", ")) {
                    connected.add(Integer.parseInt(conn));
                }
                connections.put(program, connected);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        Set<Integer> visited = new HashSet<>();
        visit(connections, visited, 0);
        System.out.println("Part 1: " + visited.size());

        int groups = 0;
        while (!connections.isEmpty()) {
            Iterator<Integer> iterator = connections.keySet().iterator();
            if (iterator.hasNext()) {
                visited.clear();
                visit(connections, visited, iterator.next());
                groups++;
                visited.forEach(connections::remove);
            }
        }
        System.out.println("Part 2: " + groups);
    }

    private static void visit(Map<Integer, List<Integer>> connections, Set<Integer> visited, int program) {
        if (!visited.contains(program)) {
            visited.add(program);
            for (int conn : connections.get(program)) {
                visit(connections, visited, conn);
            }
        }
    }
}