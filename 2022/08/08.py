'''
Un essai avec Llama3-70b-8192 pour résoudre le jour 8 de 2022
'''
def count_visible_trees(filename):
    with open(filename, 'r') as f:
        trees = [list(map(int, line.strip())) for line in f.readlines()]

    visible_trees = 0

    # Count trees on the edge
    visible_trees += len(trees) * 2 + (len(trees[0]) - 2) * 2

    # Count interior trees
    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[0]) - 1):
            tree_height = trees[i][j]
            visible = False

            # Check up
            if all(trees[k][j] < tree_height for k in range(i)):
                visible = True
            # Check down
            elif all(trees[k][j] < tree_height for k in range(i + 1, len(trees))):
                visible = True
            # Check left
            elif all(trees[i][k] < tree_height for k in range(j)):
                visible = True
            # Check right
            elif all(trees[i][k] < tree_height for k in range(j + 1, len(trees[0]))):
                visible = True

            if visible:
                visible_trees += 1

    return visible_trees

print(count_visible_trees('08.txt'))

def scenic_score(filename):
    with open(filename, 'r') as f:
        trees = [list(map(int, line.strip())) for line in f.readlines()]

    max_score = 0

    for i in range(len(trees)):
        for j in range(len(trees[0])):
            tree_height = trees[i][j]
            score = 1

            # Look up
            up = 0
            for k in range(i - 1, -1, -1):
                up += 1
                if trees[k][j] >= tree_height:
                    break
            score *= up

            # Look down
            down = 0
            for k in range(i + 1, len(trees)):
                down += 1
                if trees[k][j] >= tree_height:
                    break
            score *= down

            # Look left
            left = 0
            for k in range(j - 1, -1, -1):
                left += 1
                if trees[i][k] >= tree_height:
                    break
            score *= left

            # Look right
            right = 0
            for k in range(j + 1, len(trees[0])):
                right += 1
                if trees[i][k] >= tree_height:
                    break
            score *= right

            max_score = max(max_score, score)

    return max_score

print(scenic_score('08.txt'))