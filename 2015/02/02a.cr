puts File.read("02.txt").lines.sum { |line| l, w, h = line.split("x").map(&.to_i); 2*l*w + 2*w*h + 2*h*l + [l*w, w*h, h*l].min }