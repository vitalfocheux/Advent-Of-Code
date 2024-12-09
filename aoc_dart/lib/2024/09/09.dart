import 'package:aoc_dart/packages/AOCD/models.dart';
import 'package:aoc_dart/packages/extension/string_extension.dart';

void main() async {
  AOCD aocd = await AOCD.create(2024, 9);
  // print(part1(aocd.asStr));
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
  List<String> disk = [];
  Map<int, int> length_blocks = {};
  Map<int, (int, int)> length_free_space = {};
  space_2(disk_map, disk, 0, 0, false, length_blocks, length_free_space);
  // print(disk);
  move_2(disk, length_blocks, length_free_space);
  for(int i = 0; i < disk.length; i++){
    if(disk[i] == '.'){
      continue;
    }
    res += i * disk[i].toInt();
  }
  return res;
}

void space_2(List<String> disk_map, List<String> disk, int index_map, int ID, bool is_free_space, Map<int, int> length_blocks, Map<int, (int, int)> length_free_space){
  for(int i = 0; i < disk_map.length; i++){
    int index = disk_map[i].toInt();
    if(is_free_space){
      int disk_length = disk.length;
      for(int j = 0; j < index; j++){
        disk.add('.');
      }
      length_free_space[length_free_space.length] = (disk_length, index);
    }else{
      for(int j = 0; j < index; j++){
        disk.add(ID.toString());
      }
      length_blocks[ID] = index;
      ID++;
    }
    is_free_space = !is_free_space;
  }
}

void move_2(List<String> disk, Map<int, int> length_blocks, Map<int, (int, int)> length_free_space){
  Set<int> visited = {};
  for(int i = disk.length-1; i > 0; i--){
    print("$i");
    print(length_free_space);
    print(length_blocks);
    print(disk);
    if(disk[i] == '.'){
      continue;
    }
    int ID = disk[i].toInt();
    if(visited.contains(ID)){
      continue;
    }
    print("ID $ID");
    int length_ID = length_blocks[ID]!;
    int length_dot = -1;
    int index_dot = -1;
    int free_space = -1;
    for(int j = 0; j < length_free_space.length; ++j){
      if(length_free_space[j] == null){
        // print("null $j");
        continue;
      }
      if(length_free_space[j]!.$2 >= length_ID){
        print(j);
        length_dot = length_free_space[j]!.$2;
        index_dot = length_free_space[j]!.$1;
        free_space = j;
        break;
      }
    }
    if(length_dot == -1){
      i -= length_ID;
      continue;
    }
    for(int j = 0; j <length_ID; j++){
      disk[index_dot+j] = ID.toString();
      disk[i] = '.';
      i--;
    }
    i++;
    visited.add(ID);
    if(disk[index_dot+length_ID] == '.'){
      int new_length_dot = length_dot-length_ID;
      print("new_length_dot $length_dot - $length_ID = $new_length_dot");
      if(new_length_dot > 0){
        length_free_space.update(free_space, (value) => (index_dot+length_ID, new_length_dot));
      }else{
        length_free_space.remove(free_space);
      }
    }else{
      length_free_space.remove(free_space);
    }
  }
}

//6396171990508 is too high