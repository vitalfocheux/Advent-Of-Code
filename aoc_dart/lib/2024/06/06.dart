import 'package:aoc_dart/packages/AOCD/models.dart';

void main() async {
  AOCD aocd = await AOCD.create(2024, 6);
  print(part1(aocd.asStr));
  print(part2(aocd.asStr));
}

part1(String input) {
  List<String> lines = input.split('\n');
  int x_guard = 0;
  int y_guard = 0;
  String dir_guard = '^';
  Set<(int, int)> block = {};
  Set<(int, int)> visited = {};
  lines.forEach((line){
    for(int i = 0; i < line.length; i++){
      if(line[i] == '^' || line[i] == 'v' || line[i] == '<' || line[i] == '>'){
        x_guard = i;
        y_guard = lines.indexOf(line);
        dir_guard = line[i];
      }else if(line[i] == '#'){
        block.add((i, lines.indexOf(line)));
      }
    }
  });
  while(true){
    visited.add((x_guard, y_guard));
    (int, int) next = advance(x_guard, y_guard, dir_guard);
    if(block.contains(next)){
      dir_guard = turn_90(dir_guard);
    }else{
      x_guard = next.$1;
      y_guard = next.$2;
    }
    if(y_guard >= lines.length || y_guard < 0 || x_guard >= lines[0].length || x_guard < 0){
      break;
    }
  }
  return visited.length;
}


part2(String input) {
  int l = 0;
  List<String> lines = input.split('\n');
  int x_guard = 0;
  int y_guard = 0;
  lines.forEach((line){
    for(int i = 0; i < line.length; i++){
      if(line[i] == '^'){
        x_guard = i;
        y_guard = lines.indexOf(line);
      }
    }
  });
  int j = 0;
  for(String line in lines){
    for(int i = 0; i < line.length; i++){
      if(line[i] != '.'){
        continue;
      }
      if(line[i] == '.'){
        lines[j] = '${line.substring(0, i)}#${line.substring(i + 1)}';
        if(loop(lines, line.length, lines.length, x_guard, y_guard)){
          l++;
        }
        lines[j] = line;
      }
    }
    j++;
  }
  return l;
}

bool loop(List<String> lines, int max_x, int max_y, int x_guard, int y_guard) {
  Set<(int, int, String)> visited = {};
  String dir_guard = '^';
  
  while(true){
    visited.add((x_guard, y_guard, dir_guard));
    (int, int) next = advance(x_guard, y_guard, dir_guard);
    if(next.$2 >= max_y || next.$2 < 0 || next.$1 >= max_x || next.$1 < 0){
      break;
    }
    
    if(lines[next.$2][next.$1] == '#'){
      dir_guard = turn_90(dir_guard);
    }else{
      x_guard = next.$1;
      y_guard = next.$2;
    }

    if(visited.contains((x_guard, y_guard, dir_guard))){
      return true;
    }
  }
  return false;
}

String turn_90(String dir){
  switch(dir){
    case '^':
      return '>';
    case 'v':
      return '<';
    case '<':
      return '^';
    case '>':
      return 'v';
  }
  return '';
}

(int, int) advance(int xx, int y, String dir){
  switch(dir){
    case '^':
      return (xx, y-1);
    case 'v':
      return (xx, y+1);
    case '<':
      return (xx-1, y);
    case '>':
      return (xx+1, y);
  }
  return (-1, -1);
}