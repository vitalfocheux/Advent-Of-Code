import 'package:aoc_dart/packages/AOCD/models.dart';

void main() async {
  AOCD aocd = await AOCD.create(2024, 23);
  print(part1(aocd.asStr));
  print(part2(aocd.asStr));
}

part1(String input){
  Map<String, Set<String>> network = {};
  for(String line in input.split('\n')){
    List<String> parts = line.split('-');
    network.putIfAbsent(parts[0], () => {});
    network.putIfAbsent(parts[1], () => {});
    network[parts[0]]?.add(parts[1]);
    network[parts[1]]?.add(parts[0]);
  }
  Set<String> triplet = {};
  networkWithT(network, triplet);
  return triplet.length;
}

void networkWithT(Map<String, Set<String>> network, Set<String> triplet){
  List<List<String>> stack = network.keys.map((e) => [e]).toList();
  while(stack.isNotEmpty){
    List<String> curr = stack.removeLast();
    if(curr.length > 3){
      continue;
    }
    if(curr.length == 3 && curr.any((e) => e.startsWith('t'))){
      triplet.add((curr..sort()).join(','));
    }
    for(String next in network[curr.last]!){
      if(curr.every((e) => network[next]!.contains(e))){
        stack.add([...curr, next]);
      }
    }
  }
}

part2(String input){
  Map<String, Set<String>> network = {};
  for(String line in input.split('\n')){
    List<String> parts = line.split('-');
    network.putIfAbsent(parts[0], () => {});
    network.putIfAbsent(parts[1], () => {});
    network[parts[0]]?.add(parts[1]);
    network[parts[1]]?.add(parts[0]);
  }
  List<String> longest = [];
  Set<String> checked = {};
  longestNetwork(network, checked, longest);
  return (longest..sort()).join(',');
}

void longestNetwork(Map<String, Set<String>> network, Set<String> checked, List<String> longest){
  List<List<String>> stack = network.keys.map((e) => [e]).toList();
  while(stack.isNotEmpty){
    List<String> curr = stack.removeLast();
    if(!checked.add(curr.last)){
      continue;
    }
    if(curr.length > longest.length){
      longest.clear();
      longest.addAll(curr);
    }
    for(String next in network[curr.last]!){
      if(curr.every((e) => network[next]!.contains(e))){
        stack.add([...curr, next]);
      }
    }
  }
}