import 'dart:math';
import 'package:aoc_dart/packages/AOCD/models.dart';

void main() async {
  AOCD aocd = await AOCD.create(2024, 22);
  print(part1(aocd.asStr));
  print(part2(aocd.asStr));
}

part1(String input){
  num res = 0;
  for(String line in input.split('\n')){
    if(line.isEmpty) continue;
    int secret = int.parse(line);
    for(int i = 0; i < 2000; i++){
      secret = sequence(secret);
    }
    res += secret;
  }
  return res;
}


sequence(int secret){
  int mul = 64 * secret;
  secret = mix(mul, secret);
  secret = prune(secret);
  int div = secret ~/ 32;
  secret = mix(div, secret);
  secret = prune(secret);
  mul = 2048 * secret;
  secret = mix(mul, secret);
  return prune(secret);
}

mix(int number, int secret){
  return number ^ secret;
}

prune(int number){
  return number % 16777216;
}

part2(String input){
  num res = 0;
  Map<(int, int, int, int), int> seq_total = {};
  for(String line in input.split('\n')){
    if(line.isEmpty) continue;
    int secret = int.parse(line);
    List<int> buyers = [secret%10];
    for(int i = 0; i < 2000; i++){
      secret = sequence(secret);
      buyers.add(secret%10);
    }
    res = best_seq(buyers, {}, seq_total);
  }
  return res;
}

best_seq(List<int> buyers, Set<(int, int, int, int)> seen, Map<(int, int, int, int), int> seq_total){
  for(int i = 0; i < buyers.length-4; ++i){
    int a = buyers[i];
    int b = buyers[i+1];
    int c = buyers[i+2];
    int d = buyers[i+3];
    int e = buyers[i+4];
    (int, int, int, int) seq = (b - a, c - b, d - c, e - d);
    if(seen.contains(seq)) continue;
    seen.add(seq);
    if(!seq_total.containsKey(seq)){
      seq_total[seq] = 0;
    }
    seq_total[seq] = (seq_total[seq] ?? 0) + e;
  }
  return seq_total.values.reduce(max);
}