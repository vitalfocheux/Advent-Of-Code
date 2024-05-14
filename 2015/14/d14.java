/**
 * Un essai pour résoudre le jour 14 de l'année 2015
 */

import java.util.*;
import java.io.*;

class Reindeer {
    String name;
    int speed;
    int flyTime;
    int restTime;
    int distance = 0;
    int score = 0;
    int time = 0;
    boolean isFlying = true;

    Reindeer(String name, int speed, int flyTime, int restTime) {
        this.name = name;
        this.speed = speed;
        this.flyTime = flyTime;
        this.restTime = restTime;
    }

    void update() {
        if (isFlying) {
            distance += speed;
            time++;
            if (time == flyTime) {
                time = 0;
                isFlying = false;
            }
        } else {
            time++;
            if (time == restTime) {
                time = 0;
                isFlying = true;
            }
        }
    }
}

public class d14 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("14.txt"));
        List<Reindeer> reindeers = new ArrayList<>();
        String line;
        while ((line = reader.readLine()) != null) {
            String[] parts = line.split(" ");
            String name = parts[0];
            int speed = Integer.parseInt(parts[3]);
            int flyTime = Integer.parseInt(parts[6]);
            int restTime = Integer.parseInt(parts[13]);
            reindeers.add(new Reindeer(name, speed, flyTime, restTime));
        }
        reader.close();

        int time = 2503;
        for (int i = 0; i < time; i++) {
            for (Reindeer reindeer : reindeers) {
                reindeer.update();
            }
            int maxDistance = reindeers.stream().mapToInt(r -> r.distance).max().getAsInt();
            for (Reindeer reindeer : reindeers) {
                if (reindeer.distance == maxDistance) {
                    reindeer.score++;
                }
            }
        }

        int maxDistance = reindeers.stream().mapToInt(r -> r.distance).max().getAsInt();
        int maxScore = reindeers.stream().mapToInt(r -> r.score).max().getAsInt();
        System.out.println("Part 1: " + maxDistance);
        System.out.println("Part 2: " + maxScore);
    }
}