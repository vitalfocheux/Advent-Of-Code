/**
 * Un essai pour résoudre le jour 1 du défi de l'Avent 2015.
 */

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class d01{

    public static void main(String[] args) {
        String inputFilePath = "01.txt";
        try {
            BufferedReader reader = new BufferedReader(new FileReader(inputFilePath));
            int floor = 0;
            int position = 0;
            int charPosition = 0;
            boolean basementReached = false;
            String line = reader.readLine();
            if (line != null) {
                for (char c : line.toCharArray()) {
                    position++;
                    if (c == '(') {
                        floor++;
                    } else if (c == ')') {
                        floor--;
                    }
                    if (floor == -1 && !basementReached) {
                        charPosition = position;
                        basementReached = true;
                    }
                }
            }
            System.out.println("Final floor: " + floor);
            if (basementReached) {
                System.out.println("Position of character that causes Santa to first enter the basement: " + charPosition);
            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}