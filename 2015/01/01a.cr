puts File.read("01.txt").chars.reduce(0) { |floor, c| floor + (c == '(' ? 1 : -1) }