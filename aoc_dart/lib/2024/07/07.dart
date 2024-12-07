import 'package:aoc_dart/packages/AOCD/models.dart';
import 'package:aoc_dart/packages/extension/string_extension.dart';

void main() async {
  AOCD aocd = await AOCD.create(2024, 7);
  print(part1(aocd.asStr));
  print(part2(aocd.asStr));
}

part1(String input) {
  num res = 0;
  for(String line in input.split('\n')){
    List<String> split = line.split(':');
    num r = num.parse(split[0]);
    List<int> values = split[1].findIntList();
    if(correct_test(r, values, 0, 0)){
      res += r;
    }
  }
  return res;
}

part2(String input) {
  num res = 0;
  for(String line in input.split('\n')){
    List<String> split = line.split(':');
    num r = num.parse(split[0]);
    List<int> values = split[1].findIntList();
    if(correct_test_2(r, values, 0, 0)){
      res += r;
    }
  }
  return res;
}

bool correct_test(num r, List<int> values, int i, num value){
  if(i == values.length){
    
    return r == value;
  }
  num add = value + values[i];
  num mul;
  (value == 0) ? mul = values[i] : mul = value * values[i];
  if(correct_test(r, values, (i+1), add) || correct_test(r, values, (i+1), mul)){
    return true;
  }
  return false;
}

bool correct_test_2(num r, List<int> values, int i, num value){
  if(i == values.length){
    
    return r == value;
  }
  num add = value + values[i];
  num mul;
  (value == 0) ? mul = values[i] : mul = value * values[i];
  num concat = num.parse(value.toString() + values[i].toString());
  if(correct_test_2(r, values, (i+1), add) || correct_test_2(r, values, (i+1), mul) || correct_test_2(r, values, (i+1), concat)){
    return true;
  }
  return false;
}