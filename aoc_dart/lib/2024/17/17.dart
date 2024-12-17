import 'package:aoc_dart/packages/AOCD/models.dart';
import 'package:aoc_dart/packages/extension/string_extension.dart';
import 'package:collection/collection.dart';

void main() async {
  AOCD aocd = await AOCD.create(2024, 17);
  print(part1(aocd.asStr));
  print(part2(aocd.asStr));
}

parseInput(String input){
  return input.findIntList();
}

int A = 0;
int B = 0;
int C = 0;
List<int> program = [];

part1(String input){
  List<int> data = parseInput(input);
  A = data[0];
  B = data[1];
  C = data[2];
  data.removeAt(0);
  data.removeAt(0);
  data.removeAt(0);
  program = data;
  List<int> res = step();
  return res.join(",");
}

part2(String input){
  List<int> data = parseInput(input);
  A = data[0];
  B = data[1];
  C = data[2];
  data.removeAt(0);
  data.removeAt(0);
  data.removeAt(0);
  program = data;

  List<int> r = [];

  List<(int, int)> todo = [(program.length-1, 0)];
  while(todo.isNotEmpty){
    var curr = todo.removeAt(0);
    int p = curr.$1;
    int v = curr.$2;

    for(int a = 8*v; a < 8*(v+1); a++){
      A = a;
      B = 0;
      C = 0;
      List<int> res = step();
      if(ListEquality().equals(res, program.sublist(p))){
        if(p == 0){
          r.add(a);
        }else{
          todo.add((p-1, a));
        }
      }
    }
  }
  return r.min;
}

int? combo(int x){
  if(x == 7){
    print("$A $B $C, $program");
  }
  switch(x){
    case 4:
      return A;
    case 5:
      return B;
    case 6:
      return C;
    case 7:
      return null;
    default:
      return x;
  }
}

step(){
  List<int> res = [];
  int pointeur = 0;
  while(pointeur < program.length-1){
    int opcode = program[pointeur];
    int lit = program[pointeur + 1];
    
    
    switch(opcode){
      case 0:
        A = A >> (combo(lit)!);
        break;
      case 1:
        B ^= lit;
        break;
      case 2:
        B = (combo(lit)! % 8) & 7;
        break;
      case 3:
        if(A != 0){
          pointeur = lit-2;
        }
        break;
      case 4:
        B ^= C;
      case 5:
        res.add(combo(lit)! & 7);
      case 6:
        B = A >> (combo(lit)!);
        break;
      case 7:
        C = A >> (combo(lit)!);
        break;
    }
    pointeur += 2;
  }
  return res;
}