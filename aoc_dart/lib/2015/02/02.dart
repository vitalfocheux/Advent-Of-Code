import '../../packages/models.dart';

void main() async {
  AOCD aocd = await AOCD.create(2015, 2);
  print(part1(aocd.asStr));
}

int part1(String parser){
  int res = 0;

  List<String> lines = parser.split('\n');
  for(String line in lines){
    List<String> parts = line.split('x');
    int l = int.parse(parts[0]);
    int w = int.parse(parts[1]);
    int h = int.parse(parts[2]);
    int lw = l * w;
    int wh = w * h;
    int hl = h * l;
    res += 2 * lw + 2 * wh + 2 * hl + [lw, wh, hl].reduce((a, b) => a < b ? a : b);
  }

  return res;
}