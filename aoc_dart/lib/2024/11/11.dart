import 'package:aoc_dart/packages/extension/string_extension.dart';
import 'package:aoc_dart/packages/AOCD/models.dart';

void main() async{
  AOCD aocd = await AOCD.create(2024,11);
  List<int> stones = aocd.asStr.findIntList();
  int res = 0;
  for(int stone in stones){
    res += rec(stone, 25, {})!;
  }
  print(res);
  res = 0;
  for(int stone in stones){
    res += rec(stone, 75, {})!;
  }
  print(res);
}

int? rec(int num, int blink, Map<(int, int), int> memory){
  if(blink == 1){
    return blink_one_stone(num).length;
  }
  (int, int) memory_key = (num, blink);
  if(memory.containsKey(memory_key)){
    return memory[memory_key];
  }
  List<int> bl = blink_one_stone(num);
  int res = 0;
  for(int b in bl){
    res += rec(b, (blink-1), memory)!;
  }
  memory[memory_key] = res;
  return res;
}

List<int> blink_one_stone(int stone){
  if(stone == 0){
    return [1];
  }
  String tmp = stone.toString();
  if(tmp.length%2 == 0){
    int mid = tmp.length ~/ 2;
    String left = tmp.substring(0, mid);
    String right = tmp.substring(mid);
    return [left.toInt(), right.toInt()];
  }
  return [stone * 2024];
}