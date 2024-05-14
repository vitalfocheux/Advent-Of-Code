/**
 * Un essai pour résoudre le jour 11 du défi de l'Avent 2018.
 */
public class d11 {
    private static final int GRID_SIZE = 300;
    private static final int SERIAL_NUMBER = 3214; // Remplacez par votre numéro de série

    public static void main(String[] args) {
        int[][] grid = new int[GRID_SIZE + 1][GRID_SIZE + 1];

        // Remplir la grille avec des niveaux de puissance
        for (int y = 1; y <= GRID_SIZE; y++) {
            for (int x = 1; x <= GRID_SIZE; x++) {
                int rackId = x + 10;
                int powerLevel = rackId * y;
                powerLevel += SERIAL_NUMBER;
                powerLevel *= rackId;
                powerLevel = (powerLevel / 100) % 10;
                powerLevel -= 5;
                grid[x][y] = powerLevel;
            }
        }

        // Partie 1
        int maxPower = Integer.MIN_VALUE;
        int maxX = 0, maxY = 0;
        for (int y = 1; y <= GRID_SIZE - 2; y++) {
            for (int x = 1; x <= GRID_SIZE - 2; x++) {
                int totalPower = 0;
                for (int dy = 0; dy < 3; dy++) {
                    for (int dx = 0; dx < 3; dx++) {
                        totalPower += grid[x + dx][y + dy];
                    }
                }
                if (totalPower > maxPower) {
                    maxPower = totalPower;
                    maxX = x;
                    maxY = y;
                }
            }
        }
        System.out.println("Part 1: " + maxX + "," + maxY);

        // Partie 2
        maxPower = Integer.MIN_VALUE;
        int maxGridSize = 0;
        for (int gridSize = 1; gridSize <= GRID_SIZE; gridSize++) {
            for (int y = 1; y <= GRID_SIZE - gridSize + 1; y++) {
                for (int x = 1; x <= GRID_SIZE - gridSize + 1; x++) {
                    int totalPower = 0;
                    for (int dy = 0; dy < gridSize; dy++) {
                        for (int dx = 0; dx < gridSize; dx++) {
                            totalPower += grid[x + dx][y + dy];
                        }
                    }
                    if (totalPower > maxPower) {
                        maxPower = totalPower;
                        maxX = x;
                        maxY = y;
                        maxGridSize = gridSize;
                    }
                }
            }
        }
        System.out.println("Part 2: " + maxX + "," + maxY + "," + maxGridSize);
    }
}