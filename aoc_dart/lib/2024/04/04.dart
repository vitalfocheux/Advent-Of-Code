import 'package:aoc_dart/packages/AOCD/models.dart';

void main() async {
  AOCD aocd = await AOCD.create(2024, 4);
  print(part1(aocd.asStr));
  print(part2(aocd.asStr));
}

int part1(String input){
  int res = 0;
  List<String> lines = input.split('\n');
  for(int l = 0; l < lines.length; l++){
    String line = lines[l];
    for(int i = 0; i < line.length; i++){
      if(i+3 < line.length){
        if(isXMASHorizontal(line, i)){
          res++;
        }
      }
      if(i-3 >= 0){
        if(isXMASHorizontalBackward(line, i)){
          res++;
        }
      }
      if(l+3 < lines.length){
        if(isXMASVertical(lines, l, i)){
          res++;
        }
      }
      if(l-3 >= 0){
        if(isVerticalBackwrd(lines, l, i)){
          res++;
        }
      }
      if(l+3 < lines.length && i+3 < line.length){
        if(isXMASDiagonalSouthEast(lines, l, i)){
          res++;
        }
      }
      if(l+3 < lines.length && i-3 >= 0){
        if(isXMASDiagonalSouthWest(lines, l, i)){
          res++;
        }
      }
      if(l-3 >= 0 && i+3 < line.length){
        if(isXMASDiagonalNorthEast(lines, l, i)){
          res++;
        }
      }
      if(l-3 >= 0 && i-3 >= 0){
        if(isXMASDiagonalNorthWest(lines, l, i)){
          res++;
        }
      }
    }
  }
  return res;
}

bool isXMASHorizontal(String line, int i){
  return (line[i] == 'X' && line[i+1] == 'M' && line[i+2] == 'A' && line[i+3] == 'S');
}

bool isXMASHorizontalBackward(String line, int i){
  return line[i] == 'X' && line[i-1] == 'M' && line[i-2] == 'A' && line[i-3] == 'S';
}

bool isXMASVertical(List<String> lines, int i, int j){
  return (lines[i][j] == 'X' && lines[i+1][j] == 'M' && lines[i+2][j] == 'A' && lines[i+3][j] == 'S');
}

bool isVerticalBackwrd(List<String> lines, int i, int j){
  return lines[i][j] == 'X' && lines[i-1][j] == 'M' && lines[i-2][j] == 'A' && lines[i-3][j] == 'S';
}

bool isXMASDiagonalSouthEast(List<String> lines, int i, int j){
  return (lines[i][j] == 'X' && lines[i+1][j+1] == 'M' && lines[i+2][j+2] == 'A' && lines[i+3][j+3] == 'S');
}

bool isXMASDiagonalSouthWest(List<String> lines, int i, int j){
  return (lines[i][j] == 'X' && lines[i+1][j-1] == 'M' && lines[i+2][j-2] == 'A' && lines[i+3][j-3] == 'S');
}

bool isXMASDiagonalNorthEast(List<String> lines, int i, int j){
  return (lines[i][j] == 'X' && lines[i-1][j+1] == 'M' && lines[i-2][j+2] == 'A' && lines[i-3][j+3] == 'S');
}

bool isXMASDiagonalNorthWest(List<String> lines, int i, int j){
  return (lines[i][j] == 'X' && lines[i-1][j-1] == 'M' && lines[i-2][j-2] == 'A' && lines[i-3][j-3] == 'S');
}

int part2(String input){
  int res = 0;
  List<String> lines = input.split('\n');
  for(int l = 0; l < lines.length; l++){
    String line = lines[l];
    for(int i = 0; i < line.length; i++){
      if(l+1 < lines.length && l-1 >= 0 && i+1 < line.length && i-1 >= 0){
        if(isXMAS(lines, l, i)){
          res++;
        }
      }
    }
  }
  return res;
}

bool isXMAS(List<String> lines, int i, int j){
  if(lines[i][j] != 'A'){
    return false;
  }
  return (((MAS_NE(lines, i+1, j-1) && MAS_NW(lines, i+1, j+1)) || (MAS_NE(lines, i+1, j-1) && MAS_SE(lines, i-1, j-1)) || 
           (MAS_NW(lines, i+1, j+1) && MAS_SE(lines, i-1, j-1)) || (MAS_NW(lines, i+1, j+1) && MAS_NE(lines, i+1, j-1)) ||
           (MAS_SE(lines, i-1, j-1) && MAS_NW(lines, i+1, j+1)) || (MAS_SE(lines, i-1, j-1) && MAS_SW(lines, i-1, j+1)) ||
           (MAS_SW(lines, i-1, j+1) && MAS_SE(lines, i-1, j-1)) || (MAS_SW(lines, i-1, j+1) && MAS_NW(lines, i+1, j+1))));
}

bool MAS_SW(List<String> lines, int i, int j){
 return (lines[i][j] == 'M' && lines[i+1][j-1] == 'A' && lines[i+2][j-2] == 'S');
}

bool MAS_SE(List<String> lines, int i, int j){
  return (lines[i][j] == 'M' && lines[i+1][j+1] == 'A' && lines[i+2][j+2] == 'S');
}

bool MAS_NW(List<String> lines, int i, int j){
  return (lines[i][j] == 'M' && lines[i-1][j-1] == 'A' && lines[i-2][j-2] == 'S');
}

bool MAS_NE(List<String> lines, int i, int j){
  return (lines[i][j] == 'M' && lines[i-1][j+1] == 'A' && lines[i-2][j+2] == 'S');
}