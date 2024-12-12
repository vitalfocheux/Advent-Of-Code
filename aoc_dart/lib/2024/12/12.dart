import 'dart:collection';

import 'package:aoc_dart/packages/AOCD/models.dart';

void main() async {
  AOCD aocd = await AOCD.create(2024, 12);
  (int, int) a = part(aocd.asStr);
  print(a.$1);
  print(a.$2);
}

parseInput(String input){
  return input.split('\n');
}

part(String input) {
  int res = 0;
  int res2 = 0;
  List<String> grid = parseInput(input);
  int line = grid.length;
  int col = grid[0].length;
  List<(int, int)> dirs = [(0,1), (1,0), (0,-1), (-1,0)];
  
  Set<(int, int)> visited = {};
  

  for(int i = 0; i < line; i++){
    for(int j = 0; j < col; j++){
      if(visited.contains((i,j))) continue;
      Queue queue = Queue.from([(i,j)]);
      int area = 0;
      int perim = 0;
      Map<(int, int), Set<(int, int)>> dict = {};
      while(queue.isNotEmpty){
        (int, int) current = queue.removeFirst();
        if(visited.contains(current)) continue;
        visited.add(current);
        area++;
        for((int, int) dir in dirs){
          (int, int) next = (current.$1 + dir.$1, current.$2 + dir.$2);
          if(0 <= next.$1 && next.$1 < line && 0 <= next.$2 && next.$2 < col && grid[next.$1][next.$2] == grid[current.$1][current.$2]){
            queue.add(next);
          }else{
            perim++;
            if(!dict.containsKey(dir)){
              dict[dir] = {};
            }
            dict[dir]?.add(current);
          }
        }

      }

      int sides = 0;
      for (var entry in dict.entries) {
        Set<(int, int)> values = entry.value;
        Set<(int, int)> visited_perim = {};
        for ((int, int) value in values) {
          if (!visited_perim.contains(value)) {
            sides += 1;
            Queue<(int, int)> Q = Queue.from([value]);
            while (Q.isNotEmpty) {
              (int, int) current = Q.removeFirst();
              if (visited_perim.contains(current)) {
                continue;
              }
              visited_perim.add(current);
              for (var drdc in dirs) {
                (int, int) next = (current.$1 + drdc.$1, current.$2 + drdc.$2);
                if (values.contains(next)) {
                  Q.add(next);
                }
              }
            }
          }
        }
      }
      res += area * perim;
      res2 += area * sides;
    }
  }
  return (res, res2);
}