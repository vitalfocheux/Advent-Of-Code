import 'package:aoc_dart/packages/extension/string_extension.dart';
import 'package:test/test.dart';

void main(){

  group("findInt", (){
    test("one int", (){
      expect("123".findInt(), 123);
    });

    test("one int negative", (){
      expect("-123".findInt(), -123);
    });

    test("one int negative with other char", (){
      expect("a-123".findInt(), -123);
    });

    test("one int with other char", (){
      expect("a123".findInt(), 123);
    });

    test("one int negative with other char", (){
      expect("a-123b".findInt(), -123);
    });

    test("one int with other char", (){
      expect("a123b".findInt(), 123);
    });

    test("one int negative with other char", (){
      expect("a-123b456".findInt(), -123);
    });

    test("one int with other char", (){
      expect("a123b456".findInt(), 123);
    });

    test("no int", (){
      expect(() => "abc".findInt(), throwsException);
    });

    test("double", (){
      expect("123.456".findInt(), 123);
    });
  });

  group("findIntList", (){
    test("one int", (){
      expect("123".findIntList(), [123]);
    });

    test("one int negative", (){
      expect("-123".findIntList(), [-123]);
    });

    test("one int negative with other char", (){
      expect("a-123".findIntList(), [-123]);
    });

    test("one int with other char", (){
      expect("a123".findIntList(), [123]);
    });

    test("one int negative with other char", (){
      expect("a-123b".findIntList(), [-123]);
    });

    test("one int with other char", (){
      expect("a123b".findIntList(), [123]);
    });

    test("one int negative with other char", (){
      expect("a-123b456".findIntList(), [-123, 456]);
    });

    test("one int with other char", (){
      expect("a123b456".findIntList(), [123, 456]);
    });

    test("no int", (){
      expect("abc".findIntList(), []);
    });

    test("double", (){
      expect("123.456".findIntList(), [123, 456]);
    });

    test("postive and negative", (){
      expect("123-456".findIntList(), [123, -456]);
    });
  });

  group("findDouble", (){
    test("one double", (){
      expect("123.456".findDouble(), 123.456);
    });

    test("one double negative", (){
      expect("-123.456".findDouble(), -123.456);
    });

    test("one double negative with other char", (){
      expect("a-123.456".findDouble(), -123.456);
    });

    test("one double with other char", (){
      expect("a123.456".findDouble(), 123.456);
    });

    test("one double negative with other char", (){
      expect("a-123.456b".findDouble(), -123.456);
    });

    test("one double with other char", (){
      expect("a123.456b".findDouble(), 123.456);
    });

    test("one double negative with other char", (){
      expect("a-123.456b789.123".findDouble(), -123.456);
    });

    test("one double with other char", (){
      expect("a123.456b789.123".findDouble(), 123.456);
    });

    test("no double", (){
      expect(() => "abc".findDouble(), throwsException);
    });

    test("int", (){
      expect("123".findDouble(), 123.0);
    });

    test("int negative", (){
      expect("-123".findDouble(), -123.0);
    });
  });

  group("findDoubleList", (){
    test("one double", (){
      expect("123.456".findDoubleList(), [123.456]);
    });

    test("one double negative", (){
      expect("-123.456".findDoubleList(), [-123.456]);
    });

    test("one double negative with other char", (){
      expect("a-123.456".findDoubleList(), [-123.456]);
    });

    test("one double with other char", (){
      expect("a123.456".findDoubleList(), [123.456]);
    });

    test("one double negative with other char", (){
      expect("a-123.456b".findDoubleList(), [-123.456]);
    });

    test("one double with other char", (){
      expect("a123.456b".findDoubleList(), [123.456]);
    });

    test("one double negative with other char", (){
      expect("a-123.456b789.123".findDoubleList(), [-123.456, 789.123]);
    });

    test("one double with other char", (){
      expect("a123.456b789.123".findDoubleList(), [123.456, 789.123]);
    });

    test("no double", (){
      expect("abc".findDoubleList(), []);
    });

    test("int", (){
      expect("123".findDoubleList(), [123.0]);
    });

    test("int negative", (){
      expect("-123".findDoubleList(), [-123.0]);
    });

    test("postive and negative", (){
      expect("123-456".findDoubleList(), [123.0, -456.0]);
    });

    test("int and double", (){
      expect("123.456-789".findDoubleList(), [123.456, -789.0]);
    });

    test("double and int", (){
      expect("123-789.456".findDoubleList(), [123.0, -789.456]);
    });
  });

}