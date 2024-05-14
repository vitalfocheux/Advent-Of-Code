/**
 * Un essai pour résoudre le jour 4 du défi de l'Avent 2016.
 */

import java.nio.file.*;
import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;

public class d04 {
    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get("04.txt"));
        int sum = 0;
        for (String line : lines) {
            String[] parts = line.split("-");
            String lastPart = parts[parts.length - 1];
            int sectorId = Integer.parseInt(lastPart.substring(0, lastPart.indexOf('[')));
            String checksum = lastPart.substring(lastPart.indexOf('[') + 1, lastPart.indexOf(']'));
            String name = String.join("", Arrays.copyOfRange(parts, 0, parts.length - 1));
            if (isRealRoom(name, checksum)) {
                sum += sectorId;
                String decryptedName = decryptName(name, sectorId);
                if (decryptedName.contains("northpole")) {
                    System.out.println("Part 2: " + sectorId);
                }
            }
        }
        System.out.println("Part 1: " + sum);
    }

    private static boolean isRealRoom(String name, String checksum) {
        Map<Character, Integer> frequency = new HashMap<>();
        for (char c : name.toCharArray()) {
            frequency.put(c, frequency.getOrDefault(c, 0) + 1);
        }
        String calculatedChecksum = frequency.entrySet().stream()
            .sorted(Map.Entry.<Character, Integer>comparingByValue().reversed()
                .thenComparing(Map.Entry.comparingByKey()))
            .limit(5)
            .map(Map.Entry::getKey)
            .map(String::valueOf)
            .collect(Collectors.joining());
        return calculatedChecksum.equals(checksum);
    }

    private static String decryptName(String name, int sectorId) {
        StringBuilder decryptedName = new StringBuilder();
        for (char c : name.toCharArray()) {
            if (c == '-') {
                decryptedName.append(' ');
            } else {
                decryptedName.append((char) ((c - 'a' + sectorId) % 26 + 'a'));
            }
        }
        return decryptedName.toString();
    }
}