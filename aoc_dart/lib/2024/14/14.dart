import 'package:aoc_dart/packages/extension/string_extension.dart';
import 'package:aoc_dart/packages/AOCD/models.dart';

void main() async {
  AOCD aocd = await AOCD.create(2024, 14);
  print(part1(aocd.asStr));
  print(part2(aocd.asStr));
}

int width = 0;
int height = 0;

parseInput(String input){
  List<((int, int), (int, int))> robot = [];
  for(String line in input.split('\n')){
    List<int> ints = line.findIntList();
    if(ints[0] > width) width = ints[0]+1;
    if(ints[1] > height) height = ints[1]+1;
    robot.add(((ints[0], ints[1]), (ints[2], ints[3])));
  }
  return robot;
}

part1(String input){
  List<((int, int), (int, int))> robots = parseInput(input);
  List<(int, int)> teleports = [];
  // print(robots);
  for(((int, int), (int, int)) robot in robots){
    (int, int) pos = robot.$1;
    for(int i = 0; i < 100; ++i){
      pos = ((pos.$1 + robot.$2.$1) % width, (pos.$2 + robot.$2.$2) % height);
    }
    if(pos.$1 != width ~/ 2 && pos.$2 != height ~/ 2){
      teleports.add(pos);
    }
  }
  (int, int, int, int) num_robots_each_quadrant = (0, 0, 0, 0);
  for((int, int) teleport in teleports){
    if(teleport.$1 < width ~/ 2 && teleport.$2 < height ~/ 2){
      num_robots_each_quadrant = (num_robots_each_quadrant.$1 + 1, num_robots_each_quadrant.$2, num_robots_each_quadrant.$3, num_robots_each_quadrant.$4);
    }else if(teleport.$1 >= width ~/ 2 && teleport.$2 < height ~/ 2){
      num_robots_each_quadrant = (num_robots_each_quadrant.$1, num_robots_each_quadrant.$2 + 1, num_robots_each_quadrant.$3, num_robots_each_quadrant.$4);
    }else if(teleport.$1 < width ~/ 2 && teleport.$2 >= height ~/ 2){
      num_robots_each_quadrant = (num_robots_each_quadrant.$1, num_robots_each_quadrant.$2, num_robots_each_quadrant.$3 + 1, num_robots_each_quadrant.$4);
    }else{
      num_robots_each_quadrant = (num_robots_each_quadrant.$1, num_robots_each_quadrant.$2, num_robots_each_quadrant.$3, num_robots_each_quadrant.$4 + 1);
    }
  }
  return num_robots_each_quadrant.$1 * num_robots_each_quadrant.$2 * num_robots_each_quadrant.$3 * num_robots_each_quadrant.$4;
}

part2(String input){
  List<((int, int), (int, int))> robots = parseInput(input);
  for(int i = 0; i < width * height + 1; ++i){
    List<((int, int), (int, int))> new_robots = [];
    for(((int, int), (int, int)) robot in robots){
      new_robots.add((((robot.$1.$1 + robot.$2.$1) % width, (robot.$1.$2 + robot.$2.$2) % height), robot.$2));
    }
    if(new_robots.map((e) => e.$1).toSet().length == new_robots.length){
      return i+1;
    }
    robots = new_robots;
  }
}