import 'package:aoc_dart/packages/AOCD/models.dart';
import 'package:aoc_dart/packages/extension/string_extension.dart';

void main() async {
  AOCD aocd = await AOCD.create(2024, 24);
  print(part1(aocd.asStr));
  print(part2(aocd.asStr));
}

Map<String, int> values = {};
Set<String> all_operator = {};
Map<String, (String, String, String)> gates = {};
String highest_z = 'z00';
Set<String> xyz = {'x', 'y', 'z'};

parseInput(String input){
  for(String line in input.split('\n')){
    if(line.isEmpty) continue;
    if(line.contains(':')){
      List<String> parts = line.split(':');
      values[parts[0]] = int.parse(parts[1]);
      all_operator.add(parts[0]);
    }else{
      List<String> parts = line.split(' ');
      gates[parts[4]] = (parts[0], parts[1], parts[2]);
      all_operator.add(parts[4]);
      if(parts[4].startsWith('z')){
        int z = parts[4].findInt();
        if(z > highest_z.findInt()){
          highest_z = parts[4];
        }
      }
    }
  }
}

Map<int, int> digits = {};

part1(String input){
  parseInput(input);
  Map<String, int> memory = {};
  for(String op in all_operator){
    if(op.startsWith('z')){
      digits[op.findInt()] = evaluate(op, memory);
    }
  }
  num res = 0;
  for(int i = digits.length - 1; i >= 0; i--){
    res = res * 2 + digits[i]!;
  }
  return res;
}

int evaluate(String op, Map<String, int> memory){
  if(values.containsKey(op)) return values[op]!;
  if(memory.containsKey(op)) return memory[op]!;

  int op1 = evaluate(gates[op]!.$1, memory);
  int op2 = evaluate(gates[op]!.$3, memory);
  switch(gates[op]!.$2){
    case 'AND': 
      memory[op] = op1 & op2;
      return memory[op]!;
    case 'OR': 
      memory[op] = op1 | op2;
      return memory[op]!;
    case 'XOR': 
      memory[op] = op1 ^ op2;
      return memory[op]!;
    default: return 0;
  }
}

part2(String input){
  parseInput(input);
  Set<String> wrong = {};
  for(String gate in gates.keys){
    String op1 = gates[gate]!.$1;
    String op = gates[gate]!.$2;
    String op2 = gates[gate]!.$3;
    String res = gate;

    if(res.startsWith('z') && res != highest_z && op != "XOR"){
      wrong.add(res);
    }
    if(op == "XOR" && !xyz.contains(res[0]) && !xyz.contains(op1[0]) && !xyz.contains(op2[0])){
      wrong.add(res);
    }
    if(op == "AND" && "x00" != op1 && "x00" != op2){
      for(String g in gates.keys){
        if((gates[g]!.$1 == res || gates[g]!.$3 == res) && gates[g]!.$2 != "OR"){
          wrong.add(res);
        }
      }
    }
    if(op == "XOR"){
      for(String g in gates.keys){
        if((gates[g]!.$1 == res || gates[g]!.$3 == res) && gates[g]!.$2 == "OR"){
          wrong.add(res);
        }
      }
    }
  }
  return (wrong.toList()..sort()).join(',');
}