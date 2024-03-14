content = File.read("02.txt")

ribbon = 0

content.each_line do |line|
  l, w, h = line.split("x")
    l, w, h = l.to_i, w.to_i, h.to_i
  ribbon += 2 * (l + w + h - [l, w, h].max) + l * w * h
end

puts ribbon