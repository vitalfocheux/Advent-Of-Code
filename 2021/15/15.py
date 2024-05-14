'''
Un essai pour la partie 1
La partie 2 ne fonctionne pas
'''
import heapq

def lowest_risk_path(risk_matrix):
    # Initialize the distance matrix
    distance_matrix = [[float('inf')] * len(risk_matrix[0]) for _ in range(len(risk_matrix))]
    distance_matrix[0][0] = 0

    # Initialize the heap
    heap = [(0, 0, 0)]  # (distance, row, col)

    while heap:
        dist, row, col = heapq.heappop(heap)

        # If this position has been visited, skip it
        if dist != distance_matrix[row][col]:
            continue

        # Check all four directions
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc

            # If the new position is within the matrix
            if 0 <= new_row < len(risk_matrix) and 0 <= new_col < len(risk_matrix[0]):
                new_dist = dist + risk_matrix[new_row][new_col]

                # If the new distance is shorter, update it
                if new_dist < distance_matrix[new_row][new_col]:
                    distance_matrix[new_row][new_col] = new_dist
                    heapq.heappush(heap, (new_dist, new_row, new_col))

    return distance_matrix[-1][-1]

# Convert input to risk matrix
risk_matrix = [
    [int(c) for c in line]
    for line in open('15.txt').read().splitlines()
]
print(lowest_risk_path(risk_matrix))