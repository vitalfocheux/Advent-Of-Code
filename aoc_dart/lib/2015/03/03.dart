import '../../packages/AOCD/models.dart';

void main() async {
  AOCD aocd = await AOCD.create(2015, 3);
  print(part1(aocd.asStr));
  print(part2(aocd.asStr));
}

class Coordinate {
  final int x;
  final int y;

  Coordinate(this.x, this.y);

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is Coordinate && 
          runtimeType == other.runtimeType && 
          x == other.x && 
          y == other.y;

  @override
  int get hashCode => x.hashCode ^ y.hashCode;
}

int part1(String parser){

  Set<Coordinate> houses = {};
  int x = 0, y = 0;
  houses.add(Coordinate(x, y));
  for(int i = 0; i < parser.length; i++){
    switch(parser[i]){
      case "^":
        y++;
        break;
      case "v":
        y--;
        break;
      case ">":
        x++;
        break;
      case "<":
        x--;
        break;
    }
    Coordinate c = Coordinate(x, y);
    houses.add(c);
  }
  return houses.length;
}

int part2(String parser){
  Set<Coordinate> houses = {};
  houses.add(Coordinate(0, 0));
  int x = 0, y = 0;
  int x2 = 0, y2 = 0;

  for(int i = 0; i < parser.length; i++){
    if(i%2 == 0){
      switch(parser[i]){
        case "^":
          y++;
          break;
        case "v":
          y--;
          break;
        case ">":
          x++;
          break;
        case "<":
          x--;
          break;
      }
      Coordinate c = Coordinate(x, y);
      houses.add(c);
    } else {
      switch(parser[i]){
        case "^":
          y2++;
          break;
        case "v":
          y2--;
          break;
        case ">":
          x2++;
          break;
        case "<":
          x2--;
          break;
      }
      Coordinate c = Coordinate(x2, y2);
      houses.add(c);
    }
  }

  return houses.length;
}