'''
Un essai pour résoudre le jour 8 de l'année 2018
'''
def parse_node(data):
    child_count = data.pop(0)
    metadata_count = data.pop(0)
    children = [parse_node(data) for _ in range(child_count)]
    metadata = [data.pop(0) for _ in range(metadata_count)]
    return {'children': children, 'metadata': metadata}

def sum_metadata(node):
    return sum(node['metadata']) + sum(sum_metadata(child) for child in node['children'])

def node_value(node):
    if node['children']:
        return sum(node_value(node['children'][i - 1]) for i in node['metadata'] if 0 < i <= len(node['children']))
    else:
        return sum(node['metadata'])

def solve(input):
    data = list(map(int, input.split()))
    root = parse_node(data)
    return sum_metadata(root), node_value(root)

input = open('08.txt').read().strip()
part1, part2 = solve(input)
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")