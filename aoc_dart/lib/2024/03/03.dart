import 'package:aoc_dart/packages/AOCD/models.dart';

void main() async {
  AOCD aocd = await AOCD.create(2024, 3);
  print(part1(aocd.asStr));
  print(part2(aocd.asStr));
}

int part1(String input){
  RegExp exp = RegExp(r'mul\((\d{1,3}),(\d{1,3})\)');
  return exp.allMatches(input)
  .map((match) => int.parse(match.group(1)!)*int.parse(match.group(2)!))
  .reduce((sum, elt) => sum + elt);
}

int part2(String input){
  RegExp exp = RegExp(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)");
  int sum = 0;
  bool DO = true;
  exp.allMatches(input).forEach((e) {
    if(e.group(0) == "do()"){
      DO = true;
    }else if(e.group(0) == "don't()"){
      DO = false;
    }else if(DO){
      if (e.group(1) != null && e.group(2) != null) {
        sum += int.parse(e.group(1)!) * int.parse(e.group(2)!);
      }
    }
  });
  return sum;
}
