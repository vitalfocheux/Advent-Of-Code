/**
 * Un essai pour résoudre le jour 8 du défi de l'Avent 2023.
 */

import java.nio.file.*;
import java.util.*;

class Node {
    String left;
    String right;

    Node(String left, String right) {
        this.left = left;
        this.right = right;
    }
}

public class d08 {
    public static void main(String[] args) throws Exception {
        List<String> lines = Files.readAllLines(Paths.get("08.txt"));
        String instructions = lines.get(0);
        Map<String, Node> network = new HashMap<>();
        List<String> startNodes = new ArrayList<>();
        for (int i = 2; i < lines.size(); i++) {
            String[] parts = lines.get(i).split(" = \\(");
            String node = parts[0];
            parts = parts[1].substring(0, parts[1].length() - 1).split(", ");
            network.put(node, new Node(parts[0], parts[1]));
            if (node.endsWith("A")) {
                startNodes.add(node);
            }
        }

        String currentNode = "AAA";
        int steps = 0;
        while (!currentNode.equals("ZZZ")) {
            Node node = network.get(currentNode);
            currentNode = instructions.charAt(steps % instructions.length()) == 'L' ? node.left : node.right;
            steps++;
        }

        System.out.println("Steps to reach ZZZ: " + steps);

        long lcm = 1;
        for (String startNode : startNodes) {
            currentNode = startNode;
            steps = 0;
            while (!currentNode.endsWith("Z")) {
                Node node = network.get(currentNode);
                currentNode = instructions.charAt(steps % instructions.length()) == 'L' ? node.left : node.right;
                steps++;
            }
            lcm = lcm(lcm, steps);
        }

        System.out.println("Least common multiple of steps to reach ZZZ: " + lcm);

    }

    private static long lcm(long a, long b) {
        return a * (b / gcd(a, b));
    }

    private static long gcd(long a, long b) {
        while (b > 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}