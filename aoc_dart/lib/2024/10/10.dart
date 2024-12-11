import 'package:aoc_dart/packages/AOCD/models.dart';

void main() async {
  AOCD aocd = await AOCD.create(2024, 10);
  print(part1(aocd.asStr));
  print(part2(aocd.asStr));
}

parseInput(String input){
  List<List<int>> grid = [];
  List<String> lines = input.split('\n');
  for(String line in lines){
    List<int> row = [];
    for(String char in line.split('')){
      row.add(int.parse(char));
    }
    grid.add(row);
  }
  return grid;
}

part1(String input){
  List<List<int>> grid = parseInput(input);
  Set<(int, int)> starts = {};
  for(int i = 0; i < grid.length; i++){
    for(int j = 0; j < grid[i].length; j++){
      if(grid[i][j] == 0){
        starts.add((i, j));
      }
    }
  }
  return starts.map((start) => trailhead(grid, start.$1, start.$2).length).reduce((value, element) => value + element);
}

trailhead(List<List<int>> grid, int i, int j){
  Set<(int, int)> trail = {};
  int curr = grid[i][j];
  if(curr == 9){
    trail.add((i, j));
  }
  List<(int, int)> directions = [(0, 1), (1, 0), (0, -1), (-1, 0)];
  for((int, int) dir in directions){
    int newI = i + dir.$1;
    int newJ = j + dir.$2;
    if(newI >= 0 && newI < grid.length && newJ >= 0 && newJ < grid[newI].length){
      if(grid[newI][newJ] == curr+1){
        trail.addAll(trailhead(grid, newI, newJ));
      }
    }
  }
  return trail;
}

part2(String input){
  List<List<int>> grid = parseInput(input);
  Set<(int, int)> starts = {};
  for(int i = 0; i < grid.length; i++){
    for(int j = 0; j < grid[i].length; j++){
      if(grid[i][j] == 0){
        starts.add((i, j));
      }
    }
  }
  return starts.map((start) => trailhead_v2(grid, start.$1, start.$2).length).reduce((value, element) => value + element);
}

trailhead_v2(List<List<int>> grid, int i, int j){
  List<(int, int)> trail = [];
  int curr = grid[i][j];
  if(curr == 9){
    trail.add((i, j));
  }
  List<(int, int)> directions = [(0, 1), (1, 0), (0, -1), (-1, 0)];
  for((int, int) dir in directions){
    int newI = i + dir.$1;
    int newJ = j + dir.$2;
    if(newI >= 0 && newI < grid.length && newJ >= 0 && newJ < grid[newI].length){
      if(grid[newI][newJ] == curr+1){
        trail.addAll(trailhead_v2(grid, newI, newJ));
      }
    }
  }
  return trail;
}