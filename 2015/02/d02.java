/**
 * Un essai pour résoudre le jour 2 du défi 2015
 */

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class d02 {
    public static void main(String[] args) {
        String inputFilePath = "02.txt";
        try {
            BufferedReader reader = new BufferedReader(new FileReader(inputFilePath));
            int totalPaper = 0;
            int totalRibbon = 0;
            String line;
            while ((line = reader.readLine()) != null) {
                String[] dimensions = line.split("x");
                int l = Integer.parseInt(dimensions[0]);
                int w = Integer.parseInt(dimensions[1]);
                int h = Integer.parseInt(dimensions[2]);

                int lw = l * w;
                int wh = w * h;
                int hl = h * l;

                int smallestSide = Math.min(Math.min(lw, wh), hl);

                totalPaper += 2 * lw + 2 * wh + 2 * hl + smallestSide;

                int smallestPerimeter = Math.min(Math.min(2*(l+w), 2*(w+h)), 2*(h+l));
                int volume = l * w * h;

                totalRibbon += smallestPerimeter + volume;
            }
            System.out.println("Total wrapping paper needed: " + totalPaper);
            System.out.println("Total ribbon needed: " + totalRibbon);
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}