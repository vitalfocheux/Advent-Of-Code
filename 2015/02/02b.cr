puts File.read("02.txt").lines.map { |line| l, w, h = line.split("x"); l, w, h = l.to_i, w.to_i, h.to_i; 2 * (l + w + h - [l, w, h].max) + l * w * h }.sum