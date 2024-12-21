import 'dart:collection';

import 'package:aoc_dart/packages/AOCD/models.dart';

void main() async {
  AOCD aocd = await AOCD.create(2024, 20);
  // print(part1(aocd.asStr));
  print(part2(aocd.asStr));
}

(int, int) start = (0, 0);
(int, int) end = (0, 0);
List<(int, int)> dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)];
int ROWS = 0;
int COLS = 0;
int MAX = 0;

parseInput(String input){
  List<List<String>> data = input.split('\n').map((e) => e.split('')).toList();
  for(int i = 0; i < data.length; i++){
    for(int j = 0; j < data[i].length; j++){
      if(data[i][j] == 'S'){
        start = (i, j);
      }
      if(data[i][j] == 'E'){
        end = (i, j);
      }
    }
  }
  ROWS = data.length;
  COLS = data[0].length;
  MAX = (ROWS+1) * (COLS+1);
  return data;
}

part1(String input){
  List<List<String>> data = parseInput(input);
  List<List<int>> distS = bfs(data, start);
  List<List<int>> distE = bfs(data, end);
  return cheats(data, distS, distE, 100);
}

cheats(List<List<String>> grid, List<List<int>> distS, List<List<int>> distE, int under_pico){
  Set<String> cheats = Set();
  for(int x = 0; x < ROWS; x++){
    for(int y = 0; y < COLS; y++){
      if(grid[x][y] == "#" || distS[x][y] == MAX){
        continue;
      }
      int base = distS[x][y];


      for((int, int) dir in dirs){
        (int, int) next = (x + dir.$1, y + dir.$2);
        if(in_grid(next) && distE[next.$1][next.$2] != MAX){
          int dist = base + 1 + distE[next.$1][next.$2];
          if(distS[end.$1][end.$2] - dist >= under_pico){
            cheats.add("$x, $y, ${next.$1}, ${next.$2}");
          }
        }
      }

      for((int, int) dir1 in dirs){
        (int, int) next = (x + dir1.$1, y + dir1.$2);
        if(in_grid(next)){
          for((int, int) dir2 in dirs){
            (int, int) next2 = (next.$1 + dir2.$1, next.$2 + dir2.$2);
            if(in_grid(next2) && distE[next2.$1][next2.$2] != MAX){
              int dist = base + 2 + distE[next2.$1][next2.$2];
              if(distS[end.$1][end.$2] - dist >= under_pico){
                cheats.add("$x, $y, ${next2.$1}, ${next2.$2}");
              }
            }
          }
        }
      }
    }
  }
  return cheats.length;
}

bfs(List<List<String>> grid, (int, int) start){
  List<List<int>> dist = List.generate(ROWS, (i) => List.generate(COLS, (j) => (MAX)));
  dist[start.$1][start.$2] = 0;
  Queue<(int, int)> q = Queue();
  q.add(start);
  while(q.isNotEmpty){
    (int, int) curr = q.removeFirst();
    for((int, int) dir in dirs){
      (int, int) next = (curr.$1 + dir.$1, curr.$2 + dir.$2);
      if(next.$1 < 0 || next.$1 >= ROWS || next.$2 < 0 || next.$2 >= COLS || grid[next.$1][next.$2] == '#'){
        continue;
      }
      if(dist[next.$1][next.$2] > dist[curr.$1][curr.$2] + 1){
        dist[next.$1][next.$2] = dist[curr.$1][curr.$2] + 1;
        q.add(next);
      }
    }
  }
  return dist;
}

bool in_grid((int, int) curr){
  return 0 <= curr.$1 && curr.$1 < ROWS && 0 <= curr.$2 && curr.$2 < COLS; 
}

part2(String input){
  List<List<String>> grid = parseInput(input);
  List<List<int>> distS = bfs(grid, start);
  List<List<int>> distE = bfs(grid, end);
  Set<(int, int)> tracks_from_start = Set();
  for(int x = 0; x < ROWS; x++){
    for(int y = 0; y < COLS; y++){
      if(distS[x][y] != MAX && grid[x][y] != '#'){
        tracks_from_start.add((x, y));
      }
    }
  }

  Set<String> cheats = Set();
  for((int, int) track in tracks_from_start){
    List<List<int>> dist_ignore_walls = List.generate(ROWS, (i) => List.generate(COLS, (j) => (MAX)));
    dist_ignore_walls[track.$1][track.$2] = 0;
    Queue<(int, int)> q = Queue();
    q.add(track);

    while(q.isNotEmpty){
      (int, int) curr = q.removeFirst();
      int dist = dist_ignore_walls[curr.$1][curr.$2];

      if(dist == 20){
        continue;
      }

      for((int, int) dir in dirs){
        (int, int) next = (curr.$1 + dir.$1, curr.$2 + dir.$2);
        if(in_grid(next) && dist_ignore_walls[next.$1][next.$2] > dist + 1){
          dist_ignore_walls[next.$1][next.$2] = dist + 1;
          q.add(next);
        }
      }
    }

    int base = distS[track.$1][track.$2];

    for(int r = 0; r < ROWS; r++){
      for(int c = 0; c < COLS; c++){
        int d = dist_ignore_walls[r][c];
        if(d != MAX && d >= 1 && d <= 20 && grid[r][c] != '#'){
          if(distE[r][c] != MAX){
            int dist_cheat = base + d + distE[r][c];
            if(distS[end.$1][end.$2] - dist_cheat >= 100){
              cheats.add("${track.$1}, ${track.$2}, $r, $c");
            }
          }
        }
      }
    }
  }
  return cheats.length;
}