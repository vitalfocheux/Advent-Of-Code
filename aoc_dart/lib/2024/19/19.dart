import 'package:aoc_dart/packages/AOCD/models.dart';

void main() async {
  AOCD aocd = await AOCD.create(2024, 19);
  // print(part1(aocd.asStr));
  print(part2(aocd.asStr));
}

parseInput(String input){
  return input.split('\n\n');
}

part1(String input){
  List<String> parts = parseInput(input);
  List<String> towels = parts[0].split(',').map((e) => e.trim()).toList();
  List<String> design = parts[1].split('\n').map((e) => e.trim()).toList();
  int result = 0;
  Map<String, bool> memory = {};
  for(String d in design){
    if(possible_design(towels, d, memory)){
      result++;
    }
  }
  return result;
}

bool possible_design(List<String> towels, String design, Map<String, bool> memory){
  if(design.isEmpty) return true;
  if(memory.containsKey(design)) return memory[design]!;
  for(String towel in towels){
    if(towel.length <= design.length && design.startsWith(towel)){
      String remain = design.substring(towel.length);
      if(possible_design(towels, remain, memory)){
        memory[design] = true;
        return true;
      }
    }
  }
  memory[design] = false;
  return false;
}

part2(String input){
  List<String> parts = parseInput(input);
  List<String> towels = parts[0].split(',').map((e) => e.trim()).toList();
  List<String> design = parts[1].split('\n').map((e) => e.trim()).toList();
  num result = 0;
  Map<String, num> memory = {};
  for(String d in design){
    result += count_arrangement(towels, d, memory);
    print(result);
  }
  return result;
}

count_arrangement(List<String> towels, String design, Map<String, num> memory){
  if(design.isEmpty) return 1;
  if(memory.containsKey(design)) return memory[design]!;
  num result = 0;
  for(String towel in towels){
    if(towel.length <= design.length && design.startsWith(towel)){
      String remain = design.substring(towel.length);
      result += count_arrangement(towels, remain, memory);
    }
  }
  memory[design] = result;
  return result;
}