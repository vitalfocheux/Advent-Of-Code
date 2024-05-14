/**
 * Un essai pour résoudre le jour 8 de l'Avent de Code 2018.
 */

import java.nio.file.*;
import java.io.*;
import java.util.*;

public class d08 {
    private static int index;

    public static void main(String[] args) {
        try {
            String input = Files.readString(Paths.get("08.txt")).trim();
            int[] numbers = Arrays.stream(input.split(" ")).mapToInt(Integer::parseInt).toArray();

            // Part 1
            index = 0;
            Node root = buildTree(numbers);
            System.out.println("Part 1: " + sumMetadata(root));

            // Part 2
            System.out.println("Part 2: " + calculateValue(root));

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static Node buildTree(int[] numbers) {
        int childCount = numbers[index++];
        int metadataCount = numbers[index++];
        Node node = new Node();
        for (int i = 0; i < childCount; i++) {
            node.children.add(buildTree(numbers));
        }
        for (int i = 0; i < metadataCount; i++) {
            node.metadata.add(numbers[index++]);
        }
        return node;
    }

    static int sumMetadata(Node node) {
        int sum = node.metadata.stream().mapToInt(Integer::intValue).sum();
        for (Node child : node.children) {
            sum += sumMetadata(child);
        }
        return sum;
    }

    static int calculateValue(Node node) {
        if (node.children.isEmpty()) {
            return node.metadata.stream().mapToInt(Integer::intValue).sum();
        }
        int value = 0;
        for (int index : node.metadata) {
            if (index > 0 && index <= node.children.size()) {
                value += calculateValue(node.children.get(index - 1));
            }
        }
        return value;
    }

    static class Node {
        List<Node> children = new ArrayList<>();
        List<Integer> metadata = new ArrayList<>();
    }
}