import java.nio.file.*;
import java.io.IOException;
import java.util.regex.*;

public class d09 {
    public static void main(String[] args) throws IOException {
        String line = Files.readString(Paths.get("09.txt")).trim();
        System.out.println("Part 1: " + decompress(line, false));
        System.out.println("Part 2: " + decompress(line, true));
    }

    private static long decompress(String s, boolean recursive) {
        long length = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                int end = s.indexOf(')', i);
                String[] parts = s.substring(i + 1, end).split("x");
                int chars = Integer.parseInt(parts[0]);
                int repeat = Integer.parseInt(parts[1]);
                String sub = s.substring(end + 1, end + 1 + chars);
                length += (recursive ? decompress(sub, true) : sub.length()) * repeat;
                i = end + chars;
            } else {
                length++;
            }
        }
        return length;
    }
}