puts File.read("08.txt").lines.sum { |line| line.chomp.inspect.size - line.chomp.size }
