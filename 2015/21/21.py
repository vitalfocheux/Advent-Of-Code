'''
Trois essai pour résoudre le jour 21 de l'année 2015 mais obligé de modifier 21.txt pour que ça fonctionne
'''

from itertools import combinations

# Items: (cost, damage, armor)
weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
armor = [(0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
rings = [(0, 0, 0), (0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]

def fight(player, boss):
    player_hit_points, player_damage, player_armor = player
    boss_hit_points, boss_damage, boss_armor = boss
    while True:
        boss_hit_points -= max(1, player_damage - boss_armor)
        if boss_hit_points <= 0:
            return True
        player_hit_points -= max(1, boss_damage - player_armor)
        if player_hit_points <= 0:
            return False

def solve(boss):
    min_gold = float('inf')
    max_gold = float('-inf')
    for w in weapons:
        for a in armor:
            for r in combinations(rings, 2):
                items = [w, a, *r]
                cost = sum(item[0] for item in items)
                player = (100, sum(item[1] for item in items), sum(item[2] for item in items))
                if fight(player, boss):
                    min_gold = min(min_gold, cost)
                else:
                    max_gold = max(max_gold, cost)
    return min_gold, max_gold

boss = tuple(map(int, open('21.txt').read().splitlines()))
print(*solve(boss))  # Part 1 and 2