import 'package:aoc_dart/packages/AOCD/models.dart';
import 'package:aoc_dart/packages/extension/string_extension.dart';

void main() async {
  AOCD aocd = await AOCD.create(2024, 9);
  print(part1(aocd.asStr));
  print(part2(aocd.asStr));
}

part1(String input){
  num res = 0;
  List<String> disk_map = input.split('');
  List<String> disk = [];
  space(disk_map, disk, 0, 0, false);
  move(disk);
  for(int i = 0; i < disk.length; i++){
    if(disk[i] == '.'){
      continue;
    }
    res += i * disk[i].toInt();
  }
  return res;
}

void move(List<String> disk){
  for(int i = disk.length-1; i > 0; i--){
    if(disk[i] == '.'){
      continue;
    }
    int first_occ_dot = disk.indexWhere((elt) => elt == '.');
    if(first_occ_dot > i){
      break;
    }
    disk[first_occ_dot] = disk[i];
    disk[i] = '.';
  }
}

void space(List<String> disk_map, List<String> disk, int index_map, int ID, bool is_free_space){
  for(int i = 0; i < disk_map.length; i++){
    int index = disk_map[i].toInt();
    if(is_free_space){
      for(int j = 0; j < index; j++){
        disk.add('.');
      }
    }else{
      for(int j = 0; j < index; j++){
        disk.add(ID.toString());
      }
      ID++;
    }
    is_free_space = !is_free_space;
  }
}

part2(String input){
  num res = 0;
  List<String> disk_map = input.split('');
  List<int?> disk = [];
  space_2(disk_map, disk);
  for(int i = disk.length-1; i > 0; i--){
    if(disk[i] == null){
      continue;
    }
    int curr = disk[i]!;
    int curr_size = 1;
    for(int j = i-1; j >= 0; j--){
      if(disk[j] != curr){
        break;
      }
      curr_size++;
    }
    while(true){
      int first_free_index = disk.indexWhere((elt) => elt == null);
      if(first_free_index > i || first_free_index == -1){
        i -= curr_size-1;
        break;
      }
      int empty_space_size = disk.sublist(first_free_index, disk.indexWhere((elt) => elt != null, first_free_index)).length;
      if(empty_space_size < curr_size){
        for(int j = 0; j < empty_space_size; j++){
          disk[first_free_index+j] = -1;
        }
        continue;
      }
      for(int j = 0; j < curr_size; j++){
        disk[i-j] = null;
        disk[first_free_index+j] = curr;
      }
      i -= curr_size-1;
      break;
    }
    for(int j = 0; j < disk.length; j++){
      if(disk[j] == -1){
        disk[j] = null;
      }
    }
  }
  for(int i = 0; i < disk.length; i++){
    if(disk[i] == null){
      continue;
    }
    res += i * disk[i]!;
  }
  return res;
}

void space_2(List<String> disk_map, List<int?> disk){
  bool freeSpace = false;
  int id = 0;
  for (final char in disk_map) {
    int value = int.parse(char);
    for (int i = 0; i < value; i++) {
      if (freeSpace) {
        disk.add(null);
      } else {
        disk.add(id);
      }
    }
    if (freeSpace) {
      id++;
    }
    freeSpace = !freeSpace;
  }
}