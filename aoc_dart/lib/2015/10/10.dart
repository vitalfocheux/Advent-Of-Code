import '../../packages/models.dart';

void main() async {
  AOCD aocd = await AOCD.create(2015, 10);
  print(part(aocd.asStr, 40));
  print(part(aocd.asStr, 50));
}

int part(String parser, int times){
  for(int i = 0; i < times; i++){
    parser = lookAndSay(parser);
  }
  return parser.length;
}

String lookAndSay(String parser){
  final regExp = RegExp(r'(\d)\1*');
  return regExp.allMatches(parser).map((match) {
    final matchStr = match.group(0)!;
    return '${matchStr.length}${matchStr[0]}';
  }).join('');
}