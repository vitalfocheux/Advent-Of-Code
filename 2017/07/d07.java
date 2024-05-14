/**
 * Un essai pour résoudre le jour 7 de l'Avent de Code 2017.
 */

import java.nio.file.*;
import java.io.*;
import java.util.*;

public class d07 {
    public static void main(String[] args) {
        Map<String, Node> nodes = new HashMap<>();
        try {
            for (String line : Files.readAllLines(Paths.get("07.txt"))) {
                String[] parts = line.split(" -> ");
                String[] leftParts = parts[0].split(" ");
                String name = leftParts[0];
                int weight = Integer.parseInt(leftParts[1].substring(1, leftParts[1].length() - 1));
                Node node = nodes.getOrDefault(name, new Node(name));
                node.weight = weight;
                nodes.put(name, node);
                if (parts.length > 1) {
                    String[] children = parts[1].split(", ");
                    for (String child : children) {
                        Node childNode = nodes.getOrDefault(child, new Node(child));
                        childNode.parent = node;
                        node.children.add(childNode);
                        nodes.put(child, childNode);
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        Node root = nodes.values().iterator().next();
        while (root.parent != null) {
            root = root.parent;
        }
        System.out.println("Part 1: " + root.name);
        System.out.println("Part 2: " + findUnbalanced(root));
    }

    private static int findUnbalanced(Node node) {
        Map<Integer, List<Node>> weights = new HashMap<>();
        for (Node child : node.children) {
            int weight = child.totalWeight();
            weights.putIfAbsent(weight, new ArrayList<>());
            weights.get(weight).add(child);
        }
        if (weights.size() > 1) {
            Node unbalanced = weights.values().stream().filter(list -> list.size() == 1).findFirst().get().get(0);
            Node balanced = weights.values().stream().filter(list -> list.size() > 1).findFirst().get().get(0);
            return findUnbalanced(unbalanced) == 0 ? unbalanced.weight - unbalanced.totalWeight() + balanced.totalWeight() : findUnbalanced(unbalanced);
        }
        return 0;
    }

    static class Node {
        String name;
        int weight;
        Node parent;
        List<Node> children = new ArrayList<>();

        Node(String name) {
            this.name = name;
        }

        int totalWeight() {
            return weight + children.stream().mapToInt(Node::totalWeight).sum();
        }
    }
}