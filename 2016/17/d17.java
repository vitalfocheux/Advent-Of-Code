import java.security.*;
import java.util.*;

public class d17 {
    private static final String INPUT = "hhhxzeay";

    public static void main(String[] args) throws NoSuchAlgorithmException {
        System.out.println("Part 1: " + bfs(INPUT));
        System.out.println("Part 2: " + dfs(INPUT));
    }

    private static String bfs(String passcode) throws NoSuchAlgorithmException {
        Queue<String> queue = new LinkedList<>();
        queue.add("");
        while (!queue.isEmpty()) {
            String path = queue.poll();
            if (path.length() > 0 && isGoal(path)) {
                return path;
            }
            queue.addAll(getNextSteps(passcode, path));
        }
        return "No solution found";
    }

    private static int dfs(String passcode) throws NoSuchAlgorithmException {
        int longest = 0;
        Stack<String> stack = new Stack<>();
        stack.push("");
        while (!stack.isEmpty()) {
            String path = stack.pop();
            if (path.length() > 0 && isGoal(path)) {
                longest = Math.max(longest, path.length());
            } else {
                stack.addAll(getNextSteps(passcode, path));
            }
        }
        return longest;
    }

    private static boolean isGoal(String path) {
        int x = 0, y = 0;
        for (char move : path.toCharArray()) {
            switch (move) {
                case 'U': y--; break;
                case 'D': y++; break;
                case 'L': x--; break;
                case 'R': x++; break;
            }
        }
        return x == 3 && y == 3;
    }

    private static List<String> getNextSteps(String passcode, String path) throws NoSuchAlgorithmException {
        List<String> nextSteps = new ArrayList<>();
        String hash = getMd5Hash(passcode + path);
        int x = 0, y = 0;
        for (char move : path.toCharArray()) {
            switch (move) {
                case 'U': y--; break;
                case 'D': y++; break;
                case 'L': x--; break;
                case 'R': x++; break;
            }
        }
        if (y > 0 && hash.charAt(0) > 'a') nextSteps.add(path + 'U');
        if (y < 3 && hash.charAt(1) > 'a') nextSteps.add(path + 'D');
        if (x > 0 && hash.charAt(2) > 'a') nextSteps.add(path + 'L');
        if (x < 3 && hash.charAt(3) > 'a') nextSteps.add(path + 'R');
        return nextSteps;
    }

    private static String getMd5Hash(String input) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] digest = md.digest(input.getBytes());
        StringBuilder sb = new StringBuilder();
        for (byte b : digest) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }
}