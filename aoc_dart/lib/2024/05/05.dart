import 'package:aoc_dart/packages/AOCD/models.dart';
import 'package:aoc_dart/packages/extension/string_extension.dart';
import 'dart:collection';

void main() async{
  AOCD aocd = await AOCD.create(2024,5);
  print(part1(aocd.asStr));
  print(part2(aocd.asStr));
}

part1(String input){
  int res = 0;
  List<List<int>> page_ordering = [];
  List<List<int>> tuples = [];
  parse(page_ordering, tuples, input);
  for(List<int> page in page_ordering){
    if(is_in_order(tuples, page)){
      res += page[(page.length / 2).round()-1];
    }
  }
  return res;
}

part2(String input){
  List<List<int>> page_ordering = [];
  List<List<int>> tuples = [];
  parse(page_ordering, tuples, input);
  final graph = buildGraph(tuples);

  // Identifier les mises à jour incorrectes et les corriger
  final correctedMiddleSum = page_ordering.fold(0, (sum, update) {
    if (isValidUpdate(update, graph)) {
      return sum; // Ignorer les mises à jour déjà correctes
    } else {
      final correctedUpdate = sortUpdate(update, graph);
      final middlePage = correctedUpdate[correctedUpdate.length ~/ 2];
      return sum + middlePage;
    }
  });
  return correctedMiddleSum;
}

// Construire un graphe des dépendances à partir des règles
Map<int, List<int>> buildGraph(List<List<int>> rules) {
  final graph = <int, List<int>>{};
  for (var rule in rules) {
    graph.putIfAbsent(rule[0], () => []).add(rule[1]);
  }
  return graph;
}

// Vérifier si une mise à jour est valide en fonction des règles
bool isValidUpdate(List<int> update, Map<int, List<int>> graph) {
  final indexMap = {for (var i = 0; i < update.length; i++) update[i]: i};
  for (var entry in graph.entries) {
    final page = entry.key;
    final afterPages = entry.value;
    if (indexMap.containsKey(page)) {
      for (var afterPage in afterPages) {
        if (indexMap.containsKey(afterPage) &&
            indexMap[page]! >= indexMap[afterPage]!) {
          return false;
        }
      }
    }
  }
  return true;
}

// Réorganiser une mise à jour incorrecte en fonction des règles
List<int> sortUpdate(List<int> update, Map<int, List<int>> graph) {
  final subGraph = <int, List<int>>{};
  for (var page in update) {
    if (graph.containsKey(page)) {
      subGraph[page] = graph[page]!.where(update.contains).toList();
    }
  }
  return topologicalSort(update, subGraph);
}

// Tri topologique pour obtenir un ordre valide
List<int> topologicalSort(List<int> nodes, Map<int, List<int>> graph) {
  final inDegree = <int, int>{for (var node in nodes) node: 0};
  for (var edges in graph.values) {
    for (var node in edges) {
      if (inDegree.containsKey(node)) {
        inDegree[node] = inDegree[node]! + 1;
      }
    }
  }

  final queue = Queue<int>();
  for (var node in nodes) {
    if (inDegree[node] == 0) {
      queue.add(node);
    }
  }

  final sorted = <int>[];
  while (queue.isNotEmpty) {
    final node = queue.removeFirst();
    sorted.add(node);
    for (var neighbor in graph[node] ?? []) {
      inDegree[neighbor] = inDegree[neighbor]! - 1;
      if (inDegree[neighbor] == 0) {
        queue.add(neighbor);
      }
    }
  }

  return sorted;
}

bool is_in_order(List<List<int>> rules, List<int> page){
  for(List<int> rule in rules){
    if(page.contains(rule[0]) && page.contains(rule[1])){
      if(page.indexOf(rule[0]) > page.indexOf(rule[1])){
        return false;
      }
    }
  }
  return true;
}

void parse(List<List<int>> page_ordering, List<List<int>> tuples, String input){
  for(String line in input.split('\n')){
    if(line.contains(',')){
      page_ordering.add(line.findIntList());
    }else if(line.contains('|')){
      List<String> split = line.split('|');
      int before = split[0].findInt();
      int a = split[1].findInt();
      tuples.add([before, a]);
    }
  }
}