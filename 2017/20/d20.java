/**
 * Un essai pour résoudre le jour 20 du AoC 2017
 */

import java.nio.file.*;
import java.io.*;
import java.util.*;
import java.util.regex.*;

public class d20 {
    static class Particle {
        int id;
        long[] p, v, a;

        Particle(int id, long[] p, long[] v, long[] a) {
            this.id = id;
            this.p = p;
            this.v = v;
            this.a = a;
        }

        void update() {
            for (int i = 0; i < 3; i++) {
                v[i] += a[i];
                p[i] += v[i];
            }
        }

        long manhattan() {
            return Math.abs(p[0]) + Math.abs(p[1]) + Math.abs(p[2]);
        }
    }

    public static void main(String[] args) {
        List<Particle> particles = new ArrayList<>();
        try {
            List<String> lines = Files.readAllLines(Paths.get("20.txt"));
            Pattern pattern = Pattern.compile("p=<(.*)>, v=<(.*)>, a=<(.*)>");
            for (int i = 0; i < lines.size(); i++) {
                Matcher matcher = pattern.matcher(lines.get(i));
                if (matcher.matches()) {
                    long[] p = Arrays.stream(matcher.group(1).split(",")).mapToLong(Long::parseLong).toArray();
                    long[] v = Arrays.stream(matcher.group(2).split(",")).mapToLong(Long::parseLong).toArray();
                    long[] a = Arrays.stream(matcher.group(3).split(",")).mapToLong(Long::parseLong).toArray();
                    particles.add(new Particle(i, p, v, a));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Part 1
        Particle min = particles.stream().min(Comparator.comparingLong(p -> p.a[0] * p.a[0] + p.a[1] * p.a[1] + p.a[2] * p.a[2])).get();
        System.out.println("Part 1: " + min.id);

        // Part 2
        for (int i = 0; i < 100; i++) {
            particles.forEach(Particle::update);
            Map<String, List<Particle>> map = new HashMap<>();
            for (Particle p : particles) {
                String key = p.p[0] + "," + p.p[1] + "," + p.p[2];
                map.putIfAbsent(key, new ArrayList<>());
                map.get(key).add(p);
            }
            particles = new ArrayList<>();
            for (List<Particle> list : map.values()) {
                if (list.size() == 1) {
                    particles.add(list.get(0));
                }
            }
        }
        System.out.println("Part 2: " + particles.size());
    }
}