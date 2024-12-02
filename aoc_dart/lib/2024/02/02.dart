import 'package:aoc_dart/packages/AOCD/models.dart';
import 'package:aoc_dart/packages/extension/string_extension.dart';

void main() async{
  AOCD aocd = await AOCD.create(2024, 2);
  print(part1(aocd.asStr));
  print(part2(aocd.asStr));
}

int part1(String input) {
  int safe = 0;
  for(String line in input.split('\n')){
    List<int> ints = line.findIntList();
    if(isSafe(ints)){
      safe++;
    }
  }
  return safe;
}

int part2(String input) {
  int safe = 0;

  for(String line in input.split('\n')){
    List<int> ints = line.findIntList();
    bool is_safe = isSafe(ints);
    if(!is_safe){
      for(int i = 0; i < ints.length; ++i){
        int removedElt = ints.removeAt(i);
        if(isSafe(ints)){
          safe++;
          break;
        }
        ints.insert(i, removedElt);
      }
    }else{
      safe++;
    }
  }
  return safe;
}

bool isSafe(List<int> ints){
  if(ints[0] > ints[1]){
    if(isStriclyDecreasing(ints)){
      return true;
    }
  }else if(ints[0] < ints[1]){
    if(isStriclyIncreasing(ints)){
      return true;
    }
  }
  return false;
}

bool isStriclyIncreasing(List<int> ints){
  for(int i = 0; i < ints.length-1; i++){
    if(ints[i] >= ints[i+1] || (ints[i] - ints[i+1]).abs() > 3){
      return false;
    }
  }
  return true;
}

bool isStriclyDecreasing(List<int> ints){
  for(int i = 0; i < ints.length-1; i++){
    if(ints[i] <= ints[i+1] || (ints[i] - ints[i+1]).abs() > 3){
      return false;
    }
  }
  return true;
}