import '../../packages/AOCD/models.dart';
import 'dart:convert';
import 'package:crypto/crypto.dart';

void main() async {
  AOCD aocd = await AOCD.create(2015, 4);
  print(part(aocd.asStr, '00000'));
  print(part(aocd.asStr, '000000'));
}

int part(String parser, String lowest){
  int result = 0;
  while(true){
    String to_hash = parser + result.toString();
    if(md5.convert(utf8.encode(to_hash)).toString().startsWith(lowest)){
      break;
    }
    result++;
  }
  return result;
}