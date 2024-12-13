import 'package:aoc_dart/packages/AOCD/models.dart';
import 'package:aoc_dart/packages/extension/string_extension.dart';

void main() async {
  AOCD aocd = await AOCD.create(2024, 13);
  print(part(aocd.asStr, 0));
  print(part(aocd.asStr, 10000000000000));
}

parseInput(String input){
  List<String> data = input.split('\n');
  List<((int, int), (int, int), (int, int))> res = [];
  List<(int, int)> a = [];
  List<(int, int)> b = [];
  List<(int, int)> prize = [];
  for(String line in data){
    if(line.isEmpty) continue;
    if(line.contains('A')){
      List<int> _a = line.findIntList();
      a.add((_a[0], _a[1]));
    }else if(line.contains('B')){
      List<int> _b = line.findIntList();
      b.add((_b[0], _b[1]));
    }else if(line.contains('Prize')){
      List<int> _prize = line.findIntList();
      prize.add((_prize[0], _prize[1]));
    }
  }
  for(int i = 0; i < a.length; i++){
    res.add((a[i], b[i], prize[i]));
  }
  return res;
}

/* Solution for part1
part1(String input){
  num res = 0;
  List<((int, int), (int, int), (int, int))> data = parseInput(input);
  for(((int, int), (int, int), (int, int)) machine in data){
    bool found = false;
    for(int a = 0; a <= 100 && !found; ++a){
      for(int b = 0; b <= 100; ++b){
        if(machine.$1.$1*a + machine.$2.$1*b == machine.$3.$1 && machine.$1.$2*a + machine.$2.$2*b == machine.$3.$2){
          res += a*3 + b;
          found = true;
          break;
        }
      }
    }
  }
  return res;
}*/

part(String input, int more){
  num res = 0;
  List<((int, int), (int, int), (int, int))> data = parseInput(input);
  for(((int, int), (int, int), (int, int)) machine in data){
    int det = machine.$1.$1*machine.$2.$2 - machine.$1.$2*machine.$2.$1;
    if(det == 0) continue;
    double detA = ((machine.$3.$1+more)*machine.$2.$2 - (machine.$3.$2+more)*machine.$2.$1) / det;
    double detB = (machine.$1.$1*(machine.$3.$2+more) - machine.$1.$2*(machine.$3.$1+more)) / det;
    
    int a_int = detA.round();
    int b_int = detB.round();
    
    if (detA >= 0 && detB >= 0 && (detA - a_int).abs() < 1e-10 &&
        (detB - b_int).abs() < 1e-10) {
      
      res += 3 * a_int + b_int;
    }
  }
  return res;
}