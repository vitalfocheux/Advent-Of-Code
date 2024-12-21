import 'dart:collection';
import 'dart:math';
import 'package:aoc_dart/packages/AOCD/models.dart';
import 'package:aoc_dart/packages/extension/string_extension.dart';

void main() async {
  AOCD aocd = await AOCD.create(2024, 21);
  print(part(aocd.asStr, 2));
  print(part(aocd.asStr, 25));
}

List<List<String?>> num_keypad = [
  ["7", "8", "9"],
  ["4", "5", "6"],
  ["1", "2", "3"],
  [null, "0", "A"],
];

List<List<String?>> dir_keypad = [
  [null, "^", "A"],
  ["<", "v", ">"],
];


List<(int, int)> dirs = [
  (0, 1),
  (1, 0),
  (0, -1),
  (-1, 0),
];

part(String input, int depth){
  num res = 0;
  for(String line in input.split('\n')){
    int length = sequence_length(line, depth);
    res += length * line.findInt();
  }
  return res;
}

get_pad(List<List<String?>> grid, String char){
  for(int i = 0; i < grid.length; i++){
    for(int j = 0; j < grid[i].length; j++){
      if(grid[i][j] == char){
        return (i, j);
      }
    }
  }
  return null;
}

sequence_length(String code, int depth){
  (int, int) start = get_pad(num_keypad, "A");
  num res = 0;

  for(String char in code.split('')){
    (int, int) end = get_pad(num_keypad, char);
    List<String> paths = find_all_paths(num_keypad, start, end);
    List<int> lengths = [];
    for(String path in paths){
      lengths.add(dir_path_length(path, depth, {}));
    }
    res += lengths.reduce(min);
    start = end;
  }
  return res;
}

dir_path_length(String sequence, int depth, Map<String, num> memo){
  String key = '$sequence-$depth';
  if(memo.containsKey(key)){
    return memo[key]!;
  }

  if(depth == 0){
    memo[key] = sequence.length;
    return sequence.length;
  }

  (int, int) start = get_pad(dir_keypad, "A");
  num res = 0;

  for(String char in sequence.split('')){
    (int, int) end = get_pad(dir_keypad, char);
    List<String> paths = find_all_paths(dir_keypad, start, end);
    List<int> lengths = [];
    for(String path in paths){
      lengths.add(dir_path_length(path, depth-1, memo));
    }
    res += lengths.reduce(min);
    start = end;
  }
  memo[key] = res;
  return res;
}

find_all_paths(List<List<String?>> grid, (int, int) start, (int, int) end){
  List<String> paths = [];
  Queue<((int, int), (int, int), List<String>)> queue = Queue();
  queue.add((start, (-1, 0), []));
  int min_length = 1000000000000000000;

  while(queue.isNotEmpty){
    var curr = queue.removeFirst();
    (int, int) curr_pos = curr.$1;
    List<String> curr_path = curr.$3;

    if(curr_path.length > min_length){
      continue;
    }

    if(curr_pos.$1 == end.$1 && curr_pos.$2 == end.$2){
      if(curr_path.length <= min_length){
        min_length = curr_path.length;
        paths.add('${curr_path.map((p) => p).join('')}A');
      }
      continue;
    }

    for((int, int) dir in dirs){
      (int, int) new_pos = (curr_pos.$1 + dir.$1, curr_pos.$2 + dir.$2);
      if(0 <= new_pos.$1 && new_pos.$1 < grid.length && 0 <= new_pos.$2 && new_pos.$2 < grid[0].length && grid[new_pos.$1][new_pos.$2] != null){
        List<String> new_path = List.from(curr_path);
        String face_dir = face(dir);
        new_path.add(face_dir);
        queue.add((new_pos, dir, new_path));
      }
    }
  }
  return paths;
}

String face((int, int) dir){
  switch(dir){
    case (0, 1):
      return ">";
    case (1, 0):
      return "v";
    case (0, -1):
      return "<";
    case (-1, 0):
      return "^";
  }
  return "";
}