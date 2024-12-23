import 'package:aoc_dart/packages/AOCD/models.dart';

void main() async {
  AOCD aocd = await AOCD.create(2024, 23);
  print(part1(aocd.asStr));
  print(part2(aocd.asStr));
}

Map<String, Set<String>> parseInput(String input){
  Map<String, Set<String>> network = {};
  for(String line in input.split('\n')){
    List<String> parts = line.split('-');
    network.putIfAbsent(parts[0], () => {});
    network.putIfAbsent(parts[1], () => {});
    network[parts[0]]?.add(parts[1]);
    network[parts[1]]?.add(parts[0]);
  }
  return network;
}

part1(String input){
  Map<String, Set<String>> network = parseInput(input);
  Set<String> triplet = {};
  networkFunc(network, (curr) => curr.length > 3, (curr) {if(curr.length == 3 && curr.any((e) => e.startsWith('t'))) triplet.add((curr..sort()).join(','));});
  return triplet.length;
}

void networkFunc(Map<String, Set<String>> network, bool Function(List<String>) skip, void Function(List<String>) count){
  List<List<String>> stack = network.keys.map((e) => [e]).toList();
  while(stack.isNotEmpty){
    List<String> curr = stack.removeLast();
    if(skip(curr)){
      continue;
    }
    count(curr);
    for(String next in network[curr.last]!){
      if(curr.every((e) => network[next]!.contains(e))){
        stack.add([...curr, next]);
      }
    }
  }
}

part2(String input){
  Map<String, Set<String>> network = parseInput(input);
  List<String> longest = [];
  Set<String> checked = {};
  networkFunc(network, (curr) => !checked.add(curr.last), (curr) => curr.length > longest.length ? longest = curr : null);
  return (longest..sort()).join(',');
}