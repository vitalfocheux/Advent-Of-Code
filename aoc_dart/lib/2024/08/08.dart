import 'package:aoc_dart/packages/AOCD/models.dart';

void main() async {
  AOCD aocd = await AOCD.create(2024, 8);
  print(part1(aocd.asStr));
  print(part2(aocd.asStr));   
}

part1(String input){
  List<List<String>> grid = input.split('\n').map((e) => e.split('')).toList();
  Map<String, Set<(int, int)>> coords_antennas = {};
  coordinate_antenna(grid, coords_antennas);

  List<List<String>> grid_copy = List.generate(grid.length, (index) => List.generate(grid[index].length, (index) => '0'));

  for(String key in coords_antennas.keys){
    Set<(int, int)> coords = coords_antennas[key]!;
    for(var coord_a in coords){
      for(var coord_b in coords){
        if(coord_b == coord_a){
          continue;
        }
        int diff_line = coord_a.$1 - coord_b.$1;
        int diff_col = coord_a.$2 - coord_b.$2;
        set_grid(grid_copy, (coord_a.$1 + diff_line), (coord_a.$2 + diff_col), '#');
      }
    }
  }
  return grid_copy.map((e) => e.where((element) => element == '#').length).reduce((value, element) => value + element);
}

part2(String input){
  List<List<String>> grid = input.split('\n').map((e) => e.split('')).toList();
  Map<String, Set<(int, int)>> coords_antennas = {};
  coordinate_antenna(grid, coords_antennas);

  List<List<String>> grid_copy = List.generate(grid.length, (index) => List.generate(grid[index].length, (index) => '0'));

  for(String key in coords_antennas.keys){
    Set<(int, int)> coords = coords_antennas[key]!;
    for(var coord_a in coords){
      for(var coord_b in coords){
        if(coord_b == coord_a){
          set_grid(grid_copy, coord_a.$1, coord_a.$2, '#');
          continue;
        }
        int diff_line = coord_a.$1 - coord_b.$1;
        int diff_col = coord_a.$2 - coord_b.$2;
        int line = coord_a.$1 + diff_line;
        int col = coord_a.$2 + diff_col;
        while(line >= 0 && line < grid.length && col >= 0 && col < grid[line].length){
          set_grid(grid_copy, line, col, '#');
          line += diff_line;
          col += diff_col;
        }
      }
    }
  }

  return grid_copy.map((e) => e.where((element) => element == '#').length).reduce((value, element) => value + element);
}

void set_grid(List<List<String>> grid, int line, int col, String value){
  if(line < 0 || line >= grid.length || col < 0 || col >= grid[line].length){
    return;
  }
  grid[line][col] = value;
}


void coordinate_antenna(List<List<String>> grid, Map<String, Set<(int, int)>> coords_antennas){
  for(int line = 0; line < grid.length; line++){
    for(int col = 0; col < grid[line].length; col++){
      if(grid[line][col] == '.'){
        continue;
      }
      if(!coords_antennas.containsKey(grid[line][col])){
        coords_antennas[grid[line][col]] = {};
        coords_antennas[grid[line][col]]?.add((line, col));
      }else{
        coords_antennas[grid[line][col]]?.add((line, col));
      }
    }
  }
}

void print_grid(List<List<String>> grid){
  for(int line = 0; line < grid.length; line++){
    print(grid[line].join(''));
  }
}