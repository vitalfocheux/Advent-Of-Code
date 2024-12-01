import 'dart:math';

import 'package:aoc_dart/packages/AOCD/models.dart';
import 'package:aoc_dart/packages/extension/string_extension.dart';

void main() async{
  AOCD aocd = await AOCD.create(2024, 1);
  print(part1(aocd.asStr));
  print(part2(aocd.asStr));
}

int part1(String input) {
  List<int> left = [];
  List<int> right = [];
  int result = 0;
  for(String line in input.split('\n')) {
    List<String> parts = line.split('   ');
    left.add(parts[0].toInt());
    right.add(parts[1].toInt());
  }


  while(left.isNotEmpty){
    int l = left.reduce(min);
    left.remove(l);
    int r = right.reduce(min);
    right.remove(r);
    result += (l - r).abs();
  }
  return result;
}

int part2(String input){
  List<int> left = [];
  List<int> right = [];
  int result = 0;
  for(String line in input.split('\n')) {
    List<String> parts = line.split('   ');
    left.add(parts[0].toInt());
    right.add(parts[1].toInt());
  }

  for(int i = 0; i < left.length; i++){
    int l = left[i];
    int r = right.where((e) => e == l).length;
    result += l*r;
  }
  return result;
}