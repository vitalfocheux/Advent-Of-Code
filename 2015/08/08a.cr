puts File.read("08.txt").lines.sum { |line| line.size - line[1..-2].scan(/\\\\|\\\"|\\x[0-9a-fA-F]{2}|./).size }
