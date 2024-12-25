import 'package:aoc_dart/packages/AOCD/models.dart';

void main() async {
  AOCD aocd = await AOCD.create(2024, 25);
  print(part1(aocd.asStr));
  // print(part2(aocd.asStr));
}

part1(String input){
  List<String> lines = input.split('\n');
  Set<(int, int, int, int, int)> lock = {}, key = {};
  for(int i = 0; i < lines.length; i += 8){
    bool isLock = false;
    if(lines[i].startsWith('#####')){
      isLock = true;
    }
    int first = 0, second = 0, third = 0, fourth = 0, fifth = 0;
    for(int j = i; j < lines.length; ++j){
      if(isLock && j == i){
        continue;
      }
      if(lines[j].isEmpty){
        break;
      }
      if(lines[j][0] == '#'){
        first++;
      }
      if(lines[j][1] == '#'){
        second++;
      }
      if(lines[j][2] == '#'){
        third++;
      }
      if(lines[j][3] == '#'){
        fourth++;
      }
      if(lines[j][4] == '#'){
        fifth++;
      }
    }
    if(isLock){
      lock.add((first, second, third, fourth, fifth));
    }else{
      key.add((--first, --second, --third, --fourth, --fifth));
    }
  }
  num res = 0;
  for(var l in lock){
    for(var k in key){
      if(l.$1 + k.$1 <= 5 && l.$2 + k.$2 <= 5 && l.$3 + k.$3 <= 5 && l.$4 + k.$4 <= 5 && l.$5 + k.$5 <= 5){
        res++;
      }
    }
  }
  return res;
}